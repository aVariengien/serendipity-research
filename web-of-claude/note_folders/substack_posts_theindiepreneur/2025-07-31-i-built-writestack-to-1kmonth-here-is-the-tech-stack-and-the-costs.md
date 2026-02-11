# I Built WriteStack to $1K/month. Here is the tech stack and the costs:

*What I use. What it costs. Why it works.*

Published: 2025-07-31
Source: https://theindiepreneur.substack.com/p/writestack-tech-stack-tools-pricing

---

[![](https://substackcdn.com/image/fetch/$s_!ksua!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a8ec76d-fdc9-450e-8202-d1f46f079792_426x409.png)](https://substackcdn.com/image/fetch/$s_!ksua!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a8ec76d-fdc9-450e-8202-d1f46f079792_426x409.png)

[Share](https://theindiepreneur.substack.com/p/writestack-tech-stack-tools-pricing?utm_source=substack&utm_medium=email&utm_content=share&action=share)

Most indie founders overcomplicate their stack.

They burn months wiring up fancy infra no one asked for and wonder why they’re still at $0 MRR.

I built WriteStack solo, scaled it to paying users, and kept the stack as lean as possible.

## What is WriteStack?

WriteStack is a tool I built to solve my own problem.

Building my Substack community while developing SaaS tools and trying to not become a workaholic (failed on that front….).

So, after many iterations, I found the winning idea.

An easy to use Notes system, that helps you create, manage and schedule your Notes.

Notes are responsible for 30\-50% of big creators exposure and subscribers.

So I now have all my Notes in one place, I schedule ahead so I don’t forget and I always have a personalized AI assistance to help me bring out the creativity in me.

Now, let’s dive into the technology.

## My focus when choosing a technology

I evaluate new tech in this order:

1. Does it solve my need?
2. Do I already know it? (Faster to ship)
3. How long will it take to implement?
4. Do others recommend it?
5. How much does it cost?

I’m not allergic to paying for tools. If $50 saves me 10 hours, that’s a steal.

Now here’s every tool I use, why I chose it, and exactly how much it costs.

## Frontend\+backend

I use the basic stach for the frontend.

1. TypeScript
2. React
3. Node
4. NextJS
5. Prisma
6. Vercel to host everything

I always use TypeScript. It doesn’t take any longer than writing in plain JS, and in my opinion it’s much faster.

There were many occasions where I had to refactor old code, and without having types, I would probably spend an hour to figure it out.

**Price**: $20/month

## Coding

I use Cursor and ChatGPT only.

**Price:** \~$50/month

## Payment processing

I use Stripe to process payments, although I might switch in the near future due to the taxes process, which is a pain if you’re not a US resident.

The reason I chose Stripe is because it’s dead simple to implement and the UI is extremely easy and intuitive.

Plus it’s the \#1 payment processing service out there.

**Price: $**950/year \+ $500 one\-time payment.

## Databases

### MongoDB

I use MongoDB for saving the user’s day\-to\-day data, like user information, notes in the app, subscriptions, etc.

Why Mongo? It’s extremely lightweight, plays well with Prisma and easy to update.

**Price:** \~$30/month

### RDS (Postgres)

I use Amazon’s RDS to store the data of user’s notes from Substack and posts, so I can create statistics for them fast.

In addition, by creating a separation between the day\-to\-day database (MongoDB) and the big database, I have less load on my Mongo and the UX is much better and smoother.

**Price:** \~$52/month

### Milvus DB

Milvus DB is used to store vectorized data.

Vectorized data is a mathematical representation of the context of a text.

Why is it helpful? To search through a database of millions of rows by context, BLAZINGLY fast.

So finding notes that are relevant to the user’s niche takes 200ms.

**Price:** \~$0

## Event Tracking

### PostHog

I use PostHog for the session recording. Super simple to use, does a great job and easy to integrate.

**Price:** $0\.

## Logging

### Datadog

I have tons of experience with Datadog, it’s virtually free at this stage for me and I have boilerplate code for everything I need for it.

**Price**: \~$0\.

## Other services

### 1\. Email providers

#### Kit

I use Kit to send promotional emails and sequences to new users

#### Resend

Resend is free to use when you begin to send transactional emails.

#### Improvmx

To reroute all emails that go to \*@writestack.io to my personal email.

**Price:** \~$25/month

### 2\. Affiliates

#### 1\. Getrewardful

I use Getrewardful to manage the affiliates.

**Price:** $49/month

#### 2\. Affiliates commissions

The amount of commission I pay my affiliates

**Price:** \~$40/month

### 3\. OpenRouter

In order to be able to use different models for notes generation, I use OpenRouter, which lets me change model easily.

**Total price(credits\+fee):** \~$25/month

#### Bonus: models I use

1. Claude 3\.7 for text generation
2. DeepSeek R1 for newsletter analysis

---

## Summary

💸 Monthly expenses: \~$291  
💰 Stripe fees \+ setup: $1,450  
📅 First\-year stack cost: **$4,942**

[![](https://substackcdn.com/image/fetch/$s_!z6hq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb290fa4a-fd3b-491b-90d0-167aa67c672f_1745x1120.png)](https://substackcdn.com/image/fetch/$s_!z6hq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb290fa4a-fd3b-491b-90d0-167aa67c672f_1745x1120.png)

## Final Thought

Now, although my stack is not lean at this stage, and I have plenty of services I used and pay for, it didn’t started out this way:

I started with a simple NextJS\+Vercel, MongoDB(free) and RDS (AWS DB).

I slowly added more and more technologies to accommodate for the changes and the users’ growth.

When you start your new product, go lean. Build a small MVP.

Let people try it and collect as much feedback as you can, so you can pivot to the winning idea.

---

*P.S.*

*If you are a busy creator who doesn’t have enough time to leverage Notes, WriteStack is the **exact** product for you.*

*And you can try it, for free. Sign up and get a a 7\-day free trial.*

[Try WriteStack for Free](https://www.writestack.io/?free=7)

---