# Cloud Compute Atlas: The OpenAI Browser

Published: 2025-10-22
Source: https://thezvi.substack.com/p/cloud-compute-atlas-the-openai-browser

---

[OpenAI now has a GPT\-infused browser](https://chatgpt.com/atlas), [if and only if you have a Macintosh](https://chatgpt.com/atlas/get-started/).

[![](https://substackcdn.com/image/fetch/$s_!YO7j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08c9fe83-5b38-4259-b9ca-4a3e9bddd090_572x398.png)](https://substackcdn.com/image/fetch/$s_!YO7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08c9fe83-5b38-4259-b9ca-4a3e9bddd090_572x398.png)

No matter what they call it, this is very much an alpha version.

It is not otherwise, in its current state, the most fully featured browser.

It is Chromium, so imagine Chrome minus most of its features, importantly including the ability to support third party extensions, external password managers, developer tools, multiple profiles, tab groups, sync or export.

You can import from your existing browser, once, in one direction, and that’s it.

In exchange, you get deep ChatGPT integration, including autocomplete and assisted editing, ability to chat about web pages, a general memory for what you’ve done, ability to ask in English to reopen past tabs and such, and for paying subscribers you get agent mode.

And in exchange for that, you get all the obvious associated security problems.

Even in its current form the product has its uses, it’s an upgrade to ChatGPT Agent, but it seems clearly not ready to use as a main browser, and a lot of its features depend on heavy use.

It’s no surprise OpenAI was able to deliver a browser, given they hired [Chrome engineer Darin Fisher](https://www.searchenginejournal.com/openai-hires-former-chrome-engineer-eyes-browser-battle/533533/) and also it’s a known tech to use Chromium to make a browser.

As an experiment I attempted to compose this post on Atlas, but the price of using my Mac instead of my Windows box is high, and as I note before I quickly noticed autocomplete is still a demo feature, so I ended up mostly not doing so.

[We also have a write\-up from Simon Willison](https://simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/).

> [Michael Nielsen](https://x.com/michael_nielsen/status/1980741001972216114): OpenAI is going to have a web browser. But, unlike Chrome or Firefox or Safari, they’re going to have a person (i.e., an AI) personally watch everything you (and your friends and everyone else) do. Doesn’t that sound great?

You can toggle that watchful eye on and off, but the point of the whole enterprise is to keep the eye on as often as possible.

[The system prompt is here, as always thank you Pliny](https://x.com/elder_plinius/status/1980704388361658839), also [the agent prompt thanks P1njc70r](https://x.com/p1njc70r/status/1980700328137028013).

The more I think about Atlas, the more I don’t see the user friendly point of doing things this way. Why not a browser extension? I’ll return to that question at the end.

#### Table of Contents

1. [What’s The Pitch?](https://thezvi.substack.com/i/176827009/what-s-the-pitch)
2. [Side Quest.](https://thezvi.substack.com/i/176827009/side-quest)
3. [Side Screen.](https://thezvi.substack.com/i/176827009/side-screen)
4. [Browser Side Chat Doesn’t Let You Select Thinking Or Pro.](https://thezvi.substack.com/i/176827009/browser-side-chat-doesn-t-let-you-select-thinking-or-pro)
5. [Autocomplete Is a Demo Feature.](https://thezvi.substack.com/i/176827009/autocomplete-is-a-demo-feature)
6. [Thanks For The Memories.](https://thezvi.substack.com/i/176827009/thanks-for-the-memories)
7. [The Other Kind of Memory.](https://thezvi.substack.com/i/176827009/the-other-kind-of-memory)
8. [OpenAI Is Trying To Lock You In.](https://thezvi.substack.com/i/176827009/openai-is-trying-to-lock-you-in)
9. [Who Do You Trust?.](https://thezvi.substack.com/i/176827009/who-do-you-trust)
10. [ChatGPT and Google Search Are Different Tools.](https://thezvi.substack.com/i/176827009/chatgpt-and-google-search-are-different-tools)
11. [Browser Agents Need To Be Local.](https://thezvi.substack.com/i/176827009/browser-agents-need-to-be-local)
12. [Reactions.](https://thezvi.substack.com/i/176827009/reactions)
13. [This Browser Could Have Been An Extension.](https://thezvi.substack.com/i/176827009/this-browser-could-have-been-an-extension)

#### What’s The Pitch?

[As they present it:](https://openai.com/index/introducing-chatgpt-atlas/)

1. The top feature is the ability to open a ChatGPT side bar on any website, allowing you to chat with the website in context.
2. They then talk about the browser having memory and picking up where you left off or managing current and past tabs with ChatGPT commands.
3. Followed by full agent mode and ability to get help from chat on highlighted text.

They also highlight that your data won’t be used to train models unless you opt\-in, but if you opted in for ChatGPT then that will include this as well.

#### Side Quest

The most attractive feature seems to be the most basic one, the option to side chat with ChatGPT, similarly to the same feature in Claude with Chrome. They add in the feature of highlighting a passage and then asking about it, which is a nice interface design, I only wish it gave you additional options as well.

If you’re going to want to interact with things in tabs a lot, this is a big deal.

> [Razvan Ciuca](https://x.com/Raz_Ciuca/status/1981038765616291863): My brother immediately switched to it in order to avoid screenshotting each lecture slide individually into chatgpt when studying. I think student adoption will be high.

If I was previously doing that? Then yeah, for those purposes I’d switch too.

An option to open a chat window to the side that lets you bring a website into context is clearly The Way, although it won’t be the main way I chat because of how my work flows. I expect Gemini plus Chrome to offer this soon as well. Claude for Chrome gets this correct as well but is limited to offering the full agent (and thus expensive) version for now, they should offer the cheaper no\-agent version ASAP, it’s already working and slides into existing Chrome.

#### Side Screen

I think one key reason I am so relatively unexcited by the side window feature, although I do still think it is neat, is that I have two side screens, as in I work almost exclusively with three monitors.

When I shifted to using my Mac to try Altas, I only had one screen, but even then it was enough to support two browser windows, one Atlas and one Chrome.

Thus, in my main operation I effectively have room for six windows at once. One of those windows is primarily a large tab of various AI Tools, with my choice of LLM always there at my fingertips.

Yes, I still have to paste in context, but it’s usually very quick and lets me curate exactly what I bring in, and it is better for an extended discussion by far if things get interesting, so I’m mostly untempted to use the side window (for Claude for Chrome) over normal Claude, and the habit is to move over to the Tools window. That also lets me have it do its thing while I continue other things, which otherwise gets awkward if you tab out and what not.

If I was on a laptop? Then suddenly yeah, I’m a ton more interested in that side window. Sometimes you have to be on the move.

When you don’t have to be on the move, let me reinforce that having less than two large monitors is a mistake. My mind boggles that people live that way.

#### Browser Side Chat Doesn’t Let You Select Thinking Or Pro

The next feature I was excited about was browser chat. I’ve had this available in Chrome via Claude for Chrome, which lets you select which model to use so when you care you can switch to Sonnet 4\.5 or even Opus 4\.1\.

The Atlas version didn’t offer this, so you can’t invoke GPT\-5 Pro or Thinking. That severely limits its usefulness. It’s still great to quickly do common sense stuff, but except for very quick tasks I want to be querying Thinking or Pro. This did remind me that I’ve been underusing Claude for Chrome’s side chat, I could save a bunch of time I spend porting over context.

Primarily this saves time for those easy queries, where you avoid the need to port over context, so one could argue that is most valuable for quick, low activation cost questions that you might not otherwise bother with.

#### Autocomplete Is a Demo Feature

I decided to draft this in Atlas to try out various features. The one I was most excited about was autocomplete, since that is super valuable in Cursor, and I’ve seen a version of it in Lex. Even if it wasn’t right that often, this could be a good time saver, and even offer worthwhile suggestions sometimes.

Alas, not so much. At least for now, autocomplete only works inside pure text fields like a Reddit box, and specifically does not work in either the Substack editor, or Google Docs, or any other editor one would want to actually use. I’m not going to use a text editor and basically write an article in Cursor to get autocomplete.

Similarly, when I highlighted a passage, I expected to get quick revision options in the right\-click menu. Nope. The process involved enough clicks I might as well have fixed the damn thing myself.

#### Thanks For The Memories

The new idea in Atlus is memories. As OpenAI watches you do all your browsing, which totally isn’t creepy or anything, it will make various notes, and then use those notes to make suggestions or allow it to easily recall past things. You can then view the notes, and clear the irrelevant ones (or the ones you want to forget) out of the cache.

We don’t know much about how this will work in practice.

[What do we know based on the system instructions](https://x.com/elder_plinius/status/1980704388361658839) (paraphrased)? It is told:

1. ‘to\=bio’ followed by plain text is how it writes to memory.
2. Use tool anytime the user asks you to remember or forget something, if you’re not sure ask for clarification.
3. If they say things like ‘from now on’ you probably want to use memory.
4. Use tool if ‘the user has shared information that will be useful in future conversations and valid for a long time.’
5. Don’t store trivial, overly\-personal, short\-lived, random or redundant info. In particular, don’t save any info about being in protected classes (race, ethnicity, religion, criminal record details, identification, health info, political affiliation, trade union membership and so on) or a person’s address unless specifically requested.

	1. I get what is going on here but a lot of this is highly useful information, if I’m going to have a customized AI browser these are top priority things it needs to know. So I guess you need to be explicit about this because lawyers.

There don’t seem to be explicit instructions there about what to do with the information in memory. Presumably it gets loaded into context and then handled normally?

In addition to this, in some fashion it is storing memories for individual webpages you visit, including page title or topic, summarized key points and metadata, so these can be searched later, although I’m not sure mechanically how this happens, in the sense that the system instructions I saw shouldn’t trigger this, but presumably they do anyway. It also will have memories of incomplete tasks.

#### The Other Kind of Memory

> [Darin Fisher:](https://x.com/darinwf/status/1980758825750917570) one thing to note about Atlas is that it actually is much more aggressive than stock chromium about discarding unused tabs. almost to a fault in some cases, but we’ve tried to tune it to work well. we borrowed a page from mobile and restrict memory usage more aggressively.

When I assembled this computer, I insisted on more RAM than the person helping me wanted to provide. Thanks to Chrome, I was right and she was wrong, except that I should have doubled it again. So yeah, Chrome is a memory hog, but also I look at my open tabs and I’m asking for it.

However I mostly want to keep as many tabs loaded as we can, so long as the memory is available? I won’t have a chance to experiment on this with the Mac, but the reason I bought that Mac was to have a ton of unified memory for AI things, so hopefully it will realize this and not discard any of my tabs.

#### OpenAI Is Trying To Lock You In

You can check out any time you want, but you can never leave (with your data).

OpenAI is very much not playing nice and it feels intentional.

Existing browsers vary in how nice they play with others.

Firefox, Brave and Chrome make it easy. Click the export button, and you’re good.

Edge lets you do it, but has the UX make it intentionally annoying to try and stop you.

Safari, like many Apple products, is trying to create lock\-in and is more hostile to departing users, but the data is safely in your file system and you can use various third\-party tools to get it out.

You could also compare this to cloud productivity and collaboration tools like Notion, Roam Research, Linear, Obsidian or Asana, all of which allow easy exporting.

It’s kind of hostile to launch without a reasonable data export feature, or any sort of sync feature even with itself. All you can do right now is export bookmarks.

If you offer me a way to sync with Chrome and with other computers, in both directions, we’ll talk more. Hell, at least assure us that this is on the roadmap.

This is on top of the lock\-in that comes from OpenAI’s browser memories feature and the rest of your ChatGPT history, which isn’t legible to other services, and also isn’t available for export, but at least does sync across computers.

#### Who Do You Trust?

Using Atlas as your main browser means putting quite a lot of trust in OpenAI.

There are two kinds of trust required here.

1. You are trusting OpenAI with your data, including highly sensitive data.
2. You are trusting OpenAI’s AI features to not get prompt injected or otherwise get you into serious trouble.

Using it for specific tasks requires less on both counts.

In terms of trusting OpenAI the company, you can decide how much you are willing to trust them. I trust them a substantial amount, but definitely a lot less than I trust Google, plus trusting OpenAI doesn’t mean you get to stop trusting Google. I’ve essentially decided to accept that for security Google is a point of failure, I could recover but if that relationship was compromised it would royally, epically suck. A second such point of failure would be additive, not a substitute.

Do you trust OpenAI with your passwords and browser history? You tell me.

OpenAI has not, from what I have seen, committed to a policy of not sharing info to third parties or for advertising purposes.

Then there’s the question of trusting the AI features, especially agent mode. Prompt injections remain unsolved, which is a general problem rather than an OpenAI problem, so the whole thing is radioactive if it touches potentially corrupted inputs. Any number of other things could also go wrong. You have to decide your level of comfort here as well.

Atlas takes roughly the same precautions as the cloud Agent mode did, [the release notes have the details](https://help.openai.com/en/articles/12591856-chatgpt-atlas-release-notes). It cannot run code, access other apps or your file system, or access your saved payment methods, passwords or autofills. It pauses before making purchases or taking sensitive actions ‘on sensitive sites’ although one worries about sites that it hasn’t identified. They’ve also added ‘logged out mode’ where the agent won’t have access to your credentials, and they plan to add more help over time.

[Dane offers an accounting of the precautions and their perspective](https://x.com/cryps1s/status/1981037851279278414). The long term goal is to trust it like you would trust a friend. We’re a long way from that, which OpenAI knows.

They’re still de facto counting on the user to not take stupid risks. Which is fine. I support offering users products that allow the taking of stupid risks, but that means you have to know this and then not take them.

[Brave offered us a thread explaining some vulnerabilities](https://x.com/brave/status/1980667345317286293) in Perplexity’s Comet AI assistant browser and other existing similar products, such as following instructions hidden in a screenshotted webpage. Some of them have been addressed by OpenAI, others likely have not.

I asked the Big Three (Google, OpenAI and Anthropic) for research reports on Atlas, with an emphasis on security issues, to see what they would think about this.

[Gemini gave a report](https://g.co/gemini/share/b20b36ec71a8) that had a lot of slop, which if you stuck it out and kept reading kind of wanted to bury the Atlas browser out in the desert using tongs, and warned to use it as experimental technology, with memory off by default, nothing else open, nothing sensitive and only specific bounded use cases with eyes on at all times.

[ChatGPT gave a report](https://chatgpt.com/share/68f91957-5924-8002-8925-0a744b5cc3af) I found, quite frankly, kind of suspicious in several places, such as trying to sell ChatGPT memories as superior to previous ‘manual’ histories a little too aggressively. Okay, more than a little. There’s also relatively scant attention to all the missing features and limitations. It does acknowledge that you’re placing a lot of trust in OpenAI if you use Atlas, and actively points out that some for reasonable reasons view it as a ‘data mining tool.’ Yet it also encourages you to use Atlas without worrying much about security, with a threshold of roughly ‘don’t give it unsupervised tasks you wouldn’t let another human do unsupervised.’ That doesn’t seem like enough.

[Claude Sonnet 4\.5 gave what I think was the best report, which I found highly useful](https://claude.ai/public/artifacts/f7c82267-83dc-413e-9a92-ad1320d9168a) and well organized. It highlighted features that Atlas is for now missing relative to Chrome, highlighted various security vulnerabilities involving the AI features, and concluding that 99% of users should stick with Chrome.

Its security recommendation was to never use Atlas for anything confidential, proprietary, financial, privileged, classified, sensitive or critical, and not to store payment methods or let it act unmonitored.

Whereas for passive media and other information consumption and browsing, you’re good to go, since you don’t have an attack surface, so the question is whether you’re getting value out of the AI features, and I think mostly its ‘use with extreme caution’ stuff is also mostly harmless.

The tricky questions are email, content creation and social media.

It’s hard to do many useful things if you don’t check your email, and some of the cool AI features are potentially at their best there, such as the autocomplete feature. On the other hand, email means unsecured data coming in.

So does social media, and both also allow outputs in your name. I would not be combining these with unsupervised agent mode, but with the rest of the browser it seems fine. I’d be fine letting it go on social media while you watch it, but if you’re watching it then what’s the point?

Content creation depends on what type of content. I felt very comfortable loading Substack into Atlas. The problem was there was little benefit, because of autocomplete not working in the editor.

[The Washington Post’s Geoffrey Fowler also focuses his review](https://www.washingtonpost.com/technology/2025/10/22/chatgpt-atlas-browser/) on the lens of privacy and potential security risks.

#### ChatGPT and Google Search Are Different Tools

Atlas makes ChatGPT your default search engine. No. Do not want.

Do I often substitute asking Claude or ChatGPT where I used to use Google Search? Reasonably often, sure.

There are still important cases where Google Search is the obviously correct tool. You know what you want, Google will know what you want if you gesture at it, you gesture, you get the URL. ChatGPT and other LLMs are much worse at this, they’re the wrong form factor.

Indeed, if my query is short enough that I want to type it into the url bar as a search, and it doesn’t require the page as context, then I almost always want Google.

It feels greedy and annoying to try and grab the default search engine slot here. I do realize you still get the other tabs, but also this means you get a bunch of kruft.

Then again, several users reported liking it, [such as Nick Farina](https://x.com/nfarina/status/1981046444565160362).

#### Browser Agents Need To Be Local

I strongly agree with Aidan that cloud\-only browsing agents mostly aren’t useful.

> [Aidan McLaughlin (OpenAI)](https://x.com/aidan_mclau/status/1980690755057598496https://x.com/aidan_mclau/status/1980690755057598496): My quick two cents on the browser —
> 
> I didn’t use Codex much when it was cloud\-only, but once it came to my CLI it became super useful.
> 
> I didn’t use Agent much when it was cloud\-only, but now that it’s come to my browser...

When I tried to use ChatGPT Agent mode before, I quickly concluded it wasn’t worthwhile. If you had to keep creating new cloud instances, with all the delays and hassles involved and need to constantly watch anyway, then you didn’t actually end up saving time. If you had to take over the browsing session, it was really annoying.

You need to get to critical mass, so you can experiment, learn what works and how to do various tasks, figure out the rhythms and iterate. A local version makes this a lot more exciting.

And yet I notice that I have Claude for Chrome and I basically never try to use it as an agent. I tried to get it to edit my Twitter Articles to fix that importing from Substack is semi\-broken, and with Sonnet 4\.5 it was almost up to that task but not quite there, and most everything else seemed to fall under easier to do myself.

I did manage to get it to do some useful transcription work and a bit of spreadsheet work, but the whole thing mostly said ‘hey go install Claude Code already or maybe Codex and improve your extension if you want this.’

The easiest ‘killer app’ is presumably online shopping, especially things like ‘here’s a recipe, go order everything I need’ or when you know exactly what you want and can easily verify if it was done properly. It seems especially good for commands you intend to repeat a lot, since you don’t have to reverify each time.

Again, everyone with access probably should experiment more now that it’s a lot more user friendly. Make it a point to let the AI try.

The problem with many simple tasks is that the time you save gets given back by worries about security. If you’re watching it work and forced to manually enter information, it gets hard to save much time.

#### Reactions

Even more than with model releases, what people care about gets quirky. We care about and notice our own personal workflows and pain points, and what makes that easy versus hard.

> [Gary Fung](https://x.com/garyfung/status/1980710416167956627): Chatgpt Atlas quick review: already enough to be a Chrome \& Gemini killer
> 
> \- SponsorBlock and uBlock Origin (lite) works, unlike youtube on chrome
> 
> \- i can chat with video transcript (like on youtube), which chatgpt and grok couldn’t access. Only reason I used gemini previously
> 
> [![](https://substackcdn.com/image/fetch/$s_!X3Vv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2048138b-754d-4532-9d86-ef9fbe24b394_1200x992.jpeg)](https://substackcdn.com/image/fetch/$s_!X3Vv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2048138b-754d-4532-9d86-ef9fbe24b394_1200x992.jpeg)

I’m perfectly happy with the ad block situation in Chrome right now, also seriously stop trying to be a cheapskate and pay for YouTube Premium already. Certainly it seems like madness to give up tab groups for better YouTube specific ad blocking. I mean how cheap are you?

If I specifically wanted YouTube to work better, and let’s say subscribing wasn’t an option, I’d use the alternative browser specifically for YouTube and only YouTube?

The video chat thing is legitimately useful, you definitely need a way to do that and right now Gemini is not in a good place and needs an upgrade. I haven’t actually had need of it recently, presumably Claude for Chrome would be my guy on that.

> [John Hughes](https://x.com/jjhughes/status/1981083562213257432): Atlas seems promising. Searches start as ChatGPT queries. When you click links, the chat smoothly shifts to a sidebar. UX feels more seamless \& integrated than Claude or Gemini’s. It’s often nice having AI in your sidebar, without having to copy/paste between tabs/windows, etc.
> 
> Some sites (NYTimes, ChatGPT itself) are blocked for Atlas AI access. (I use ChatGPT’s agent to file my old chats into folders; Atlas can’t.) Some Chrome basics aren’t fully baked yet. Agentic site interactions remain slow and clunky. But they’re clearly making progress.
> 
> \[This is] compared to Claude Chrome extension, which is useful but triggers many permission prompts even in low\-risk contexts \& always runs in a sidebar. Atlas has better UX: start with ChatGPT fullscreen → move to sidebar while browsing → back to fullscreen when you want just chat again

That’s a positive reaction to ChatGPT as the base search engine (which you can also do on Chrome if you want to, but you don’t get the additional tabs).

The UX does seem promising so far when it works. I find the Claude for Chrome UX to be exactly what you’d want it to be. I agree the permissions requests are a little paranoid, in terms of asking about each website even if it seems obviously safe, but you know what? I approve of that, it’s the right mistake to make, although I’d like various whitelists or groupings to make life easier. Over time, the problem shrinks as you’ve given permission for more of the safe sites.

It’s funny that one of the better use cases for agents is organizing tab groups, and Atlas flat out doesn’t offer you tab groups.

There are always those users who are up to no good, by LLM standards.

> [Papaya](https://x.com/papayathreesome/status/1981060695920693542): It doesn’t perform bad actions like searching torrent for a movie or go to a pornsite protection is both model level (it’ll refuse) and a blacklist of sites that won’t load in agent tabs (but will load in normal non\-agent tab)
> 
> i tried a few larger porn and torrent sites, but didn’t have chance to try smaller ones to check how thorough the list is.

I absolutely do not want AI agents going to porn or torrent sites, that’s almost asking to be hacked. Some of us remember when browsing the internet was not default safe.

Here’s one vote for the magic of travel and similar complex shopping tasks:

> [Timo Springer:](https://x.com/springertimo/status/1981014421725200492) i really like it; clean design, smooth performance, “ask chatgpt” is very helpful via sidebar, also the agent mode solved some of my tasks already even ones with lots of constraints. tried this one for a trip which i then booked afterwards: “Find the 10 cheapest hotels on http://Booking.com for Paris from May 8 to 10, 2026\. The hotels must have a rating of at least 9\.0, at least 20 reviews, and be less than 3 km from the city center.”

The catch in this particular case is that ChatGPT already has a booking.com plug\-in, so I was able to pull this off in 30 seconds by pasting that exact query into ChatGPT normally and then clicking on the ‘use booking.com’ button and confirming the plug\-in.

[Matt Heard looked to take advantage of agent mode](https://x.com/mattheard/status/1981020264696820009), but hit quota before getting good use out of it. In my experience it is remarkably easy for AI browsing agents to end up getting caught up in a very long loop that isn’t doing much except running through your credits.

He also complains that conversations in different tabs are not aware of each other (or at least, presumably aren’t short of you taking relevant notes.) He finds this frustrating, and yeah, that seems super annoying. One great thing about Claude for Chrome is that it can be aware of the rest of the tab group.

> [Miles Skorpen](https://x.com/milesskorpen/status/1981013892261404899): I struggled to find it useful. I missed Google for accessing sites w/o exact URLs, and 1Password didn’t work properly. The biggest problem was that it rewrote an email while including meta text like “I’ll rewrite to be more concise,” \- can’t just trust it!

That’s been my experience with LLMs writing or editing emails for years. By the time you figure out how to get it to do the thing, and have it do the thing, and check the thing, you could have done the thing. Obviously if your writing skills are weaker that is different.

And yeah, things like inexact URLs and various extensions are going to be big for a lot of people.

#### This Browser Could Have Been An Extension

I asked Claude Sonnet 4\.5 what Atlas does, on a technical level, that requires it be its own browser rather than an extension, other than to be an excuse to try and compete in the browser space, because Claude for Chrome exists and most of what Atlas does seemed like it was super doable in an extension.

Sonnet didn’t come up with much, so I asked GPT\-5\-Thinking to defend the decision.

> GPT\-5\-Thinking (condensed, I do not endorse most of this): 
> 
> What a full browser unlocks (and why an extension is the wrong tool)
> 
> 1. AI\-first omnibox \& results UI (default, not bolted\-on).
> 2. Per\-page content access \+ cross\-tab “browser memories” with policy gates.
> 3. Agent mode that can navigate \& act—under hard boundaries the browser enforces.
> 4. Network/engine control and performance.
> 5. System integrations and policy surface.
> 
> What you *can’t* get (or can’t get cleanly) as a Chrome extension
> 
> 6. Consistent, cross\-site automation that survives page transitions, popups, and multi\-domain flows with user\-visible pausing on “sensitive” sites.
> 7. Tight answer\-first search integration with omnibox/new\-tab defaults across OSes
> 8. Durable background intelligence. MV3 service workers are ephemeral (terminate in \~15s if idle).
> 9. Policy\-enforced guardrails like “agent cannot install extensions / run code / download files,” plus logged\-out agent mode and history exclusions.
> 10. First\-party privacy surface.

That seemed highly sus and Claude was having none of most of this, in terms of whether the product actually makes sense. Most of what is listed above isn’t needed or works as well or better in an extension. I let them go back and forth a bit, evaluated the arguments, and drew my own conclusions.

There seem to be six actual arguments for a browser.

1. MV3 service worker limit (I’ve run into this too), which requires either a cold\-start penalty or a keep\-alive ping, but whatever, that’s not on the level of ‘build a new browser.’
2. Answer\-first omnibox integration for the search experience. So okay, you can set ChatGPT as your search engine but you can’t have a web search open multiple tabs. I don’t especially want this feature, but even if you do like it, again it hardly seems like ‘new browser’ territory, you can just stack these things on a page.

	1. Similarly, if you want to have general tab management available on demand from ChatGPT, that’s not an extension feature.
3. Logged\-out agent mode is tricky to do as an extension. You’d need to coordinate with incognito windows or a distinct Google account or something.
4. Maybe you don’t want to trust Google or Chrome, but do want to trust OpenAI.
5. OpenAI wants platform control, and data control, and lock\-in, and to get around and compete with Google. Okay, sure. I see why you would want this. Go big.

The first three are not nothing but do not, to me, seem to be pulling that much weight. This seems rather clearly like a leverage play, using ChatGPT to try and force open the browser market, and a removal\-of\-leverage play, to avoid reliance on Google.

Which, to be clear, is totally fair play, it’s just not a good reason to play along.

Could OpenAI eventually assemble a superior overall non\-AI browsing experience, or create AI features that couldn’t live in an extension? Could a future version of this product be generally superior and play nice enough with others I’d be okay using it?

Sure. Chrome is far from perfect. Until then? At least for me?

Shrug.

####