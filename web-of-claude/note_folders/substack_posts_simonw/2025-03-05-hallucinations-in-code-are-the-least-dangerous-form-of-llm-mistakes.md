# Hallucinations in code are the least dangerous form of LLM mistakes

*Plus notes on accessibility and generative AI, and an automaton called Squadron*

Published: 2025-03-05
Source: https://simonw.substack.com/p/hallucinations-in-code-are-the-least

---

In this newsletter:

* Hallucinations in code are the least dangerous form of LLM mistakes
* Notes from my Accessibility and Gen AI podcast appearance
* I built an automaton called Squadron

Plus 6 links and 2 quotations

### [Hallucinations in code are the least dangerous form of LLM mistakes](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/) \- 2025\-03\-02

A surprisingly common complaint I see from developers who have tried using LLMs for code is that they encountered a hallucination \- usually the LLM inventing a method or even a full software library that doesn't exist \- and it crashed their confidence in LLMs as a tool for writing code. How could anyone productively use these things if they invent methods that don't exist?

Hallucinations in code **are the least harmful hallucinations you can encounter from a model**.

(When I talk about *hallucinations* here I mean instances where an LLM invents a completely untrue fact, or in this case outputs code references which don't exist at all. I see these as a separate issue from bugs and other mistakes, which are the topic of the rest of this post.)

The real risk from using LLMs for code is that they'll make mistakes that *aren't* instantly caught by the language compiler or interpreter. And these happen *all the time*!

The moment you run LLM generated code, any hallucinated methods will be instantly obvious: you'll get an error. You can fix that yourself or you can feed the error back into the LLM and watch it correct itself.

Compare this to hallucinations in regular prose, where you need a critical eye, strong intuitions and well developed fact checking skills to avoid sharing information that's incorrect and directly harmful to your reputation.

With code you get a powerful form of fact checking for free. Run the code, see if it works.

In some setups \- [ChatGPT Code Interpreter](https://simonwillison.net/tags/code-interpreter/), [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), any of the growing number of "agentic" code systems that write and then execute code in a loop \- the LLM system itself will spot the error and automatically correct itself.

If you're using an LLM to write code without even running it yourself, *what are you doing?*

Hallucinated methods are such a tiny roadblock that when people complain about them I assume they've spent minimal time learning how to effectively use these systems \- they dropped them at the first hurdle.

My cynical side suspects they may have been looking for a reason to dismiss the technology and jumped at the first one they found.

My less cynical side assumes that nobody ever warned them that you have to put a lot of work in to learn how to get good results out of these systems. I've been exploring [their applications for writing code](https://simonwillison.net/tags/ai-assisted-programming/) for over two years now and I'm still learning new tricks (and new strengths and weaknesses) almost every day.

#### Manually testing code is essential

Just because code looks good and runs without errors doesn't mean it's actually doing the right thing. No amount of meticulous code review \- or even comprehensive automated tests \- will demonstrably prove that code actually does the right thing. You have to run it yourself!

Proving to yourself that the code works is your job. This is one of the many reasons I don't think LLMs are going to put software professionals out of work.

LLM code will usually look fantastic: good variable names, convincing comments, clear type annotations and a logical structure. This can lull you into a false sense of security, in the same way that a gramatically correct and confident answer from ChatGPT might tempt you to skip fact checking or applying a skeptical eye.

The way to avoid *those* problems is the same as how you avoid problems in code by other humans that you are reviewing, or code that you've written yourself: you need to actively exercise that code. You need to have great manual QA skills.

A general rule for programming is that you should *never* trust any piece of code until you've seen it work with your own eye \- or, even better, seen it fail and then fixed it.

Across my entire career, almost every time I've assumed some code works without actively executing it \- some branch condition that rarely gets hit, or an error message that I don't expect to occur \- I've later come to regret that assumption.

#### Tips for reducing hallucinations

If you really are seeing a deluge of hallucinated details in the code LLMs are producing for you, there are a bunch of things you can do about it.

* Try different models. It might be that another model has better training data for your chosen platform. As a Python and JavaScript programmer my favorite models right now are Claude 3\.7 Sonnet with thinking turned on, OpenAI's o3\-mini\-high and GPT\-4o with Code Interpreter (for Python).
* Learn how to use the context. If an LLM doesn't know a particular library you can often fix this by dumping in a few dozen lines of example code. LLMs are incredibly good at imitating things, and at rapidly picking up patterns from very limited examples. Modern model's have increasingly large context windows \- I've recently started using Claude's new [GitHub integration](https://support.anthropic.com/en/articles/10167454-using-the-github-integration) to dump entire repositories into the context and it's been working extremely well for me.
* Chose [boring technology](https://boringtechnology.club/). I genuinely find myself picking libraries that have been around for a while partly because that way it's much more likely that LLMs will be able to use them.

I'll finish this rant with a related observation: I keep seeing people say "if I have to review every line of code an LLM writes, it would have been faster to write it myself!"

Those people are loudly declaring that they have under\-invested in the crucial skills of reading, understanding and reviewing code written by other people. I suggest getting some more practice in. Reviewing code written for you by LLMs is a great way to do that.

---

*Bonus section*: I asked Claude 3\.7 Sonnet "extended thinking mode" to review an earlier draft of this post \- "`Review my rant of a blog entry. I want to know if the argument is convincing, small changes I can make to improve it, if there are things I've missed.`". It was quite helpful, especially in providing tips to make that first draft a little less confrontational! Since you can share Claude chats now [here's that transcript](https://claude.ai/share/685cd6d9-f18a-47ef-ae42-e9815df821f1).

---

### [Notes from my Accessibility and Gen AI podcast appearance](https://simonwillison.net/2025/Mar/2/accessibility-and-gen-ai/) \- 2025\-03\-02

I was a guest on [the most recent episode](https://accessibility-and-gen-ai.simplecast.com/episodes/ep-6-simon-willison-datasette) of the [Accessibility \+ Gen AI Podcast](https://linktr.ee/a11ygenai), hosted by Eamon McErlean and Joe Devon. We had a really fun, wide\-ranging conversation about a host of different topics. I've extracted a few choice quotes from the transcript.

#### LLMs for drafting alt text

I use LLMs for the first draft of my alt text ([22:10](https://www.youtube.com/watch?v=zoxpEM6TLEU&t=22m10s)):

> I actually use Large Language Models for most of my alt text these days. Whenever I tweet an image or whatever, I've got a Claude project called Alt text writer. It's got a prompt and an example. I dump an image in and it gives me the alt text.
> 
> I very rarely just use it because that's rude, right? You should never dump text onto people that you haven't reviewed yourself. But it's always a good starting point.
> 
> Normally I'll edit a tiny little bit. I'll delete an unimportant detail or I'll bulk something up. And then I've got alt text that works.
> 
> Often it's actually got really good taste. A great example is if you've got a screenshot of an interface, there's a lot of words in that screenshot and most of them don't matter.
> 
> The message you're trying to give in the alt text is that it's two panels on the left, there's a conversation on the right, there's a preview of the SVG file or something. My alt text writer normally gets that right.
> 
> It's even good at summarizing tables of data where it will notice that actually what really matters is that Gemini got a score of 57 and Nova got a score of 53 \- so it will pull those details out and ignore \[irrelevant columns] like the release dates and so forth.

Here's the current custom instructions prompt I'm using for that Claude Project:

> `You write alt text for any image pasted in by the user. Alt text is always presented in a fenced code block to make it easy to copy and paste out. It is always presented on a single line so it can be used easily in Markdown images. All text on the image (for screenshots etc) must be exactly included. A short note describing the nature of the image itself should go first.`

#### Is it ethical to build unreliable accessibility tools?

On the ethics of building accessibility tools on top of inherently unreliable technology ([5:33](https://www.youtube.com/watch?v=zoxpEM6TLEU&t=5m35s)):

> Some people I've talked to have been skeptical about the accessibility benefits because their argument is that if you give somebody unreliable technology that might hallucinate and make things up, surely that's harming them.
> 
> I don't think that's true. I feel like people who use screen readers are used to unreliable technology.
> 
> You know, if you use a guide dog \- it's a wonderful thing and a *very* unreliable piece of technology.
> 
> When you consider that people with accessibility needs have agency, they can understand the limitations of the technology they're using. I feel like giving them a tool where they can point their phone at something and it can describe it to them is a world away from accessibility technology just three or four years ago.

#### Why I don't feel threatened as a software engineer

This is probably my most coherent explanation yet of why I don't see generative AI as a threat to my career as a software engineer ([33:49](https://www.youtube.com/watch?v=zoxpEM6TLEU&t=33m51s)):

> My perspective on this as a developer who's been using these systems on a daily basis for a couple of years now is that I find that they enhance my value. I am so much more competent and capable as a developer because I've got these tools assisting me. I can write code in dozens of new programming languages that I never learned before.
> 
> But I still get to benefit from my 20 years of experience.
> 
> Take somebody off the street who's never written any code before and ask them to build an iPhone app with ChatGPT. They are going to run into so many pitfalls, because programming isn't just about can you write code \- it's about thinking through the problems, understanding what's possible and what's not, understanding how to QA, what good code is, having good taste.
> 
> There's so much depth to what we do as software engineers.
> 
> I've said before that generative AI probably gives me like two to five times productivity boost on the part of my job that involves typing code into a laptop. But that's only 10 percent of what I do. As a software engineer, most of my time isn't actually spent with the typing of the code. It's all of those other activities.
> 
> The AI systems help with those other activities, too. They can help me think through architectural decisions and research library options and so on. But I still have to have that agency to understand what I'm doing.
> 
> So as a software engineer, I don't feel threatened. My most optimistic view of this is that the cost of developing software goes down because an engineer like myself can be more ambitious, can take on more things. As a result, demand for software goes up \- because if you're a company that previously would never have dreamed of building a custom CRM for your industry because it would have taken 20 engineers a year before you got any results... If it now takes four engineers three months to get results, maybe you're in the market for software engineers now that you weren't before.

---

### [I built an automaton called Squadron](https://simonwillison.net/2025/Mar/4/squadron/) \- 2025\-03\-04

I believe that the price you have to pay for taking on a project is [writing about it afterwards](https://simonwillison.net/2022/Nov/6/what-to-blog-about/#projects). On that basis, I feel compelled to write up my decidedly non\-software project from this weekend: Squadron, an automaton.

I've been obsessed with [automata](https://en.wikipedia.org/wiki/Automaton) for decades, ever since I first encountered the [Cabaret Mechanical Theater](https://en.wikipedia.org/wiki/Cabaret_Mechanical_Theatre) in Covent Garden in London (there from 1984\-2003 \- today it's a roaming collection). If you're not familiar with them, they are animated mechanical sculptures. I consider them to be the highest form of art.

For my birthday this year Natalie signed me up for a two day, 16 hour hour weekend class to make one at [The Crucible](https://www.thecrucible.org/) in Oakland. If you live in the SF Bay Area and are not yet aware of the Crucible I'm delighted to introduce you \- it's a phenomenal non\-profit art school with an enormous warehouse that teaches blacksmithing, glass blowing, welding, ceramics, woodwork and dozens of other crafts. Here's [their course catalog](https://www.thecrucible.org/course-search/). Go enrich your soul!

I took their class in "Mechanical Sculpture", which turned out to be *exactly* a class in how to make automata. I guess the term "automota" isn't widely enough known to use in the course description!

The class was small \- two students and one instructor \- which meant that we got an extremely personalized experience.

#### What I built

On day one we worked together on a class project. I suggested a pelican, and we built exactly that \- a single glorious pelican that flapped its wings and swooped from side to side.

Day two was when we got to build our own things. We'd already built a pelican, but I wanted one of my own... so I figured the only thing better than a pelican is a full squadron of them!

Hence, Squadron. Here's a video of my finished piece in action:

I think it captures their pelican charisma pretty well!

#### How I built it

I was delighted to learn from the class that the tools needed to build simple automata are actually quite accessible:

* A power drill
* A saw \- we used a Japanese pull saw
* Wood glue
* Screws
* Wood \- we mainly worked with basswood, plus I used some poplar wood for the wings
* Brass wires and rods
* Pliers for working with the wire

The most sophisticated tool we used was a reciprocating [scroll saw](https://en.wikipedia.org/wiki/Scroll_saw), for cutting shapes out of the wood. We also had access to a bench sander and a drill press, but those really just sped up processes that can be achieved using sand paper and a regular hand drill.

I've taken a lot of photos of pelicans over the years. I found this side\-on photograph that I liked of two pelicans in flight:

[![Two glorious pelicans in flight, viewed sideways on](https://substackcdn.com/image/fetch/$s_!kIuw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a3f9ba3-c956-461f-9674-187b2fa99746_1086x724.jpeg "Two glorious pelicans in flight, viewed sideways on")](https://substackcdn.com/image/fetch/$s_!kIuw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a3f9ba3-c956-461f-9674-187b2fa99746_1086x724.jpeg)

Then I used the iOS Photos app feature where you can extract an object from a photo as a "sticker" and pasted the result into iOS Notes.

[![Screenshot of iOS notes - just the first pelican is in the note, with a white background instead of the sky](https://substackcdn.com/image/fetch/$s_!_miO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e3e801a-8c0f-4860-8ee9-4a73fe7c7589_1320x1191.jpeg "Screenshot of iOS notes - just the first pelican is in the note, with a white background instead of the sky")](https://substackcdn.com/image/fetch/$s_!_miO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e3e801a-8c0f-4860-8ee9-4a73fe7c7589_1320x1191.jpeg)

I printed the image from there, which gave me a pelican shape on paper. I cut out just the body and used it to trace the shape onto the wood, then ran the wood through the scroll saw. I made three of these, not paying too much attention to accuracy as it's better for them to have slight differences to each other.

For the wings I started with rectangles of poplar wood, cut using the Japanese saw and attached to the pelican's body using bent brass wire through small drilled holes. I later sketched out a more interesting wing shape on some foam board as a prototype (loosely inspired by photos I had taken), then traced that shape onto the wood and shaped them with the scroll saw and sander.

Most automata are driven using [cams](https://en.wikipedia.org/wiki/Cam_(mechanism)), and that was the pattern we stuck to in our class as well. Cams are incredibly simple: you have a rotating rod (here driven by a 12V 10RPM motor) and you attach an offset disc to it. That disc can then drive all manner of useful mechanisms.

For my pelicans the cams lift rods up and down via a "foot" that sits on the cam. The feet turned out to be essential \- we made one from copper and another from wood. Without feet the mechanism was liable to jam.

I made both cams by tracing out shapes with a pencil and then cutting the wood with the scroll saw, then using the drill press to add the hole for the rod.

The front pelican's body sits on a brass rod that lifts up and down, with the wings fixed to wires.

The back two share a single wooden dowel, sitting on brass wires attached to two small holes drilled into the end.

To attach the cams to the drive shaft I drilled a small hole through the cam and the brass drive shaft, then hammered in a brass pin to hold the cam in place. Without that there's a risk of the cam slipping around the driving rod rather than rotating firmly in place.

After adding the pelicans with their fixed wings I ran into a problem: the tension from the wing wiring caused friction between the rod and the base, resulting in the up\-and\-down motion getting stuck. We were running low on time so our instructor stepped in to help rescue my project with the additional brass tubes shown in the final piece.

#### What I learned

The main thing I learned from the weekend is that automata building is a much more accessible craft than I had initially expected. The tools and techniques are surprisingly inexpensive, and a weekend (really a single day for my solo project) was enough time to build something that I'm really happy with.

The hardest part turns out to be the fiddling at the very end to get all of the motions just right. I'm still iterating on this now (hence the elastic hair tie and visible pieces of tape) \- it's difficult to find the right balance between position, motion and composition. I guess I need to get comfortable with the idea that art is [never finished, merely abandoned](https://quoteinvestigator.com/2019/03/01/abandon/).

I've been looking out for a good analog hobby for a while now. Maybe this is the one!

---

**Link** 2025\-03\-01 [llm\-anthropic \#24: Use new URL parameter to send attachments](https://github.com/simonw/llm-anthropic/issues/24):

Anthropic released a neat quality of life improvement today. [Alex Albert](https://twitter.com/alexalbert__/status/1895504248206709246):

> We've added the ability to specify a public facing URL as the source for an image / document block in the Anthropic API

Prior to this, any time you wanted to send an image to the Claude API you needed to base64\-encode it and then include that data in the JSON. This got pretty bulky, especially in conversation scenarios where the same image data needs to get passed in every follow\-up prompt.

I implemented this for [llm\-anthropic](https://github.com/simonw/llm-anthropic) and shipped it just now in version 0\.15\.1 (here's [the commit](https://github.com/simonw/llm-anthropic/commit/ac4fe809aff9842b05118e83c256690b92b49c4c)) \- I went with a patch release version number bump because this is effectively a performance optimization which doesn't provide any new features, previously LLM would accept URLs just fine and would download and then base64 them behind the scenes.

In testing this out I had a *really* impressive result from Claude 3\.7 Sonnet. I found [a newspaper page](https://chroniclingamerica.loc.gov/lccn/sn86086481/1900-01-29/ed-1/seq-2/#date1=1756&index=10&rows=20&words=PELICAN+Pelican+Pelicans+PELICANS&searchType=basic&sequence=0&state=&date2=1922&proxtext=pelicans&y=0&x=0&dateFilterType=yearRange&page=1) from 1900 on the Library of Congress (the "Worcester spy.") and fed a URL to the PDF into Sonnet like this:

```
llm -m claude-3.7-sonnet \
  -a 'https://tile.loc.gov/storage-services/service/ndnp/mb/batch_mb_gaia_ver02/data/sn86086481/0051717161A/1900012901/0296.pdf' \
'transcribe all text from this image, formatted as markdown'
```

[![Screenshot of the PDF - it has many dense columns](https://substackcdn.com/image/fetch/$s_!qqn3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd80dbb5a-46a6-4ecc-9f39-ff3f52295648_1257x605.jpeg "Screenshot of the PDF - it has many dense columns")](https://substackcdn.com/image/fetch/$s_!qqn3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd80dbb5a-46a6-4ecc-9f39-ff3f52295648_1257x605.jpeg)

I haven't checked every sentence but it appears to have done [an excellent job](https://gist.github.com/simonw/df1a0473e122830d55a0a3abb51384c9), at a cost of 16 cents.

As another experiment, I tried running that against my example `people` template from the schemas feature I released [this morning](https://simonwillison.net/2025/Feb/28/llm-schemas/):

```
llm -m claude-3.7-sonnet \
  -a 'https://tile.loc.gov/storage-services/service/ndnp/mb/batch_mb_gaia_ver02/data/sn86086481/0051717161A/1900012901/0296.pdf' \
  -t people
```

That only gave me [two results](https://github.com/simonw/llm-anthropic/issues/24#issuecomment-2691773883) \- so I tried an alternative approach where I looped the OCR text back through the same template, using `llm logs --cid` with the logged conversation ID and `-r` to extract just the raw response from the logs:

```
llm logs --cid 01jn7h45x2dafa34zk30z7ayfy -r | \
  llm -t people -m claude-3.7-sonnet
```

... and that worked fantastically well! The result started like this:

```
{
  "items": [
    {
      "name": "Capt. W. R. Abercrombie",
      "organization": "United States Army",
      "role": "Commander of Copper River exploring expedition",
      "learned": "Reported on the horrors along the Copper River in Alaska, including starvation, scurvy, and mental illness affecting 70% of people. He was tasked with laying out a trans-Alaskan military route and assessing resources.",
      "article_headline": "MUCH SUFFERING",
      "article_date": "1900-01-28"
    },
    {
      "name": "Edward Gillette",
      "organization": "Copper River expedition",
      "role": "Member of the expedition",
      "learned": "Contributed a chapter to Abercrombie's report on the feasibility of establishing a railroad route up the Copper River valley, comparing it favorably to the Seattle to Skaguay route.",
      "article_headline": "MUCH SUFFERING",
      "article_date": "1900-01-28"
    }
```

[Full response here](https://github.com/simonw/llm-anthropic/issues/24#issuecomment-2691773883).

---

**Link** 2025\-03\-02 [18f.org](https://18f.org/):

New site by members of 18F, the team within the US government that were doing some of the most effective work at improving government efficiency.

> For over 11 years, 18F has been proudly serving you to make government technology work better. We are non\-partisan civil servants. 18F has worked on hundreds of projects, all designed to make government technology not just efficient but effective, and to save money for American taxpayers.
> 
> However, all employees at 18F – a group that the Trump Administration GSA Technology Transformation Services Director called "the gold standard" of civic tech – were terminated today at midnight ET.
> 
> **18F was doing exactly the type of work that DOGE claims to want – yet we were eliminated.**

The entire team is now on "administrative leave" and locked out of their computers.

But these are not the kind of civil servants to abandon their mission without a fight:

> **We’re not done yet.**
> 
> We’re still absorbing what has happened. We’re wrestling with what it will mean for ourselves and our families, as well as the impact on our partners and the American people.
> 
> But we came to the government to fix things. And we’re not done with this work yet.
> 
> More to come.

You can [follow @team18f.bsky.social](https://bsky.app/profile/team18f.bsky.social) on Bluesky.

---

**Quote** 2025\-03\-02

> *Regarding [the recent blog post](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/), I think a simpler explanation is that hallucinating a non\-existent library is a such an inhuman error it throws people. A human making such an error would be almost unforgivably careless.*

[Kellan Elliott\-McCrea](https://fiasco.social/@kellan/114092761910766291)

---

**Quote** 2025\-03\-02

> *After publishing this piece, I was contacted by Anthropic who told me that Sonnet 3\.7 would not be considered a 10^26 FLOP model and cost a few tens of millions of dollars to train, though future models will be much bigger.*

[Ethan Mollick](https://www.oneusefulthing.org/p/a-new-generation-of-ais-claude-37)

---

**Link** 2025\-03\-03 [The features of Python's help() function](https://www.pythonmorsels.com/help-features/):

I've only ever used Python's `help()` feature by passing references to modules, classes functions and objects to it. Trey Hunner just taught me that it accepts strings too \- `help("**")` tells you about the `**` operator, `help("if")` describes the `if` statement and `help("topics")` reveals even more options, including things like `help("SPECIALATTRIBUTES")` to learn about specific advanced topics.

---

**Link** 2025\-03\-04 [llm\-mistral 0\.11](https://github.com/simonw/llm-mistral/releases/tag/0.11):

I added [schema support](https://simonwillison.net/2025/Feb/28/llm-schemas/) to this plugin which adds support for the [Mistral API](https://docs.mistral.ai/api/) to LLM. Release notes:

> * Support for LLM [schemas](https://llm.datasette.io/en/stable/schemas.html). [\#19](https://github.com/simonw/llm-mistral/issues/19)
> * `-o prefix '{'` option for forcing a response prefix. [\#18](https://github.com/simonw/llm-mistral/issues/18)

Schemas now work with OpenAI, Anthropic, Gemini and Mistral hosted models, plus self\-hosted models via [Ollama](https://www.ollama.com/) and [llm\-ollama](https://github.com/taketwo/llm-ollama).

---

**Link** 2025\-03\-04 [llm\-ollama 0\.9\.0](https://github.com/taketwo/llm-ollama/releases/tag/0.9.0):

This release of the `llm-ollama` plugin adds support for [schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/), thanks to a [PR by Adam Compton](https://github.com/taketwo/llm-ollama/pull/36).

Ollama provides very robust support for this pattern thanks to their [structured outputs](https://ollama.com/blog/structured-outputs) feature, which works across all of the models that they support by intercepting the logic that outputs the next token and restricting it to only tokens that would be valid in the context of the provided schema.

With Ollama and `llm-ollama` installed you can run even run structured schemas against vision prompts for local models. Here's one against Ollama's [llama3\.2\-vision](https://ollama.com/library/llama3.2-vision):

```
llm -m llama3.2-vision:latest \
  'describe images' \
  --schema 'species,description,count int' \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg
```

I got back this:

```
{
    "species": "Pelicans",
    "description": "The image features a striking brown pelican with its distinctive orange beak, characterized by its large size and impressive wingspan.",
    "count": 1
}
```

(Actually a bit disappointing, as there are [two pelicans](https://static.simonwillison.net/static/2025/two-pelicans.jpg) and their beaks are brown.)

---

**Link** 2025\-03\-04 [A Practical Guide to Implementing DeepSearch / DeepResearch](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/):

I really like the definitions Han Xiao from Jina AI proposes for the terms DeepSearch and DeepResearch in this piece:

> **DeepSearch** runs through an iterative loop of searching, reading, and reasoning until it finds the optimal answer. \[...]
> 
> **DeepResearch** builds upon DeepSearch by adding a structured framework for generating long research reports.

I've recently found myself cooling a little on the classic RAG pattern of finding relevant documents and dumping them into the context for a single call to an LLM.

I think this definition of DeepSearch helps explain why. RAG is about answering questions that fall outside of the knowledge baked into a model. The DeepSearch pattern offers a tools\-based alternative to classic RAG: we give the model extra tools for running multiple searches (which could be vector\-based, or FTS, or even systems like ripgrep) and run it for several steps in a loop to try to find an answer.

I think DeepSearch is a lot more interesting than DeepResearch, which feels to me more like a presentation layer thing. Pulling together the results from multiple searches into a "report" looks more impressive, but I [still worry](https://simonwillison.net/2025/Feb/25/deep-research-system-card/) that the report format provides a misleading impression of the quality of the "research" that took place.

---