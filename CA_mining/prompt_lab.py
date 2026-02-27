# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "streamlit",
#   "openai",
# ]
# ///

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st
from openai import OpenAI, RateLimitError, APIError

USERS_DIR = Path(__file__).parent / "outputs" / "users"
VERSIONS_FILE = Path(__file__).parent / "prompt_versions.json"
MODEL = "zai-glm-4.7"
CHARS_PER_TOKEN = 4
CHUNK_SIZE_CHARS = 50_000 * CHARS_PER_TOKEN  # 200_000

DEFAULT_USERS = ["A_Variengien", "exgenesis", "ValsTutor"]

DEFAULT_EXTRACT = """\
You are extracting the intellectual portrait of a Twitter user from their tweets.

Your goal: find the JUICE. Not a summary — a portrait of what's alive to them.

Weight costly signals heavily:
- Long tweets and threads = they spent real mental effort here
- Topics that appear at multiple distinct time points = persistent obsession, not just reaction
- Sources, papers, people, links they cite with genuine engagement (not just casual mention)
- Arguments they make repeatedly = deep conviction
- Questions they keep asking = live uncertainty

Output a compact, dense portrait in markdown. Use their actual words and phrases.
No padding. No generic observations. Favor specificity.

## What's Alive Right Now
The 2-4 topics they're most actively thinking/writing about in the most recent tweets.

## Recurring Obsessions
Themes that appear across multiple time periods — what they keep returning to.

## Sources & Things That Struck Them
Papers, books, people, links, ideas they reference with genuine engagement. Be specific.

## Their Vocabulary
The distinctive words, phrases, and framings they use. What conceptual language is theirs?

## Where They Spend Real Time
Their longest threads and most elaborated thoughts. What did they work through carefully?\
"""

DEFAULT_SYNTHESIS = """\
You have partial analyses of a Twitter user's tweets from multiple chunks.
Synthesize into a single, coherent intellectual portrait.

Prioritize:
- What appears in MULTIPLE chunks = persistent signal
- Costly elaborated thinking (threads, long arguments)
- Distinctive vocabulary that recurs

Collapse redundancy. Preserve specificity. Use their actual words.

Output the same sections as the input analyses, but unified and distilled.

## What's Alive Right Now
## Recurring Obsessions
## Sources & Things That Struck Them
## Their Vocabulary
## Where They Spend Real Time\
"""


# ── prompt version store ──────────────────────────────────────────────────────

def load_versions() -> list[dict]:
    if not VERSIONS_FILE.exists():
        return []
    try:
        return json.loads(VERSIONS_FILE.read_text())
    except Exception:
        return []


def save_version(label: str, extract: str, synthesis: str) -> None:
    versions = load_versions()
    versions.insert(0, {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "label": label.strip() or "(no label)",
        "extract": extract,
        "synthesis": synthesis,
    })
    VERSIONS_FILE.write_text(json.dumps(versions, indent=2))


def version_display(v: dict) -> str:
    return f"{v['ts']}  —  {v['label']}"


# ── analysis helpers ──────────────────────────────────────────────────────────

def get_available_users() -> list[str]:
    return sorted(p.stem for p in USERS_DIR.glob("*.md"))


def load_user_file(username: str) -> str | None:
    path = USERS_DIR / f"{username}.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE_CHARS) -> list[str]:
    if len(text) <= chunk_size:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end >= len(text):
            chunks.append(text[start:])
            break
        sep = text.rfind("\n---\n", start + chunk_size // 2, end)
        if sep != -1:
            end = sep + 5
        chunks.append(text[start:end])
        start = end
    return chunks


def call_api(client: OpenAI, system: str, user: str) -> str:
    delay = 5
    last_exc: Exception | None = None
    for attempt in range(5):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                max_tokens=10_000,
                temperature=0.7,
            )
            return response.choices[0].message.content or ""
        except (RateLimitError, APIError) as e:
            last_exc = e
            if attempt == 4:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 60)
        except Exception:
            raise
    raise RuntimeError("All retries failed") from last_exc


