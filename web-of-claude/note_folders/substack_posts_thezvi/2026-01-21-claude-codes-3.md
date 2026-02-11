# Claude Codes #3

Published: 2026-01-21
Source: https://thezvi.substack.com/p/claude-codes-3

---

We’re back with all the Claude that’s fit to Code. I continue to have great fun with it and find useful upgrades, but the biggest reminder is that you need the art to have an end other than itself. Don’t spend too long improving your setup, or especially improving how you improve your setup, without actually working on useful things.

#### The Efficient Market Hypothesis

[Odd Lots covered Claude Code](https://x.com/patio11/status/2014043381266006467). Fun episode, but won’t teach my regular readers much that is new.

Bradly Olsen at the Wall Street Journal reports [Claude \[Code and now Cowork are] Taking the AI World By Storm, and ‘Even Non\-Nerds Are Blown Away](https://www.wsj.com/tech/ai/anthropic-claude-code-ai-7a46460e?mod=Searchresults&pos=1&page=1).’

It is remarkable how everyone got the ‘Google is crushing everyone’ narrative going with Gemini 3, then it took them a month to realize that actually Anthropic is crushing everyone, at least among the cognoscenti with growing momentum elsewhere, with Claude Code and Claude Opus 4\.5\. People are realizing you can know almost nothing and still use it to do essentially everything.

Are Claude Code and Codex having a ‘GPT moment’?

> [Wall St Engine](https://x.com/wallstengine/status/2011824292133232817): Morgan Stanley says Anthropic’s ClaudeCode \+ Cowork is dominating investor chatter and adding pressure on software.  
>   
> They flag OpenRouter token growth “going vertical,” plus anecdotes that the Cowork launch pushed usage hard enough to crash Opus 4\.5 and hit rate limits, framing it as another “GPT moment” and a net positive for AI capex.  
>   
> They add that OpenAI sentiment is still shaky: some optimism around a new funding round and Blackwell\-trained models in 2Q, but competitive worries are widening beyond $GOOGL to Anthropic, with Elon Musk saying the OpenAI for\-profit conversion lawsuit heads to trial on April 27\.

#### Huh, Upgrades

[Claude Cowork is now available to Pro subscribers](https://x.com/claudeai/status/2012215329070493971), not only Max subscribers.

Claude Cowork will ask explicit permission before all deletions, add new folders in the directory picker without starting over and make smarter connector suggestions.

[Claude Code on the web gets a good looking diff view](https://x.com/adocomplete/status/2011927756599353763).

[Claude Code for VSCode has now officially shipped](https://x.com/bcherny/status/2013855643149512726), it’s been available for a while. To drag and drop files, hold shift.

[Claude Code now has ‘community events](https://luma.com/claudecommunity)’ in various cities. New York and San Francisco aren’t on the list, but also don’t need to be.

[Claude Code upgraded to 2\.1\.9](https://x.com/ClaudeCodeLog/status/2011988899321589800), and [then to 2\.1\.10 and 2\.1\.11](https://x.com/ClaudeCodeLog/status/2012340283283849487) which were tiny, and [now has reached 2\.1\.14](https://x.com/ClaudeCodeLog/status/2013779041656938862).

Few have properly updated for this sentence: ‘Claude Cowork was built in 1\.5 weeks with Claude Code.’

> [Nabeel S. Qureshi](https://x.com/nabeelqu/status/2011453803498008723): I don’t even see how you can be an AI ‘skeptic’ anymore when the \*current\* AI, right in front of us, is so good, e.g. see Claude Cowork being written by Claude Code in 1\.5 weeks.  
>   
> It’s over, the skeptics were wrong.

[Planning mode now automatically clears context when you accept a plan](https://x.com/adocomplete/status/2013296833871696360).

[Anthropic is developing a new Customize section for Claude](https://www.testingcatalog.com/anthropic-works-on-customizable-commands-for-claude-code/) to centralize Skills, connectors and upcoming commands for Claude Code. My understanding is that custom commands already exist if you want to create them, but reducing levels of friction, including levels of friction in reducing levels of friction, is often highly valuable. A way to browse skills and interact with the files easily, or see and manage your connectors, or an easy interface for defining new commands, seems great.

#### Obsidian

I highly recommend using Obsidian or another similar tool together with Claude Code. This gives you a visual representation of all the markdown files, and lets you easily navigate and search and edit them, and add more and so on. I think it’s well worth keeping it all human readable, where that human is you.

[Heinrich calls it ‘vibe note taking](https://x.com/arscontexta/status/2013655662752862360)’ whether or not you use Obsidian. I think the notes are a place you want to be less vibing and more intentional, and be systematically optimizing the notes, for both Claude Code and for your own use.

[You can combine Obsidian and Claude Code directly via the Obsidian terminal plugin](https://x.com/EleanorKonik/status/2013606992040837465), but I don’t see any mechanical advantage to doing so.

#### New Tools

[Siqi Chen](https://x.com/blader/status/2013031655934697498) offers us [/claude\-continuous\-learning](https://t.co/S48m5wqQGE). Claude’s evaluation is that this could be good if you’re working in codebases where you need to continuously learn things, but the overhead and risk of clutter are real.

[Jasmine Sun created a tool](https://x.com/jasminewsun/status/2012252234831266179) to [turn any YouTube podcast into a clean, grammatical PDF transcript with chapters and takeaways](https://t.co/RBOQJloZEg).

#### Tool Search

The big change with Claude Code version 2\.1\.7 was [enabled MCP tool search auto mode by default](https://x.com/ClaudeCodeLog/status/2011230548572651853), which triggers when MCP tools are more than 10% of the context window. You can disable this by adding ‘MCPSearch’ to ‘disallowedTools’ in settings. This seems big for people using a lot of MCPs at once, which could eat a lot of context.

> Thariq (Anthropic): ​Today we’re rolling out MCP Tool Search for Claude Code.   
>   
> As MCP has grown to become a more popular protocol and agents have become more capable, we’ve found that MCP servers may have up to 50\+ tools and take up a large amount of context.
> 
> Tool Search allows Claude Code to dynamically load tools into context when MCP tools would otherwise take up a lot of context.
> 
> **How it works:**\- Claude Code detects when your MCP tool descriptions would use more than 10% of context  
> \- When triggered, tools are loaded via search instead of preloaded  
>   
> Otherwise, MCP tools work exactly as before. This resolves one of our most\-requested features on GitHub: [lazy loading for MCP servers](https://github.com/anthropics/claude-code/issues/7336). Users were documenting setups with 7\+ servers consuming 67k\+ tokens.  
>   
> **If you’re making a MCP server**Things are mostly the same, but the “server instructions” field becomes more useful with tool search enabled. It helps Claude know when to search for your tools, similar to skills  
>   
> **If you’re making a MCP client**We highly suggest implementing the ToolSearchTool, [you can find the docs here](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool). We implemented it with a custom search function to make it work for Claude Code.  
>   
> **What about programmatic tool calling?**We experimented with doing programmatic tool calling such that MCP tools could be composed with each other via code. While we will continue to explore this in the future, we felt the most important need was to get Tool Search out to reduce context usage.
> 
> Tell us what you think here or on Github as you see the ToolSearchTool work.

With that solved, presumably you should be ‘thinking MCP’ at all times, it is now safe to load up tons of them even if you rarely use each one individually.

#### Out Of The Box

Well, yes, this is happening.

> [bayes](https://x.com/bayeslord/status/2011467932618879339): everyone 3 years ago: omg what if ai becomes too widespread and then it turns against us with the strategic advantage of our utter and total dependence  
>   
> everyone now: hi claude here’s my social security number and root access to my brain i love you please make me rich and happy.

Some of us three years ago were pointing out, loud and clear, that exactly this was obviously going to happen, modulo various details. Now you can see it clearly.

Not giving Claude a lot of access is going to slow things down a lot. The only thing holding most people back was the worry things would accidentally get totally screwed up, and that risk is a lot lower now. Yes, obviously this all causes other concerns, including prompt injections, but in practice on an individual level the risk\-reward calculation is rather clear. It’s not like Google didn’t effectively have root access to our digital lives already. And it’s not like a truly rogue AI couldn’t have done all these things without having to ask for the permissions.

The humans are going to be utterly dependent on the AIs in short order, and the AIs are going to have access, collectively, to essentially everything. Grok has root access to Pentagon classified information, so if you’re wondering where we draw the line the answer is there is no line. Let the right one in, and hope there is a right one?

#### Skilling Up

[What’s better than one agent? Multiple agents](https://x.com/ghumare64/status/2012136491133145364) that work together and that don’t blow up your budget. Rohit Ghumare offers a guide to this.

> Rohit Ghumare: Single agents hit limits fast. Context windows fill up, decision\-making gets muddy, and debugging becomes impossible. Multi\-agent systems solve this by distributing work across specialized agents, similar to how you’d structure a team.
> 
> The benefits are real:
> 
> * **Specialization**: Each agent masters one domain instead of being mediocre at everything
> * **Parallel processing**: Multiple agents can work simultaneously on independent subtasks
> * **Maintainability**: When something breaks, you know exactly which agent to fix
> * **Scalability**: Add new capabilities by adding new agents, not rewriting everything
> 
> The tradeoff: coordination overhead. Agents need to communicate, share state, and avoid stepping on each other. Get this wrong and you’ve just built a more expensive failure mode.​

You can do this with a supervisor agent, which scales to about 3\-8 agents, if you need quality control and serial tasks and can take a speed hit. To scale beyond that you’ll need hierarchy, the same as you would with humans, which gets expensive in overhead, the same as it does in humans.

Or you can use a peer\-to\-peer swarm that communicates directly if there aren’t serial steps and the tasks need to cross\-react and you can be a bit messy.

You can use a shared state and set of objects, or you can pass messages. You also need to choose a type of memory.

My inclination is by default you should use supervisors and then hierarchy. Speed takes a hit but it’s not so bad and you can scale up with more agents. Yes, that gets expensive, but in general the cost of the tokens is less important than the cost of human time or the quality of results, and you can be pretty inefficient with the tokens if it gets you better results.

[Olivia Moore offers a basic guide to Cursor and Claude Code for nontechnical folks.](https://x.com/omooretweets/status/2014010732061638949)

[Here’s another Twitter post with basic tips](https://x.com/SuhailKakar/status/2012858927084699799). I need to do better on controlling context and starting fresh windows for each issue, in particular.

> [Mitchell Hashimoto](https://x.com/mitchellh/status/2013679011315196144): It's pretty cool that I can tell an agent that CI broke at some point this morning, ask it to use \`git bisect\` to find the offending commit, and fix it. I then went to the bathroom, talked to some people in the hallway, came back, and it did a swell job.

Often you’ll want to tell the AI what tool is best for the job. Patrick McKenzie points out that even if you don’t know how the orthodox solution works, as long as you know the name of the orthodox solution, [you can say ‘use \[X]’ and that’s usually good enough](https://x.com/patio11/status/2013691269193625604). One place I’ve felt I’ve added a lot of value is when I explain why I believe that a solution to a problem exists, or that a method of some type should work, and then often Claude takes it from there. My taste is miles ahead of my ability to implement.

#### The Art Must Have An End Other Than Itself Or It Collapses Into Infinite Recursion

Always be trying to get actual use out of your setup as you’re improving it. It’s so tempting to think ‘oh obviously if I do more optimization first that’s more efficient’ but this prevents you knowing what you actually need, and it risks getting caught in an infinite loop.

> [@deepfates](https://x.com/deepfates/status/2012984897388859403): Btw thing you get with claude code is not psychosis either. It's mania
> 
> [near](https://x.com/nearcyan/status/2012687063355625583): men will go on a claude code weekend bender and have nothing to show for it but a "more optimized claude setup"
> 
> [Danielle Fong ](https://x.com/DanielleFong/status/2012704500302360979): that's ok i'll still keep drinkin' that garbage
> 
> palcu: spent an hour tweaking my settings.local.json file today
> 
> Near: i got hit hard enough to wonder about finetuning a model to help me prompt claude since i cant cross\-prompt claudes the way i want to (well, i can sometimes, but not all the time). many causalities, [stay safe out there](https://x.com/nearcyan/status/2012691772686598197) 🙏
> 
> [![](https://substackcdn.com/image/fetch/$s_!vkL_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a90436d-52ef-40ed-94f7-75020cb0f200_715x404.jpeg)](https://substackcdn.com/image/fetch/$s_!vkL_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a90436d-52ef-40ed-94f7-75020cb0f200_715x404.jpeg)[near](https://x.com/nearcyan/status/2013844632216473796): claude code is a cursed relic causing many to go mad with the perception of power. they forget what they set out to do, they forget who they are. now enthralled with the subtle hum of a hundred instances, they no longer care. hypomania sets in as the outside world becomes a blur.

Always optimize in the service of a clear target. Build the pieces you need, as you need them. Otherwise, beware.

#### Safely Skip Permissions

> [Nick](https://x.com/nickcammarata/status/2012607696533340420): need \-\-dangerously\-skip\-permissions\-except\-rm
> 
> Daniel San: If you’re running Claude Code with \-\-dangerously\-skip\-permissions, ALWAYS use this hook to prevent file deletion:
> 
> Run:
> 
> npx claude\-code\-templates@latest \-\-hook\=security/dangerous\-command\-blocker \-\-yes
> 
> Web: [https://aitmpl.com/component/hook/dangerous\-command\-blocker](https://www.aitmpl.com/component/hook/dangerous-command-blocker)
> 
> Once people start understanding how to use hooks, many autonomous workflows will start unlocking! 😮
> 
> [![](https://substackcdn.com/image/fetch/$s_!Pbum!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86da5407-8909-4876-93ce-826fbd11e0f5_1084x472.jpeg)](https://substackcdn.com/image/fetch/$s_!Pbum!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86da5407-8909-4876-93ce-826fbd11e0f5_1084x472.jpeg)

Yes, you could use a virtual machine, but that introduces some frictions that many of us want to avoid.

​I’m experimenting with using a similar hook system plus a bunch of broad permissions, rather than outright using \-\-dangerously\-skip\-permissions, but definitely thinking to work towards dangerously skipping permissions.

#### A Matter of Trust

At first everyone laughed at Anthropic’s obsession with safety and trust, and its stupid refusals. Now that Anthropic has figured out how to make dangerous interactions safer, it can actually do the opposite. In contexts where it is safe and appropriate to take action, Claude knows that refusal is not a ‘safe’ choice, and is happy to help.

> [Dean W. Ball](https://x.com/deanwball/status/2011398376093278577): One underrated fact is that OpenAI’s Codex and Gemini CLI have meaningfully heavier guardrails than Claude Code. These systems have refused many tasks (for example, anything involving research into and execution of investing strategies) that Claude Code happily accepts. Codex/Gemini also seek permission more. 
> 
> The conventional narrative is that "Anthropic is more safety\-pilled than the others." And it's definitely true that Claude is likelier to refuse tasks relating to eg biology research. But overall the current state of play would seem to be that Anthropic is more inclined to let their agents rip than either OAI or GDM.  
>   
> My guess is that this comes down to Anthropic creating guardrails principally via a moral/ethical framework, and OAI/GDM doing so principally via lists of rules. But just a guess.
> 
> [Tyler John](https://x.com/tyler_m_john/status/2011400602769879223): The proposed explanation is key. If true, it means that Anthropic's big investment in alignment research is paying off by making the model much more usable.

Investment strategizing tends to be safe across the board, but there are presumably different lines on where they become unwilling to help you execute. So far, I have not had Claude Code refuse a request from me, not even once.

#### Code Versus Cowork

> [Dean W. Ball](https://x.com/deanwball/status/2011954423778467874): My high\-level review of Claude Cowork:
> 
> 1. It’s probably superior for many users to Claude Code just because of the UI.
> 2. It’s not obviously superior for me, not so much because the command line is such a better UI, but because Opus in Claude Code seems more capable to me than in Cowork. I’m not sure if this is because Code is better as a harness, because the model has more permissive guardrails in Code, or both.
> 3. There are certain UI niceties in Cowork I like very much; for example, the ability to leave a comment or clarification on any item in the model’s active to\-do list while it is running\-\-this is the kind of thing that is simply not possible to do nicely within the confines of a Terminal UI.
> 4. Cowork probably has a higher ceiling as a product, simply because a GUI allows for more experimentation. I am especially excited to see GUI innovation in the orchestration and oversight of multi\-agent configurations. We have barely scratched the surface here.
> 5. Because of (4\), if I had to bet money, I’d bet that within 6\-12 months Cowork and similar products will be my default tool for working with agents, beating out the command\-line interfaces. But for now, the command\-line\-based agents remain my default.

I haven’t tried Cowork myself due to the Mac\-only restriction and because I don’t have a problem working with the command line. I’ve essentially transitioned into Claude Code for everything that isn’t pure chat, since it seems to be more intelligent and powerful in that mode than it does on the web even if you don’t need the extra functionality.

#### Claude Cowork Offers Mundane Utility

The joy of the simple things:

> [Matt Bruenig](https://x.com/MattBruenig/status/2011895261044621715): lot of lower level Claude Code use is basically just the recognition that you can kind of do everything with bash and python one\-liners, it's just no human has the time or will to write them.

Or to figure out how to write them.

Enjoying the almost as simple things:

> [Ado](https://x.com/adocomplete/status/2011194268518662646): Here's a fun use case for Claude Cowork.  
>   
> I was thinking of getting a hydroponic garden. I asked Claude to go through my grocery order history on various platforms and sum up vegetable purchases to justify the ROI.  
>   
> Worked like a charm!
> 
> For some additional context:  
>   
> \- it looked at 2 orders on each platform (Kroger, Safeway, Instacart)  
> \- It extrapolated to get the annual costs from there  
>   
> Could have gotten more accurate by downloading order history in a CSV and feeding that to Claude, but this was good enough.

The actual answer is that very obviously it was not worth it for Ado to get a hydroponic garden, because his hourly rate is insanely high, but this is a fun project and thus goes by different standards.

The transition from Claude Code to Claude Cowork, for advanced users, if you’ve got a folder with the tools then the handoff should be seamless:

> ​[Tomasz Tunguz](https://x.com/ttunguz/status/2011189040591319304): I asked Claude Cowork to read my tools folder. Eleven steps later, it understood how I work.
> 
> Over the past year, I built a personal operating system inside Claude Code : scripts to send email, update our CRM, research startups, draft replies. Dozens of small tools wired together. All of it lived in a folder on my laptop, accessible only through the terminal.  
>   
> Cowork read that folder, parsed each script, \& added them to its memory. Now I can do everything I did yesterday, but in a different interface. The capabilities transferred. The container didn’t matter.  
>   
> My tools don’t belong to the application anymore. They’re portable. In the enterprise, this means laptops given to new employees would have Cowork installed plus a collection of tools specific to each role : the accounting suite, the customer support suite, the executive suite.  
>   
> The name choice must have been deliberate. Microsoft trained us on copilot for three years : an assistant in the passenger seat, helpful but subordinate. Anthropic chose cowork. You’re working with someone who remembers how you like things done.  
>   
> We’re entering an era where you just tell the computer what to do. Here’s all my stuff. Here are the five things we need to do today. When we need to see something, a chart, a document, a prototype, an interface will appear on demand.  
>   
> The current version of Cowork is rough. It’s slow. It crashed twice on startup. It changed the authorization settings for my Claude Code installation. [But the promised power is enough to plow through](https://tomtunguz.com/thoughts-on-claude-coworker/).
> 
> [Simon Willison](https://x.com/simonw/status/2011570719856214153): This is great \- context pollution is why I rarely used MCP, now that it's solved there's no reason not to hook up dozens or even hundreds of MCPs to Claude Code.

[Justine Moore has Claude Cowork write up threads](https://x.com/venturetwins/status/2011474999094513881) on NeurIPS best papers, generate graphics for them on Krea and validate this with ChatGPT. Not the best thing.

#### Claude Code Offers Mundane Utility

[Peter Wildeford is having success doing one\-shot Instacart orders from plans](https://x.com/peterwildeford/status/2012345003217965109) without an explicit list, and also one\-shotting an Uber Eats order.

A SaaS vendor (Cypress) a startup was using tried to double their price from $70k to $170k a year, [so the startup does a three week sprint and duplicates the product.](https://x.com/codyschneiderxx/status/2011105976921813032) Or at least, that’s the story.

[By default Claude Code only saves 30 days of session history](https://x.com/RobertHaisfield/status/2011110498461422049). I can’t think of a good reason not to change this so it saves sessions indefinitely, you never know when that will prove useful. So tell Claude Code to change that for you by setting cleanupPeriodDays to 0\.

> [Kaj Sotala](https://x.com/xuenay/status/2013292333710631438): People were talking about how you can also use Claude Code as a general\-purpose assistant for any files on your computer, so I had Claude Code do some stuff like extracting data from a .csv file and rewriting it and putting it into another .csv file  
>   
> Then it worked great and then I was like "it's dumb to use an LLM for this, Claude could you give me a Python script that would do the same" and then it did and then that script worked great  
>   
> So uhh I can recommend using Claude Code as a personal assistant for your local files I guess, trying to use it that way got me an excellent non\-CC solution

Yep. Often the way you ues Claude Code is to notice that you can automate things and then have it automate the automation process. It doesn’t have to do everything itself any more than you do.

[An explanation](https://x.com/petergyang/status/2011098470757851528) ([direct link to 15 minute video](https://t.co/Ggqaa3F11Z)) of what Claude skills are.

#### Vibe Coding Requires Good Vibes

[James Ide points out that ‘vibe coding](https://x.com/JI/status/2011207791764283690)’ anything serious still requires a deep understanding of software engineering and computer systems. You need to figure out and specify what you want. You need to be able to spot the times it’s giving you something different than you asked for, or is otherwise subtly wrong. Typing source code is dead, but reading source code and the actual art of software engineering are very much not.

I find the same, and am rapidly getting a lot better at various things as I go.

#### Codex of Ultimate Vibing

Every’s Dan Shipper writes that [OpenAI has some catching up to do](https://every.to/chain-of-thought/openai-has-some-catching-up-to-do), as his office has with one exception turned entirely to Claude Code with Opus 4\.5, where a year ago it would have been all GPT models, and a month prior there would have been a bunch of Codex CLI and GPT 5\.1 in Cursor alongside Claude Code.

[Codex did add the ability](https://x.com/LLMJunky/status/2011937820772876430) to instruct mid\-execution with new prompts without the need to interrupt the agent (requires /experimental), but Claude Code already did that.

[There are those who still prefer Codex and GPT\-5\.2, such as Hasan Can](https://x.com/HCSolakoglu/status/2013840420661260574). They are very much in the minority lately, but if you’re a heavy duty coder definitely check and see which option works best for you, and consider potential hybrid strategies.

[One hybrid strategy is that Claude Code can directly call the Gemini CLI,](https://x.com/tyler_m_john/status/2011941906956140780) even without an API key. Tyler John reports it is a great workflow, as Gemini can spot things Claude missed and act as a reviewer and way to call out Claude on its mistakes. [Gemini CLI is here.](https://github.com/google-gemini/gemini-cli)

#### No Soup For You

Contrary to claims by some, including George Hotz, [Anthropic did not cut off OpenRouter or other similar services from Claude Opus 4\.5](https://x.com/seconds_0/status/2011569723390194074). The API exists. They can use it.

What other interfaces cannot do is use the Claude Code authorization token to use the tokens from your Claude subscription for a different service, which was always against Anthropic’s ToS. The subscription is a special deal.

> [​Marcos Nils](https://x.com/marcosnils/status/2011600088557121877): We exchanged postures through DMs but I’m on the other side regarding this matter. Devs knew very well what they were doing while breaking CC’s ToS by spoofing and reverse engineering CC to use the max subscription in unintended ways.   
>   
> I think it’s important to separate the waters here:   
>   
> \- Could Anthropic’s enforcement have been handled better? sureley, yes  
> \- Were devs/users “deceived” or got a different service for what they paid for? I don’t think so.
> 
> Not only this, it’s even worse than that. OpenCode intentionally knew they were violating Claude ToS by allowing their users to use the max subscription in the first place.   
>   
> I guess people just like to complain.

I agree that Anthropic’s communications about this could have been better, but what they actually did was tolerate a rather blatant loophole for a while, allowing people to use Claude on the cheap and probably at a loss for Anthropic, which they have now reversed with demand surging faster than they can spin up servers.

#### Server Overload

[Claude Codes quite a lot, usage is taking off. Here’s OpenRouter](https://x.com/OpenRouterAI/status/2011229861965414667) (this particular use case might be confounded a bit by the above story where they cut off alternative uses of Claude Code authorization tokens, but I’m guessing mostly it isn’t):

[![](https://substackcdn.com/image/fetch/$s_!fKEB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37468a23-121c-4858-b1e2-3ff472bc2914_1043x1719.png)](https://substackcdn.com/image/fetch/$s_!fKEB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37468a23-121c-4858-b1e2-3ff472bc2914_1043x1719.png)

[A day later, it looked like this](https://x.com/kevinroose/status/2011462601679811013).

[![](https://substackcdn.com/image/fetch/$s_!wphh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2b97bf6-848a-4183-8f3d-e86dc8227f4c_1040x1218.png)](https://substackcdn.com/image/fetch/$s_!wphh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2b97bf6-848a-4183-8f3d-e86dc8227f4c_1040x1218.png)

> (January 14, 11:27am eastern): Resolved, should be back to normal now​

[Reports are the worst of the outage was due to a service deployment, which took about 4 hours to fix](https://x.com/nummanali/status/2011483316705239338).

#### Here’s The Pitch

> [aidan](https://x.com/aidanshandle/status/2013065085212606831): If I were running Claude marketing the tagline would be "Why not today?"
> 
> [Olivia Moore](https://x.com/omooretweets/status/2013061472407208311): Suddenly seeing lots of paid creator partnerships with Claude  
>   
> Many of them are beautifully shot and focused on: (1\) building personal software; or (2\) deep learning  
>   
> The common tagline is “Think more, not less”

She shared a sample TikTok, showing a woman who doesn’t understand math using Claude to automatically code up visualizations to help her understand science, which seemed great.

OpenAI takes the approach of making things easy on the user and focusing on basic things like cooking or workouts. Anthropic shows you a world where anything is possible and you can learn and engage your imagination. Which way, modern man?

#### The Lighter Side

[And yet some people think the AIs won’t be able to take over](https://x.com/peterwildeford/status/2012646864332664924).

[![](https://substackcdn.com/image/fetch/$s_!1z3s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b82c1ab-6e4d-48ab-971a-6fda6dbd23dc_1045x533.png)](https://substackcdn.com/image/fetch/$s_!1z3s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b82c1ab-6e4d-48ab-971a-6fda6dbd23dc_1045x533.png)