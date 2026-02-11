# From idea to Product Hunt launch

*The journey of PinkyPartner*

Published: 2024-06-20
Source: https://theindiepreneur.substack.com/p/from-idea-to-product-hunt-launch

---

*👋 Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as a solopreneur who quit his job to chase his dreams.*

*I am a software developer, and so far I have x3 failed projects, and x2 ongoing.*

*I also publish [Tech Books](https://open.substack.com/pub/techbooks) summaries along with [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions).*

Join hundreds of subscribes to get weekly insights and personal experiences from the life of a solopreneur.

Subscribe

Two months ago I came up with an idea to write an app that will help me build a running habit.

It was a period of time when I felt extremely lonely and looked for ways to battle it.

So I reached out to a friend and asked him if he’s up for building a running habit with me. Run 2KM twice a week.

Luckily, he was in for it.  
We created a contract on google docs to make it official and followed up on each other weekly on WhatsApp.

In the beginning it was awesome and really helped me stay motivated and improved the loneliness feeling.

But as time went by the enthusiasm slowly faded, at least for me, to a point when I stopped.

And the reason I stopped is that it was too much work.

→ Write a contract on google docs every few weeks to reflect the improvement or changes needed.

→ Follow up on WhatsApp once/twice a week to share your progress.

→ Remind your partner if they didn’t update you on their progress.

I know, it might sound like it’s just a few minutes every week.  
But building habits is hard enough as it is. Adding more friction doesn’t help.

That’s when I thought: I wish there was something simpler. Much simpler.

#### 💡 Moment

That’s when I thought: “Why not code something simple myself?”

That way everybody can enjoy the benefits of having a partner to build habits with and have as little friction as possible.

# The idea

PinkyPartner main goal was to be simple.

1. Find your partner
2. Create a contract with habits
3. Notify your partner when you’re done

After spending days on writing something quite complex, I figured that it’s too much and the design is too messy.

Hiring a UX designer to redesign everything would be a waste of time and money.

Instead I tried to figure out how can I do simple, easy and have a quick MVP?  
This is what I came up with:

1. Have an invite button if your partner is not on PinkyPartner
2. Each contract will contain only one habit
3. Have a satisfying checkbox for each task
4. Build a notification system
5. Notify on: Task done/New contract created.

# The execution

At first I thought about writing a very stable app, with a dedicated serverless backend, using AWS and learning React Native.

Then I remembered of what I read in [Itzy Sabo](https://open.substack.com/users/18876758-itzy-sabo?utm_source=mentions)’s [Web Apps are Native Apps](https://www.ctologic.pro/p/web-apps-are-native-apps) and figured that writing a PWA with NextJS would be the fastest way to build an MVP.

And I can also make it completely free if I use MongoDB or Supabase.

After some contemplating, this is the tech stack I decided on:

---

#### **Front, Back**

**React, TailwindCSS, Shadcn, NextJS.**

I have a lot of experience with this stack combination, so it was a no\-brainer for me.

#### **DB**

**MongoDB**

After watching a few of Marc Lou’s videos on YouTube, where he advocates for MongoDB, I figured I could give it a go.

It plays well with Prisma, which is a fantastic ORM library, and it’s free.

#### **Cloud**

**Vercel**

This is another no\-brainer. The developer experience of Vercel is unmatched.   
Vercel automatically publishes your product after you push your changes to master.

It creates both the frontend deployment and the backend lambdas.

---

One month later, I officially announced PinkyPartner on LinkedIn and Substack.

[I wrote about it in length here](https://theindiepreneur.substack.com/p/i-launched-a-productit-wasnt-what).

Another month after that, I launched on ProductHunt.

# The big launch (Product Hunt)

---

#### Short introduction to Product Hunt:

Every work day Product Hunt runs a competition of products.  
It can be anything from a newsletter (See [Tom Orbach](https://open.substack.com/users/11987234-tom-orbach?utm_source=mentions)’s incredible achievement [I hit \#1 on Product Hunt… here’s how I guaranteed my win 🏆](https://www.marketingideas.com/p/i-hit-1-on-product-hunt-heres-how)) to a SaaS product.

Then people can upvote products they like, and the product with the most upvotes and quality upvotes (Product Hunt has an algorithm to determine that) wins.

Now, there’s the featured page, which is the first page of products you see.  
This is where every creator hopes to end up.

Now, to avoid “pay to win”, in the first 4 hours of the competition Product Hunt randomizes the order of the product in the and hides the upvote count, so everybody can have an equal chance and the featured page is much bigger.

---

A week before I launched, I started building the showcase of PinkyPartner.

A few images, Product Hunt teaser page, emails list and contact ways to people who I supported their product, so they can support back, if they like PinkyPartner.

I prepared for a massive flow of people to the website, which didn’t happen.

[![](https://substackcdn.com/image/fetch/$s_!qTOJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9814a8ad-df2e-4ed8-9fc4-1312a6b15d65_383x530.png)](https://substackcdn.com/image/fetch/$s_!qTOJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9814a8ad-df2e-4ed8-9fc4-1312a6b15d65_383x530.png)

But… **I got 11 new sign ups! 🎉**From \~138 unique visits, which is a \~9% conversion rate.

That might not sound like a lot, but it’s a milestone :).

**BTW:**There’s another peak (See in this articles cover image) from when I published [How a 6 months partnership has ended](https://theindiepreneur.substack.com/p/how-a-6-months-partnership-ended), which was quite popular.

# The future

To be honest, I am not sure what I am going to do next with PinkyPartner.

This is the first product that I published this way and measuring a product’s success is something I believe you learn with time with experience and by reading about it.

I personally use it for my own habits and I will keep promoting it to people.

Whether or not I’ll be developing new features depends on returning users and interaction with PinkyPartner.

If I’ll see that there are several people who enjoy it and use it regularly, I will improve it and market it more.

If you are a user of PinkyPartner, let me know what you think about it in the comments! I’d love to hear your feedback :)

Besides, I neglected BookWiz for too long and it’s time to show it some love and perhaps post it on ProductHunt soon as well!

# Final words

The launch day was very exciting and a very important milestone for me.

It’s the first product I built that I can wholeheartedly say I have completed.

So I want to thank whoever took part in the launch, upvoted the product, commented, liked on LinkedIn and signed up.

More great things are coming [❤️](https://emojipedia.org/red-heart).

# 📣 What I enjoyed reading this week

[The no\-budget marketing strategy every founder needs 🌠](https://www.marketingideas.com/p/should-you-be-doing-founder-marketing) by [Tom Orbach](https://open.substack.com/users/11987234-tom-orbach?utm_source=mentions) \- Seriously, I enjoy reading every article on Tom’s newsletter. Whether you’re into marketing or not, you’ll enjoy it and learn something new.

[How to keep up with all the digital content](https://zaidesanton.substack.com/p/the-toughest-challenge-in-2024-consuming?utm_source=%2Finbox&utm_medium=reader2) by [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions) \- There’s so much knowledge out there but not enough time. Having a system to read only the best of the best is a must. Anton gives valuable tips and systems he uses to read only things that would give him the most value.

Join hundreds of subscribes to get weekly insights and personal experiences from the life of a solopreneur.

Subscribe