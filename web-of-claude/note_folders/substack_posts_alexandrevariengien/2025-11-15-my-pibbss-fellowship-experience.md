# My PIBBSS fellowship experience

*Reflections on effectively receiving mentorship, iterating quickly on UI software projects, and fiction writing.*

Published: 2025-11-15
Source: https://alexandrevariengien.substack.com/p/my-pibbss-fellowship-experience

---

This summer, I took part in the [PIBBSS fellowship](https://princint.ai/programs/fellowship/), a 3-month program aimed at bringing interdisciplinary perspectives to the field of AI safety.

[![img](https://substackcdn.com/image/fetch/$s_!Kes7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c340ec0-bf8f-47dd-b2fb-93a6f836e4db_2560x1447.jpeg "img")](https://substackcdn.com/image/fetch/$s_!Kes7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c340ec0-bf8f-47dd-b2fb-93a6f836e4db_2560x1447.jpeg)

*The manifestation of the PIBBSS spirit at the closing retreat.*

I am sharing here a retrospective of my experience: I will start by giving a short summary of my work for context, followed by a list of advice I would have liked my past self to receive before starting the fellowship. I expect the lessons to be most useful for fellows part of a research mentorship program with a strong vision for their project.

### **What did I work on?**

I worked on [differential development](https://michaelnotebook.com/dtd/), specifically focusing on imagination: making legible alternative paths for AI development and integration with society that support human flourishing.

My work included a combination of fiction writing (I published a short story, [The Connection](https://alexandrevariengien.com/the-connection)), AI interface prototyping (see [here](https://docs.google.com/presentation/d/1UFhrjoh3xpxWYXs7VmM53mXjrPg7IR_0J7wnau9jWvo/edit) for a presentation of Butterfly, a brainstorming tool), and conceptual research (see my final essay, “[Thick practices for AI tools](https://alexandrevariengien.com/thick-practice-ai-tools)”).

It was a high-exploration project, with a very unusual shape for a fellowship focused on AI safety. I am very grateful for the space provided by the program to develop these ideas. It shaped the way I am approaching my professional future now. I am also thankful for all the thoughtful people I met there, especially [Sahil](https://www.lesswrong.com/users/sahil-1?from=search_autocomplete), my mentor during the program.

### **Advice for my past self**

Ordered from the most general to the most specific.

##### **Mentor interaction.**

In a mentor-mentee relationship, there is a tension between the direction the mentee wants to explore and the research interests of the mentor. In theory, the mentee and the mentor are matched before the program for alignment. However, in practice, the match is not always perfect, and this tension will continue to play a role in their interactions as the project unfolds.

I would say this is the area where I succeeded the least. I followed my own ideas too strongly and left little room for Sahil to influence the direction of my projects, despite having a lot to learn from him.

I gained a lot from our discussions; they helped me grok important aspects of his vision for [live theory](https://www.lesswrong.com/posts/QvnzEHvodmwfBXu94/live-theory-part-0-taking-intelligence-seriously). Yet when I returned to work on my project, the content of our discussions did not change my priorities or the direction I was pursuing.

Good mentorship is a scarce resource, and even if it doesn’t feel like a 100% match with your interests, I would advise my past self to be more open to adjusting the project to align with the research area of their mentor. One learns a lot by following the path of an expert. Even if it is not a direction you want to follow long-term, there are long-lasting skills to pick up along the way. In practice, this often means working on a problem that the mentor designed and/or cares about.

This improves mentorship quality by raising i) legibility; the mentor can rely on their cached intuition to guide you during weekly meetings because it is the center of their expertise, and ii) motivation; the mentor is willing to spend more effort mentoring because it matches their own research priorities.

To check if you are, in fact, receiving project guidance, you could ask yourself: How is this meeting influencing the work I am doing? Which meeting outcome would change my default plan for the week? Do I start the meeting with an already formed idea of next steps and expect my mentor to nod along? Is my update understandable to my mentor? Do I provide enough information so they can form an opinion? If the answers indicate that the meetings have no bearing on the project direction, it would make sense to redefine the project with the mentor so they can effectively provide guidance.

That being said, having the flexibility to pursue independent work and engaging in a thread of conversations progressing deeper after each interaction was far from a waste of time and could be an optimal use of mentorship in some context.

But for the last two weeks of the program, I decided to drop my default plan and allocate a large part of my time to solving assignments designed to onboard fellows from another program to the live theory agenda. Even if it didn’t contribute to a clear output, upon reflection, I still believe that delving deeper into Sahil’s worldview was worth it. I would recommend my past self to do the assignment at the start rather than at the end of the project.

##### **Interface design.**

One line of work I pursued involved software engineering to design [Butterfly](https://docs.google.com/presentation/d/1UFhrjoh3xpxWYXs7VmM53mXjrPg7IR_0J7wnau9jWvo/edit), a whiteboard interface built on top of [tl;draw](https://tldraw.dev/). I had no experience using frontend frameworks like React; I had only used Streamlit before. I started going through the [React tic-tac-toe tutorial](https://react.dev/learn/tutorial-tic-tac-toe) using Claude as a coach to explain parts of the code, but I did not write any code myself.

**AI-assisted coding.**

I then used Claude Code to develop most of the interface. I enjoyed prompting using [SuperWhisper](https://superwhisper.com/) to seamlessly use voice-to-text with Claude Code and create richer prompts than what I would have done by typing.

Upon reflection, I could have spent more time learning frontend/backend best practices or design patterns for structuring the code, setting up a test environment, separating files, etc. This could have been done by looking at medium-sized open-source project repositories similar to what I wanted to design and using Claude Code to understand the structure of the codebase at a high level.

I feel I understood the role of the code pretty well, but the codebase grew really fast, and I could have organized the code better.

**Test your ideas earlier.**

You don’t need code to test your ideas. An MVP can be created by manually simulating the features you want to implement in code. Anything you learn purely through testing before writing any lines of code is a huge win.

I started conducting user panels to test the idea of the interface by creating a static mockup on a shared [tldraw](https://www.tldraw.com/) whiteboard. The user would brainstorm their ideas, and I would manually create cards in response. It is important that you don’t say anything to the test user beyond a short introduction to simulate a final user loading interacting for the software for the first time. Don’t communicate during the test session; let them struggle to understand the dynamics, and only intervene if they have been stuck for more than five minutes.

**Make your ideas simpler.**

Good interfaces rarely come from the combination of ten features that together create something great. Streamline your vision into one core mechanic that feels the most promising, and implement a bare-bones version of that. I often implemented features that sounded good but did not serve a core function, only to roll back because they introduced unmanageable complexity in the codebase.

I wanted to implement a type check for the cards created by the user, combining both the type checker from the Python package [pydantic](https://docs.pydantic.dev/latest/) and a LLM-based type checker that would verify if the content of each field matches its natural language description. I was really attached to supporting nested type checking, where a card could have fields that are themselves cards. I implemented it, but later decided to delete it because of the bugs that arose from the complexity it introduced. It was an elegant idea but not particularly useful in practice. There was a lot to be learned from a flat card structure alone.

##### **Fiction writing.**

I spent the first two weeks of the program writing the short story [The Connection](https://alexandrevariengien.com/the-connection). It was by far my most ambitious fiction writing project to date, even though it is still quite far from a novel-sized piece (7,300 words, approximately 15-20 pages). Around 50% of the first draft was already written when I started the fellowship. These first two weeks were spent finishing the initial draft, going through rounds of revisions, and translating the story into English (I wrote the original in French).

If you are interested in improving your writing, I strongly recommend *A Swim in a Pond in the Rain* by George Saunders. Its most useful contributions for me were the mental models on how to approach iterative story revisions and how stories evolve.

**AI assisted fiction writing.**

I wrote the initial draft by myself and used AI assistance for the revisions. I vibe-coded a simple Streamlit interface called Feather to help with iterating on the drafts (code [here](https://github.com/aVariengien/feather)). I started with an ambitious prompt containing some passages from *A Swim in a Pond in the Rain*, some of my writing from other projects, and instructed Claude Sonnet 3.5 to generate three variations of a given paragraph. I would then use them as inspiration to improve the passage.

I realized the prompt was costly (even with prompt caching) and unnecessarily long. I simplified the prompt to provide only the paragraph to revise, as well as two paragraphs above and two paragraphs below. This was enough for the LLM to pick up on the style.

I would say the AI assistance was worth it; it made me about 50% faster at going from the initial draft to the final story (though self-estimation is [not always reliable](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)), at the cost of making the tone of the writing a bit bland. I also used LLM for the final translation, I prompted the model to provide variations of the sentences or words in brackets so I could choose among the options.

I don’t regret the time I spent vibe-coding the Feather interface (~2 days), as there were no other easy ways to get variations of text integrated like Google Doc comments.

### **Closing thoughts**

The PIBBSS fellowship was overall a great experience. Beyond the content of the program, I learn a bit more on how to approach mentorship effectively, and quickly iterate on UI projects. May my experience benefit future fellows!