# $500K milestone – my reflections after 1 year of building Typing Mind

*Also in this issue: one-off purchase vs. subscription, selling Xnapper, and other updates from me in Feb 2024*

Published: 2024-02-26
Source: https://news.tonydinh.com/p/500k-milestone-my-reflections-after

---

Hi everyone, it’s Tony again with another update! 👋

[![](https://substackcdn.com/image/fetch/$s_!_sx_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aa009b7-4910-4aba-bd73-6a034f798712_1000x1333.jpeg)](https://substackcdn.com/image/fetch/$s_!_sx_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aa009b7-4910-4aba-bd73-6a034f798712_1000x1333.jpeg)

I’m working remotely from a coffee in Bangkok. Amazing city :)

In February 2024, my ChatGPT chat frontend, [Typing Mind](https://www.typingmind.com), reaches $500K in total revenue. It started out almost exactly one year ago as a simple UI for ChatGPT API.

[![](https://substackcdn.com/image/fetch/$s_!pU11!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc1c15e-af7d-4175-b0ad-e0f28758d764_3080x1572.png)](https://substackcdn.com/image/fetch/$s_!pU11!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc1c15e-af7d-4175-b0ad-e0f28758d764_3080x1572.png)

Thanks to everyone who has purchased and enjoyed using the app!

Looking back, I have some thoughts on this amazing one-year journey I want to share with you here.

## **Being early to the niche is a huge advantage**

Typing Mind [was released](https://news.tonydinh.com/p/making-22k-in-7-days-the-story) just 5 days after OpenAI announced the API. I think it is the first of its kind, providing an alternative UI for ChatGPT with the “Use your own API Key” concept.

When you’re first to the niche, your first version (MVP) doesn’t have to be so amazing. People have an itch, and there’s nothing on the market to fix it. If you give them something to scratch that itch, even just a bit, they’ll be happy to buy.

In this case, there were many annoying things with the standard ChatGPT interface e.g., it keeps logging you out every day, it types the answer very slowly, and there was no way to search past conversations…

Even though OpenAI fixed all this a few months later, I was able to capture the public attention during this time. If I were late to the party, there wouldn’t be any annoying problems to solve anymore, or at least the problems wouldn’t be that painful/important anymore.

Another example I’ve seen that captured a niche early is Chatbase (built by [Yasser](https://x.com/yasser_elsaid_/status/1759603542489272384?s=20)) - an AI chatbot SaaS. He launched on February 2023 when most of us still hadn’t really realized how big the AI chatbot (or chat with documents/website/etc) space could be. Now he is making $3M/year. Compared to Chatbase, Typing Mind is a tiny product.

## Pressure to keep up

The AI space is moving incredibly fast.

Once captured the initial traction, I need to keep moving to catch up.

Within the last 12 months, I pushed out [171 updates](https://www.typingmind.com/changelog) to Typing Mind, and I still have [a ton more](https://typingmind.com/ideas) to do.

People come up with new ways to chat with AI all the time; OpenAI also drops new big announcements once every few months. And all this won’t be stopping anytime soon.

I had to spend all of my time building and improving the product. Very little time to do anything else like marketing, SEO, trying paid ads, cold outreach, building community, etc.

The good thing is that I enjoyed building/coding. New customers still come in every day, so the overall experience wasn’t so bad for me personally.

However, to create a sustainable business, I’m not sure I can rely solely on organic traffic forever. I’ve been considering doing some “real marketing” or at least hiring someone to do it, but this comes with a different set of problems I need to learn to solve.

## One-time purchase vs. Subscription

In the beginning, Typing Mind started with a one-time purchase. It was one of the reasons why the app sold so well in the beginning.

This was possible because the core product of Typing Mind is just a static web app with no back end and no database. It doesn’t even have an account system or login/logout. Typing Mind is activated using only a license key. That means it costs me almost nothing to host and run the app, and that’s why I can afford to sell the license as a one-time purchase.

Then, I gradually added a new subscription sources:

* A Cloud Sync & Backup server to allow users to seamlessly sync data across devices. This comes with a server and database to run, so I charge a subscription.
* The custom version of Typing Mind for teams ([Typing Mind Custom](https://custom.typingmind.com)) requires a subscription, as it needs servers and databases.
* In the custom version, there is also an “Additional training data limit plan” which is also a subscription.

Typing Mind’s revenue is now a mix of one-off purchases and subscription revenue. It’s a healthy mix!

As of now, the subscription part of Typing Mind is at $15K MRR. This has surpassed my last record of a subscription product, Black Magic (which was making $14K MRR at the time of acquisition).

[![](https://substackcdn.com/image/fetch/$s_!iufM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F743cfde7-4794-447c-8fd0-0ff85ce27a3c_1162x770.png)](https://substackcdn.com/image/fetch/$s_!iufM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F743cfde7-4794-447c-8fd0-0ff85ce27a3c_1162x770.png)

I find this mix of subscription and one-time purchase to be the best model.

* On the one hand, I don’t have to worry about not being sustainable for providing lifetime access. The revenue from the subscription sources could easily justify the costs for lifetime users (mostly the cost of customer support).
* On the other hand, every feature and improvement I add to the static version (one-time purchase) will automatically benefit the Custom version (subscription), and vice versa. This will also help make the static version more attractive to new users and encourage them to buy.

Obviously, an all-subscription model would bring me more stable revenue. But the benefit here is that I can sell to regular users more easily with a lifetime license, as it only costs once. Most users will be happy to pay once and use the product forever, which saves them more money in the long term.

The downside is that I need to be very careful every time I add a new feature to the static version (one-time purchase). I can’t simply add a feature that requires an ongoing cost (like a free sync service). The maths must check out. Otherwise, it’s hard to keep my promise of giving lifetime access.

## Other updates: I’m selling Xnapper

Last week, I posted on Twitter that I was looking for a buyer for Xnapper. I’ve already found a buyer, and I’m in the process of acquisition.

[![](https://substackcdn.com/image/fetch/$s_!kvX5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F406c61a8-f85a-4e24-bd05-6992b1e812be_1466x1734.png)](https://x.com/tdinh_me/status/1758085010127749310?s=20)

The main reason I want to sell Xnapper is that I feel like I’m wasting its potential. I spend all of my time on Typing Mind these days, which brings me the majority of my revenue, so I have little time and motivation left to continue growing Xnapper.

Of course, I can just leave it on autopilot and take my sweet passive income, but it just feels very “wasteful” to me, considering I know how much potential Xnapper has for growth.

I love and use Xnapper every day (as you can see from the screenshots in this post), but right now, I don’t have the time to bring it to the next level.

I’ve evaluated all the potential buyers who reached out and agreed to go forward with a very enthusiastic, energetic buyer who is super interested in growing Xnapper.

I’ll share more about this acquisition in the next newsletter issue once the acquisition officially closes.

## That’s all for now!

Thank you for reading my updates. I hope it’s been helpful in some way 😄

I’ll see you next month with more updates and follow-up on the acquisition of Xnapper.

Until next time!

- Tony