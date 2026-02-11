# How to build new products

*Technical details on PinkyPartner*

Published: 2024-07-18
Source: https://theindiepreneur.substack.com/p/how-to-build-new-products

---

*👋 Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as a solopreneur who quit his job to chase his dreams.*

*I am a software developer, and so far I have x3 failed projects, and x2 ongoing.*

*I also publish [Tech Books](https://open.substack.com/pub/techbooks) summaries along with [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions).*

It’s been exactly 30 days since I published PinkyPartner on Product Hunt.

And since it was the first solo project I intended to complete no matter what, I learned a lot from it.

Join hundreds of subscribers to read a weekly article about the solopreneur’s life

Subscribe

Today’s article will be more tech\-oriented. I will share the technologies I used, challenges, timelines and what I would have done differently starting over.

# The tech stack

### Frontend

#### React, TS

React is the most popular framework and the one I used in the last 6\+ years. The interesting choice here is to go for TypeScript.

Although JavaScript may be a bit faster to develop with in the short run, it can be hell to maintain its code, unless written well with documentation and prop types.

But then why not use TS? The learning curve is gentle, assuming you have experience with JS.

#### TailwindCSS

After you write several components with Tailwind you usually get hooked. It makes your project file structure so much cleaner and makes you write CSS so much faster.

#### NextJS, Vercel

NextJS takes care of so much boilerplate code and allows you to write both your frontend and your backend in the same project.

I use Vercel to deploy and host my applications.  
Their developer experience is fantastic and, unless your app is pretty popular, you can expect to pay nothing for their services.

### Backend

#### Node.js, TS

When using Next.js, Node.js is typically the default environment on the server side.

### Specific libraries

#### [Shadcn](https://ui.shadcn.com/)

They have all the components I ever needed, highly customizable.

#### **[@ducanh2912/next\-pwa](https://www.npmjs.com/package/@ducanh2912/next-pwa)**

I use this library to have all the configurations ready for a mobile app for the Play/App Store. Then I use [pwabuilder](https://www.pwabuilder.com/) to do the rest of the magic.

#### [Datadog](https://www.datadoghq.com/)

For logs. It can be a bit complicated at first, but I had experience working with it in 2 companies I worked for, so for me, it was the natural choice.

#### [PostHog](https://posthog.com/)

Even tracker and sessions recorder. Hands down, this is the easiest library to set up and it gives you the most value out of the box. They also have a substack @ [PostHog](https://open.substack.com/users/69984721-posthog?utm_source=mentions).

# Challenges

### Notifications

I thought that setting up notifications would be the easiest part and that it should not take more than a day.

Well, it took more like a week. And then some more time to fix duplicated notifications.

If you ever get stuck with adding notifications to your PWA or you are interested in the solution, send me a message and I’ll share with you snippets and guidance.

### Apple

Not only is it a huge pain to set up practically anything related to Apple (Authentication, upload to app store), but they seem to not like PWA at all.

[![](https://substackcdn.com/image/fetch/$s_!ZOUS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2e015f2-1b38-4c62-858f-284d7cc28406_1210x320.png)](https://substackcdn.com/image/fetch/$s_!ZOUS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2e015f2-1b38-4c62-858f-284d7cc28406_1210x320.png)

I mean, a PWA is built upon and uses a browser to run. How can you make it sufficiently different? ¯\\\_(ツ)\_/¯

### Design

This is a mistake that I am not going to repeat.

When I started coding PinkyPartner, I had no design on Figma or in mind and I just winged it.   
It cost me hours of redesigning, consulting and adjusting it to both desktop and mobile.

It might take a few hours to learn Figma, but every frontend developer knows that having a design ready is so much easier and faster than writing something out of your head.

### Features

I spent over a week developing features that would probably never see the light of day, or be refactored completely.

Why? Because I didn’t have a written plan, nor did I have a deadline.

Once I figured out what a waste of time, I immediately wrote:

1. A deadline
2. What’s the minimum core feature
3. Launch plan
4. Nice to haves

And I executed in that order.

So after developing for 3\+ weeks, I set another 2 weeks for the deadline and I managed to get much more than I did in the previous 3 weeks.

# Things to do differently

### Better landing page

This was the first landing page I used:

[![](https://substackcdn.com/image/fetch/$s_!VUHi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F585366cc-d651-4f44-ad51-a26f7df06ca8_1861x860.png)](https://substackcdn.com/image/fetch/$s_!VUHi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F585366cc-d651-4f44-ad51-a26f7df06ca8_1861x860.png)

First landing page of PinkyPartner

This is the current one:

[![](https://substackcdn.com/image/fetch/$s_!xZAN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F408b0176-b32f-4b88-832b-a907a87b430c_1916x929.png)](https://substackcdn.com/image/fetch/$s_!xZAN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F408b0176-b32f-4b88-832b-a907a87b430c_1916x929.png)

Current landing page of PinkyPartner

The first one doesn’t give a lot of information about the product.

The second one explains exactly what’s the purpose of the app and even let’s you play with a small demo.

Make sure that your landing page is engaging and gives as many details as early as possible, so the user knows exactly what it is and whether they want it or not.

Otherwise they’ll leave as fast as they came.

To summarise, have a concise, informative and interactive (if needed) landing page.

### Better color scheme

I tried different color schemes.

[![](https://substackcdn.com/image/fetch/$s_!Z9r5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfd37954-cb34-4968-8741-5fd221b192b3_701x406.png)](https://substackcdn.com/image/fetch/$s_!Z9r5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfd37954-cb34-4968-8741-5fd221b192b3_701x406.png)

None of them converted as good as the final one:

[![](https://substackcdn.com/image/fetch/$s_!As0T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F678186ec-8177-4254-80f4-c72d9484e134_367x660.png)](https://substackcdn.com/image/fetch/$s_!As0T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F678186ec-8177-4254-80f4-c72d9484e134_367x660.png)

According to color psychology, green represents calm, health, growth and joy. The exact combination I need for such a product.

The black background sends a message of intensity and sophistication, while the dark blue/gray one is more comfortable and less aggressive.

# Final words

Everyone has a different set of skills and will encounter different challenges along the way.

Make sure that whatever challenges you have, you learn from them and share them so you don’t forget for next time and you help other people avoid or overcome the same challenges.

# What I enjoyed reading this week

[How to Get Wealthy (Without Any Hacks)](https://timdenning.substack.com/p/how-to-get-wealthy-without-any-hacks) by [Tim Denning](https://open.substack.com/users/33842544-tim-denning?utm_source=mentions) \- I recently came across Tim’s newsletter, and it’s fantastic. And in this article specifically, he talks about a few struggles most of us have and how to handle them.

[Another way to make money online](https://1personbusiness.substack.com/p/another-way-to-make-money-online) by [Maya Sayvanova](https://open.substack.com/users/3104492-maya-sayvanova?utm_source=mentions) \- Another article for those of us who struggle to choose what to do and take immediate action.

[How to Create Consistently Despite a Hectic Life](https://theunstoppablecreator.substack.com/p/how-to-create-consistently-despite) by [Alberto Cabas Vidani](https://open.substack.com/users/11413123-alberto-cabas-vidani?utm_source=mentions) \- It’s so hard to stay consistent with anything. I experience it personally on a daily basis. Alberto shares his take on it and helps people like me improve.

Join hundreds of subscribers to get a weekly article about the solopreneur’s life

Subscribe