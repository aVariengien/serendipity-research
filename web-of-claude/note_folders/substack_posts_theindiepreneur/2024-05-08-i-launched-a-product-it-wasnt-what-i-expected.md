# I launched a product! (It wasn't what I expected)

*Lessons from my first product launch*

Published: 2024-05-08
Source: https://theindiepreneur.substack.com/p/i-launched-a-productit-wasnt-what

---

*👋 Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as an entrepreneur who quit his job to chase his dreams.*

*I am a software developer, and so far I have x3 failed projects, and x2 ongoing.*

*I am also publishing along with* [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions) *tech book summaries weekly [here](https://techbooks.substack.com/)*

Last Saturday was the first time my solo project saw the light of day.  
It’s called PinkyPartner and I shared more details about it [here](https://theindiepreneur.substack.com/p/my-first-solo-product-is-launched).

[Visit PinkyPartner](https://www.pinkypartner.com)

I would love it if you could check it out and give me your feedback!

I learned a lot from this launch about product, design and user behavior and I am going to share everything with you today.

# Key Takeaways:

1. Don't sweat cool designs.
2. A clear landing page \> A beautiful one.
3. Make sure people understand your product.
4. People don't like to have their time wasted. At all.
5. Your product needs to have a "single\-player" mode.

# Metrics

Let’s start with some metrics from PostHog (They have a fascinating substack [Product for Engineers](https://open.substack.com/pub/productforengineers)):

## Unique visits

[![](https://substackcdn.com/image/fetch/$s_!HIs8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e62037b-efba-4c0a-8e65-ffb78debcc54_292x577.png)](https://substackcdn.com/image/fetch/$s_!HIs8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e62037b-efba-4c0a-8e65-ffb78debcc54_292x577.png)

Total unique visits: **158**Total sign\-ups: 6  
Total unbribed (People I never talked to) signups: **2  
Conversion rate: 1\.2%.**

### Conversion rate

1\.2% conversion rate is very low, and here’s why I think it is:

**The landing page is tedious and unclear**

**5 sections, 3 videos and 5 clicks** before the user can understand what to do and get started with the app.

Nobody wants to go through a long, boring welcoming just to use an obscure app that they never heard of before.

Heck, even my brother didn’t manage to get through the landing page (I saw it in the PostHog session recordings ;))

#### **The lessons:**

1. If you need more sections, they should they’re **optional** for the user.
2. Make sure the core feature is clear in the first section of the landing page.
3. Videos that are longer than 5\-8 seconds do not work. Make them concise and clear.

## Returning users

[![](https://substackcdn.com/image/fetch/$s_!-MYI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b5deb62-aab4-4490-92c7-8d5703ce5a75_177x278.png)](https://substackcdn.com/image/fetch/$s_!-MYI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b5deb62-aab4-4490-92c7-8d5703ce5a75_177x278.png)

*Keep in mind that I visited the website daily since then, so I kept that last bar alive :)*

Besides my friend [Michał Poczwardowski](https://open.substack.com/users/141222242-micha-poczwardowski?utm_source=mentions), nobody revisited the website.

The reasons are crucial for the app's next phases and future products:

#### Have a single\-player mode

The way the app works right now, for it to be operational I need to convince you to:

1. Sign up
2. Create a promise
3. Create a contract
4. Invite your friend
5. Convince your friend to join
6. Make sure your friend goes through the process
7. Have you and your friend use the app constantly

Not only that it’s extremely hard to convince users to sign up and use your product, but in the current state of the app I need you to want to do the same. Which is like 10\-20x times harder.

So here’s how I am going to build my future products:

1. Build your “Convincing flow”.
2. Remove as many convincing as possible.
3. Design the core feature according to the flow.

In my case, here’s an example of my new convincing flow.

1. Sign up
2. ~~Create a promise~~
3. Create a contract
4. Start tracking your habits
5. ~~Invite your friend~~
6. ~~Convince your friend to join~~
7. ~~Make sure your friend goes through the process~~
8. ~~Have you and your friend use the app constantly~~

Much simpler, less coding.

Plus, it will be much easier to convince you to invite a friend once I know you’re using the app.

#### Make sure the UI is easy enough to follow

This is the flow you’ll encounter after you sign up:

[![](https://substackcdn.com/image/fetch/$s_!1dlI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23c2723c-2111-4e8c-a06d-5cfb4b90e94f_1868x815.png)](https://substackcdn.com/image/fetch/$s_!1dlI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23c2723c-2111-4e8c-a06d-5cfb4b90e94f_1868x815.png)

1. You are prompted to add a promise
2. You create a promise
3. You are prompted to create a contract
4. You search for a user or continue without one
5. You fill out the contract form
6. You have an option to invite a partner
7. You’re done.

There are several problematic things.

#### Chosen words

**Promise** (A repeating habit) and **Contract (**An agreement to follow up on the habits agreed upon) are not some day\-to\-day words that people can easily understand their context.

They are indeed cute and fit the theme of the website, **but if you decide to use such words, make sure people understand exactly what they mean so they can translate them into another word they understand better.**

#### Too much friction

Adding the Promises tab adds more complexity and friction to the app usage.

Promises are directly connected to a contract. No contract \- no usage of promises.  
Since they are directly connected and are each other’s requirements, why not let users create their promises inside the contract?

A combination of the two into one GREATLY reduces friction and the complexity of using the app.

#### Not enough incentive and help

I don’t tell the user why he should use the app at any point.  
For a regular habits app, I might not need to, because it’s pretty clear when you see these landing pages:

[![](https://substackcdn.com/image/fetch/$s_!apHE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1834bbf8-961c-4607-8bcd-262a941f1527_961x407.png)](https://substackcdn.com/image/fetch/$s_!apHE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1834bbf8-961c-4607-8bcd-262a941f1527_961x407.png)

[![](https://substackcdn.com/image/fetch/$s_!8UPk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf84f17b-5056-4348-bf48-2e79760a1955_884x422.png)](https://substackcdn.com/image/fetch/$s_!8UPk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf84f17b-5056-4348-bf48-2e79760a1955_884x422.png)

[![](https://substackcdn.com/image/fetch/$s_!V5Lq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9290c485-8e72-4948-a5b6-450e920ac58b_1208x510.png)](https://substackcdn.com/image/fetch/$s_!V5Lq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9290c485-8e72-4948-a5b6-450e920ac58b_1208x510.png)

We already know what they mean and what’s the purpose.

But when you create something new that is already widespread, you need to make sure that your onboarding process tells the users what is the app meant for and why they should use it.

Now, if you need them to do something extra, like inviting a friend, make it as simple as possible for them.

For example, instead of letting them copy the URL, then choose the platform to share it with and send it to their partner, like this:

[![](https://substackcdn.com/image/fetch/$s_!bB4t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F091b9d38-ce50-4194-9d9f-f79435c406b2_570x353.png)](https://substackcdn.com/image/fetch/$s_!bB4t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F091b9d38-ce50-4194-9d9f-f79435c406b2_570x353.png)

I can show a popup, like on YouTube, that they can share with a click:

[![](https://substackcdn.com/image/fetch/$s_!XNzw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbbefb31-971d-43bb-b40e-1dc41f37e441_506x456.png)](https://substackcdn.com/image/fetch/$s_!XNzw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbbefb31-971d-43bb-b40e-1dc41f37e441_506x456.png)

# Mobile vs Desktop first

[![from bookwiz.app](https://substackcdn.com/image/fetch/$s_!KjR3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcac840cd-4cc4-4721-9640-9ad8164c9d90_996x178.png "from bookwiz.app")](https://substackcdn.com/image/fetch/$s_!KjR3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcac840cd-4cc4-4721-9640-9ad8164c9d90_996x178.png)

From bookwiz.app

[![](https://substackcdn.com/image/fetch/$s_!sLGf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabac6d91-d6c3-4a3e-9349-9187df842699_1673x197.png)](https://substackcdn.com/image/fetch/$s_!sLGf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabac6d91-d6c3-4a3e-9349-9187df842699_1673x197.png)

From pinkypartner.com

I think this is more of a technical question.  
Although the data supports the fact that more people come from desktops, I think that the mobile\-first approach is the better one.

1. popular CSS libraries, like TailwindCSS, are built for a mobile\-first approach.
2. Going from a mobile design to a desktop design requires a lot less effort than going from a desktop to a mobile.
3. **Mobile will look decent on desktop.** Even if you don’t consider any desktop designs when you build your app mobile\-first, the desktop will still look decent. **It doesn’t work the other way around.**

These are the main reasons why **I will always start with mobile design.**

# Is there a future for PinkyPartner?

To be honest, I don’t know. The feedback I got from people who spoke to me personally is very good.

The data shows something else, but I believe that it’s because there are many flaws that I need to take care of before I can really measure it.

**One thing is for sure, there’s going to be a Phase 2,** where I will improve all the things I talked about in this article and share it again.

This time, I will make it bigger.

* LinkedIn
* YouTube
* ProductHunt
* Reddit
* Hacker
* YC

And that will be the big test to know whether the app has a potential or not.

I believe it’s going to take me at least a couple of weeks. I am going to set a deadline soon and share it as a post here and on LinkedIn.

[Follow on LinkedIn](https://www.linkedin.com/in/orel-zilberman-225a37137/)

# Final words

Building this project was exciting and exhausting.  
It took me around 120 hours to complete the project, end to end, in 10 days, and it was worth it.

I learned a lot, both technical and product stuff, so the next phase and my next products will be much better.

I would like to thank [Michał Poczwardowski](https://open.substack.com/users/141222242-micha-poczwardowski?utm_source=mentions), [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions), [Akash Mukherjee](https://open.substack.com/users/197891722-akash-mukherjee?utm_source=mentions) and other people(Sara, Esty, Raz, Mor and Amitay) who are not on Substack, for being early testers and giving me feedback [❤️](https://emojipedia.org/red-heart)

# 📣 Shout\-outs of the week

[👉](https://emojipedia.org/backhand-index-pointing-right) [Why I have a love/hate relationship with scripts](https://newsletter.weskao.com/p/love-hate-relationship-with-scripts) by [Wes Kao](https://open.substack.com/users/4005715-wes-kao?utm_source=mentions) \- Wes talks about the good side and the pitfalls of using scripts in customer interactions.

> "Your script should serve you, not the other way around. Remember to stay present and use your judgment."

---

[👉](https://emojipedia.org/backhand-index-pointing-right) [An engineer’s guide to talking to users](https://newsletter.posthog.com/p/talk-to-users) by [Product for Engineers](https://open.substack.com/pub/productforengineers) \- Seven great insights for engineers on effective user communication.

> “We have a simple theory about building successful products: the people building them should be as close to people using them as possible.”

---

[Engineering Project Estimation](https://www.leadership-letters.com/p/engineering-project-estimation) by [Akash Mukherjee](https://open.substack.com/users/197891722-akash-mukherjee?utm_source=mentions) \- Akash shares his five practical strategies to improve engineering project estimations.

> "The goal is not to get it right, but to get it less wrong."