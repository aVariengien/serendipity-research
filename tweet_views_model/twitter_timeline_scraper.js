/* eslint-disable no-console */
/**
 * Twitter/X timeline scraper (run in browser console on x.com).
 *
 * Features:
 * - startScrape(): begins periodic scraping + optional auto-scroll.
 * - stopScrape(): stops scraping.
 * - getData(): returns collected rows.
 * - downloadJSON(): exports collected rows to a JSON file.
 *
 * Usage:
 *   // 1) Paste this whole file in DevTools Console and press Enter
 *   // 2) Start scraping
 *   TwitterTimelineScraper.startScrape({
 *     scrapeIntervalMs: 2000,
 *     statusIntervalMs: 5000,
 *     autoScroll: true,
 *     scrollStepPx: 1400
 *   });
 *
 *   // 3) Stop when enough tweets collected
 *   TwitterTimelineScraper.stopScrape();
 *
 *   // 4) Export
 *   TwitterTimelineScraper.downloadJSON("twitter_timeline_metrics.json");
 */
(function attachTwitterTimelineScraper(global) {
  const state = {
    byTweetId: new Map(),
    scrapeTimer: null,
    scrollTimer: null,
    statusTimer: null,
    running: false,
    startedAt: null,
  };

  function parseCompactNumber(raw) {
    if (raw == null) return null;
    const s = String(raw).trim().replace(/,/g, "").toUpperCase();
    if (!s) return null;

    const match = s.match(/^([0-9]*\.?[0-9]+)\s*([KMB])?$/i);
    if (!match) {
      const n = Number(s);
      return Number.isFinite(n) ? n : null;
    }

    const base = Number(match[1]);
    if (!Number.isFinite(base)) return null;
    const suffix = match[2];
    if (suffix === "K") return Math.round(base * 1e3);
    if (suffix === "M") return Math.round(base * 1e6);
    if (suffix === "B") return Math.round(base * 1e9);
    return Math.round(base);
  }

  function safeText(el) {
    if (!el) return null;
    const text = (el.innerText || el.textContent || "").trim();
    return text || null;
  }

  function extractMetricsFromAriaLabel(label) {
    const out = {
      replies: null,
      retweets: null,
      likes: null,
      views: null,
      bookmarks: null,
    };
    if (!label) return out;

    // Examples:
    // "1 reply, 8 reposts, 67 likes, 52 bookmarks, 9560 views"
    // "2 likes, 52 views"
    const patterns = [
      { key: "replies", re: /([\d.,]+[KMB]?)\s+repl(?:y|ies)\b/i },
      { key: "retweets", re: /([\d.,]+[KMB]?)\s+(?:reposts|retweets)\b/i },
      { key: "likes", re: /([\d.,]+[KMB]?)\s+likes?\b/i },
      { key: "views", re: /([\d.,]+[KMB]?)\s+views?\b/i },
      { key: "bookmarks", re: /([\d.,]+[KMB]?)\s+bookmarks?\b/i },
    ];

    for (const { key, re } of patterns) {
      const m = label.match(re);
      if (m) out[key] = parseCompactNumber(m[1]);
    }
    return out;
  }

  function extractMetricFromControl(controlEl, metricName) {
    if (!controlEl) return null;

    // Prefer aria-label (it usually includes full number and name)
    const aria = controlEl.getAttribute("aria-label");
    if (aria) {
      const metrics = extractMetricsFromAriaLabel(aria);
      if (metrics[metricName] != null) return metrics[metricName];
    }

    // Fallback: visible count text
    const countSpan = controlEl.querySelector(
      '[data-testid="app-text-transition-container"]'
    );
    const raw = safeText(countSpan);
    return parseCompactNumber(raw);
  }

  function getTweetIdFromArticle(articleEl) {
    // Prefer direct status URL, avoid analytics URL.
    const statusLink = articleEl.querySelector(
      'a[href*="/status/"]:not([href*="/analytics"])'
    );
    if (!statusLink) return null;
    const href = statusLink.getAttribute("href") || "";
    const m = href.match(/\/status\/(\d+)/);
    return m ? m[1] : null;
  }

  function getAuthorHandle(articleEl) {
    // Usually @handle appears near name area.
    const nameBlock = articleEl.querySelector('[data-testid="User-Name"]');
    if (!nameBlock) return null;
    const text = safeText(nameBlock);
    if (!text) return null;

    const m = text.match(/@([A-Za-z0-9_]+)/);
    return m ? `@${m[1]}` : null;
  }

  function extractTweetRecord(articleEl) {
    const tweetId = getTweetIdFromArticle(articleEl);
    if (!tweetId) return null;

    const textEl = articleEl.querySelector('[data-testid="tweetText"]');
    const timeEl = articleEl.querySelector("time[datetime]");

    const groupEl = articleEl.querySelector('[role="group"][aria-label]');
    const groupMetrics = extractMetricsFromAriaLabel(
      groupEl ? groupEl.getAttribute("aria-label") : null
    );

    const repliesBtn = articleEl.querySelector('button[data-testid="reply"]');
    const retweetBtn = articleEl.querySelector('button[data-testid="retweet"]');
    const likeBtn = articleEl.querySelector('button[data-testid="like"]');
    const viewsLink = articleEl.querySelector('a[href*="/analytics"]');
    const bookmarkBtn = articleEl.querySelector('button[data-testid="bookmark"]');

    const replies =
      extractMetricFromControl(repliesBtn, "replies") ?? groupMetrics.replies;
    const retweets =
      extractMetricFromControl(retweetBtn, "retweets") ?? groupMetrics.retweets;
    const likes =
      extractMetricFromControl(likeBtn, "likes") ?? groupMetrics.likes;
    const views =
      extractMetricFromControl(viewsLink, "views") ?? groupMetrics.views;
    const bookmarks =
      extractMetricFromControl(bookmarkBtn, "bookmarks") ?? groupMetrics.bookmarks;

    return {
      tweetId,
      url: `https://x.com/i/web/status/${tweetId}`,
      authorHandle: getAuthorHandle(articleEl),
      createdAt: timeEl ? timeEl.getAttribute("datetime") : null,
      text: safeText(textEl),
      likes,
      retweets,
      replies,
      views,
      bookmarks,
      scrapedAt: new Date().toISOString(),
    };
  }

  function mergeRecord(oldRec, newRec) {
    if (!oldRec) return newRec;
    const merged = { ...oldRec, ...newRec };

    // Keep max for counters in case of partial load/state transitions.
    for (const key of ["likes", "retweets", "replies", "views", "bookmarks"]) {
      const oldV = oldRec[key];
      const newV = newRec[key];
      if (oldV == null) merged[key] = newV;
      else if (newV == null) merged[key] = oldV;
      else merged[key] = Math.max(oldV, newV);
    }
    return merged;
  }

  function scrapeVisibleTweets() {
    const articles = document.querySelectorAll('article[data-testid="tweet"]');
    let seenThisPass = 0;
    let addedThisPass = 0;

    for (const article of articles) {
      const rec = extractTweetRecord(article);
      if (!rec) continue;
      seenThisPass += 1;
      const prev = state.byTweetId.get(rec.tweetId);
      if (!prev) addedThisPass += 1;
      state.byTweetId.set(rec.tweetId, mergeRecord(prev, rec));
    }
    return { seenThisPass, addedThisPass, total: state.byTweetId.size };
  }

  function printStatus(prefix) {
    const elapsedSec = Math.round((Date.now() - state.startedAt) / 1000);
    console.log(
      `[TwitterTimelineScraper] ${prefix} total=${state.byTweetId.size} elapsed=${elapsedSec}s`
    );
  }

  function startScrape(options = {}) {
    if (state.running) {
      console.warn("[TwitterTimelineScraper] Already running.");
      return;
    }

    const {
      scrapeIntervalMs = 2000,
      statusIntervalMs = 5000,
      autoScroll = true,
      scrollIntervalMs = 1500,
      scrollStepPx = 1400,
    } = options;

    state.running = true;
    state.startedAt = Date.now();

    // Immediate scrape so you get first snapshot quickly.
    const first = scrapeVisibleTweets();
    printStatus(`start seen=${first.seenThisPass} added=${first.addedThisPass}`);

    state.scrapeTimer = setInterval(() => {
      const s = scrapeVisibleTweets();
      if (s.addedThisPass > 0) {
        printStatus(`scrape seen=${s.seenThisPass} added=${s.addedThisPass}`);
      }
    }, scrapeIntervalMs);

    state.statusTimer = setInterval(() => {
      printStatus("heartbeat");
    }, statusIntervalMs);

    if (autoScroll) {
      state.scrollTimer = setInterval(() => {
        window.scrollBy(0, scrollStepPx);
      }, scrollIntervalMs);
    }

    console.log(
      "[TwitterTimelineScraper] Started. Call TwitterTimelineScraper.stopScrape() when done."
    );
  }

  function stopScrape() {
    if (!state.running) {
      console.warn("[TwitterTimelineScraper] Not running.");
      return;
    }
    state.running = false;
    if (state.scrapeTimer) clearInterval(state.scrapeTimer);
    if (state.statusTimer) clearInterval(state.statusTimer);
    if (state.scrollTimer) clearInterval(state.scrollTimer);
    state.scrapeTimer = null;
    state.statusTimer = null;
    state.scrollTimer = null;
    printStatus("stopped");
  }

  function getData() {
    return Array.from(state.byTweetId.values()).sort((a, b) => {
      // Sort most recent scraped first
      return String(b.scrapedAt).localeCompare(String(a.scrapedAt));
    });
  }

  function downloadJSON(filename = "twitter_timeline_metrics.json") {
    const payload = {
      exportedAt: new Date().toISOString(),
      count: state.byTweetId.size,
      rows: getData(),
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
    console.log(`[TwitterTimelineScraper] Downloaded ${filename}`);
  }

  function clearData() {
    state.byTweetId.clear();
    console.log("[TwitterTimelineScraper] Cleared collected rows.");
  }

  global.TwitterTimelineScraper = {
    startScrape,
    stopScrape,
    getData,
    downloadJSON,
    clearData,
  };

  console.log(
    "[TwitterTimelineScraper] Ready. Use startScrape(), stopScrape(), getData(), downloadJSON()."
  );
})(window);
