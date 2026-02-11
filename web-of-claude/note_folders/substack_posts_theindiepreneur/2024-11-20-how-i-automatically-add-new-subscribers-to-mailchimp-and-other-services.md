# How I automatically add new subscribers to MailChimp and other services

*A new product walkthrough*

Published: 2024-11-20
Source: https://theindiepreneur.substack.com/p/how-i-automatically-add-new-subscribers

---

*👋 Hey, it’s [Orel](https://www.linkedin.com/in/orel-zilberman-225a37137/) here! Welcome to my weekly newsletter where I share my journey and lessons as a solopreneur who quit his 6 figures job to chase his dreams.*

*I develop crazy fast at a very high level. [PM me](https://substack.com/@orelzilberman) if you want me to build your next 6 figures SaaS business.*

I started writing this newsletter back in February, to share my journey as a full\-time solopreneur.

It’s been over 450 days, and I feel like I barely made any progress.

After reading Russell brunson’s book, Dotcom Secrets, I realized I need to step up my game and start communicating on a more personal level.

Via emails.

After digging around for quite a while I couldn’t find any product that will let me add new Substack subscribers to a list.

That’s when I decided to take matters into my own hands.

## The beginning

First, before you start thinking about developing a product that does not exist, make sure that you can actually do it.

So before writing any “real” code, I, along with a friend, sat in Discord for half a day, trying to figure out how can we make it work.

And there were many questions.

* Does Gmail’s API allow me, as a developer, to read only specific emails?
* Do all services work like MailChimp and allow you to take actions on the user’s behalf?
* If not, how can we handle that?
* People fear for their privacy. How can we make sure we address it?
* Can we implement the core feature?

Fortunately, we found the answer to all of our questions.

Some were disappointing, but we found ways to work around them and get things moving.

## How does it work?

##### From the product perspective

The flow is pretty simple.

You will receive many mails from Substack. We only care about the “New subscriber” ones.

Once this type of mail is received, we read ONLY the email and the name of the new subscriber and add them to your list.

##### From the user perspective

Signup (Google) → Tell us which mail service you use → Give us authorization to act on your behalf → Tell us the list you want to add new subscribers to.

[Give EasySequence a go](https://easy-sequence.vercel.app/)

## Is it in production yet?

Yes!

But not fully functional yet.

A moment before we dive deep into implementation, we wanted to validate the idea.

We made sure this is doable, and the rest is on you.

If this is something you’re interested in and will need it, go ahead and sign up. Early users will be able to affect the roadmap of the product and which mail services will be integrated first.

## Are there any other features?

At the moment we are focusing on making the addition of new subscribers to mailing list as easy and seamless as possible.

We have plenty more ideas, like statistics, classification of different users to different lists and more automations.

Once we launch the core feature, we’ll build a roadmap and give you the opportunity to affect it.

## Okay, sounds good. How do we proceed?

Awesome!

Go ahead and sign up here:

[EasySequence](https://easy-sequence.vercel.app/)

And we’ll keep you updated on the progress.

**Keep in mind**: The more people sign up, the faster we will develop the product.

So if it’s something you’re interested in, sign up now :)