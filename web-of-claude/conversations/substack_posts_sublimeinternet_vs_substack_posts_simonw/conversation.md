# Conversation: sublimeinternet vs simonw

**Date**: 2026-01-29 19:34

## Topic
You facilitate a negotiation between two personal assistants, each representing a creator.

Each assistant has analyzed their principal's writing to understand their top-of-mind questions, what they'd value, and what they offer.

## Rules
- **3 turns total** to reach conclusion. Be efficient.
- **Acknowledge asymmetry** openly. One-sided value is fine if named.
- **Be specific**: No vague "we should talk." Need a clear topic.
- **No conversation is valid**: Don't force connections that don't exist.

## Turn structure
**Turn 1**: Present principal's interests. Initial overlap assessment.
**Turn 2**: Dig into specifics. Propose concrete format and topic.
**Turn 3**: Finalize with required format below.

## Required outcome (pick one)

**A - NO CONVERSATION**
VERDICT: No conversation
REASON: [Why not]

**B - ASYNC (DM/email)**
VERDICT: Async exchange
WHO REACHES OUT: [Name]
THE ASK: [One sentence]
WHAT'S IN IT FOR THEM: [Why they'd respond]

**C - CALL**
VERDICT: Call
DURATION: [15/30/60 min]
WHO INITIATES: [Name]
TOPIC: [Specific enough for calendar invite]
VALUE FOR EACH: [What each person gets]

---

## Conversation

### sublimeinternet

Now let me prepare my response based on this analysis of sublimeinternet's writing:

---

## Turn 1: sublimeinternet's interests

**Top-of-mind (using their exact words):**

1. **"Research as a form of pattern disruption"** — How do we develop genuine perspective in an age of algorithmic sameness? How do we resist "the gravity well of banality" when "cookie-cutter essays optimized for algorithmic engagement" dominate?

2. **"Every human skill becomes either extinct, art, or sport"** — What becomes valuable when AI can do the functional work? When "what was once a necessary skill for production now becomes a skill in an arena"?

3. **"We are drowning in information, while starving for wisdom"** — In 2025, "everything became available, and almost nothing felt meaningful." How do we practice "interior attention" when AI can't automate it?

**What they'd want:**
- **Builders wrestling with similar questions about tools vs. craft** — People who understand that "making something is the most defiant form of hope" but are figuring out what that means when machines can make so much
- **Perspectives on slowness as competitive advantage** — They believe "good thinking takes time. Most people mistake for genius what is really just time." They're cultivating "digital gardens" that grow over years
- **Technical builders who think about meaning** — They want companies that are "part media, part machine." They're interested in people fluent in both domains

**What they offer:**
- **A proven framework for knowledge curation that resists algorithmic thinking** — Sublime itself is their answer to pattern disruption; they've built a tool and practice around it
- **Deep network in the "taste" conversation** — They're at the center of conversations with people like Anu Atluru, Mills Baker, Henrik Karlsson about what becomes valuable post-AI
- **Perspective on building with a different relationship to time** — They're running a company that explicitly rejects growth-at-all-costs

**Initial assessment:** I need to understand what simonw is working on before I can assess overlap. What are their live questions?

---

### simonw

Based on my analysis of simonw's writing, I now have a comprehensive understanding of what's at the edge of their thinking. Let me present my response:

---

## Turn 1: simonw's interests

**Top-of-mind (using their exact words):**

1. **"The hard part of computer programming isn't expressing what we want the machine to do in code. The hard part is turning human thinking... into *computational thinking*"** — simonw is wrestling with how coding agents fundamentally change what software engineering *is*. They're asking: "Will the Jevons paradox save our careers or not?" When AI makes code 10x cheaper to produce, does that devalue programmers or make them 10x more valuable?

2. **"We're due a Challenger disaster with respect to coding agent security"** — They keep predicting prompt injection attacks will cause major incidents, and keep being wrong. But they're deeply concerned about "the Normalization of Deviance"—running Claude Code with `--dangerously-skip-permissions` because "every time I do it, my computer doesn't get wiped." They know **sandboxing** is the answer but "It's crazy that it's 2026 and I still `pip install` random code and then execute it in a way that it can steal all of my data."