def run_analysis(
    client: OpenAI,
    username: str,
    extract_prompt: str,
    synthesis_prompt: str,
    status_placeholder,
) -> str:
    text = load_user_file(username)
    if text is None:
        return f"❌ No file found for `{username}` in `outputs/users/`"

    file_chars = len(text)
    chunks = chunk_text(text)
    n = len(chunks)
    approx_tokens = file_chars // CHARS_PER_TOKEN

    status_placeholder.info(
        f"**@{username}** — {file_chars:,} chars (~{approx_tokens:,} tokens), {n} chunk(s)"
    )

    if n == 1:
        status_placeholder.info("Calling GLM 4.7…")
        result = call_api(client, extract_prompt, f"Twitter user: @{username}\n\n{chunks[0]}")
    else:
        partial: list[str] = []
        for i, chunk in enumerate(chunks, 1):
            status_placeholder.info(f"Analyzing chunk {i}/{n}…")
            partial.append(
                call_api(
                    client,
                    extract_prompt,
                    f"Twitter user: @{username} — part {i}/{n}\n\n{chunk}",
                )
            )
        status_placeholder.info("Synthesizing chunks…")
        combined = "\n\n---\n\n".join(
            f"### Part {i + 1}\n{a}" for i, a in enumerate(partial)
        )
        result = call_api(
            client,
            synthesis_prompt,
            f"Twitter user: @{username}\n\nPartial analyses:\n\n{combined}",
        )

    status_placeholder.empty()
    return result


# ── page ──────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Prompt Lab", layout="wide")
st.title("Prompt Lab — User Portrait")

# ── API key ───────────────────────────────────────────────────────────────────
api_key = os.environ.get("CEREBRAS_API_KEY", "")
if not api_key:
    api_key = st.sidebar.text_input("Cerebras API key", type="password")
if not api_key:
    st.warning("Set `CEREBRAS_API_KEY` env var or enter it in the sidebar.")
    st.stop()

client = OpenAI(api_key=api_key, base_url="https://api.cerebras.ai/v1")

# ── session state defaults ────────────────────────────────────────────────────
if "extract" not in st.session_state:
    st.session_state["extract"] = DEFAULT_EXTRACT
if "synthesis" not in st.session_state:
    st.session_state["synthesis"] = DEFAULT_SYNTHESIS

# ── sidebar: version picker ───────────────────────────────────────────────────
st.sidebar.header("Prompt versions")

versions = load_versions()
version_labels = [version_display(v) for v in versions]

if versions:
    selected_idx = st.sidebar.selectbox(
        "Saved versions",
        options=range(len(versions)),
        format_func=lambda i: version_labels[i],
        index=0,
    )
    if st.sidebar.button("⬆ Load selected version"):
        st.session_state["extract"] = versions[selected_idx]["extract"]
        st.session_state["synthesis"] = versions[selected_idx]["synthesis"]
        st.rerun()
else:
    st.sidebar.caption("No saved versions yet.")

st.sidebar.divider()

# ── sidebar: save current ─────────────────────────────────────────────────────
st.sidebar.subheader("Save current prompts")
save_label = st.sidebar.text_input("Label (optional)", placeholder="e.g. shorter sections")
if st.sidebar.button("💾 Save"):
    save_version(save_label, st.session_state["extract"], st.session_state["synthesis"])
    st.sidebar.success("Saved!")
    st.rerun()

st.sidebar.divider()

# ── sidebar: prompt editors ───────────────────────────────────────────────────
st.sidebar.subheader("Edit prompts")

st.sidebar.text_area(
    "Extract system prompt",
    key="extract",
    height=380,
)
st.sidebar.text_area(
    "Synthesis prompt (multi-chunk only)",
    key="synthesis",
    height=220,
)

if st.sidebar.button("↺ Reset to defaults"):
    st.session_state["extract"] = DEFAULT_EXTRACT
    st.session_state["synthesis"] = DEFAULT_SYNTHESIS
    st.rerun()

# ── main: user selection ──────────────────────────────────────────────────────
col_pick, col_custom = st.columns([2, 2])

with col_pick:
    st.subheader("Pick a user")
    chosen = st.radio("Quick select", DEFAULT_USERS, horizontal=True)

with col_custom:
    st.subheader("Or type a handle")
    available = get_available_users()
    custom = st.selectbox(
        "Search / type handle",
        options=[""] + available,
        index=0,
        placeholder="start typing…",
    )

username = (custom.lstrip("@").strip() if custom else None) or chosen
st.caption(f"Selected: **@{username}**")

# ── run ───────────────────────────────────────────────────────────────────────
run_btn = st.button("▶ Run analysis", type="primary")

status = st.empty()
result_area = st.container()

if run_btn:
    with st.spinner(f"Running on @{username}…"):
        try:
            result = run_analysis(
                client, username,
                st.session_state["extract"],
                st.session_state["synthesis"],
                status,
            )
            with result_area:
                st.markdown("---")
                if result:
                    st.markdown(result)
                else:
                    st.warning("Model returned an empty response.")
        except Exception as e:
            status.empty()
            st.error(f"**Error:** {type(e).__name__}: {e}")
