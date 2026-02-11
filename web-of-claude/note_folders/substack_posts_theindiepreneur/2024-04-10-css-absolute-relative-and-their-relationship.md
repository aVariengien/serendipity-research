# CSS - Absolute, Relative and their relationship

*How absolute and Relative interact together*

Published: 2024-04-10
Source: https://theindiepreneur.substack.com/p/css-absolute-relative-and-their-relationship

---

👋 *Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as an entrepreneur who quit his job to chase his dreams.*

*I am a software developer, and so far I have x3 failed projects, and x2 ongoing.*

*I am also publishing along with* [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions)tech book summaries

In today’s article, I am going to discuss CSS positioning.  
Specifically Relative, Absolute and how they interact.

As a FullStack developer, I found this concept one of the hardest to grasp, so I decided to make it easier for fellas who still struggle with it.

# Relative, Absolute and how they interact

## Relative

**Relative positioning** lets you move an element a bit from where it would usually sit on the page. But unlike some magic tricks in CSS, it doesn’t make the element disappear from its normal place. It’s still there, taking up space, but you can move it up, down, left, or right.

Think of it as a layer that defines the relation between its children to the layer.  
Every child within the layer is bound to its size and z\-index.

We’ll see the relationship more in\-depth in a few moments.

## Absolute

**Absolute** positioning is like being given a magic wand in the world of CSS. It allows you to place an element exactly where you want it, regardless of where other components are placed in the layer.

This comes with some caveats:

* **Layout Disruptions**: Absolute positioned elements are removed from the normal HTML elements stack. therefore, they no longer take up space among their sibling elements.  
That means that if your layout changes in the future, you might need to address each absolute element separately.
* **Responsiveness Challenges**: When an element is Absolute positioned, it might not adjust as expected when the screen size changes.
* **Dynamic Content Risks**: In web apps where content size can change dynamically (think a list that you can add items to), using absolute positioning without careful consideration can lead to elements overlapping in ways that break your design.

