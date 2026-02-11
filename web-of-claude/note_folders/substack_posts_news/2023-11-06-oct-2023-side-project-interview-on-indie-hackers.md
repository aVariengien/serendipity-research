# Oct 2023: side project, interview on Indie Hackers

*Going viral, my thoughts, and updates from me in October 2023.*

Published: 2023-11-06
Source: https://news.tonydinh.com/p/oct-2023-side-project-interview-on

---

Happy Monday, everyone 👋

I want to spend some time today to write about some updates in the last few weeks.

## I went viral + my thoughts.

My [last newsletter issue](https://news.tonydinh.com/p/my-solopreneur-story-zero-to-45kmo) was the most popular issue I’ve ever written in this newsletter.

It went “semi-viral” [on Twitter](https://x.com/tdinh_me/status/1705155679819084179?s=20) and [#1 on Hacker News](https://news.ycombinator.com/item?id=37622702) for a whole day.

I’ve read through almost all of the 600 comments, and I want to share some random thoughts on things people have talked about.

### **Indie products are “largely useless products” and “pet rocks”?**

This is a common attitude towards indie products, and it’s completely wrong.

I make a living from a screenshot app. It contributes almost nothing to advancing humanity to a better world, but at least I’m helping some people out there with their tiny problems, and I’m proud of it.

If you’re building an indie product, never let anyone tell you that it’s useless or not. Only listen to “the market” and your customers, they are the ones who can decide the value of your product.

### **Is it all luck? Survivorship bias?**

I can confirm that luck is a factor. However, it’s not all luck. If you put in consistent effort, when luck comes, it multiplies your output. It’s called “be prepared to get lucky”.

I could be a “survivor”, and I’m aware of that possibility. That’s why in the post, I encouraged people to cherry-pick things they learned from my story, not to try to replicate everything. However, it seems many people didn’t really read the whole post, or they read, but because of their biases, they only “see what they want to see”.

### **The positivity**

Other than the negative comments, there are also a lot of positive comments in the Hacker News thread. Thank you to everyone who has put in nice words!

My intention to write the post is to share and inspire, and I think going viral really helped.

I don’t know about you, but for me, knowing “something is possible” before attempting to do it is quite important, and sometimes is the decision maker for a lot of things I do.

By writing the post, I want to let people know that it’s possible to become a solopreneur/indie hacker and make a good living from it. No need to spend half of your waking hours working a job you don’t like, stuck living in one city because that’s where your job is, or drown yourself in corporate drama.

## New side project

Last week, I built [a new project](https://twitter.com/tdinh_me/status/1718168640783294941):

[![](https://substackcdn.com/image/fetch/$s_!llKa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F546dee10-649b-4356-832c-392f72a3aa98_1418x1906.png)](https://substackcdn.com/image/fetch/$s_!llKa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F546dee10-649b-4356-832c-392f72a3aa98_1418x1906.png)

I’ve been wanting to build this since ElevenLabs announced the [input streaming API](https://twitter.com/elevenlabsio/status/1688638033980014592).

The idea was to create an “AI conversation” as real as possible so I could talk to an AI like in real life.

Previously, [Typing Mind](https://typingmind.com) could do this too, but one big problem is that the voice can only start after the full response from GPT-4 is received. This causes a delay, and it kills the “feeling” of real-time conversation.

You can play with it here (with your own API keys): [speakdual.com](https://speakdual.com)

It is built using three main components:

* Browser Speech-to-Text API: run directly on the browser.
* ElevenLabs streaming input/output: also runs directly on the browser using Web Socket and Audio API.
* Browser CaptureStream API to visualize the microphone voice and audio output.

The latency between “you finish talking” and “AI start talking” is about 2 seconds, which I was very happy with!

I tried to make it run entirely on the browser, it kinda works. The only problem is that not all browsers support the APIs I listed above (not yet). Most importantly, it doesn’t work on iOS Safari, so that’s a big turndown.

The browser limitation demotivates me a bit, knowing that whatever product I built out of this will not run on all devices. I released it anyway and told people to use Chrome for the best experience 😂

If I do this again, I will probably give up on trying to make it work entirely on the browser. Instead, I would stream the input to the server, do GPT-4 and text-to-speech on the server, and then stream the output back to the client. That would work on most browsers and devices.

On another related note, just yesterday, the ChatGPT mobile app finally became available in the Vietnam App Store. I have never been able to try the mobile app until now.

[![](https://substackcdn.com/image/fetch/$s_!NdTg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe45e935-6ffd-4918-b010-404bf33a41c7_1290x2796.png)](https://substackcdn.com/image/fetch/$s_!NdTg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe45e935-6ffd-4918-b010-404bf33a41c7_1290x2796.png)

When I used the voice chat feature of ChatGPT, it was waaay better than what I’d built. The latency and the animation were extremely good. The voice-to-text recognition could have been better (but that’s probably because of my English accent.)

If I had access to the ChatGPT mobile app since the beginning, I probably wouldn’t have built the [speakdual.com](https://speakdual.com) side project. But anyway, I got some new experience working with audio APIs, plus owning a cool new domain name!

---

## *A quick word*

*As I'm about to send out this email, **[Daniel Vassallo](https://twitter.com/dvassallo)** reached out for a sponsorship.*

*Daniel is one of my indie hacker idols. I learned about him via the Indie Hacker podcast 2 years ago when I started my journey. Daniel has been really supportive of me, especially in the early days. We also shared the same mindset on a lot of topics related to indie hacking and solopreneur.*

*I’m happy to do a one-off sponsorship with Daniel and his latest work. Here is a message from Daniel:*

> Hey friends of Tony! — I run the Small Bets community with my co-host Louie Bacaj. If you're interested in solopreneurship, forget about "starting a company". Try making $1,000 with a small project first :)
>
> We learn a lot more from small wins than from big failures. When you join Small Bets you'll find a support network ready to help you get your first small wins, along with regular live workshops to teach you various solopreneurship topics.
>
> If this interests you, we're running an early Black Friday deal. $185 instead of $375 for a lifetime membership. Pay once, member forever. No recurring fees.
>
> [Join us today!](https://smallbets.co/?ref=news.tonydinh.com&utm_source=news.tonydinh.com)

---

## My interview on Indie Hackers

A few weeks ago, I did an email interview with James from Indie Hackers. James later turned this into a conversation format, which I find interesting, it changed the flow and the tone of the conversation a bit, but overall no major issues 😄

We talked about indie hacking, platform risk, mindset, work/life balance, and some more random topics. [You can read the interview here.](https://www.indiehackers.com/post/tony-dinh-hit-22k-in-11-days-by-decoupling-input-from-output-e07829fe23)

[![](https://substackcdn.com/image/fetch/$s_!QbQm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea36c15e-58ed-4aa7-8c65-d195dd4d682c_2008x1992.png)](https://substackcdn.com/image/fetch/$s_!QbQm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea36c15e-58ed-4aa7-8c65-d195dd4d682c_2008x1992.png)

## Other updates

As for work, I’m still focusing on building out Typing Mind.

Most noticeably, I decided to automate the selling process of the self-host version of [Typing Mind Custom](https://custom.typingmind.com). Previously, anyone who wanted to buy had to “Contact Us”. Now, it’s all self-serve.

[![](https://substackcdn.com/image/fetch/$s_!yLAw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b7f0763-4912-4ede-a103-14e1ea43bbc2_1606x1864.png)](https://substackcdn.com/image/fetch/$s_!yLAw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b7f0763-4912-4ede-a103-14e1ea43bbc2_1606x1864.png)

Some people are curious about the decision to sell the self-host version. Here are answers to some frequently asked questions:

* This self-host version only gives the compiled source, so I’m not selling the whole product. Even though, if a big customer (enterprise) comes and asks for the full source code, I could probably consider that if the deal size is big enough.
* The price is set high enough so that I can reduce the risk of bad actors trying to get the compiled source and reverse engineer it.
* The price is a one-time purchase because after the customer buys the self-host source code, they’ll deploy it on their infra, and it doesn’t cost me the server and database.
* Do people buy this? Yes, they do. I have 3 customers buying the self-host version so far.

In October, my overall revenue from Typing Mind went down. Fluctuations are expected as it’s just a one-time purchase revenue.

However, the recurring revenue MRR is still going up. This is a good sign and gives me more confidence in focusing on the custom version of Typing Mind!

[![Image](https://substackcdn.com/image/fetch/$s_!zAIP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d431cd1-9491-4977-ae74-9ac082fdda83_1772x1690.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!zAIP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d431cd1-9491-4977-ae74-9ac082fdda83_1772x1690.jpeg)

## That’s all for now!

This newsletter now has almost 10,000 subscribers. Thank you for being a part of my journey!

I’ll see you again next month with more updates.

Have a great week ahead!

- Tony