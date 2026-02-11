# Claude Coworks

Published: 2026-01-13
Source: https://thezvi.substack.com/p/claude-coworks

---

Claude Code does a lot more than code, but the name and command line scare people.

Anthropic realized a rebrand was in order. [Two weeks later, we have Claude Cowork](https://x.com/blakeir/status/2010837251505205656), [written entirely by Claude Code](https://x.com/_simonsmith/status/2010820240330956895).

Did you know that chat interfaces were always (mostly) secretly a command line?

This is still very much a research preview, available only for Claude Max users on Macs with a bunch of bugs and missing features. It will improve rapidly over time.

Cowork combines a lot of the power of Claude Code with the ordinary chat interface, giving it access to a folder on your computer and to Claude Code’s planning and agentic capabilities. It can use that folder as context, to download, to organize and create files, and it can be paired with Claude for Chrome and use your existing connectors.

> [Anthropic](https://x.com/claudeai/status/2010805682434666759): Introducing Cowork: Claude Code for the rest of your work.  
>   
> Cowork lets you complete non\-technical tasks much like how developers use Claude Code.
> 
> In Cowork, you give Claude access to a folder on your computer. Claude can then read, edit, or create files in that folder. Try it to create a spreadsheet from a pile of screenshots, or produce a first draft from scattered notes.
> 
> Once you've set a task, Claude makes a plan and steadily completes it, looping you in along the way. Claude will ask before taking any significant actions so you can course\-correct as needed.
> 
> Claude can use your existing connectors, which link Claude to external information. You can also pair Cowork with Claude in Chrome for tasks that need browser access.
> 
> [Cowork is available as a research preview](https://t.co/kWnDq1psWQ) for Claude Max subscribers in the macOS app. Click on “Cowork” in the sidebar.
> 
> [Sholto Douglas](https://x.com/_sholtodouglas/status/2010822023715471623) (Anthropic): Claude code for all other knowledge work. Many of our best engineers no longer manually write code, they multiplex across multiple cc sessions \- soon this will be true for everything else.

[The system prompt is here](https://x.com/p1njc70r/status/2010843436279021635), the core non\-tooling parts seem unchanged. This post will cover Claude Cowork, and also updates since last week on Claude Code.

#### Early Takes

What exactly can it do at this early stage?

> [Dean W. Ball](https://x.com/deanwball/status/2010844935512006943): it's basically what I expected. the ui is normal claude, but instead of showing you the bash commands it is executing, it just says "using bash" or "command" (you can click for detail of course). very useful for many I'm sure! not sure if useful for me over cc; still learning.
> 
> There are ui niceties that I could see myself preferring to the command line, even as someone very comfortable with terminals. and of course one would expect more such niceties in future iterations.
> 
> Vie: My guess is that the prompt scaffolding makes the results and actual work a few times more general for non\-code use cases, and a few times more interpretable by lay\-people, at the cost of the tail of IQ being a big smaller
> 
> [Claire Vo](https://x.com/clairevo/status/2010835704931369379): It’s basically local Claude Code with a Mac OS app wrapper focused on a few core primitives:
> 
> * **Connectors / MCPs** \- external services Cowork has access to
> * **Filesystem** \- runs locally so will create/read things on your file system
> * **TODOs/Steps** \- discrete trackable steps cowork will take to execute your tasks
> * **Artifacts** \- files generated in the process of doing your task
> * **Context** \- files / sources / connectors used when doing your task
> * **Skills** \- preloaded with a few key skills, esp. file type creation ones like DOCX, PPT, etc. Claude generally has access to these, so not new.
> 
> Every chat is now a **task** (focused on doing\-a\-thing) and **steps, artifacts, and context** get first class treatment in the UI.
> 
> … Speaking of skills, Cowork seemingly comes bundled with a few key ones around document creation (you can find them in your file system.)
> 
> … **Despite it's flaws, Cowork** ***did*** **create better outputs than straight Chat.**

[Lenny Rachitsky tests Cowork with a set of 320 of his podcast transcripts](https://x.com/lennysan/status/2010840092865413254) and asks it to pull out the 10 most important themes and 10 most counterintuitive truths, and thinks it did a good job in its 15 minutes of work. Seemed solid to me.

The most credible signal of respect is admitting that a release killed your startup product, [which we see here with Eigent](https://x.com/guohao_li/status/2010899322825744745).

> Steve Hou: Another win for ‘the foundation model is the product.’​

This is the first feedback so far about what it’s intended to do:

> [John Wittle](https://x.com/JohnWittle/status/2011112597731356915): My mom, sharp old woman, seems to be taking to it with quite a lot of enthusiasm, in a way she had trouble doing with, say, windows\-mcp and claude desktop.  
>   
> seems to unlock normie powers a lot better.
> 
> Neil: I think amazing for non coders to discover what’s possible
> 
> [![](https://substackcdn.com/image/fetch/$s_!obXO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9f7eab8-675d-4779-9ff8-42d83880df21_1200x597.jpeg)](https://substackcdn.com/image/fetch/$s_!obXO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9f7eab8-675d-4779-9ff8-42d83880df21_1200x597.jpeg)

Rename it away from code, normie figures out they can have it code.

If that’s true with the version that’s two weeks old, the sky’s the limit. We don’t have much data because there aren’t that many normies with $200/month Claude Max subscriptions.

#### Minimum Viable Product

It’s early days, and she reports there were still some other kinks being worked out. In particular, the connectors are having problems.

> [Tibor Blaho](https://x.com/btibor91/status/2010818434595242083): Available now for Max subscribers on macOS desktop app only, with no project support, no memory between sessions, no sharing, app must stay open during tasks, and consumes more usage than regular chat, with plans to add cross\-device sync and Windows support

One thing Claire Vo noted was it asked for approvals on file openings too much. I have a similar complaint with Claude Code, that there’s a bunch of highly safe similar actions that shouldn’t need permission.

Claire also noted that Claude Cowork exposed too many technical files and notes about what it was doing to the user, such as the code used to generate things, which could be confusing to non\-technical users. My guess is that such files can be stored in a subdirectory where such users won’t notice, which keeps it available for those who want it, and ‘tell me more about what you’re doing on a technical level’ can be a setting, since the users who want it set to no won’t even notice the option exists.

#### Maximum Viable Product

There is a huge overhang in AI capabilities.

Thus, a common pattern is that someone figures out a way to do useful things at all that humans are willing to learn how to use. And then we muddle down that road, and it’s not first best but it still wins big.

That’s what Claude Code was, and now that’s what Claude Cowork will be for normies. Presumably OpenAI and Google, and then others, will soon follow suit.

> [Chris Barber](https://x.com/chrisbarber/status/2011139690364313654): do you see the vision of claude cowork?  
>   
> imagine claude for execl, powerpoint, word, outlook, chrome, bloomberg terminal, etc. gmail connector. ability to code.  
>   
> this is the pathway to big knowledge worker adoption  
>   
> openai and google will need to follow  
>   
> this will be very strong pmf and growth  
>   
> invest in it, compete with it, join anthropic/oai/gdm and work on it/competitors, etc  
>   
> this will be central  
>   
> claude code \*is\* the ai coworker, it'll all build up from there.

#### Backup Your Directory

If you’re worried Claude Cowork or Claude Code will delete a bunch of stuff in a directory, and you don’t want to use a full virtual sandbox solution, there’s a rather simple solution that also works, which is: Backup the directory, to a place Claude can’t get to it. Then if the worst happens, you restore the backup.

#### Meanwhile In Claude Code News

[The latest guide to Claude Code](https://x.com/eyad_khrais/status/2010076957938188661), feedback seems very good. Key highlights:

1. Think before you type. Enter plan mode first and go back and forth a lot.
2. Keep claude.md short, max 50\-100 instructions. Use \# while working to edit it.
3. Store things in external files.
4. Try to only use 30% of the context window, after that performance degrades.
5. Make your prompts as specific as possible, including what not to do.
6. Try out various hooks, MCPs, you name it. Experiment.
7. When stuck, be creative, pivot, simplify, clear the conversation and start again.
8. Build systems, not one\-off tasks.

Here’s another report of what Claude Code has been good for, with three big unlocks for APIs, connecting distinct products and running things regularly:

> [Nikhil Krishnan](https://x.com/nikillinit/status/2010481404987990350): I’ve spent the last 48 hours in Claude Code \- as a non\-technical person it’s basically unlocked three very big things for me
> 
> 1. The ability to interact with APIs generally \- again, as a non\-technical person one of the big barriers to running the business has been touching APIs. For example, what you can do in Stripe in the non\-developer portal vs. through the API is night and day.
> 2. The ability to thread things together \- another issue has been threading several different products we work with together to do cohesive tasks. Zapier gets you part of the way for triggers, but Claude Code let’s me do way more complex things that touches multiple things simultaneously
> 3. Run something regularly \- being able to set a script and run it regularly with this level of ease is a game changer. In about an hour I set up a daily email to myself that tells me the top 3 emails I need to respond to based on a priority scoring system we made together that pulls data from a few different places.
> 
> I know I’m late to this and I’m probably doing things poorly so be nice to me. But it’s really been awesome to dive into this.

As always, one could have done all of this any number of other ways, but this deals with the problem of activation energy.

[Dean Ball has, in the past month, used coding agents to do the following](https://www.hyperdimensional.co/p/among-the-agents?utm_source=post-email-title&publication_id=2244049&post_id=183828760&utm_campaign=email-post-title&isFreemail=true&r=3o9&triedRedirect=true&utm_medium=email):

> 1. ​Automated invoice creation, sending, and tracking;
> 2. Created scientifically realistic simulations of hydrological systems as a learning project;
> 3. Automated my research process of gathering and analyzing all proposed state legislation related to AI (though this is no substitute for reading the bill for anything I am going to write about);
> 4. Orchestrated a complex chain of autonomous data collection, processing, analysis, and presentation steps related to manufacturing and industrial policy;
> 5. Created a machine\-learning model capable of predicting US corn yields with what appears to be very high accuracy (the proof will be in the pudding), based on climate, soil, Earth\-observation satellite, and other data sources;
> 6. Replicated three machine\-learning research papers and modified the approach to suit my own research ends;
> 7. Performed hundreds of experiments with Byte\-level language models, an emerging interest of mine;
> 8. Created an autonomous prediction market agent;
> 9. Created an autonomous options trader based on a specific investment thesis I developed;
> 10. Built dozens of games and simulations to educate myself about various physical or industrial phenomena;
> 11. Created an agent that monitors a particular art market in which I am potentially interested in making an acquisition;
> 12. Created a new personal blog complete with a Squarespace\-style content management system behind the scenes;
> 13. Other things I cannot talk about publicly just yet.

I’m not there yet, largely because we think in different ways, but largely because I’m just getting started with ‘oh right coding things just happens, do coding agent shaped things.’

[Dean Ball nails it](https://x.com/deanwball/status/2009612291436577280) that coding agents are most helpful exactly when you don’t have to ship your software to third parties. I presume that the code underneath everything I’m having Claude build would horrify professional coders. That’s fine, because even in the places I do ship (cause why not ship, someone might find it useful) I’m not trying to not horrify people. What matters is it works, and that I’m ‘using coding agent shaped requests,’ as Dean puts it, to increasingly get things done.

The coding agents will still produce the most value for professional coders, because they can go into supercharged mode with them and get the most out of them, but that requires the professionals to swim upstream in ways the rest of us don’t have to.

So, say this is what you want:

> [Prakesh](https://x.com/8teAPi/status/2009694934950129767): what i really want as a writer is an automated fact checker and alternative viewpoint giver. there’s a lot of fact rechecking after you have the initial concept of a piece which is tedious but necessary​.
> 
> Jon Stokes: I literally have this (the fact checker). It’s amazing (not just saying that because my team built it.. it’s truly wild). Happy to demo for you... DM if interested.

Exactly. I haven’t built a custom fact checker yet, but the only thing stopping me is ‘it hadn’t yet occured to me it was sufficiently easy to do that’ combined with ‘I have not yet gotten around to it.’ Check back with me in six months and I bet I do have one, I’m actually building towards such things but it’s not near the top of that queue yet.

[As Alex Albert puts it](https://x.com/simonw/status/2009709346377302432), you get to stop thinking doing something is ‘not worth your time,’ or for Simon Willison entire features are no longer ‘not worth your time’ at least not until they run into serious trouble.

Dean offers various additional coding agent thoughts, and a highly basic guide, [in the rest of his weekly post](https://www.hyperdimensional.co/p/among-the-agents?utm_source=post-email-title&publication_id=2244049&post_id=183828760&utm_campaign=email-post-title&isFreemail=true&r=3o9&triedRedirect=true&utm_medium=email).

[Alex Tabarrok did his first Claude Code project](https://x.com/ATabarrok/status/2010788591950315977). Noncoders skilling up is a big deal.

[Joe Weisenthal did his first Claude Code project](https://www.bloomberg.com/news/newsletters/2026-01-13/ai-s-productivity-potential-has-never-more-obvious?srnd=phx-oddlots) and now we have [Havelock.ai](https://havelock.ai/), which gives us an ‘orality detector’ for text, essentially employing the Ralph Wiggum technique by continuously asking ‘what should I do to make it better?’

[Linus Torvarlds (the creator of Linux) is doing at least some vibe coding](https://x.com/theo/status/2010154568211120349), in this case using Antigravity.

Claude may not yet in its official test be a Pokemon master, [but Claude Code is now somewhat of a RollerCoaster Tycoon](https://labs.ramp.com/rct?utm_source=youtube&utm_campaign=content&utm_medium=organic-social), with various strengths and weaknesses. Dean Ball suggests you can use [Claude Code to do game dev on new ‘\[x] tycoon’ games](https://x.com/ohabryka/status/2010566862137155924) as a niche topic learning exercise. Oliver Habryka challenges whether it’s good enough at game dev for this. As Patrick McKenzie points out, if the game is text based that helps a lot, since visual aspects are a key weakness for now.

#### You Are The Bottleneck

[Kelsey Piper reports on her experience with using and yelling at Claude Code](https://www.theargumentmag.com/p/i-cant-stop-yelling-at-claude-code?utm_source=%2Finbox&utm_medium=reader2).

She and I are very similar types of programmers:

> Kelsey Piper: ​In college, I was once told that the really hard part of programming was knowing, in sufficient detail, what you wanted the computer to do. This was not my experience of programming.
> 
> In my experience of programming, the really hard part was figuring out which packages weren’t installed or weren’t updated or were in the wrong folder, causing the test we’d done in class to completely fail to work in the same way on my own computer. The next really hard part was Googling everything the debugger spat out to find an explanation of how to make it go away.
> 
> … Claude Code solves all of that. Programming, now, really is just a matter of knowing in sufficient detail what you want the computer to do.
> 
> … Now, 99% of the time, it feels like magic. The remaining 1% is absolutely maddening.

It’s not that it is easy to know what you want the computer to do, especially if you expand that to include ‘what do I even want to be trying to do today at all.’ Both the macro and micro ‘what are we even doing’ questions are hard. I still spent 90% of my time dealing with packages and syntax and setup and knowing exactly how to do it.

The problem is that, as Kelsey observes, you will spend your time on the bottleneck, whatever that bottleneck might be, and this will be frustrating, especially as this will often be something stupid, or the particular place Claude Code happens to act stupid given the way you’re prompting it.

> I said that 99% of the time Claude was great. By which I mean, 99% of the work Claude completed was great, but that doesn’t mean 99% of my time was spent sitting back and marveling. When something worked great, we’d breeze right past it. When Claude had shuffled all the audio files again, we’d spend a really long time fixing that. I found myself, well, yelling at it.​

I am happy to report that I haven’t been yelling at Claude Code when it messes up. But yeah, it messes up, because I keep trying to get it to do more until it messes up.

#### Claude Code Upgrades

> [Anthony Morris ツ](https://x.com/amorriscode/status/2010808647459488020): We shipped A LOT of updates to Claude Code on desktop in the last week.  
>   
> \- Plan mode (coming soon to web)  
> \- Notifications for permissions  
> \- Perf improvements  
> \- Fixed slash commands  
> \- Improved env access  
> \- Tons of polish

[Numman Ali says v2\.1\.3 has ‘solved the compaction issue’](https://x.com/nummanali/status/2010042788566720955) so long as you use planning mode and explicitly ask the model for a comprehensive TODO list. It’s hard to tell, but I’ve certainly blown over the compaction line on many tasks and when I’ve saved the necessary context elsewhere it’s mostly turned out fine.

[What Clade Code cannot do](https://x.com/trq212/status/2009689809875591565) is allow its harness to be spoofed to use subscriptions. You can either use Claude Code, or you can access Claude via the API, but it’s a terms of service violation to spoof the harness to let you use your subscription allocation. I’d be inclined to let the harnesses stay in place despite the problems described here, so long as the unit economics are not too horrendous. In general I think Anthropic is too focused on getting to profitability quickly, even if you think OpenAI is rather too willing to burn money.

[Anthropic reportedly cuts xAI and other major competitors off from Claude](https://x.com/kyliebytes/status/2009686466746822731).

#### Oh No

In the interest of not silencing critics, [Holly Elmore claims I’m bad now](https://x.com/ilex_ulmus/status/2010140670300959222) because I’m enthusiastic about getting use out of Claude Code, a ‘recursively self\-improving agent.’

I affirm David Manheim’s response that there is no reason for an individual not to use such tools for their own purposes, or not to get excited about what it can do outside of potentially dangerous forms of self\-improvement.

I do agree that the vibes in that post were a bit off by not also including awareness of where sufficiently advanced coding agents lead once they start self\-improving in earnest, and there is value in having a voice like Holly’s that says the basic thing clearly.

However I also think that there is no contradiction between ‘recursive self\-improvement is super dangerous and likely to get us all killed’ and ‘you should be taking full advantage of Claude Code for practical purposes and you’re leaving a lot on the table if you don’t.’

#### I’m In Danger

There is a new method [called the ‘Ralph Wiggum’ technique](https://www.wsj.com/tech/ai/our-ai-future-is-already-here-its-just-not-evenly-distributed-cf7a6f35?mod=hp_featst_pos3), where you tell Claude Code continuously to ‘improve the code’ it has already written. Some say it works great, but the name does not inspire confidence.

The world is collectively underinvesting in optimizing and standardizing such techniques. Some well\-designed version of this would presumably be great, and the more parallelization of agents is going on the more valuable it is to optimize non\-interruption over token efficiency.

#### In The Beginning Was The Command Line

What is the difference between a command line and a chat interface?

Both are text in and text out.

Both allow attachments, at least in Claude Code mode.

Both can have sandboxes, run code, and so on.

The main real difference is that the terminal makes it annoying to edit prompts?

It’s almost entirely about perception. One feels like talk with an entity, one like commands and bash scripts. One looks like a slick modern UI, the other a stark black text box.

There is also a clear plan to have different system prompts, and to build in a different more user friendly set of default connectors and tools.

That plus the change in perception could be a really, really big deal.