[![](https://substackcdn.com/image/fetch/$s_!Uf4W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd509555-e97e-401b-a0fc-a7a7d927b8c8_854x386.png)](https://substackcdn.com/image/fetch/$s_!Uf4W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd509555-e97e-401b-a0fc-a7a7d927b8c8_854x386.png)

## Relative and Absolute interaction

### **A Defined Size**

Each element can have a defined size, specified by setting its width and height properties.

When you create a relative element with size, all it’s children will be bound to its size.  
Therefore, if you place an absolute element within that relative parent, the 0,0 coordinates are the left corner of the wrapping relative parent.

Let’s see an example:

[![](https://substackcdn.com/image/fetch/$s_!DtEr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aef0d86-9cf2-4867-a822-9c4d9df7ad4d_326x340.png)](https://substackcdn.com/image/fetch/$s_!DtEr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aef0d86-9cf2-4867-a822-9c4d9df7ad4d_326x340.png)

[![](https://substackcdn.com/image/fetch/$s_!yv1u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14ac7ec3-090e-43b9-aa49-8f99e6ed68fe_326x340.png)](https://substackcdn.com/image/fetch/$s_!yv1u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14ac7ec3-090e-43b9-aa49-8f99e6ed68fe_326x340.png)

### **A Different Set of Z\-indexes**

The z\-index property controls the stacking order of elements that overlap.   
**It can only be applied to elements with a position ≠ static (the default).**

This is where the concept of layers comes into play. By assigning different z\-index values, you can control which layers appear on top of others. Here's how the z\-index works:

* Without a z\-index, elements stack in the order they appear in the HTML.
* With z\-index, a higher value means the element will be closer to the top of the stacking order.
* Elements with the same z\-index value will stack in their source order (the order they appear in the HTML).

Now here’s the tricky part:

Each relative element with a specified z\-index value creates a new stacking context for its child elements. This means that the z\-index values of children are calculated relative to the parent, and not to the document as a whole.

Essentially, the stacking context isolates a part of the webpage's elements.  
Those element’s z\-index work within that specific context, rather than interacting with the entire page's elements.

Let’s see an example:

[![](https://substackcdn.com/image/fetch/$s_!QXtW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70b0f6f9-57ed-4dd7-a87a-00e4af76c9ca_1123x507.png)](https://substackcdn.com/image/fetch/$s_!QXtW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70b0f6f9-57ed-4dd7-a87a-00e4af76c9ca_1123x507.png)

###

## 📣 Shout\-outs of the week

[What we learned about hiring from our first five employees](https://newsletter.posthog.com/p/what-we-learned-about-hiring-from?utm_source=profile&utm_medium=reader2) by [Andy Vandervell](https://open.substack.com/users/69984721-andy-vandervell?utm_source=mentions) \- PostHog started with 5 people. These 5 people stayed with them 4 years and 39 employees later.  
As a user of PostHog, I am not surprised.

**[10 Must\-Reads for Engineering Leaders](https://zaidesanton.substack.com/p/10-must-reads-for-engineering-leaders)** by [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions) \- Anton recently became a Director of Engineering and decided to share his top 10 books for engineering leaders.

**[Circle of Competence \- Mental Model](https://read.perspectiveship.com/p/circle-of-competence?utm_source=%2Finbox&utm_medium=reader2)** by [Michał Poczwardowski](https://open.substack.com/users/141222242-micha-poczwardowski?utm_source=mentions) \- Michal talks about the concept of the Circle of Competence and the importance of looking outside of it for growth.

“Be aware of what you are good at and where you lack expertise. Ensure you minimize the gap between what you *think* you know and what you actually know. Remember, the best solution to a problem may lie outside your Circle of Competence. So, ask and explore.”

**[How I Upgraded My Conflict Resolution Skills (Part 2\)](https://www.leadership-letters.com/p/how-i-upgraded-my-conflict-resolution-93e?utm_source=%2Finbox&utm_medium=reader2)** by [Akash Mukherjee](https://open.substack.com/users/197891722-akash-mukherjee?utm_source=mentions) \- With great illustrations, Akash shares part 2 of his conflict resolution skills. A great read for people who lead or want to lead.

“…It is okay to feel uncomfortable providing feedback. I still feel the same. What is not okay is hiding areas of improvement to protect our feelings.”

## 🎉 Welcome to new subscribers!

[Christian Kuntz](https://open.substack.com/users/183484727-christian-kuntz?utm_source=mentions) [Salameh](https://open.substack.com/users/133682535-salameh?utm_source=mentions)[Seeking Insights](https://open.substack.com/users/8580497-seeking-insights?utm_source=mentions)[Raksha Kannusami](https://open.substack.com/users/46242383-raksha-kannusami?utm_source=mentions)[Savas](https://open.substack.com/users/33693308-savas?utm_source=mentions)[Schlubbi](https://open.substack.com/users/120666048-schlubbi?utm_source=mentions)[Bogdan Veliscu](https://open.substack.com/users/115684107-bogdan-veliscu?utm_source=mentions)[Kedson Queiroz](https://open.substack.com/users/113277270-kedson-queiroz?utm_source=mentions)[Duy Nghia Dev](https://open.substack.com/users/85147097-duy-nghia-dev?utm_source=mentions)[Koushlendra Kumar](https://open.substack.com/users/201399431-koushlendra-kumar?utm_source=mentions)[Mahesh Shastry](https://open.substack.com/users/153234272-mahesh-shastry?utm_source=mentions)[Laurence Charles](https://open.substack.com/users/121358032-laurence-charles?utm_source=mentions)[Yassine A.](https://open.substack.com/users/216230553-yassine-a?utm_source=mentions)[Pranav Raj](https://open.substack.com/users/185451636-pranav-raj?utm_source=mentions)[Rajan Sharma](https://open.substack.com/users/126754254-rajan-sharma?utm_source=mentions)[Gabriel Damalis](https://open.substack.com/users/166911166-gabriel-damalis?utm_source=mentions)[Aysen Benli](https://open.substack.com/users/116036735-aysen-benli?utm_source=mentions)[Jay](https://open.substack.com/users/110328575-jay?utm_source=mentions)

Sorry for those of you I missed, SubStack’s search is awful.