# How I built a product in less than 3 days

*And how you can do it MUCH faster*

Published: 2024-11-13
Source: https://theindiepreneur.substack.com/p/how-i-built-a-product-in-less-than

---

*👋 Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as a solopreneur who quit his 6 figures job to chase his dreams.*

*I develop crazy fast at a very high level. [PM me](https://substack.com/@orelzilberman) if you want me to build your next 6 figures SaaS business (0\-100\).*

I spent last week writing code, developing a product to help developers start new products and verify them in minutes.

And in today’s article I am going to tell you how I managed to write a prototype of the core feature and a beautifully designed landing page in less than 3 days.

> Full disclosure:
> 
> I took me over 7 days to publish it. The first 3 days were spent building everything, the other 4 spent overthinking it and adding unnecessary things.
> 
> In the end of the article I’ll tell you if it was worth it.

---

## TL;DR

I built a new product that will help you, as a developer, publish your product idea in a few minutes, rather than a few days or weeks.

The product is called Build Quick.

[Deploy in minutes NOW](https://www.buildquick.app)

I built it extremely fast, thanks to the help of v0\.dev, helping me generate landing pages for you to choose out of and design BuildQuick.

Also, much of the repository is code that’s repeated over and over in many of my projects. So, using AI (GitHub Copilot and GPT o1\-preview, I perfected it along with comments).

---

## Core feature

The main idea of the product is to give users a beautifully designed landing page, based on a template they choose, an idea name and a description.

Here’s the flow:

> Choose a template → Write a name → Write description → Get the landing page.

In order to achieve that, I converted the selected template file (template.tsx) into a string, compressed it by removing spaces and new lines.

Then, I worked a few hours on a good prompt to use with ChatGPT.

The prompt is focused on updating the template with the new information and add all libraries required for installation.

---

#### How did I create many templates fast?

I have over 11 beautifully design templates you can choose from in the website.

And creating them was way easier than you can imagine.

1. Ask ChatGPT for 10 ideas for SaaS products, along with a styling guide.
2. Ask v0\.dev to generate those templates, using your favorite libraries.
3. Adjust it according to your requirements

It took me less than 2 hours to write 11 landing pages and use them as templates.

---

## Get a full project repository

Now, for those who need more than a landing page and also want a full repository to deploy in a few minutes, you’re covered.

The results of the previous stage will be attached to a GitHub repository, which includes everything from authentication through db integration to PayPal subscriptions and mail sending.

And as a developer, it’s going to take you minutes to deploy.

How?

1. Add relevant keys to .env
2. Add the new repository to your GitHub
3. Deploy via Vercel

As simple as that.

---

#### How did I manage to write this fast?

After writing many products, I realized that most of it is repeated code that can be put into a template.

Using GitHub Copilot to help me write 80% of my code, I moved all the repeated code into a repository, along with comments.

From here, the process to send you your repository is simple:

According to your description, the product will build a landing page for you and add it as the src/page.tsx file.

---

[Deploy in minutes NOW](https://www.buildquick.app)

## Technologies I used to write the product

The tech stack I used is the only one I use over and over.

* React (TS)
* NextJS
* TailwindCSS, Shadcn
* Prisma
* MailGun
* PayPal
* MongoDB/Supabase

> This template is extremely useful for those who do not live in a country that’s accepted by Stripe.

## Final words

Two weeks ago I decided to improve my focus, by choosing one thing per week.

Focusing on one thing **only** every week has boosted my productivity and motivation 10 folds.

Every week I am excited to focus on something new and I feel like I am completing projects and not leaving them half\-assed to a future point in time in which I’ll attend to fix the bugs.

Plus, it forces me to be creative and write MVPs that would work by the end of the week.

I’ll write more about it in future articles.

### P.S.

It was worth it spending extra 4 days. I managed to make the little things, that make a huge difference, be better.

For next time though I will create a plan instead of just changing things randomly.

## Articles I enjoyed reading

1. [Diminishing Returns \- Mental Model](https://read.perspectiveship.com/p/diminishing-returns) by [Michał Poczwardowski](https://open.substack.com/users/141222242-micha-poczwardowski?utm_source=mentions) \- Sometimes trying to push too hard will not get you to the results you’re looking for. This is when knowing the diminishing returns mental model can help.
2. [I ran a 42\-day audience growth experiment on Notes. Here's what I did, and everything I learned](https://thedavidmcilroy.substack.com/p/i-ran-a-42-day-audience-growth-experiment) by [David McIlroy](https://open.substack.com/users/151696008-david-mcilroy?utm_source=mentions) \- David tried posting 6 times a day for 42 days. He wrote about the results in the article above.
3. [The $1,000 cold email alternative that's breaking B2B sales 💸](https://www.marketingideas.com/p/the-1000-cold-email-alternative-thats) by [Tom Orbach](https://open.substack.com/users/11987234-tom-orbach?utm_source=mentions) \- I can’t have enough of Tom’s articles. If you’re not subscribed yet, well, your loss.