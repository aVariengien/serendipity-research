# Llama 3.2 and plugins for Django

*Plus things I’ve learned on the board of the Python Software Foundation*

Published: 2024-09-25
Source: https://simonw.substack.com/p/llama-32-and-plugins-for-django

---

In this newsletter:

* Llama 3\.2
* DJP: A plugin system for Django
* Notes on using LLMs for code
* Things I've learned serving on the board of the Python Software Foundation

Plus 22 links and 12 quotations and 1 TIL

**Link**: [Llama 3\.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)

In further evidence that AI labs are terrible at naming things, Llama 3\.2 is a *huge* upgrade to the Llama 3 series \- they've released their first multi\-modal vision models!

> Today, we’re releasing Llama 3\.2, which includes small and medium\-sized vision LLMs (11B and 90B), and lightweight, text\-only models (1B and 3B) that fit onto edge and mobile devices, including pre\-trained and instruction\-tuned versions.

The 1B and 3B text\-only models are exciting too, with a 128,000 token context length and optimized for edge devices (Qualcomm and MediaTek hardware get called out specifically).

Meta partnered directly with Ollama to help with distribution, [here's the Ollama blog post](https://ollama.com/blog/llama3.2). They only support the two smaller text\-only models at the moment \- this command will get the 3B model (2GB):

```
ollama run llama3.2 
```

And for the 1B model (a 1\.3GB download):

```
ollama run llama3.2:1b
```

I had to first upgrade my Ollama by clicking on the icon in my macOS task tray and selecting "Restart to update".

The two vision models are coming to Ollama "very soon".

Once you have fetched the Ollama model you can access it from my [LLM](https://llm.datasette.io/) command\-line tool like this:

```
pipx install llm
llm install llm-ollama
llm chat -m llama3.2:1b
```

I tried running my [djp codebase](https://github.com/simonw/djp) through that tiny 1B model just now and got [a surprisingly good result](https://gist.github.com/simonw/64c5f5b111fe473999144932bef4218b) \- by no means comprehensive, but way better than I would ever expect from a model of that size:

```
files-to-prompt **/*.py -c | llm -m llama3.2:1b --system 'describe this code'
```

Here's a portion of the output:

> The first section defines several test functions using the `@djp.hookimpl`decorator from the djp library. These hook implementations allow you to intercept and manipulate Django's behavior.
> 
> * `test_middleware_order`: This function checks that the middleware order is correct by comparing the `MIDDLEWARE` setting with a predefined list.
> * `test_middleware`: This function tests various aspects of middleware:
> 
> 
> 	+ It retrieves the response from the URL `/from-plugin/` using the `Client` object, which simulates a request to this view.
> 	+ It checks that certain values are present in the response:
> 	
> 	
> 		- `X-DJP-Middleware-After`
> 		- `X-DJP-Middleware`
> 		- `X-DJP-Middleware-Before` \[...]

I found the GGUF file that had been downloaded by Ollama in my `~/.ollama/models/blobs`directory. The following command let me run that model directly in LLM using the [llm\-gguf](https://github.com/simonw/llm-gguf)plugin:

```
llm install llm-gguf
llm gguf register-model ~/.ollama/models/blobs/sha256-74701a8c35f6c8d9a4b91f3f3497643001d63e0c7a84e085bed452548fa88d45 -a llama321b
llm chat -m llama321b
```

Meta themselves claim impressive performance against other existing models:

> Our evaluation suggests that the Llama 3\.2 vision models are competitive with leading foundation models, Claude 3 Haiku and GPT4o\-mini on image recognition and a range of visual understanding tasks. The 3B model outperforms the Gemma 2 2\.6B and Phi 3\.5\-mini models on tasks such as following instructions, summarization, prompt rewriting, and tool\-use, while the 1B is competitive with Gemma.

Here's the [Llama 3\.2 collection](https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf) on Hugging Face. You need to accept the new Llama 3\.2 Community License Agreement there in order to download those models.

You can try the four new models out via the [Chatbot Arena](https://lmarena.ai/) \- navigate to "Direct Chat" there and select them from the dropdown menu. You can upload images directly to the chat there to try out the vision features.

### **[DJP: A plugin system for Django](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/) \- 2024\-09\-25**

**[DJP](https://djp.readthedocs.io/)** is a new plugin mechanism for Django, built on top of [Pluggy](https://pluggy.readthedocs.io/). I announced the first version of DJP during my talk yesterday at DjangoCon US 2024, [How to design and implement extensible software with plugins](https://2024.djangocon.us/talks/how-to-design-and-implement-extensible-software-with-plugins/). I'll post a full write\-up of that talk once the video becomes available \- this post describes DJP and how to use what I've built so far.

* [Why plugins?](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#why-plugins-)
* [Setting up DJP](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#setting-up-djp)
* [django\-plugin\-django\-header](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#django-plugin-django-header)
* [django\-plugin\-blog](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#django-plugin-blog)
* [django\-plugin\-database\-url](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#django-plugin-database-url)
* [Writing a plugin](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#writing-a-plugin)
* [Writing tests for plugins](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#writing-tests-for-plugins)
* [Why call it DJP?](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#why-call-it-djp-)
* [What's next for DJP?](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/#what-s-next-for-djp-)

#### **Why plugins?**

Django already has a thriving ecosystem of third\-party apps and extensions. What can a plugin system add here?

If you've ever installed a Django extension \- such as [django\-debug\-toolbar](https://django-debug-toolbar.readthedocs.io/) or [django\-extensions](https://django-extensions.readthedocs.io/) \- you'll be familiar with the process. You `pip install` the package, then add it to your list of `INSTALLED_APPS` in `settings.py` \- and often configure other picees, like adding something to `MIDDLEWARE` or updating your `urls.py` with new URL patterns.

This isn't exactly a huge burden, but it's added friction. It's also the exact kind of thing plugin systems are designed to solve.

DJP addresses this. You configure DJP just once, and then any additional DJP\-enabled plugins you `pip install` can automatically register configure themselves within your Django project.

#### **Setting up DJP**

There are three steps to adding DJP to an existing Django project:

1. `pip install djp` \- or add it to your `requirements.txt` or similar.
2. Modify your `settings.py` to add these two lines:

```
# Can be at the start of the file:
import djp

# This MUST be the last line:
djp.settings(globals())
```

1. Modify your `urls.py` to contain the following:

```
import djp

urlpatterns = [
    # Your existing URL patterns
] + djp.urlpatterns()
```

That's everything. The `djp.settings(globals())` line is a little bit of magic \- it gives `djp` an opportunity to make any changes it likes to your configured settings.

You can see [what that does here](https://github.com/simonw/djp/blob/5dd9ba1ac8b9c6d29fc88936451ad0e2eaa7248c/djp/__init__.py#L74-L84). Short version: it adds `"djp"` and any other apps from plugins to `INSTALLED_APPS`, modifies `MIDDLEWARE` for any plugins that need to do that and gives plugins a chance to modify any other settings they need to.

One of my personal rules of plugin system design is that you should never ship a plugin hook (a customization point) without releasing at least one plugin that uses it. This validates the design and provides executable documentation in the form of working code.

I've released three plugins for DJP so far.

#### **django\-plugin\-django\-header**

**[django\-plugin\-django\-header](https://github.com/simonw/django-plugin-django-header)** is a very simple initial example. It registers a [Django middleware class](https://docs.djangoproject.com/en/5.1/topics/http/middleware/) that adds a `Django-Composition:` HTTP header to every response with the name of a random [Composition by Django Reinhardt](https://github.com/simonw/django-plugin-django-header/blob/6e6be545e756f43b35b737c120e3c5d85b27dfd3/django_plugin_django_header/middleware.py#L24-L151) (thanks,[Wikipedia](https://en.wikipedia.org/wiki/List_of_compositions_by_Django_Reinhardt)).

```
pip install django-plugin-django-header
```

Then try it out with `curl`:

```
curl -I http://localhost:8000/
```

You should get back something like this:

```
...
Django-Composition: Nuages
...

```

I'm running this on my blog right now! Try this command to see it in action:

```
curl -I https://simonwillison.net/
```

The plugin is very simple. Its [\_\_init\_\_.py](https://github.com/simonw/django-plugin-django-header/blob/main/django_plugin_django_header/__init__.py)registers middleware like this:

```
import djp

@djp.hookimpl
def middleware():
    return [
        "django_plugin_django_header.middleware.DjangoHeaderMiddleware"
    ]
```

That string references the middleware class [in this file](https://github.com/simonw/django-plugin-django-header/blob/main/django_plugin_django_header/middleware.py).

#### **django\-plugin\-blog**

**[django\-plugin\-blog](https://github.com/simonw/django-plugin-blog)** is a much bigger example. It implements a full blog system for your Django application, with bundled models and templates and views and a URL configuration.

You'll need to have configured auth and the Django admin already (those already there by default in the `django-admin startproject`template). Now install the plugin:

```
pip install django-plugin-blog
```

And run migrations to create the new database tables:

```
python manage.py migrate
```

That's all you need to do. Navigating to `/blog/`will present the index page of the blog, including a link to a working Atom feed.

You can add entries and tags through the Django admin (configured for you by the plugin) and those will show up on `/blog/`, get their own URLs at `/blog/2024/<slug>/` and be included in the Atom feed, the `/blog/archive/` list and the `/blog/2024/` year\-based index too.

The default design is very basic, but you can customize that by providing your own base template or providing custom templates for each of the pages. There are details on the templates [in the README](https://github.com/simonw/django-plugin-blog).

The blog implementation is directly adapted from my [Building a blog in Django](https://til.simonwillison.net/django/building-a-blog-in-django) TIL.

The primary goal of this plugin is to demonstrate what a plugin with views, templates, models and a URL configuration looks like. Here's the full [\_\_init\_\_.py for the plugin](https://github.com/simonw/django-plugin-blog/blob/main/django_plugin_blog/__init__.py):

```
from django.urls import path
from django.conf import settings
import djp

@djp.hookimpl
def installed_apps():
    return ["django_plugin_blog"]

@djp.hookimpl
def urlpatterns():
    from .views import index, entry, year, archive, tag, BlogFeed

    blog = getattr(settings, "DJANGO_PLUGIN_BLOG_URL_PREFIX", None) or "blog"
    return [
        path(f"{blog}/", index, name="django_plugin_blog_index"),
        path(f"{blog}/<int:year>/<slug:slug>/", entry, name="django_plugin_blog_entry"),
        path(f"{blog}/archive/", archive, name="django_plugin_blog_archive"),
        path(f"{blog}/<int:year>/", year, name="django_plugin_blog_year"),
        path(f"{blog}/tag/<slug:slug>/", tag, name="django_plugin_blog_tag"),
        path(f"{blog}/feed/", BlogFeed(), name="django_plugin_blog_feed"),
    ]
```

It still only needs to implement two hooks: one to add `django_plugin_blog` to the `INSTALLED_APPS` list and another to add the necessary URL patterns to the project.

The `from .views import ...` line is nested inside the `urlpatterns()` hook because I was hitting circular import issues with those imports at the top of the module.

#### **django\-plugin\-database\-url**

**[django\-plugin\-database\-url](https://github.com/simonw/django-plugin-database-url)** is the smallest of my example plugins. It exists mainly to exercise the `settings()` plugin hook, which allows plugins to further manipulate settings in any way they like.

Quoting [the README](https://github.com/simonw/django-plugin-database-url/blob/main/README.md):

> Once installed, any `DATABASE_URL`environment variable will be automatically used to configure your Django database setting, using [dj\-database\-url](https://github.com/jazzband/dj-database-url).

Here's the [full implementation](https://github.com/simonw/django-plugin-database-url/blob/main/django_plugin_database_url/__init__.py) of that plugin, most of which is copied straight from the [dj\-database\-url documentation](https://github.com/jazzband/dj-database-url/blob/master/README.rst#usage):

```
import djp
import dj_database_url

@djp.hookimpl
def settings(current_settings):
    current_settings["DATABASES"]["default"] = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
```

If DJP gains tration, I expect that a lot of plugins will look like this \- thin wrappers around existing libraries where the only added value is that they configure those libraries automatically once the plugin is installed.

#### **Writing a plugin**

A plugin is a Python package bundling a module that implements one or more of the [DJP plugin hooks](https://djp.readthedocs.io/en/latest/plugin_hooks.html).

As I've shown above, the Python code for plugins can be very short. The larger challenge is correctly packaging and distributing the plugin \- plugins are discovered using [Entry Points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) which are defined in a `pyproject.toml`file, and you need to get those exactly right for your plugin to be discovered.

DJP includes [documentation on creating a plugin](https://djp.readthedocs.io/en/latest/creating_a_plugin.html), but to make it as frictionless as possible I've released a new [django\-plugin cookiecutter template](https://github.com/simonw/django-plugin).

This means you can start a new plugin like this:

```
pip install cookiecutter
cookiecutter gh:simonw/django-plugin
```

Then answer the questions:

```
  [1/6] plugin_name (): django-plugin-example
  [2/6] description (): A simple example plugin
  [3/6] hyphenated (django-plugin-example):
  [4/6] underscored (django_plugin_example):
  [5/6] github_username (): simonw
  [6/6] author_name (): Simon Willison
```

And you'l get a `django-plugin-example` directory with a fully configured plugin ready to be published to PyPI.

The template includes a `.github/workflows`directory with actions that can run tests, and an action that publishes your plugin to PyPI any time you create a new release on GitHub.

I've used that pattern myself for hundreds of plugin projects for [Datasette](https://datasette.io/) and [LLM](https://llm.datasette.io/), so I'm confident this is an effective way to release plugins.

The workflows use PyPI's [Trusted Publishers](https://docs.pypi.org/trusted-publishers/)mechanism (see [my TIL](https://til.simonwillison.net/pypi/pypi-releases-from-github)), which means you don't need to worry about API keys or PyPI credentials \- configure the GitHub repo once using the PyPI UI and everything should just work.

#### **Writing tests for plugins**

Writing tests for plugins can be a little tricky, especially if they need to spin up a full Django environment in order to run the tests.

I previously published [a TIL about that](https://til.simonwillison.net/django/pytest-django), showing how to have tests with their own `tests/test_project` project that can be used by [pytest\-django](https://pytest-django.readthedocs.io/).

I've baked that pattern into the `simon/django-plugin` cookiecutter template as well, plus a single default test which checks that a hit to the `/` index page returns a 200 status code \- still a valuable default test since it confirms the plugin hasn't broken everything!

The tests [for django\-plugin\-django\-header](https://github.com/simonw/django-plugin-django-header/blob/main/tests/test_django_plugin_django_header.py) and [for django\-plugin\-blog](https://github.com/simonw/django-plugin-blog/blob/main/tests/test_django_plugin_blog.py) should provide a useful starting point for writing tests for your own plugins.

#### **Why call it DJP?**

Because [django\-plugins](https://pypi.org/project/django-plugins/) already existed on PyPI, and I like [my three letter acronyms](https://pypi.org/project/llm/) there!

#### **What's next for DJP?**

I presented this at DjangoCon US 2024 yesterday afternoon. Initial response seemed positive, and I'm going to be attending the conference sprints on Thursday morning to see if anyone wants to write their own plugin or help extend the system further.

Is this a good idea? I think so. Plugins have been transformative for both Datasette and LLM, and I think [Pluggy](https://pluggy.readthedocs.io/) provides a mature, well\-designed foundation for this kind of system.

I'm optimistic about plugins as a natural extension of Django's existing ecosystem. Let's see where this goes.

---

### **[Notes on using LLMs for code](https://simonwillison.net/2024/Sep/20/using-llms-for-code/) \- 2024\-09\-20**

I was recently the guest on TWIML \- the This Week in Machine Learning \& AI podcast. Our episode is titled [Supercharging Developer Productivity with ChatGPT and Claude with Simon Willison](https://twimlai.com/podcast/twimlai/supercharging-developer-productivity-with-chatgpt-and-claude/), and the focus of the conversation was the ways in which I use LLM tools in my day\-to\-day work as a software developer and product engineer.

Here's the [YouTube video](https://www.youtube.com/watch?v=CRpHNB87gRY) version of the episode:

I ran the transcript through MacWhisper and extracted some edited highligts below.

#### **Two different modes of LLM use**

At [19:53](https://www.youtube.com/watch?v=CRpHNB87gRY&t=1193):

> There are two different modes that I use LLMs for with programming.
> 
> The first is **exploratory mode**, which is mainly quick prototyping \- sometimes in programming languages I don't even know.
> 
> I love asking these things to give me options. I will often start a prompting session by saying, "I want to draw a visualization of an audio wave. What are my options for this?"
> 
> And have it just spit out five different things. Then I'll say "Do me a quick prototype of option three that illustrates how that would work."
> 
> The other side is when I'm writing **production code**, code that I intend to ship, then it's much more like I'm treating it basically as an intern who's faster at typing than I am.
> 
> That's when I'll say things like, "Write me a function that takes this and this and returns exactly that."
> 
> I'll often iterate on these a lot. I'll say, "I don't like the variable names you used there. Change those." Or "Refactor that to remove the duplication."
> 
> I call it my weird intern, because it really does feel like you've got this intern who is screamingly fast, and they've read all of the documentation for everything, and they're massively overconfident, and they make mistakes and they don't realize them.
> 
> But crucially, they never get tired, and they never get upset. So you can basically just keep on pushing them and say, "No, do it again. Do it differently. Change that. Change that."
> 
> At three in the morning, I can be like, "Hey, write me 100 lines of code that does X, Y, and Z," and it'll do it. It won't complain about it.
> 
> It's weird having this small army of super talented interns that never complain about anything, but that's kind of how this stuff ends up working.

Here are all of my other notes about [AI\-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/).

#### **Prototyping**

At [25:22](https://www.youtube.com/watch?v=CRpHNB87gRY&t=1522s):

> My entire career has always been about prototyping.
> 
> Django itself, the web framework, we built that in a local newspaper so that we could ship features that supported news stories faster. How can we make it so we can turn around a production\-grade web application in a few days?
> 
> Ever since then, I've always been interested in finding new technologies that let me build things quicker, and my development process has always been to start with a prototype.
> 
> You have an idea, you build a prototype that illustrates the idea, you can then have a better conversation about it. If you go to a meeting with five people, and you've got a working prototype, the conversation will be so much more informed than if you go in with an idea and a whiteboard sketch.
> 
> I've always been a prototyper, but I feel like the speed at which I can prototype things in the past 12 months has gone up by an order of magnitude.
> 
> I was already a very productive prototype producer. Now, I can tap a thing into my phone, and 30 seconds later, I've got a user interface in Claude Artifacts that illustrates the idea that I'm trying to explore.
> 
> Honestly, if I didn't use these models for anything else, if I just used them for prototyping, they would still have an enormous impact on the work that I do.

Here are [examples of prototypes](https://simonwillison.net/tags/claude-artifacts/) I've built using Claude Artifacts. A lot of them end up in my [tools collection](https://tools.simonwillison.net/).

The full conversation covers a bunch of other topics. I ran the transcript through Claude, told it "Give me a bullet point list of the most interesting topics covered in this transcript" and then deleted the ones that I didn't think were particularly interesting \- here's what was left:

* Using AI\-powered voice interfaces like ChatGPT's Voice Mode to code while walking a dog
* Leveraging AI tools like Claude and ChatGPT for rapid prototyping and development
* Using AI to analyze and extract data from images, including complex documents like campaign finance reports
* The challenges of using AI for tasks that may trigger safety filters, particularly for journalism
* The evolution of local AI models like Llama and their improving capabilities
* The potential of AI for data extraction from complex sources like scanned tables in PDFs
* Strategies for staying up\-to\-date with rapidly evolving AI technologies
* The development of vision\-language models and their applications
* The balance between hosted AI services and running models locally
* The importance of examples in prompting for better AI performance

---

### **[Things I've learned serving on the board of the Python Software Foundation](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/) \- 2024\-09\-18**

Two years ago [I was elected](https://simonwillison.net/2022/Jul/30/psf-board/) to the board of directors for the [Python Software Foundation](https://www.python.org/psf-landing/) \- the PSF. I recently returned from the annual PSF board retreat (this one was in Lisbon, Portugal) and this feels like a good opportunity to write up some of the things I've learned along the way.

* [What is the PSF?](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#what-is-the-psf)
* [The PSF employs staff](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#the-psf-employs-staff)
* [A lot of this is about money](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#a-lot-of-this-is-about-money)
* [The PSF does not directly develop Python itself](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#the-psf-does-not-directly-develop-python-itself)
* [PyPI \- the Python Package Index](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#pypi-the-python-package-index)
* [PyCon is a key commitment](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#pycon-is-a-key-commitment)
* [Other PSF activities](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#other-psf-activities)
* [Work Groups](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#work-groups)
* [Acting as a fiscal sponsor](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#acting-as-a-fiscal-sponsor)
* [Life as a board member](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#life-as-a-board-member)
* [The kinds of things the board talks about](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#the-kinds-of-things-the-board-talks-about)
* [Want to know more?](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#want-to-know-more-)

#### **What is the PSF?**

The PSF is a [US 501(c)(3\)](https://en.wikipedia.org/wiki/501(c)(3)_organization) non\-profit organization with the following [mission](https://www.python.org/psf/mission/):

> The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.

That mission definition is *really important*. Board members and paid staff come and go, but the mission remains constant \- it's the single most critical resource to help make decisions about whether the PSF should be investing time, money and effort into an activity or not.

The board's 501(c)(3\) status is predicated on following the [full expanded mission statement](https://www.python.org/psf/mission/). When our finances get audited (we conduct an annual "friendly audit", which is considered best practice for organizations at our size), the auditors need to be able to confirm that we've been supporting that mission through our management of the tax\-exempt funds that have been entrusted to us.

This auditability is an interesting aspect of how 501(c)(3\) organizations work, because it means you can donate funds to them and know that the IRS will ostensibly be ensuring that the money is spent in a way that supports their stated mission.

Board members have fiduciary responsibility for the PSF. A good explanation of this can be found [here on BoardSource](https://boardsource.org/resources/fiduciary-responsibilities/), which also has other useful resources for understanding [the roles and responsibilities](https://boardsource.org/fundamental-topics-of-nonprofit-board-service/roles-responsibilities/) of non\-profit board members.

(Developing at least a loose intuition for US tax law around non\-profits is one of the many surprising things that are necessary to be an effective board member.)

#### **The PSF employs staff**

The PSF currently employs [12 full\-time staff members](https://www.python.org/psf/records/staff/). Members of the board do not directly manage the activities of the staff \- in fact board members telling staff what to do is highly inappropriate.

Instead, the board is responsible for hiring an Executive Director \- currently Deb Nicholson \- who is then responsible for hiring and managing (directly on indirectly) those other staff members. The board is responsible for evaluating the Executive Director's performance.

I joined the board shortly after Deb was hired, so I have not personally been part of a board hiring committee for a new Executive Director.

While paid staff support and enact many of the activities of the PSF, the foundation is fundamentally a volunteer\-based organization. Many PSF activities are carried out by [these volunteers](https://www.python.org/psf/volunteer/), in particular via [Work Groups](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#work-groups).

#### **A lot of this is about money**

A grossly simplified way to think about the PSF is that it's a bucket of money that is raised from [sponsors](https://www.python.org/psf/sponsors/) and the Python community (via donations and membership fees), and then spent to support the community and the language in different ways.

The PSF spends money on staff, on grants to Python\-related causes and on infrastructure and activities that support Python development and the Python community itself.

You can see how that money has been spent in the [2023 Annual Impact Report](https://www.python.org/psf/annual-report/2023/). The PSF had $4,356,000 revenue for that year and spent $4,508,000 \- running a small loss, but not a concerning one given our assets from previous years.

The most significant categories of expenditure in 2023 were PyCon US ($1,800,000\), our Grants program ($677,000\), Infrastructure (including PyPI) ($286,000\) and our Fiscal Sponsorees ($204,000\) \- I'll describe these in more detail below.

#### **The PSF does not directly develop Python itself**

This is an important detail to understand. The PSF is responsible for protecting and supporting the Python language and community, but development of [CPython](https://github.com/python/cpython) itself is not directly managed by the PSF.

Python development is handled by the [Python core team](https://devguide.python.org/core-developers/developer-log/), who are governed by the 5\-person [Python Steering Council](https://github.com/python/steering-council/blob/main/README.md). The Steering Council is elected by the core team. The process for becoming a core developer [is described here](https://devguide.python.org/core-developers/become-core-developer/).

How this all works is defined by [PEP 13: Python Language Governance](https://peps.python.org/pep-0013/) (and several subsequent PEPs). This structure was created \- with much discussion \- after Guido van Rossum stepped down from his role as Python BDFL in 2018\.

The PSF's executive director maintains close ties with the steering council, meeting with them 2\-3 times a month. The PSF provides financial support for some Python core activities, such as infrastructure used for Python development and sponsoring travel to and logistics for core Python sprints.

More recently, the PSF has started employing Developers in Residence to directly support the work of both the core Python team and initiatives such as the Python Package Index.

#### **PyPI \- the Python Package Index**

One of the most consequential projects directly managed by the PSF is [PyPI](https://pypi.org/), the Python Package Index. This is the system that enables `pip install name-of-package` to do its thing.

Having PyPI managed by a non\-profit that answers directly to the community it serves is a very good thing.

PyPI's numbers are staggering. Today there are 570,000 projects consisting of 12,035,133 files, serving 1\.9 billion downloads a day (that number from [PyPI Stats](https://pypistats.org/packages/__all__)). Bandwidth for these downloads is donated by [Fastly](https://www.fastly.com/), a PSF Visionary Sponsor who recently signed [a five year agreement](https://fosstodon.org/@ThePSF/112456715341751673) to continue this service.

(This was a big deal \- prior to that agreement there was concern over what would happen if Fastly ever decided to end that sponsorship.)

#### **PyCon is a key commitment**

The annual US Python Conference \- [PyCon US](https://us.pycon.org/) \- is a big part of the PSF's annual activities and operations. With over 3,000 attendees each year (and a $1\.8m budget for 2023\) running that conference represents a full\-time job for several PSF staff members.

In the past PyCon US has also been responsible for the majority of the PSF's operating income. This is no longer true today \- in fact it ran at a slight loss this year. This is not a big problem: the PSF's funding has diversified, and the importance of PyCon US to the Python community is such that the PSF is happy to lose money running the event if necessary.

#### **Other PSF activities**

Many of these are detailed in [the full mission statement](https://www.python.org/psf/mission/).

* Operating [python.org](https://www.python.org/) and making Python available to download. It's interesting to note that Python is distributed through many alternative routes that are not managed by the PSF \- through Linux packaging systems like Ubuntu, Debian and Red Hat, via tools like Docker or Homebrew, by companies such as [Anaconda](https://www.anaconda.com/download) or through newer channels such as [uv](https://docs.astral.sh/uv/guides/install-python/).
* Owning and protecting the Python trademarks and the Python intellectual property rights under the ([OSI compliant](https://opensource.org/license/python-2-0)) Python license. This is one of the fundamental reasons for the organization to exist, but thankfully is one of the smaller commitments in terms of cost and staff time.
* Running the annual PyCon US conference.
* Operating the Python Packaging Index. Fastly provide the CDN, but the PSF still takes on the task of developing and operating the core PyPI web application and the large amounts of moderation and user support that entails.
* Supporting infrastructure used for core Python development, and logistics for core Python sprints.
* Issuing grants to Python community efforts.
* Caring for fiscal sponsorees.
* Supporting the work of PSF Work Groups.

#### **Work Groups**

A number of PSF initiatives take place in the form of Work Groups, [listed here](https://www.python.org/psf/workgroups/). Work Groups are teams of volunteers from the community who collaborate on projects relevant to the PSF's mission.

Each Work Group sets its own cadence and ways of working. Some groups have decisions delegated to them by the board \- for example the Grants Work Group for reviewing grant proposals and the Code of Conduct Work Group for enforcing Code of Conduct activity. Others coordinate technical projects such as the [Infrastructure Working Group](https://wiki.python.org/psf/InfrastructureWG), who manage and make decisions on various pieces of technical infrastructure relevant to Python and the PSF.

Work Groups are formed by a board vote, with a designated charter. Most recently the board approved [a charter](https://github.com/psf/user-success-wg/blob/main/WG-charter.md) for a new User Success Work Group, focusing on things like improving the new Python user onboarding experience.

#### **Acting as a fiscal sponsor**

This is another term I was unfamiliar with before joining the board: the idea of a **fiscal sponsor**, which is a key role played by the PSF.

Running a non\-profit organization is decidedly not\-trivial: you need a legal structure, a bank account, accounting, governance, the ability to handle audits \- there's a whole lot of complexity behind the scenes.

Looking to run an annual community conference? You'll need a bank account, and an entity that can sign agreements with venues and vendors.

Want to accept donations to support work you are doing? Again, you need an entity, and a bank account, and some form of legal structure that ensures your donors can confidently trust you with their money.

Instead of forming a whole new non\-profit for this, you can instead find an existing non\-profit that is willing to be your "fiscal sponsor". They'll handle the accounting and various other legal aspects, which allows you to invest your efforts in the distinctive work that you are trying to do.

The PSF acts as a fiscal sponsor for a number of different organizations \- 20 as\-of the 2023 report \- including PyLadies, Twisted, Pallets, Jazzband, PyCascades and North Bay Python. The PSF's accounting team invest a great deal of effort in making all of this work.

The PSF generally takes a 10% cut of donations to its fiscal sponsorees. This doesn't actually cover the full staffing cost of servicing these organizations, but this all still makes financial sense in terms of the PSF's mission to support the global Python community.

#### **Life as a board member**

There are 12 board members. Elections are held every year after PyCon US, voted on by the PSF membership \- by both paid members and members who have earned voting rights through being acknowledged as PSF fellows.

Board members are elected for three year terms. Since 1\-3 new board members are likely to join annually, these terms ensure there is overlap which helps maintain institutional knowledge about how the board operates.

The board's activities are governed by [the PSF Bylaws](https://www.python.org/psf/bylaws/), and there is a documented process for modifying them (see ARTICLE XI).

We have board members from all over the world. This is extremely important, because the PSF is responsible for the health and growth of the global Python community. A perennial concern is how to ensure that board candidates are nominated from around the world, in order to maintain that critical global focus.

The board meets once a month over Zoom, has ongoing conversations via Slack and meets in\-person twice a year: once at PyCon US and once at a "retreat" in a different global city, selected to try and minimize the total amount of travel needed to get all of our global board members together in the same place.

Our most recent retreat was in Lisbon, Portugal. The retreat before that was in Malmö in Sweden.

I considered using an analogy that describes each board member as 1/12th of the "brain" of the PSF, but that doesn't hold up: the paid, full\-time staff of the PSF make an enormous number of decisions that impact how the PSF works.

Instead, the board acts to set strategy, represent the global community and help ensure that the PSF's activities are staying true to that mission. Like I said earlier, the mission definition really is *critical*. I admit that in the past I've been a bit cynical about the importance of mission statements: being a board member of a 501(c)(3\) non\-profit has entirely cured me of that skepticism!

Board members can also sit on board committees, of which there are currently four: the Executive Committee, Finance Committee, PyCon US Committee and Membership Committee. These mainly exist so that relevant decisions can be delegated to them, helping reduce the topics that must be considered by the full board in our monthly meetings.

#### **The kinds of things the board talks about**

Our Lisbon retreat involved two full 9\-hour days of discussion, plus social breakfasts, lunches and dinners. It was an *intense* workload.

I won't even attempt to do it justice here, but I'll use a couple of topics to illustrate the kind of things we think about on the board.

The first is our **grants strategy**. The PSF financially sponsors Python community events around the world. In the past this grants program has suffered from low visibility and, to simplify, we've felt that we weren't giving away enough money.

Over the past year we've fixed that: board outreach around the grants program and initiatives such as grants office hours have put our grants program in a much healthier position... but potentially *too* healthy.

We took steps to improve that visibily and streamline that process, and they worked! This gives us a new problem: we now have no shortage of applicants, so we need to figure out how to stick within a budget that won't harm the financial sustainability of the PSF itself.

Does this mean we say no to more events? Should we instead reduce the size of our grants? Can we take other initiatives, like more actively helping events find alternative forms of sponsorship?

Grants shouldn't just be about events \- but if we're making grants to other initiatives that support the Python community how can we fairly select those, manage the budget allocated to supporting them and maximize the value the Python community gets from the money managed by the PSF?

A much larger topic for the retreat was **strategic planning**. What should our goals be for the PSF that can't be achieved over a short period of time? Projects and initiatives that might require a one\-year, three\-year or five\-year margin of planning.

Director terms only last three years (though board members can and frequently do stand for re\-election), so having these long\-term goals planned and documented in detail is crucial.

A five\-year plan is not something that can be put together over two days of work, but the in\-person meeting is a fantastic opportunity to kick things off and ensure each board member gets to participate in shaping that process.

#### **Want to know more?**

The above is by no means a comprehensive manual to the PSF, but it's a good representation of the things I would have found most valuable to understand when I first got involved with the organization.

For a broader set of perspectives on how the board works and what it does, I recommend the [FAQs about the PSF Board](https://www.youtube.com/watch?v=kD6cPBfR4A4) video on YouTube.

If you're interested in helping the PSF achieve its mission, we would love to have you involved:

* Encourage your company to sponsor the PSF directly, or to sponsor Python events worldwide
* Volunteer at PyCon US or help with other suitable PSF initiatives
* Join a Work Group that's addressing problems you want to help solve
* Run your own event and [apply for a grant](https://www.python.org/psf/grants/)
* Join the PSF as a voting member and vote in our elections
* Run for the board elections yourself!

We're always interested in hearing from our community. We host public office hours on the PSF Discord every month, at different times of day to to cater for people in different timezones \- here's [the full calendar of upcoming office hours](https://pyfound.blogspot.com/2024/08/ask-questions-or-tell-us-what-you-think.html).

---

**Quote** 2024\-09\-13

> *Believe it or not, the name Strawberry does not come from the “How many r’s are in strawberry” meme. We just chose a random word. As far as we know it was a complete coincidence.*

[Noam Brown, OpenAI](https://twitter.com/polynoamial/status/1834312400419652079)

---

**Link** 2024\-09\-14 [Notes on running Go in the browser with WebAssembly](https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/):

Neat, concise tutorial by Eli Bendersky on compiling Go applications that can then be loaded into a browser using WebAssembly and integrated with JavaScript. Go functions can be exported to JavaScript like this:

```
js.Global().Set("calcHarmonic", jsCalcHarmonic)
```

And Go code can even access the DOM using a pattern like this:

```
doc := js.Global().Get("document")
inputElement := doc.Call("getElementById", "timeInput")
input := inputElement.Get("value")
```

Bundling the WASM Go runtime involves a 2\.5MB file load, but there’s also a TinyGo alternative which reduces that size to a fourth.

---

**Quote** 2024\-09\-14

> *It's a bit sad and confusing that LLMs ("Large Language Models") have little to do with language; It's just historical. They are highly general purpose technology for statistical modeling of token streams. A better name would be Autoregressive Transformers or something.  
>   
> They don't care if the tokens happen to represent little text chunks. It could just as well be little image patches, audio chunks, action choices, molecules, or whatever. If you can reduce your problem to that of modeling token streams (for any arbitrary vocabulary of some set of discrete tokens), you can "throw an LLM at it".*

[Andrej Karpathy](https://twitter.com/karpathy/status/1835024197506187617)

---

**Quote** 2024\-09\-15

> *\[… OpenAI’s o1] could work its way to a correct (and well\-written) solution ifprovided a lot of hints and prodding, but did not generate the key conceptual ideas on its own, and did make some non\-trivial mistakes. The experience seemed roughly on par with trying to advise a mediocre, but not completely incompetent, graduate student. However, this was an improvement over previous models, whose capability was closer to an actually incompetent graduate student.*

[Terrence Tao](https://mathstodon.xyz/@tao/113132503432772494)

---

**Link** 2024\-09\-15 [Speed matters](https://www.scattered-thoughts.net/writing/speed-matters/):

Jamie Brandon in 2021, talking about the importance of optimizing for the speed at which you can work as a developer:

> Being 10x faster also changes the kinds of projects that are worth doing.
> 
> Last year I spent something like 100 hours writing a text editor. \[…] If I was 10x slower it would have been 20\-50 weeks. Suddenly that doesn't seem like such a good deal any more \- what a waste of a year!

It’s not just about speed of writing code:

> When I think about speed I think about the whole process \- researching, planning, designing, arguing, coding, testing, debugging, documenting etc.
> 
> Often when I try to convince someone to get faster at one of those steps, they'll argue that the others are more important so it's not worthwhile trying to be faster. Eg choosing the right idea is more important than coding the wrong idea really quickly.
> 
> But that's totally conditional on the speed of everything else! If you could code 10x as fast then you could try out 10 different ideas in the time it would previously have taken to try out 1 idea. Or you could just try out 1 idea, but have 90% of your previous coding time available as extra idea time.

Jamie’s model here helps explain the effect I described in [AI\-enhanced development makes me more ambitious with my projects](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/). Prompting an LLM to write portions of my code for me gives me that 5\-10x boost in the time I spend typing code into a computer, which has a big effect on my ambitions despite being only about 10% of the activities I perform relevant to building software.

I also increasingly lean on LLMs as assistants in the research phase \- exploring library options, building experimental prototypes \- and for activities like writing tests and even a little bit [of documentation](https://simonwillison.net/2024/Sep/7/json-flatten/).

---

**Link** 2024\-09\-15 [How to succeed in MrBeast production (leaked PDF)](https://twitter.com/thepatwalls/status/1835041188099113179):

Whether or not you enjoy MrBeast’s format of YouTube videos (here’s [a 2022 Rolling Stone profile](https://www.rollingstone.com/culture/culture-features/mrbeast-youtube-cover-story-interview-1334604/) if you’re unfamiliar), this leaked onboarding document for new members of his production company is a compelling read.

It’s a snapshot of what it takes to run a massive scale viral YouTube operation in the 2020s, as well as a detailed description of a very specific company culture evolved to fulfill that mission.

It starts in the most on\-brand MrBeast way possible:

> I genuinely believe if you attently read and understand the knowledge here you will be much better set up for success. So, if you read this book and pass a quiz I’ll give you $1,000\.

Everything is focused very specifically on YouTube as a format:

> Your goal here is to make the best YOUTUBE videos possible. That’s the number one goal of this production company. It’s not to make the best produced videos. Not to make the funniest videos. Not to make the best looking videos. Not the highest quality videos.. It’s to make the best YOUTUBE videos possible.

The MrBeast definition of A, B and C\-team players is one I haven’t heard before:

> A\-Players are obsessive, learn from mistakes, coachable, intelligent, don’t make excuses, believe in Youtube, see the value of this company, and are the best in the goddamn world at their job. B\-Players are new people that need to be trained into A\-Players, and C\-Players are just average employees. \[…] They arn’t obsessive and learning. C\-Players are poisonous and should be transitioned to a different company IMMEDIATELY. (It’s okay we give everyone severance, they’ll be fine).

The key characteristic outlined here, if you read between the hustle\-culture lines, is learning. Employees who constantly learn are valued. Employees who don’t are not.

There’s a lot of stuff in there about YouTube virality, starting with the Click Thru Rate (CTR) for the all\-important video thumbnails:

> This is what dictates what we do for videos. “I Spent 50 Hours In My Front Yard” is lame and you wouldn’t click it. But you would hypothetically click “I Spent 50 Hours In Ketchup”. Both are relatively similar in time/effort but the ketchup one is easily 100x more viral. An image of someone sitting in ketchup in a bathtub is exponentially more interesting than someone sitting in their front yard.

The creative process for every video they produce starts with the title and thumbnail. These set the expectations for the viewer, and everything that follows needs to be defined with those in mind. If a viewer feels their expectations are not being matched, they’ll click away \- driving down the crucial Average View Duration that informs how much the video is promoted by YouTube’s all\-important mystical algorithms.

MrBeast videos have a strictly defined formula, outlined in detail on pages 6\-10\.

The first minute captures the viewer’s attention and demonstrates that their expectations from the thumbnail will be met. Losing 21 million viewers in the first minute after 60 million initial clicks is considered a reasonably good result! Minutes 1\-3, 3\-6 and 6\-end all have their own clearly defined responsibilities as well.

Ideally, a video will feature something they call the “wow factor”:

> An example of the “wow factor” would be our 100 days in the circle video. We offered someone $500,000 if they could live in a circle in a field for 100 days ([video](https://www.youtube.com/watch?v=gHzuabZUd6c)) and instead of starting with his house in the circle that he would live in, we bring it in on a crane 30 seconds into the video. Why? Because who the fuck else on Youtube can do that lol.

Chapter 2 (pages 10\-24\) is about creating content. This is crammed with insights into what it takes to produce surprising, spectacular and very expensive content for YouTube.

A lot of this is about coordination and intense management of your dependencies:

> I want you to look them in the eyes and tell them they are the bottleneck and take it a step further and explain why they are the bottleneck so you both are on the same page. “Tyler, you are my bottleneck. I have 45 days to make this video happen and I can not begin to work on it until I know what the contents of the video is. I need you to confirm you understand this is important and we need to set a date on when the creative will be done.” \[…] Every single day you must check in on Tyler and make sure he is still on track to hit the target date.

It also introduces the concept of “critical components”:

> Critical components are the things that are essential to your video. If I want to put 100 people on an island and give it away to one of them, then securing an island is a critical component. It doesn’t matter how well planned the challenges on the island are, how good the weather is, etc. Without that island there is no video.
> 
> \[…]
> 
> Critical Components can come from literally anywhere and once something you’re working on is labeled as such, you treat it like your baby. WITHOUT WHAT YOU’RE WORKING ON WE DO NOT HAVE A VIDEO! Protect it at all costs, check in on it 10x a day, obsess over it, make a backup, if it requires shipping pay someone to pick it up and drive it, don’t trust standard shipping, and speak up the second anything goes wrong. The literal second. Never coin flip a Critical Component (that means you’re coinfliping the video aka a million plus dollars)

There’s a bunch of stuff about communication, with a strong bias towards “higher forms of communication”: in\-person beats a phone call beats a text message beats an email.

Unsurprisingly for this organization, video is a highly valued tool for documenting work:

> Which is more important, that one person has a good mental grip of something or that their entire team of 10 people have a good mental grip on something? Obviously the team. And the easiest way to bring your team up to the same page is to freaken video everything and store it where they can constantly reference it. A lot of problems can be solved if we just video sets and ask for videos when ordering things.

I enjoyed this note:

> Since we are on the topic of communication, written communication also does not constitute communication unless they confirm they read it.

And this bit about the value of consultants:

> Consultants are literally cheat codes. Need to make the world's largest slice of cake? Start off by calling the person who made the previous world’s largest slice of cake lol. He’s already done countless tests and can save you weeks worth of work. \[…] In every single freakin task assigned to you, always always always ask yourself first if you can find a consultant to help you.

Here’s a darker note from the section “Random things you should know”:

> Do not leave consteatants waiting in the sun (ideally waiting in general) for more than 3 hours. Squid game it cost us $500,000 and boys vs girls it got a lot of people out. Ask James to know more

And to finish, this note on budgeting:

> I want money spent to be shown on camera ideally. If you’re spending over $10,000 on something and it won’t be shown on camera, seriously think about it.

I’m always interested in finding management advice from unexpected sources. For example, I love [The Eleven Laws of Showrunning](https://simonwillison.net/2019/Feb/19/eleven-laws-showrunning/) as a case study in managing and successfully delegating for a large, creative project.

I don’t think this MrBeast document has as many lessons directly relevant to my own work, but as an honest peek under the hood of a weirdly shaped and absurdly ambitious enterprise it’s legitimately fascinating.

---

**Link** 2024\-09\-15 [UV — I am (somewhat) sold](https://andrich.me/2024/09/uv-i-am-somewhat-sold/):

Oliver Andrich's detailed notes on adopting `uv`. Oliver has some pretty specific requirements:

> I need to have various Python versions installed locally to test my work and my personal projects. Ranging from Python 3\.8 to 3\.13\. \[...] I also require decent dependency management in my projects that goes beyond manually editing a `pyproject.toml` file. Likewise, I am way too accustomed to `poetry add ...`. And I run a number of Python\-based tools \-\-\- [djhtml](https://pypi.org/project/djhtml/), [poetry](https://pypi.org/project/poetry/), [ipython](https://pypi.org/project/ipython/), [llm](https://pypi.org/project/llm/), [mkdocs](https://pypi.org/project/mkdocs/), [pre\-commit](https://pypi.org/project/pre-commit/), [tox](https://pypi.org/project/tox/), ...

He's braver than I am!

> I started by removing all Python installations, pyenv, pipx and Homebrew from my machine. Rendering me unable to do my work.

Here's a neat trick: first install a specific Python version with `uv` like this:

```
uv python install 3.11
```

Then create an alias to run it like this:

```
alias python3.11 'uv run --python=3.11 python3'
```

And install standalone tools with optional extra dependencies like this (a replacement for `pipx`and `pipx inject`):

```
uv tool install --python=3.12 --with mkdocs-material mkdocs
```

Oliver also links to Anže Pečar's handy guide on using [UV with Django](https://blog.pecar.me/uv-with-django).

---

**Quote** 2024\-09\-16

> *o1 prompting is alien to me. Its thinking, gloriously effective at times, is also dreamlike and unamenable to advice.  
>   
> Just say what you want and pray. Any notes on “how” will be followed with the diligence of a brilliant intern on ketamine.*

[Riley Goodside](https://twitter.com/goodside/status/1834975429960011851)

---

**Quote** 2024\-09\-17

> *Do not fall into the trap of anthropomorphizing Larry Ellison. You need to think of Larry Ellison the way you think of a lawnmower. You don’t anthropomorphize your lawnmower, the lawnmower just mows the lawn \- you stick your hand in there and it’ll chop it off, the end. You don’t think "oh, the lawnmower hates me" – lawnmower doesn’t give a shit about you, lawnmower can’t hate you. Don’t anthropomorphize the lawnmower. Don’t fall into that trap about Oracle.*

[Bryan Cantrill](https://www.youtube.com/watch?v=-zRN7XLCRhc&t=2308s)

---

**Link** 2024\-09\-17 [Supercharging Developer Productivity with ChatGPT and Claude with Simon Willison](https://twimlai.com/podcast/twimlai/supercharging-developer-productivity-with-chatgpt-and-claude/):

I'm the guest for the latest episode of the [TWIML AI podcast](https://twimlai.com/) \- This Week in Machine Learning \& AI, hosted by Sam Charrington.

We mainly talked about how I use LLM tooling for my own work \- Claude, ChatGPT, Code Interpreter, Claude Artifacts, LLM and GitHub Copilot \- plus a bit about my experiments with local models.

---

**Link** 2024\-09\-17 [Serializing package requirements in marimo notebooks](https://marimo.io/blog/sandboxed-notebooks):

The [latest release](https://github.com/marimo-team/marimo/releases/tag/0.8.15) of [Marimo](https://marimo.io/) \- a reactive alternative to Jupyter notebooks \- has a very neat new feature enabled by its integration with [uv](https://docs.astral.sh/uv/):

> One of marimo’s goals is to make notebooks reproducible, down to the packages used in them. To that end, it’s now possible to create marimo notebooks that have their package requirements serialized into them as a top\-level comment.

This takes advantage of the [PEP 723](https://peps.python.org/pep-0723/) inline metadata mechanism, where a code comment at the top of a Python file can list package dependencies (and their versions).

I tried this out by installing `marimo` using `uv`:

```
uv tool install --python=3.12 marimo
```

Then grabbing one of [their example notebooks](https://github.com/marimo-team/spotlights):

```
wget 'https://raw.githubusercontent.com/marimo-team/spotlights/main/001-anywidget/tldraw_colorpicker.py'
```

And running it in a fresh dependency sandbox like this:

```
marimo run --sandbox tldraw_colorpicker.py
```

Also neat is that when editing a notebook using `marimo edit`:

```
marimo edit --sandbox notebook.py
```

Just importing a missing package is enough for Marimo to prompt to add that to the dependencies \- at which point it automatically adds that package to the comment at the top of the file:

[![In the Marimo editor, running import httpx opens a dialog that offers to install that using pip or another chosen package manager](https://substackcdn.com/image/fetch/$s_!ejZd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd28275fb-ff5d-40e5-9288-eeb052bf3ead_1410x1254.jpeg "In the Marimo editor, running import httpx opens a dialog that offers to install that using pip or another chosen package manager")](https://substackcdn.com/image/fetch/$s_!ejZd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd28275fb-ff5d-40e5-9288-eeb052bf3ead_1410x1254.jpeg)

---

**Quote** 2024\-09\-17

> *Something that I confirmed that other conference organisers are also experiencing is last\-minute ticket sales. This is something that happened with UX London this year. For most of the year, ticket sales were trickling along. Then in the last few weeks before the event we sold more tickets than we had sold in the six months previously. \[…]  
>   
> When I was in Ireland I had a chat with a friend of mine who works at the Everyman Theatre in Cork. They’re experiencing something similar. So maybe it’s not related to the tech industry specifically.*

[Jeremy Keith](https://adactio.com/journal/21421)

---

**Quote** 2024\-09\-17

> *In general, the claims about how long people are living mostly don’t stack up. I’ve tracked down 80% of the people aged over 110 in the world (the other 20% are from countries you can’t meaningfully analyse). Of those, almost none have a birth certificate. \[...]  
>   
> Regions where people most often reach 100\-110 years old are the ones where there’s the most pressure to commit pension fraud, and they also have the worst records.*

[Saul Justin Newman](https://theconversation.com/the-data-on-extreme-human-ageing-is-rotten-from-the-inside-out-ig-nobel-winner-saul-justin-newman-239023)

---

**Link** 2024\-09\-17 [Oracle, it’s time to free JavaScript.](https://javascript.tm/):

Oracle have held the trademark on JavaScript since their acquisition of Sun Microsystems in 2009\. They’ve continued to renew that trademark over the years despite having no major products that use the mark.

Their December 2019 renewal included [a screenshot of the Node.js homepage](https://tsdr.uspto.gov/documentviewer?caseId=sn75026640&docId=SPE20191227132243&linkId=2#docIndex=1&page=1) as a supporting specimen!

Now a group lead by a team that includes Ryan Dahl and Brendan Eich is coordinating a legal challenge to have the USPTO treat the trademark as abandoned and “recognize it as a generic name for the world’s most popular programming language, which has multiple implementations across the industry.”

---

**Quote** 2024\-09\-18

> *The problem that you face is that it's relatively easy to take a model and make it look like it's aligned. You ask GPT\-4, “how do I end all of humans?” And the model says, “I can't possibly help you with that”. But there are a million and one ways to take the exact same question \- pick your favorite \- and you can make the model still answer the question even though initially it would have refused. And the question this reminds me a lot of coming from adversarial machine learning. We have a very simple objective: Classify the image correctly according to the original label. And yet, despite the fact that it was essentially trivial to find all of the bugs in principle, the community had a very hard time coming up with actually effective defenses. We wrote like over 9,000 papers in ten years, and have made very very very limited progress on this one small problem. You all have a harder problem and maybe less time.*

[Nicholas Carlini](https://www.youtube.com/watch?v=umfeF0Dx-r4)

---

**Link** 2024\-09\-19 [The web's clipboard, and how it stores data of different types](https://alexharri.com/blog/clipboard):

Alex Harri's deep dive into the [Web clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API), the more recent alternative to the old `document.execCommand()` mechanism for accessing the clipboard.

There's a *lot* to understand here! Some of these APIs have a history dating back to Internet Explorer 4 in 1997, and there have been plenty of changes over the years to account for improved understanding of the security risks of allowing untrusted code to interact with the system clipboard.

Today, the most reliable data formats for interacting with the clipboard are the "standard" formats of `text/plain`, `text/html` and `image/png`.

Figma does a particularly clever trick where they share custom Figma binary data structures by encoding them as base64 in `data-metadata`and `data-buffer` attributes on a `<span>` element, then write the result to the clipboard as HTML. This enables copy\-and\-paste between the Figma web and native apps via the system clipboard.

---

**Link** 2024\-09\-19 [Moshi](https://github.com/kyutai-labs/moshi):

Moshi is "a speech\-text foundation model and full\-duplex spoken dialogue framework". It's effectively a text\-to\-text model \- like an LLM but you input audio directly to it and it replies with its own audio.

It's fun to play around with, but it's not particularly useful in comparison to other pure text models: I tried to talk to it about California Brown Pelicans and it gave me some very basic hallucinated thoughts about California Condors instead.

It's very easy to run locally, at least on a Mac (and likely on other systems too). I used `uv` and got the 8 bit quantized version running as a local web server using this one\-liner:

```
uv run --with moshi_mlx python -m moshi_mlx.local_web -q 8
```

That downloads \~8\.17G of model to a folder in `~/.cache/huggingface/hub/` \- or you can use `-q 4` and get a 4\.81G version instead (albeit even lower quality).

---

**Link** 2024\-09\-20 [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval):

Here's an interesting new embedding/RAG technique, described by Anthropic but it should work for any embedding model against any other LLM.

One of the big challenges in implementing semantic search against vector embeddings \- often used as part of a RAG system \- is creating "chunks" of documents that are most likely to semantically match queries from users.

Anthropic provide this solid example where semantic chunks might let you down:

> Imagine you had a collection of financial information (say, U.S. SEC filings) embedded in your knowledge base, and you received the following question: "What was the revenue growth for ACME Corp in Q2 2023?"
> 
> A relevant chunk might contain the text: "The company's revenue grew by 3% over the previous quarter." However, this chunk on its own doesn't specify which company it's referring to or the relevant time period, making it difficult to retrieve the right information or use the information effectively.

Their proposed solution is to take each chunk at indexing time and expand it using an LLM \- so the above sentence would become this instead:

> This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."

This chunk was created by Claude 3 Haiku (their least expensive model) using the following prompt template:

> `<document>`  
> `{{WHOLE_DOCUMENT}}`  
> `</document>`  
> `Here is the chunk we want to situate within the whole document`  
> `<chunk>`  
> `{{CHUNK_CONTENT}}`  
> `</chunk>`  
> `Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.`

Here's the really clever bit: running the above prompt for every chunk in a document could get really expensive thanks to the inclusion of the entire document in each prompt. Claude [added context caching](https://simonwillison.net/2024/Aug/14/prompt-caching-with-claude/) last month, which allows you to pay around 1/10th of the cost for tokens cached up to your specified beakpoint.

By Anthropic's calculations:

> Assuming 800 token chunks, 8k token documents, 50 token context instructions, and 100 tokens of context per chunk, the one\-time cost to generate contextualized chunks is $1\.02 per million document tokens.

Anthropic provide a [detailed notebook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/contextual-embeddings/guide.ipynb)demonstrating an implementation of this pattern. Their eventual solution combines cosine similarity and BM25 indexing, uses embeddings from [Voyage AI](https://docs.voyageai.com/docs/embeddings) and adds a reranking step powered by [Cohere](https://cohere.com/rerank).

The notebook also includes an evaluation set using JSONL \- here's that evaluation data [in Datasette Lite](https://lite.datasette.io/?json=https://github.com/anthropics/anthropic-cookbook/blob/main/skills/contextual-embeddings/data/evaluation_set.jsonl#/data/evaluation_set).

---

**Link** 2024\-09\-20 [YouTube Thumbnail Viewer](https://tools.simonwillison.net/youtube-thumbnails?url=CRpHNB87gRY):

I wanted to find the best quality thumbnail image for a YouTube video, so I could use it as a social media card. I know from past experience that GPT\-4 has memorized the various URL patterns for `img.youtube.com`, so I [asked it](https://chatgpt.com/share/66ecf1a3-928c-8006-81f3-8869faa57071) to guess the URL for my specific video.

This piqued my interest as to what the other patterns were, so I got it to spit those out too. Then, to save myself from needing to look those up again in the future, I asked it to build me a little HTML and JavaScript tool for turning a YouTube video URL into a set of visible thumbnails.

I [iterated on the code](https://github.com/simonw/tools/commits/main/youtube-thumbnails.html) a bit more after pasting it into Claude and ended up with this, now hosted in my [tools](https://tools.simonwillison.net/) collection.

---

**Link** 2024\-09\-21 [Markdown and Math Live Renderer](https://tools.simonwillison.net/markdown-math):

Another of my tiny Claude\-assisted JavaScript tools. This one lets you enter Markdown with embedded mathematical expressions (like `$ax^2 + bx + c = 0$`) and live renders those on the page, with an HTML version using MathML that you can export through copy and paste.

[![Screenshot of the tool in action - Markdown plus math at the top is rendered underneath.](https://substackcdn.com/image/fetch/$s_!8Mzz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F323705d4-7018-439e-8740-8010dcc1e57d_837x698.jpeg "Screenshot of the tool in action - Markdown plus math at the top is rendered underneath.")](https://substackcdn.com/image/fetch/$s_!8Mzz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F323705d4-7018-439e-8740-8010dcc1e57d_837x698.jpeg)

Here's the [Claude transcript](https://gist.github.com/simonw/a6c23ba1c95613d41b98f432f273dd85). I started by asking:

> Are there any client side JavaScript markdown libraries that can also handle inline math and render it?

Claude gave me several options including the combination of [Marked](https://marked.js.org/) and [KaTeX](https://katex.org/), so I followed up by asking:

> Build an artifact that demonstrates Marked plus KaTeX \- it should include a text area I can enter markdown in (repopulated with a good example) and live update the rendered version below. No react.

Which gave me [this artifact](https://claude.site/artifacts/66492f54-425d-4a37-9b71-01f42f004fdc), instantly demonstrating that what I wanted to do was possible.

I [iterated on it](https://github.com/simonw/tools/commit/ceff93492cc5c9a0be5607f4dba74ccecd5056c2) a tiny bit to get to the final version, mainly to add that HTML export and a Copy button. The final source code [is here](https://github.com/simonw/tools/blob/main/markdown-math.html).

---

**Quote** 2024\-09\-21

> *Whether you think coding with AI works today or not doesn’t really matter.   
>   
> But if you think functional AI helping to code will make humans dumber or isn’t real programming just consider that’s been the argument against every generation of programming tools going back to Fortran.*

[Steven Sinofsky](https://twitter.com/stevesi/status/1837467257863340179)

---

**TIL** 2024\-09\-21 [How streaming LLM APIs work](https://til.simonwillison.net/llms/streaming-llm-apis):

I decided to have a poke around and see if I could figure out how the HTTP streaming APIs from the various hosted LLM providers actually worked. Here are my notes so far. …

---

**Link** 2024\-09\-22 [How streaming LLM APIs work](https://til.simonwillison.net/llms/streaming-llm-apis):

New TIL. I used `curl` to explore the streaming APIs provided by OpenAI, Anthropic and Google Gemini and wrote up detailed notes on what I learned.

Also includes example code for [receiving streaming events in Python with HTTPX](https://til.simonwillison.net/llms/streaming-llm-apis#user-content-bonus-accessing-these-streams-using-httpx) and [receiving streaming events in client\-side JavaScript using fetch()](https://til.simonwillison.net/llms/streaming-llm-apis#user-content-bonus--2-processing-streaming-events-in-javascript-with-fetch).

---

**Link** 2024\-09\-22 [Jiter](https://github.com/pydantic/jiter/tree/main/crates/jiter-python):

One of the challenges in dealing with LLM streaming APIs is the need to parse partial JSON \- until the stream has ended you won't have a complete valid JSON object, but you may want to display components of that JSON as they become available.

I've solved this previously using the [ijson](https://pypi.org/project/ijson/)streaming JSON library, see [my previous TIL](https://til.simonwillison.net/json/ijson-stream).

Today I found out about Jiter, a new option from the team behind Pydantic. It's written in Rust and extracted from [pydantic\-core](https://github.com/pydantic/pydantic-core), so the Python wrapper for it can be installed using:

```
pip install jiter
```

You can feed it an incomplete JSON bytes object and use `partial_mode="on"` to parse the valid subset:

```
import jiter
partial_json = b'{"name": "John", "age": 30, "city": "New Yor'
jiter.from_json(partial_json, partial_mode="on")
# {'name': 'John', 'age': 30}
```

Or use `partial_mode="trailing-strings"` to include incomplete string fields too:

```
jiter.from_json(partial_json, partial_mode="trailing-strings")
# {'name': 'John', 'age': 30, 'city': 'New Yor'}
```

The [current README](https://github.com/pydantic/jiter/blob/ae5fc7d8548c90ad8762dfdf2ea6461776c2feb6/crates/jiter-python/README.md) was a little thin, so I submiitted [a PR](https://github.com/pydantic/jiter/pull/143) with some extra examples. I [got some help](https://gist.github.com/simonw/264d487db1a18f8585c2ca0c68e50d1e) from `files-to-prompt` and Claude 3\.5 Sonnet):

> `cd crates/jiter-python/ && files-to-prompt -c README.md tests | llm -m claude-3.5-sonnet --system 'write a new README with comprehensive documentation'`

---

**Quote** 2024\-09\-22

> *The problem I have with \[pipenv shell] is that the act of manipulating the shell environment is crappy and can never be good. What all these "X shell" things do is just an abomination we should not promote IMO.  
>   
> Tools should be written so that you do not need to reconfigure shells. That we normalized this over the last 10 years was a mistake and we are not forced to continue walking down that path :)*

[Armin Ronacher](https://twitter.com/mitsuhiko/status/1837540764538056925)

---

**Quote** 2024\-09\-23

> *SPAs incur complexity that simply doesn't exist with traditional server\-based websites: issues such as search engine optimization, browser history management, web analytics and first page load time all need to be addressed. Proper analysis and consideration of the trade\-offs is required to determine if that complexity is warranted for business or user experience reasons. Too often teams are skipping that trade\-off analysis, blindly accepting the complexity of **SPAs by default** even when business needs don't justify it. We still see some developers who aren't aware of an alternative approach because they've spent their entire career in a framework like React.*

[Thoughtworks, October 2022](https://www.thoughtworks.com/radar/techniques/spa-by-default)

---

**Link** 2024\-09\-23 [simonw/docs cookiecutter template](https://github.com/simonw/docs):

Over the last few years I’ve settled on the combination of [Sphinx](https://www.sphinx-doc.org/), the [Furo](https://github.com/pradyunsg/furo) theme and the [myst\-parser](https://myst-parser.readthedocs.io/en/latest/) extension (enabling Markdown in place of reStructuredText) as my documentation toolkit of choice, maintained in GitHub and hosted using [ReadTheDocs](https://about.readthedocs.com/).

My [LLM](https://llm.datasette.io/) and [shot\-scraper](https://shot-scraper.datasette.io/) projects are two examples of that stack in action.

Today I wanted to spin up a new documentation site so I finally took the time to construct a [cookiecutter](https://cookiecutter.readthedocs.io/) template for my preferred configuration. You can use it like this:

```
pipx install cookiecutter
cookiecutter gh:simonw/docs
```

Or with [uv](https://docs.astral.sh/uv/):

```
uv tool run cookiecutter gh:simonw/docs
```

Answer a few questions:

```
[1/3] project (): shot-scraper
[2/3] author (): Simon Willison
[3/3] docs_directory (docs): 
```

And it creates a `docs/` directory ready for you to start editing docs:

```
cd docs
pip install -r requirements.txt
make livehtml
```

---

**Link** 2024\-09\-24 [Things I've Learned Serving on the Board of The Perl Foundation](https://blogs.perl.org/users/makoto_nozaki/2024/09/things-ive-learned-serving-on-the-board-of-the-perl-foundation.html):

My [post about the PSF board](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/) inspired Perl Foundation secretary Makoto Nozaki to publish similar notes about how TPF (also known since 2019 as TPRF, for The Perl and Raku Foundation) operates.

Seeing this level of explanation about other open source foundations is fascinating. I’d love to see more of these.

Along those lines, I found the [2024 Financial Report](https://ziglang.org/news/2024-financials/) from the Zig foundation really interesting too.

---

**Link** 2024\-09\-24 [XKCD 1425 (Tasks) turns ten years old today](https://xkcd.com/1425/):

One of the all\-time great XKCDs. It's amazing that "check whether the photo is of a bird" has gone from PhD\-level to trivially easy to solve (with a [vision LLM](https://simonwillison.net/tags/vision-llms/), or [CLIP](https://simonwillison.net/tags/clip/), or [ResNet\+ImageNet](https://pytorch.org/hub/pytorch_vision_resnet/) among others).

[![XKCD comic. Cueball: When a user takes a photo, the app should check whether they're in a national park... Ponytail: Sure, easy GIS lookup gimme a few hours. Cueball: ...and check whether the photo is of a bird. Ponytail: I'll need a research team and five years. Caption: In CS, it can be hard to explain the difference between the easy and the virtually impossible.](https://substackcdn.com/image/fetch/$s_!AK2K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2985b3b1-abae-460c-a1e9-c583b5024ff9_533x895.png "XKCD comic. Cueball: When a user takes a photo, the app should check whether they're in a national park... Ponytail: Sure, easy GIS lookup gimme a few hours. Cueball: ...and check whether the photo is of a bird. Ponytail: I'll need a research team and five years. Caption: In CS, it can be hard to explain the difference between the easy and the virtually impossible.")](https://substackcdn.com/image/fetch/$s_!AK2K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2985b3b1-abae-460c-a1e9-c583b5024ff9_533x895.png)

The key idea still very much stands though. Understanding the difference between easy and hard challenges in software development continues to require an enormous depth of experience.

I'd argue that LLMs have made this even worse.

Understanding what kind of tasks LLMs can and cannot reliably solve remains incredibly difficult and unintuitive. They're computer systems that are terrible at maths and that can't reliably lookup facts!

On top of that, the rise of AI\-assisted programming tools means more people than ever are beginning to create their own custom software.

These brand new AI\-assisted proto\-programmers are having a crash course in this easy\-v.s.\-hard problem.

I saw someone recently complaining that they couldn't build a Claude Artifact that could analyze images, even though they knew Claude itself could do that. Understanding why that's not possible involves understanding how the [CSP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) that are used to serve Artifacts prevent the generated code from making its own API calls out to an LLM!

---

**Link** 2024\-09\-24 [nanodjango](https://github.com/radiac/nanodjango):

Richard Terry demonstrated this in a lightning talk at DjangoCon US today. It's the latest in a long line of attempts to get Django to work with a single file (I had a go at this problem 15 years ago with [djng](https://github.com/simonw/djng)) but this one is *really* compelling.

I tried nanodjango out just now and it works exactly as advertised. First install it like this:

```
pip install nanodjango
```

Create a `counter.py` file:

```
from django.db import models
from nanodjango import Django

app = Django()

@app.admin # Registers with the Django admin
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    CountLog.objects.create()
    return f"<p>Number of page loads: {CountLog.objects.count()}</p>"
```

Then run it like this (it will run migrations and create a superuser as part of that first run):

```
nanodjango run counter.py
```

That's it! This gave me a fully configured Django application with models, migrations, the Django Admin configured and a bunch of other goodies such as [Django Ninja](https://django-ninja.dev/) for API endpoints.

Here's the [full documentation](https://nanodjango.readthedocs.io/).

---

**Link** 2024\-09\-24 [Updated production\-ready Gemini models](https://developers.googleblog.com/en/updated-production-ready-gemini-models-reduced-15-pro-pricing-increased-rate-limits-and-more/):

Two new models from Google Gemini today: `gemini-1.5-pro-002` and `gemini-1.5-flash-002`. Their `-latest` aliases will update to these new models in "the next few days", and new `-001`suffixes can be used to stick with the older models. The new models benchmark slightly better in various ways and should respond faster.

Flash continues to have a 1,048,576 input token and 8,192 output token limit. Pro is 2,097,152 input tokens.

Google also announced a significant price reduction for Pro, effective on the 1st of October. Inputs less than 128,000 tokens drop from $3\.50/million to $1\.25/million (above 128,000 tokens it's dropping from $7 to $5\) and output costs drop from $10\.50/million to $2\.50/million ($21 down to $10 for the \>128,000 case).

For comparison, GPT\-4o is currently $5/m input and $15/m output and Claude 3\.5 Sonnet is $3/m input and $15/m output. Gemini 1\.5 Pro was already the cheapest of the frontier models and now it's even cheaper.

Correction: I missed `gpt-4o-2024-08-06` which is listed later on [the OpenAI pricing page](https://openai.com/api/pricing/) and priced at $2\.50/m input and $10/m output. So the new Gemini 1\.5 Pro prices are undercutting that.

Gemini has always offered finely grained [safety filters](https://ai.google.dev/gemini-api/docs/safety-settings) \- it sounds like those are now turned down to minimum by default, which is a welcome change:

> For the models released today, the filters will not be applied by default so that developers can determine the configuration best suited for their use case.

Also interesting: they've tweaked the expected length of default responses:

> For use cases like summarization, question answering, and extraction, the default output length of the updated models is \~5\-20% shorter than previous models.

---

**Link** 2024\-09\-25 [The Pragmatic Engineer Podcast: AI tools for software engineers, but without the hype – with Simon Willison](https://newsletter.pragmaticengineer.com/p/ai-tools-for-software-engineers-simon-willison):

Gergely Orosz has a brand new podcast, and I was the guest for the first episode. We covered a bunch of ground, but my favorite topic was an exploration of the (very legitimate) reasons that many engineers are resistant to taking advantage of AI\-assisted programming tools.

---

**Quote** 2024\-09\-25

> *We used this model \[periodically transmitting configuration to different hosts] to distribute translations, feature flags, configuration, search indexes, etc at Airbnb. But instead of SQLite we used [Sparkey](https://github.com/spotify/sparkey), a KV file format developed by Spotify. In early years there was a Cron job on every box that pulled that service’s thingies; then once we switched to Kubernetes we used a daemonset \& host tagging (taints?) to pull a variety of thingies to each host and then ensure the services that use the thingies only ran on the hosts that had the thingies.*

[Jake Teton\-Landis](https://news.ycombinator.com/item?id=41645173#41648480)

---

**Link** 2024\-09\-25 [Solving a bug with o1\-preview, files\-to\-prompt and LLM](https://gist.github.com/simonw/03776d9f80534aa8e5348580dc6a800b):

I added [a new feature](https://github.com/simonw/djp/issues/10) to DJP this morning: you can now have plugins specify their metadata in terms of how it should be positioned relative to other metadata \- inserted directly before or directly after `django.middleware.common.CommonMiddleware`for example.

At one point I got stuck with a weird test failure, and after ten minutes of head scratching I decided to pipe the entire thing into OpenAI's `o1-preview` to see if it could spot the problem. I used [files\-to\-prompt](https://github.com/simonw/files-to-prompt) to gather the code and [LLM](https://llm.datasette.io/)to run the prompt:

```
files-to-prompt */.py -c | llm -m o1-preview "
The middleware test is failing showing all of these - why is MiddlewareAfter repeated so many times?

['MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware5', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware2', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware5', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware4', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware5', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware2', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware5', 'MiddlewareAfter', 'Middleware3', 'MiddlewareAfter', 'Middleware', 'MiddlewareBefore']"
```

The model whirled away for a few seconds and spat out[an explanation](https://gist.github.com/simonw/03776d9f80534aa8e5348580dc6a800b#response)of the problem \- one of my middleware classes was accidentally calling`self.get_response(request)`in two different places.

I did enjoy how o1 attempted to reference the [relevant Django documentation](https://docs.djangoproject.com/en/5.1/topics/http/middleware/#writing-your-own-middleware) and then half\-repeated, half\-hallucinated a quote from it:

[![Reference: From the Django documentation on writing middleware: Each middleware component is responsible for doing some specific function. They accept the request, do something, and pass the request to the next middleware component (if needed). They can also modify the response before sending it back to the client.](https://substackcdn.com/image/fetch/$s_!rzGO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff6d9f36-79db-4506-9685-c0d6e68ed99e_1224x438.jpeg "Reference: From the Django documentation on writing middleware: Each middleware component is responsible for doing some specific function. They accept the request, do something, and pass the request to the next middleware component (if needed). They can also modify the response before sending it back to the client.")](https://substackcdn.com/image/fetch/$s_!rzGO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff6d9f36-79db-4506-9685-c0d6e68ed99e_1224x438.jpeg)

This took 2,538 input tokens and 4,354 output tokens \- [by my calculations](https://gist.github.com/simonw/03776d9f80534aa8e5348580dc6a800b?permalink_comment_id=5207703#gistcomment-5207703) at $15/million input and $60/million output that prompt cost just under 30 cents.