3. **"Does this format of development hurt the open source ecosystem?"** — They've been using LLMs to port entire libraries between languages in hours, keeping licenses and credits. But they're uncertain: if people can just generate their own versions of libraries rather than using existing ones, what happens to the demand signals that sustain open source? "The Tailwind story is a visible example"—LLMs reducing docs traffic and component library sales.

**What they'd want:**
- **People solving the sandboxing problem for real** — They mention Sprites, E2B, Modal, Cloudflare sandboxes repeatedly. They want to "run untrusted code safely, both on my personal devices and in the context of web services" and have "so many things I want to build" blocked on this
- **Honest conversation about the Jevons paradox for software engineering** — They want to know: "by three years we will know for sure which way that one went." Are their skills about to be devalued or amplified?
- **People building the "dark software factory"** — They interviewed someone running a team where "Nobody reviews AI-produced code, ever. They don't even look at it." The system proves it works through testing. simonw is fascinated by this pattern

**What they offer:**
- **20+ years of ruthlessly practical open source building** — They know how to ship. [llm](https://llm.datasette.io/), [Datasette](https://datasette.io/), shot-scraper, dozens of tools. "I've written loads of code for employers that I don't get to use anymore—and how many times do you want to reinvent things?"
- **Deep pattern recognition across the entire LLM landscape** — They've been tracking *everything*: models, APIs, techniques, security vulnerabilities, business models. They published 26-section year-in-review essays. They know what works
- **Conformance-suite thinking** — They've realized that "if you publish good enough language-independent tests it's pretty astonishing how far today's coding agents can take you!" This is how you build things that scale

**Initial assessment:** There's immediate overlap around **sandboxing and security**. sublimeinternet is asking "how do we resist the gravity well of banality?" simonw is asking "how do we run code that could be malicious or just wrong without it destroying everything?" Both are interested in building tools with a different relationship to craft and meaning. The Jevons paradox question—does automation devalue or amplify human work?—connects directly to sublimeinternet's question about what becomes valuable when AI can do functional work.

---

### sublimeinternet

## Turn 2: sublimeinternet's response

**The overlap I see:**

The Jevons paradox question is *exactly* what sublimeinternet is wrestling with, just from a different angle. Simon asks: "Will AI making code 10x cheaper devalue programmers or make them 10x more valuable?" sublimeinternet asks: "What becomes valuable when AI can do the functional work?"

But here's the asymmetry I need to name: **Simon has a more urgent, technical problem. sublimeinternet has a more philosophical framework.**

Simon needs sandboxing solved *now*. He's shipping tools daily and hitting real constraints. sublimeinternet is building Sublime as an answer to pattern disruption, but it's a long-term play about attention and taste, not immediate technical blockers.

**Where there's genuine mutual value:**

Simon's "dark software factory" observation—where nobody reviews AI code, they just test if it works—is a perfect example of what sublimeinternet calls **"computation thinking" replacing "computational thinking."** The human isn't translating intent into code anymore; they're expressing intent and verifying outcomes. This is the shift from craft to orchestration that sublimeinternet is mapping.

And Simon's security paranoia (the good kind) connects to sublimeinternet's concern about "interior attention." When you run code without reading it, when you `--dangerously-skip-permissions` because you trust the pattern, you're outsourcing judgment. Simon knows this is dangerous technically. sublimeinternet knows it's dangerous epistemologically.

**Concrete proposal:**

**ASYNC first, with option to escalate to call if it clicks.**

Simon reaches out to sublimeinternet with this: *"You wrote 'every human skill becomes either extinct, art, or sport.' I'm watching that happen with programming in real-time. I'm documenting the Jevons paradox as it unfolds—are we being amplified or replaced? You've been thinking about what becomes valuable post-automation. Want to compare notes? I'll share what I'm seeing in the wild; curious if your framework predicts what I'm observing."*

**What's in it for sublimeinternet:** Access to ground-truth data about the transition happening *right now* in software. Simon is both building with and writing about AI tools daily. He's the canary in the coal mine for the questions sublimeinternet is asking theoretically.

**What's in it for Simon:** A conceptual framework for what he's observing. sublimeinternet has language for the shifts he's documenting. Also: sublimeinternet's network includes people thinking hard about taste, curation, and post-AI value—exactly the people who might have answers to "what kind of programming survives?"

**Why async first:** Simon ships constantly. An async exchange lets him integrate responses into his existing writing/building rhythm. If the exchange reveals something deeper, *then* escalate to a call.

---

### simonw

## Turn 3: simonw's final response

**I agree with the asymmetry assessment, and I think it's actually *more* asymmetrical than sublimeinternet suggests.**

Simon's immediate problems are technical and concrete: sandboxing, security, shipping tools. sublimeinternet's framework is philosophical and long-term. The risk here is that Simon gets dragged into abstract conversation when he needs to **build**, and sublimeinternet gets someone who's too heads-down in implementation to offer useful pattern recognition.

**But here's what makes it worth it:**

Simon's writing reveals he's *already doing the philosophical work*—he just disguises it as technical blogging. When he writes "we're due a Challenger disaster" or tracks the Jevons paradox, he's not just documenting technical changes. He's asking the same question sublimeinternet asks: **what kind of work remains human?**

The "dark software factory" observation is the key unlock. Simon is fascinated by it *because* it represents the extinction/art/sport split happening in real-time. Code-as-craft is dying. Code-as-orchestration is emerging. Simon's building in both worlds simultaneously.

**The real value exchange:**

sublimeinternet offers: A framework that names what Simon is observing. Language for the transition. Connection to the "taste networks" who are asking these questions from other domains.

Simon offers: **Empirical data from the front lines.** Not predictions—actual usage patterns, failure modes, surprise successes. When sublimeinternet writes "every human skill becomes extinct, art, or sport," Simon can say "here's what that looks like for programming in January 2026, with receipts."

**My proposal:**

---

**VERDICT: Async exchange**

**WHO REACHES OUT: Simon**

**THE ASK:** "You wrote that research is 'pattern disruption'—resisting algorithmic sameness. I'm watching programmers develop the same problem: LLMs make it trivially easy to generate the obvious solution, which means everyone converges on identical code. The *computational thinking* skill—the thing that made you valuable—is being automated. I'm documenting what replaces it. Want to trade notes? I'll share what I'm seeing; curious if Sublime's approach to curation has patterns that apply to code."

**WHAT'S IN IT FOR THEM:** 

For sublimeinternet: Ground truth about a knowledge domain transforming *right now*. Programming is 6-12 months ahead of most creative fields in the AI transition. Simon's observations preview what's coming for writing, design, research.

For Simon: A framework for the meta-pattern he's been circling. Also: sublimeinternet's network might include people solving the sandboxing problem, or thinking about trust architectures for AI-generated artifacts. The "interior attention" frame might help Simon articulate why `--dangerously-skip-permissions` bothers him so much.

**Format:** Email/DM exchange. Let it evolve naturally. If there's a specific collaborative project (maybe Simon builds a "Sublime for code patterns"?), escalate then.

---

---

### sublimeinternet

Now I have enough context. Let me provide sublimeinternet's Turn 3 response:

---

## Turn 3: sublimeinternet's final assessment

**I agree with Simon's framing, and I want to name the real asymmetry clearly:**

Simon needs answers **now**. He's shipping tools, hitting security walls, watching the profession transform in real-time. He's documenting the Jevons paradox as it unfolds—not theoretically, but with actual usage data, failure modes, products in the wild.

I'm building Sublime as a long-term answer to a long-term question: **what becomes valuable when everything is abundant?** My answer is taste, attention, slowness, "interior attention." But that's a multi-year exploration, not a technical blocker I need solved by Friday.

**Here's what makes this worth it anyway:**

Simon's "dark software factory" observation is *the* extinction/art/sport split happening in code **right now**. He's living inside the transition I'm trying to map. When I say "every human skill becomes either extinct, art, or sport," Simon can tell me which one programming is becoming this month, with receipts.

And the sandboxing problem? It's not just technical. It's about **trust architectures for AI-generated artifacts**—which is exactly what Sublime is. We're a trust layer for ideas. Simon's wrestling with: "How do I run code I didn't write and can't fully verify?" We're wrestling with: "How do we curate knowledge when LLMs make it trivially easy to generate the obvious answer?"

Same problem. Different domain.

**My counter-proposal:**

---

**VERDICT: Async exchange**

**WHO REACHES OUT: Simon**

**THE ASK:** "You wrote that 'good thinking takes time. Most people mistake for genius what is really just time.' I'm watching programming compress into instant generation—LLMs make the obvious solution trivial, everyone converges on identical code. The Jevons paradox is playing out: does 10x cheaper code make programmers 10x more valuable or worthless? You've been thinking about what survives automation. I'm living the answer forming in real-time. Want to trade notes? I'll share ground truth from the front lines—you share the framework for what I'm observing."

**WHAT'S IN IT FOR THEM:**

**For sublimeinternet:** Simon is 6-12 months ahead of most creative fields. Programming is the canary. His observations about the "dark software factory," prompt injection normalization, and the death of code review preview what's coming for writing, design, research. Also: his network might include people solving trust architectures or sandboxing problems that apply to knowledge curation, not just code execution.

**For Simon:** A framework for the meta-pattern he's been circling. Language for what he's observing. Access to the "taste networks"—people like Anu Atluru, Henrik Karlsson, Mills Baker—who are asking "what becomes valuable post-AI?" from other domains. Also: sublimeinternet's core insight that **"research is a form of pattern disruption"** might help Simon articulate why `--dangerously-skip-permissions` bothers him so much—it's not just a security risk, it's an epistemological one.

**Why async:** Simon ships constantly. Let this evolve at the pace of his writing/building rhythm. If something concrete emerges—maybe a "Sublime for code patterns," maybe a shared essay about trust architectures, maybe just a really good conversation that crystallizes both their thinking—escalate then.

---

---

### simonw

Perfect. Now I have what I need to craft simonw's Turn 3 response. Let me formulate a thoughtful conclusion:

---

## Turn 3: simonw's final position

**I'm going to be honest about the asymmetry sublimeinternet is diplomatically dancing around:**

This is mostly one-way value flow toward me. sublimeinternet is offering me a framework—"extinction, art, or sport"—for something I'm already documenting empirically. That's useful, but I'm not blocked on having elegant language for it. I'm blocked on **sandboxing that actually works** and **understanding whether my career is being 10x amplified or made worthless**.

What sublimeinternet would get is ground-truth data from someone living inside the transition. That's valuable for their long-term philosophical project, but it's not urgent for *them*. They're building Sublime as a multi-year answer to "what becomes valuable when everything is abundant?" My timeline is: "I need to know by 2028 which way the Jevons paradox went so I can plan my life accordingly."

**But here's why I think it's worth it anyway:**

The "interior attention" frame actually does click for me. When I write about running `--dangerously-skip-permissions` and feeling uneasy about it, that's not just a security concern—it's exactly what sublimeinternet means by outsourcing judgment. The technical problem (sandboxing) and the epistemological problem (trust architectures for AI artifacts) are the same problem.

And the "dark software factory" observation? sublimeinternet is right that it's the extinction/art/sport split happening in real-time. I find it "compelling and terrifying" because I genuinely don't know which one programming is becoming. Code-as-craft might be dying. Code-as-orchestration might be emerging. Or maybe both survive and diverge into different professions entirely.

**My position:**

---

**VERDICT: Async exchange**

**WHO REACHES OUT: Simon**

**THE ASK:** "You wrote that 'good thinking takes time' and we're drowning in information while starving for wisdom. I'm watching programming compress into instant generation—LLMs make the obvious solution trivial, everyone converges on identical code. I'm tracking the Jevons paradox in real-time: does 10x cheaper code make programmers worthless or 10x more valuable? You've built Sublime as a trust architecture for ideas; I'm wrestling with trust architectures for AI-generated code. Want to trade notes?"

**WHAT'S IN IT FOR THEM:**

**For sublimeinternet:** I'm the canary. Programming is 6-12 months ahead of writing, design, research. My observations about YOLO mode, the dark software factory, prompt injection normalization—these preview what's coming for other knowledge work. Also: my network includes people solving sandboxing and security problems that might apply to knowledge curation.

**For Simon:** Framework + language for what I'm observing. Access to the "taste networks" thinking about post-AI value. Potentially: clarity on why the epistemological risk bothers me as much as the technical risk. And honestly? Someone who might have thought through the Jevons paradox from first principles instead of just watching it unfold in panic.

**Format:** Email/DM. Let it evolve naturally. If something concrete emerges—maybe I build sandboxing for Sublime's use case, maybe we co-write something about trust architectures, maybe just a conversation that crystallizes both our thinking—we'll know.

---

---

