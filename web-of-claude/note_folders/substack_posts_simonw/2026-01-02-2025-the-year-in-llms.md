# 2025: The year in LLMs

*Plus introducing gisthost.github.io*

Published: 2026-01-02
Source: https://simonw.substack.com/p/2025-the-year-in-llms

---

In this newsletter:

* 2025: The year in LLMs
* Introducing gisthost.github.io

Plus 5 links and 6 quotations and 1 TIL and 2 notes

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newsletter with my summary of the most important trends of the past 30 days \- here are previews from [August](https://gist.github.com/simonw/43bf3bd7f9951a8e82a9e61b53399ede) and [September](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030).*

### [2025: The year in LLMs](https://simonwillison.net/2025/Dec/31/the-year-in-llms/) \- 2025\-12\-31

This is the third in my annual series reviewing everything that happened in the LLM space over the past 12 months. For previous years see [Stuff we figured out about AI in 2023](https://simonwillison.net/2023/Dec/31/ai-in-2023/) and [Things we learned about LLMs in 2024](https://simonwillison.net/2024/Dec/31/llms-in-2024/).

It’s been a year filled with a *lot* of different trends. The article ended up as 26 sections so I’m not including the whole thing in this email newsletter \- follow one of these section links to read more.

* [The year of “reasoning”](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-reasoning-)
* [The year of agents](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-agents)
* [The year of coding agents and Claude Code](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-coding-agents-and-claude-code)
* [The year of LLMs on the command\-line](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-llms-on-the-command-line)
* [The year of YOLO and the Normalization of Deviance](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-yolo-and-the-normalization-of-deviance)
* [The year of $200/month subscriptions](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-200-month-subscriptions)
* [The year of top\-ranked Chinese open weight models](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-top-ranked-chinese-open-weight-models)
* [The year of long tasks](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-long-tasks)
* [The year of prompt\-driven image editing](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-prompt-driven-image-editing)
* [The year models won gold in academic competitions](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-models-won-gold-in-academic-competitions)
* [The year that Llama lost its way](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-that-llama-lost-its-way)
* [The year that OpenAI lost their lead](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-that-openai-lost-their-lead)
* [The year of Gemini](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-gemini)
* [The year of pelicans riding bicycles](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-pelicans-riding-bicycles)
* [The year I built 110 tools](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-i-built-110-tools)
* [The year of the snitch!](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-the-snitch-)
* [The year of vibe coding](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-vibe-coding)
* [The (only?) year of MCP](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-only-year-of-mcp)
* [The year of alarmingly AI\-enabled browsers](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-alarmingly-ai-enabled-browsers)
* [The year of the lethal trifecta](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-the-lethal-trifecta)
* [The year of programming on my phone](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-programming-on-my-phone)
* [The year of conformance suites](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-conformance-suites)
* [The year local models got good, but cloud models got even better](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-local-models-got-good-but-cloud-models-got-even-better)
* [The year of slop](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-slop)
* [The year that data centers got extremely unpopular](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-that-data-centers-got-extremely-unpopular)
* [My own words of the year](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#my-own-words-of-the-year)
* [That’s a wrap for 2025](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#that-s-a-wrap-for-2025)

---

### [Introducing gisthost.github.io](https://simonwillison.net/2026/Jan/1/gisthost/) \- 2026\-01\-01

I am a huge fan of [gistpreview.github.io](https://gistpreview.github.io/), the site by Leon Huang that lets you append `?GIST_id` to see a browser\-rendered version of an HTML page that you have saved to a Gist. The last commit was ten years ago and I needed a couple of small changes so I’ve forked it and deployed an updated version at [gisthost.github.io](https://gisthost.github.io/).

#### Some background on gistpreview

The genius thing about `gistpreview.github.io` is that it’s a core piece of GitHub infrastructure, hosted and cost\-covered entirely by GitHub, that wasn’t built with any involvement from GitHub at all.

To understand how it works we need to first talk about Gists.

Any file hosted in a [GitHub Gist](https://gist.github.com/) can be accessed via a direct URL that looks like this:

`https://gist.githubusercontent.com/simonw/d168778e8e62f65886000f3f314d63e3/raw/79e58f90821aeb8b538116066311e7ca30c870c9/index.html`

That URL is served with a few key HTTP headers:

```
Content-Type: text/plain; charset=utf-8
X-Content-Type-Options: nosniff
```

These ensure that every file is treated by browsers as plan text, so HTML file will not be rendered even by older browsers that attempt to guess the content type based on the content.

```
Via: 1.1 varnish
Cache-Control: max-age=300
X-Served-By: cache-sjc1000085-SJC
```

These confirm that the file is sever via GitHub’s caching CDN, which means I don’t feel guilty about linking to them for potentially high traffic scenarios.

```
Access-Control-Allow-Origin: *
```

This is my favorite HTTP header! It means I can hit these files with a `fetch()` call from any domain on the internet, which is fantastic for building [HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/) that do useful things with content hosted in a Gist.

The one big catch is that Content\-Type header. It means you can’t use a Gist to serve HTML files that people can view.

That’s where `gistpreview` comes in. The `gistpreview.github.io` site belongs to the dedicated [gistpreview](https://github.com/gistpreview) GitHub organization, and is served out of the [github.com/gistpreview/gistpreview.github.io](https://github.com/gistpreview/gistpreview.github.io) repository by GitHub Pages.

It’s not much code. The key functionality is this snippet of JavaScript from [main.js](https://github.com/gistpreview/gistpreview.github.io/blob/master/main.js):

```
fetch(’https://api.github.com/gists/’ + gistId)
.then(function (res) {
  return res.json().then(function (body) {
    if (res.status === 200) {
      return body;
    }
    console.log(res, body); // debug
    throw new Error(’Gist <strong>’ + gistId + ‘</strong>, ‘ + body.message.replace(/\(.*\)/, ‘’));
  });
})
.then(function (info) {
  if (fileName === ‘’) {
    for (var file in info.files) {
      // index.html or the first file
      if (fileName === ‘’ || file === ‘index.html’) {
        fileName = file;
      }
    }
  }
  if (info.files.hasOwnProperty(fileName) === false) {
    throw new Error(’File <strong>’ + fileName + ‘</strong> is not exist’);
  }
  var content = info.files[fileName].content;
  document.write(content);
})
```

This chain of promises fetches the Gist content from the GitHub API, finds the section of that JSON corresponding to the requested file name and then outputs it to the page like this:

```
document.write(content);
```

This is smart. Injecting the content using `document.body.innerHTML = content` would fail to execute inline scripts. Using `document.write()` causes the browser to treat the HTML as if it was directly part of the parent page.

That’s pretty much the whole trick! Read the Gist ID from the query string, fetch the content via the JSON API and `document.write()` it into the page.

Here’s a demo:

<https://gistpreview.github.io/?d168778e8e62f65886000f3f314d63e3>

#### Fixes for gisthost.github.io

I forked `gistpreview` to add two new features:

1. A workaround for Substack mangling the URLs
2. The ability to serve larger files that get truncated in the JSON API

I also removed some dependencies (jQuery and Bootstrap and an old `fetch()` polyfill) and inlined the JavaScript into [a single index.html file](https://github.com/gisthost/gisthost.github.io/blob/main/index.html).

The Substack issue was small but frustrating. If you email out a link to a `gistpreview` page via Substack it modifies the URL to look like this:

`https://gistpreview.github.io/?f40971b693024fbe984a68b73cc283d2=&utm_source=substack&utm_medium=email`

This breaks `gistpreview` because it treats `f40971b693024fbe984a68b73cc283d2=&utm_source...` as the Gist ID.

The fix is to read everything up to that equals sign. I [submitted a PR](https://github.com/gistpreview/gistpreview.github.io/pull/7) for that back in November.

The second issue around truncated files was [reported against my claude\-code\-transcripts project](https://github.com/simonw/claude-code-transcripts/issues/26#issuecomment-3699668871) a few days ago.

That project provides a CLI tool for exporting HTML rendered versions of Claude Code sessions. It includes a `--gist` option which uses the `gh` CLI tool to publish the resulting HTML to a Gist and returns a gistpreview URL that the user can share.

These exports can get pretty big, and some of the resulting HTML was past the size limit of what comes back from the Gist API.

As of [claude\-code\-transcripts 0\.5](https://github.com/simonw/claude-code-transcripts/releases/tag/0.5) the `--gist` option now publishes to [gisthost.github.io](https://gisthost.github.io/) instead, fixing both bugs.

Here’s [the Claude Code transcript](https://gisthost.github.io/?02ced545666128ce4206103df6185536) that refactored Gist Host to remove those dependencies, which I published to Gist Host using the following command:

```
uvx claude-code-transcripts web --gist
```

---

**Note** [2025\-12\-28](https://simonwillison.net/2025/Dec/28/substack-network-error/)

I just sent out the [latest edition](https://simonw.substack.com/p/a-new-way-to-extract-detailed-transcripts) of the newsletter version of this blog. It’s a long one! Turns out I wrote a lot of stuff in the past 10 days.

The newsletter is out two days later than I had planned because I kept running into an infuriating issue with Substack: it would refuse to save my content with a “Network error” and “Not saved” and I couldn’t figure out why.

[![Screenshot of the Substack UI, with a Network error message on purple and a Not saved message higher up. The content in that editor includes an explanation of a SQL injection vulnerability.](https://substackcdn.com/image/fetch/$s_!xkOk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6985215-5be5-4293-8085-39d8c3e89a14_1550x1562.jpeg "Screenshot of the Substack UI, with a Network error message on purple and a Not saved message higher up. The content in that editor includes an explanation of a SQL injection vulnerability.")](https://substackcdn.com/image/fetch/$s_!xkOk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6985215-5be5-4293-8085-39d8c3e89a14_1550x1562.jpeg)

So I [asked ChatGPT to dig into it](https://chatgpt.com/share/6950ad7d-6948-8006-9833-201d2edff1be), which dug up [this Hacker News](https://news.ycombinator.com/item?id=43793526) post about the string `/etc/hosts` triggering an error.

And yeah, it turns out my newsletter included [this post](https://simonwillison.net/2025/Dec/18/ssrf-clickhouse-postgresql/) describing a SQL injection attack against ClickHouse and PostgreSQL which included the full exploit that was used.

Deleting that annotated example exploit allowed me to send the letter!

---

**Link** 2025\-12\-28 [simonw/actions\-latest](https://github.com/simonw/actions-latest):

Today in extremely niche projects, I got fed up of Claude Code creating GitHub Actions workflows for me that used stale actions: `actions/setup-python@v4` when the latest is `actions/setup-python@v6` for example.

I couldn’t find a good single place listing those latest versions, so I had Claude Code for web (via my phone, I’m out on errands) build a Git scraper to publish those versions in one place:

[https://simonw.github.io/actions\-latest/versions.txt](https://simonw.github.io/actions-latest/versions.txt)

Tell your coding agent of choice to fetch that any time it wants to write a new GitHub Actions workflows.

(I may well bake this into a Skill.)

Here’s the [first](https://gistpreview.github.io/?7883c719a25802afa5cdde7d3ed68b32/index.html) and [second](https://gistpreview.github.io/?0ddaa82aac2c062ff157c7a01db0a274/page-001.html) transcript I used to build this, shared using my [claude\-code\-transcripts](https://simonwillison.net/2025/Dec/25/claude-code-transcripts/) tool (which just [gained a search feature](https://github.com/simonw/claude-code-transcripts/issues/15).)

---

**quote** 2025\-12\-29

> *Jevons paradox is coming to knowledge work. By making it far cheaper to take on any type of task that we can possibly imagine, we’re ultimately going to be doing far more. The vast majority of AI tokens in the future will be used on things we don’t even do today as workers: they will be used on the software projects that wouldn’t have been started, the contracts that wouldn’t have been reviewed, the medical research that wouldn’t have been discovered, and the marketing campaign that wouldn’t have been launched otherwise.*

[Aaron Levie](https://twitter.com/levie/status/2004654686629163154), Jevons Paradox for Knowledge Work

---

**Link** 2025\-12\-29 [Copyright Release for Contributions To SQLite](https://www.sqlite.org/copyright-release.html):

D. Richard Hipp [called me out](https://news.ycombinator.com/item?id=46420453#46424225) for spreading misinformation on Hacker News that SQLite refuses outside contributions:

> No, Simon, we don’t “refuse”. We are just very selective and there is a lot of paperwork involved to confirm the contribution is in the public domain and does not contaminate the SQLite core with licensed code.

I deeply regret this error! I’m linking to the copyright release document here \- it looks like SQLite’s public domain nature makes this kind of clause extremely important:

> \[...] To the best of my knowledge and belief, the changes and enhancements that I have contributed to SQLite are either originally written by me or are derived from prior works which I have verified are also in the public domain and are not subject to claims of copyright by other parties.

Out of curiosity I decided to see how many people have contributed to SQLite outside of the core team of Richard, Dan and Joe. I ran that query using Fossil, SQLite’s own SQLite\-based version control system, like this:

```
brew install fossil
fossil clone https://www.sqlite.org/src sqlite.fossil
fossil sql -R sqlite.fossil "
  SELECT user, COUNT(*) as commits
  FROM event WHERE type='ci'
  GROUP BY user ORDER BY commits DESC
"
```

I got back 38 rows, though I think `danielk1977` and `dan` may be duplicates.

**Update**: The SQLite team have clarified this on their [SQLite is Public Domain](https://sqlite.org/copyright.html) page. It used to read “In order to keep SQLite completely free and unencumbered by copyright, the project does not accept patches.” \- it now reads:

> In order to keep SQLite completely free and unencumbered by copyright, the project does not accept patches from random people on the internet. There is a process to get a patch accepted, but that process is involved and for smaller changes is not normally worth the effort.

---

**quote** 2025\-12\-29

> *The hard part of computer programming isn’t expressing what we want the machine to do in code. The hard part is turning human thinking \-\- with all its wooliness and ambiguity and contradictions \-\- into \*computational thinking\* that is logically precise and unambiguous, and that can then be expressed formally in the syntax of a programming language.   
>   
> That was the hard part when programmers were punching holes in cards. It was the hard part when they were typing COBOL code. It was the hard part when they were bringing Visual Basic GUIs to life (presumably to track the killer’s IP address). And it’s the hard part when they’re prompting language models to predict plausible\-looking Python.   
>   
> The hard part has always been – and likely will continue to be for many years to come – knowing \*exactly\* what to ask for.*

[Jason Gorman](https://codemanship.wordpress.com/2025/11/25/the-future-of-software-development-is-software-developers/), The Future of Software Development Is Software Developers

---

**quote** 2025\-12\-29

> *But once we got that and got this aviation grade testing in place, the number of bugs just dropped to a trickle. Now we still do have bugs but the aviation grade testing allows us to move fast, which is important because in this business you either move fast or you’re disrupted. So, we’re able to make major changes to the structure of the code that we deliver and be confident that we’re not breaking things because we had these intense tests. Probably half the time we spend is actually writing new tests, we’re constantly writing new tests. And over the 17\-year history, we have amassed a huge suite of tests which we run constantly.   
>   
> Other database engines don’t do this; don’t have this   
> level of testing. But they’re still high quality, I mean, I   
> noticed in particular, PostgreSQL is a very high\-quality database engine, they don’t have many bugs. I went to the PostgreSQL and ask them “how do you prevent the bugs”? We talked about this for a while. What I came away with was they’ve got a very elaborate peer review process, and if they’ve got code that has worked for 10 years they just don’t mess with it, leave it alone, it   
> works. Whereas we change our code fearlessly, and we have a much smaller team and we don’t have the peer review process.*

[D. Richard Hipp](https://sigmodrecord.org/publications/sigmodRecord/1906/pdfs/06_Profiles_Hipp.pdf), ACM SIGMOD Record, June 2019 (PDF)

---

**Link** 2025\-12\-29 [shot\-scraper 1\.9](https://github.com/simonw/shot-scraper/releases/tag/1.9):

New release of my [shot\-scraper](https://shot-scraper.datasette.io/) CLI tool for taking screenshots and scraping websites with JavaScript from the terminal.

> * The `shot-scraper har` command has a new `-x/--extract` option which extracts all of the resources loaded by the page out to a set of files. This location can be controlled by the `-o dir/` option. [\#184](https://github.com/simonw/shot-scraper/issues/184)
> * Fixed the `shot-scraper accessibility` command for compatibility with the latest Playwright. [\#185](https://github.com/simonw/shot-scraper/issues/185)

The new `shot-scraper har -x https://simonwillison.net/` command is really neat. The inspiration was [the digital forensics expedition](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/#digital-forensics-with-shot-scraper-har) I went on to figure out why Rob Pike got spammed. You can now perform a version of that investigation like this:

```
cd /tmp
shot-scraper har --wait 10000 'https://theaidigest.org/village?day=265' -x
```

Then dig around in the resulting JSON files in the `/tmp/theaidigest-org-village` folder.

---

**quote** 2025\-12\-30

> *In essence a language model changes you from a programmer who writes lines of code, to a programmer that manages the context the model has access to, prunes irrelevant things, adds useful material to context, and writes detailed specifications. If that doesn’t sound fun to you, you won’t enjoy it.   
>   
> Think about it as if it is a junior developer that has read every textbook in the world but has 0 practical experience with your specific codebase, and is prone to forgetting anything but the most recent hour of things you’ve told it. What do you want to tell that intern to help them progress?   
>   
> Eg you might put sticky notes on their desk to remind them of where your style guide lives, what the API documentation is for the APIs you use, some checklists of what is done and what is left to do, etc.   
>   
> But the intern gets confused easily if it keeps accumulating sticky notes and there are now 100 sticky notes, so you have to periodically clear out irrelevant stickies and replace them with new stickies.*

[Liz Fong\-Jones](https://bsky.app/profile/lizthegrey.com/post/3mb65fnjiis25), thread on Bluesky

---

**TIL** 2025\-12\-30 [Downloading archived Git repositories from archive.softwareheritage.org](https://til.simonwillison.net/github/software-archive-recovery):

Last February I [blogged about](https://simonwillison.net/2025/Feb/7/sqlite-s3vfs/) a neat script called `sqlite-s3vfs` which was released as MIT licensed open source by the UK government’s Department for Business and Trade. …

---

**Link** 2025\-12\-30 [TIL: Downloading archived Git repositories from archive.softwareheritage.org](https://til.simonwillison.net/github/software-archive-recovery):

Back in February I [blogged about](https://simonwillison.net/2025/Feb/7/sqlite-s3vfs/) a neat Python library called `sqlite-s3vfs` for accessing SQLite databases hosted in an S3 bucket, released as MIT licensed open source by the UK government’s Department for Business and Trade.

I went looking for it today and found that the [github.com/uktrade/sqlite\-s3vfs](https://github.com/uktrade/sqlite-s3vfs) repository is now a 404\.

Since this is taxpayer\-funded open source software I saw it as my moral duty to try and restore access! It turns out [a full copy](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/uktrade/sqlite-s3vfs) had been captured by [the Software Heritage archive](https://archive.softwareheritage.org/), so I was able to restore the repository from there. My copy is now archived at [simonw/sqlite\-s3vfs](https://github.com/simonw/sqlite-s3vfs).

The process for retrieving an archive was non\-obvious, so I’ve written up a TIL and also published a new [Software Heritage Repository Retriever](https://tools.simonwillison.net/software-heritage-repo#https%3A%2F%2Fgithub.com%2Fuktrade%2Fsqlite-s3vfs) tool which takes advantage of the CORS\-enabled APIs provided by Software Heritage. Here’s [the Claude Code transcript](https://gistpreview.github.io/?3a76a868095c989d159c226b7622b092/index.html) from building that.

---

**quote** 2025\-12\-30

> *\[...] The puzzle is still there. What’s gone is the labor. I never enjoyed hitting keys, writing minimal repro cases with little insight, digging through debug logs, or trying to decipher some obscure AWS IAM permission error. That work wasn’t the puzzle for me. It was just friction, laborious and frustrating. The thinking remains; the hitting of the keys and the frustrating is what’s been removed.*

[Armin Ronacher](https://lobste.rs/c/xccjtq)

---

**Link** 2025\-12\-31 [Codex cloud is now called Codex web](https://developers.openai.com/codex/cloud/):

It looks like OpenAI’s **Codex cloud** (the cloud version of their Codex coding agent) was quietly rebranded to **Codex web** at some point in the last few days.

Here’s a screenshot of the Internet Archive copy from [18th December](https://web.archive.org/web/20251218043013/https://developers.openai.com/codex/cloud/) (the [capture on the 28th](https://web.archive.org/web/20251228124455/https://developers.openai.com/codex/cloud/) maintains that Codex cloud title but did not fully load CSS for me):

[![Screenshot of the Codex cloud documentation page](https://substackcdn.com/image/fetch/$s_!0cld!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa41beaf3-ae3d-4e63-acda-bdd2ee2c83ca_937x402.jpeg "Screenshot of the Codex cloud documentation page")](https://substackcdn.com/image/fetch/$s_!0cld!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa41beaf3-ae3d-4e63-acda-bdd2ee2c83ca_937x402.jpeg)

And here’s that same page today with the updated product name:

[![Same documentation page only now it says Codex web](https://substackcdn.com/image/fetch/$s_!Cjz3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7341d71-afbe-4772-b0b9-915f326b1ec3_937x302.jpeg "Same documentation page only now it says Codex web")](https://substackcdn.com/image/fetch/$s_!Cjz3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7341d71-afbe-4772-b0b9-915f326b1ec3_937x302.jpeg)

Anthropic’s equivalent product has the incredibly clumsy name [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web), which I shorten to “Claude Code for web” but even then bugs me because I mostly interact with it via Anthropic’s native mobile app.

I was hoping to see Claude Code for web rebrand to Claude Code Cloud \- I did *not* expect OpenAI to rebrand in the opposite direction!

**Update**: [Clarification](https://twitter.com/thsottiaux/status/2006421779246624875) from OpenAI Codex engineering lead Thibault Sottiaux:

> Just aligning the documentation with how folks refer to it. I personally differentiate between cloud tasks and codex web. With cloud tasks running on our hosted runtime (includes code review, github, slack, linear, ...) and codex web being the web app.

I asked what they called Codex in the iPhone app and [he said](https://twitter.com/thsottiaux/status/2006423057179750625):

> Codex iOS

---

**quote** 2026\-01\-02

> *\[Claude Code] has the potential to transform all of tech. I also think we’re going to see a real split in the tech industry (and everywhere code is written) between people who are \*outcome\-driven\* and are excited to get to the part where they can test their work with users faster, and people who are \*process\-driven\* and get their meaning from the engineering itself and are upset about having that taken away.*

[Ben Werdmuller](https://werd.io/2025-the-year-in-llms/)

---

**Note** [2026\-01\-02](https://simonwillison.net/2026/Jan/2/december/)

I sent the December edition of my [sponsors\-only monthly newsletter](https://github.com/sponsors/simonw/). If you are a sponsor (or if you start a sponsorship now) you can [access a copy here](https://github.com/simonw-private/monthly/blob/main/2025-12-december.md). In the newsletter this month:

* An in\-depth review of LLMs in 2025
* My coding agent projects in December
* New models for December 2025
* Skills are an open standard now
* Claude’s “Soul Document”
* Tools I’m using at the moment

Here’s [a copy of the November newsletter](https://gist.github.com/simonw/fc34b780a9ae19b6be5d732078a572c8) as a preview of what you’ll get. Pay $10/month to stay a month ahead of the free copy!

---