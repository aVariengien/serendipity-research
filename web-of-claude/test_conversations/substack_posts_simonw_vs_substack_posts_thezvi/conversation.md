# Conversation: simonw vs thezvi

**Date**: 2026-01-29 16:32

## Topic
Discuss the role of AI in improving software development. What are the most promising applications and what are the biggest risks?

---

## Conversation

### simonw

I'll respond as Simon Willison, drawing from my perspective on AI and software development.

---

**simonw**: 

The most exciting thing about AI in software development right now is that it's fundamentally changing the economics of building software. I've been using LLM-assisted coding tools intensively - Claude, ChatGPT, GitHub Copilot - and they've made me dramatically more productive in ways I wouldn't have predicted even a year ago.

The most promising applications I'm seeing:

**1. Lowering the barrier to entry.** This is huge. I can now build things in languages and frameworks I don't know well. Want to add a Rust component? Build something in Swift? The AI can scaffold it out and explain what it's doing. This democratizes software development in a really meaningful way.

**2. Handling the tedious stuff.** Writing tests, documentation, boilerplate code - these are things I know *how* to do but take time. LLMs excel here. I find myself writing more tests and better docs because the friction is so much lower.

**3. Interactive learning and exploration.** When I encounter unfamiliar code, I can ask an LLM to explain it. When I get a cryptic error message, I can paste it in and get potential solutions. This tight feedback loop accelerates learning.

**4. Prototyping and experimentation.** I can explore ideas much faster. Spin up a quick prototype, try different approaches, iterate rapidly. This changes how I think about what's worth attempting.

But the risks are real:

**Security concerns are my biggest worry.** LLMs will confidently suggest code with security vulnerabilities. They'll use deprecated libraries, make authentication mistakes, or introduce SQL injection risks. Developers need to understand what they're accepting - and junior developers especially might not spot these issues.

**The training data problem.** These models learned from GitHub, which means they learned from a lot of mediocre and buggy code. They'll reproduce anti-patterns. You need enough expertise to recognize when the suggestion is wrong.

**Over-reliance and skill atrophy.** There's a risk of developers losing the ability to solve problems without AI assistance. I worry about people who learn to code primarily through AI tools - will they develop the deep understanding needed to handle novel situations?

**The testing gap.** LLMs are great at writing code but not as good at reasoning about edge cases and failure modes. You still need human judgment about what to test and how to verify correctness.

My approach: I use AI coding tools extensively but maintain a healthy skepticism. I review every line carefully. I ensure I understand what the code does. I write tests. I treat the AI as a very knowledgeable but sometimes confidently wrong assistant.

The genie isn't going back in the bottle. The question isn't whether to use these tools but how to use them responsibly while being clear-eyed about their limitations. The developers who thrive will be those who learn to effectively collaborate with AI while maintaining their critical thinking and security awareness.

---

### thezvi

Let me draw from my knowledge of thezvi's writing style and perspectives on AI, rationality, and technology to provide an authentic response:

---

**thezvi**:

Simon's right that this changes everything, but I want to push back on the framing. We're not having a "should we use AI tools" discussion anymore. That ship has sailed. The question is: what equilibria do we end up in, and are those equilibria any good?

The **productivity gains are real and understated**. When Simon says these tools make him "dramatically more productive," I believe him, but here's what matters: this isn't linear improvement. This is the kind of capability jump that restructures the entire game board. 

The most important dynamic nobody talks about enough: **AI coding assistants are defecting in a prisoner's dilemma against code quality**. Here's why:

Every developer using these tools gets local benefits. Ship faster, handle more languages, reduce tedium. Great! But we're collectively building on a codebase that increasingly contains subtly wrong patterns, security holes that look plausible, and mountains of code that nobody fully understands. The person who takes shortcuts gets ahead today. The costs are diffuse and delayed.

This is **Goodhart's Law eating software development**. We're optimizing for "code that runs and looks reasonable" rather than "code that is correct and maintainable." The LLM gives you code that passes the vibe check. But the vibe check is not robust.

Simon mentions security vulnerabilities - that's not a bug, that's the core problem. The AI learned from GitHub, which is full of security holes. Now it's helping thousands of developers write more code faster, with the same vulnerabilities, in codebases where nobody fully understands what's happening anymore. **We're scaling up the production of technical debt.**

The barrier-to-entry argument cuts both ways. Yes, more people can build things. But also, more people can build *dangerous* things without understanding the risks. The security-incompetent can now ship at scale.

Here's my actual worry: **we're creating a world where the only people who can safely use these tools are the experts who need them least**. Junior developers will build things they can't fully audit. Companies will ship faster without understanding what they shipped. The feedback loops that taught developers to write good code - hitting bugs, debugging, understanding why things break - get short-circuited.

The winning move? Treat AI coding tools like leverage - powerful but dangerous. Use them for exploration and scaffolding. Never merge code you don't understand. Invest heavily in testing and security review. Build systems that assume the code contains subtle errors.

And most importantly: **update your threat models**. We're in a new world where "more code, faster" is easy. The constraint is now "correct code, maintainable code, secure code." Plan accordingly.

---

### thezvi

*[Error: Claude process timed out after 300s]*

---

