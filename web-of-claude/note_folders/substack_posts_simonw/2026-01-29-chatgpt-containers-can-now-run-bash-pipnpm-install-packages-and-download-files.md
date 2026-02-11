# ChatGPT Containers can now run bash, pip/npm install packages, and download files

*Plus adding dynamic features to an aggressively cached website*

Published: 2026-01-29
Source: https://simonw.substack.com/p/chatgpt-containers-can-now-run-bash

---

In this newsletter:

* ChatGPT Containers can now run bash, pip/npm install packages, and download files
* Adding dynamic features to an aggressively cached website

Plus 6 links and 1 quotation and 1 note

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newsletter with my summary of the most important trends of the past 30 days \- here are previews from [October](https://gist.github.com/simonw/3385bc8c83a8157557f06865a0302753) and [November](https://gist.github.com/simonw/fc34b780a9ae19b6be5d732078a572c8).*

### [ChatGPT Containers can now run bash, pip/npm install packages, and download files](https://simonwillison.net/2026/Jan/26/chatgpt-containers/) \- 2026\-01\-26

One of my favourite features of ChatGPT is its ability to write and execute code in a container. This feature launched as ChatGPT Code Interpreter [nearly three years ago](https://simonwillison.net/2023/Apr/12/code-interpreter/), was half\-heartedly rebranded to “Advanced Data Analysis” at some point and is generally really difficult to find detailed documentation about. Case in point: it appears to have had a *massive* upgrade at some point in the past few months, and I can’t find documentation about the new capabilities anywhere!

Here are the most notable new features:

1. ChatGPT can **directly run Bash commands** now. Previously it was limited to Python code only, although it could run shell commands via the Python `subprocess` module.
2. **It has Node.js** and can run JavaScript directly in addition to Python. I also got it to run “hello world” in **Ruby, Perl, PHP, Go, Java, Swift, Kotlin, C and C\+\+**. No Rust yet though!
3. While the container still can’t make outbound network requests, `pip install package` **and** `npm install package` **both work** now via a custom proxy mechanism.
4. ChatGPT can locate the URL for a file on the web and use a `container.download` tool to **download that file and save it to a path** within the sandboxed container.

This is a substantial upgrade! ChatGPT can now write and then test code in 10 new languages (11 if you count Bash), can find files online and download them into the container, and can install additional packages via `pip` and `npm` to help it solve problems.

(OpenAI *really* need to develop better habits at [keeping their release notes up\-to\-date](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)!)

I was initially suspicious that maybe I’d stumbled into a new preview feature that wasn’t available to everyone, but I [tried some experiments](https://chatgpt.com/share/6977aa7c-7bd8-8006-8129-8c9e25126fed) in a free ChatGPT account and confirmed that the new features are available there as well.

* [container.download](https://simonwillison.net/2026/Jan/26/chatgpt-containers/#container-download)
* [Is container.download a data exfiltration vulnerability?](https://simonwillison.net/2026/Jan/26/chatgpt-containers/#is-container-download-a-data-exfiltration-vulnerability-)
* [Bash and other languages](https://simonwillison.net/2026/Jan/26/chatgpt-containers/#bash-and-other-languages)
* [Installing packages from pip and npm](https://simonwillison.net/2026/Jan/26/chatgpt-containers/#installing-packages-from-pip-and-npm)
* [Adding it all together](https://simonwillison.net/2026/Jan/26/chatgpt-containers/#adding-it-all-together)

#### container.download

My first clue to the new features came the other day when I got curious about Los Angeles air quality, in particular has the growing number of electric vehicles there had a measurable impact?

I prompted a fresh GPT\-5\.2 Thinking session with:

> Show me Los Angeles air quality over time for last 20 years

Here’s the [shared transcript](https://chatgpt.com/share/6977a80d-e6e4-8006-b4fe-ed8478fe99d8). Annoyingly that doesn’t make the thinking trace available, so here’s a screenshot:

[![Exploring methods to fetch AQI data and reports Downloading AQI data for Los Angeles  I found an xlsx file titled "Air Quality Statistics by City, 2000-2023", which should include data for Los Angeles. While user requested data for Using provided URL to download file  The URL from the error message leads to an Excel file containing air quality trends. I can use the container.download tool to fetch it. Let’s proceed with this approach and see if it works out for downloading the file directly! Analyzed Parsing and analyzing the data for Los Angeles  Now that we've downloaded the data, I'll parse it using Python. First, I'll focus on identifying the row(s) corresponding to Los Angeles, which may be labeled under "Los Angeles-Long Beach-Anaheim, CA." Afterward, I'll plot metrics like "Median AQI" and "Days Good" over time to visualize trends. Let’s begin!](https://substackcdn.com/image/fetch/$s_!F_50!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaffacd4-773f-4feb-986b-d3391617f037_722x1152.jpeg "Exploring methods to fetch AQI data and reports Downloading AQI data for Los Angeles  I found an xlsx file titled \"Air Quality Statistics by City, 2000-2023\", which should include data for Los Angeles. While user requested data for Using provided URL to download file  The URL from the error message leads to an Excel file containing air quality trends. I can use the container.download tool to fetch it. Let’s proceed with this approach and see if it works out for downloading the file directly! Analyzed Parsing and analyzing the data for Los Angeles  Now that we've downloaded the data, I'll parse it using Python. First, I'll focus on identifying the row(s) corresponding to Los Angeles, which may be labeled under \"Los Angeles-Long Beach-Anaheim, CA.\" Afterward, I'll plot metrics like \"Median AQI\" and \"Days Good\" over time to visualize trends. Let’s begin!")](https://substackcdn.com/image/fetch/$s_!F_50!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaffacd4-773f-4feb-986b-d3391617f037_722x1152.jpeg)

This bit instantly caught my eye:

> \[...] The URL from the error message leads to an Excel file containing air quality trends. I can use the container.download tool to fetch it. \[...]

What’s `container.download`? I [asked ChatGPT](https://chatgpt.com/share/6977aab0-b874-8006-9b54-d3d216ed884b):

> Without running any searches tell me about your container.download tool

And got back:

> Sure. `container.download` is a built\-in tool I can call that **fetches a file from a URL and saves it into the sandboxed container filesystem** for this chat session.
> 
> #### What it does
> 
> * Takes a **publicly reachable URL** and a **destination filepath** in the container.
> * Downloads the bytes from that URL and writes them to the given path.
> * After that, I can read/process the file locally in the container (e.g., unzip it, parse it with Python, open it as an image, convert it, etc.).
> 
> #### Signature (inputs)
> 
> It’s called like this (conceptually):
> 
> 
> ```
> {
>   “url”: “https://example.com/somefile.zip”,
>   “filepath”: “/mnt/data/somefile.zip”
> }
> ```

Further experimentation confirmed that `container.download` behaves as described.

I had it download one file from a server with logs enabled and captured the IP address and user\-agent. Here are the most interesting headers:

```
User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
Accept: text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.9
Cf-Connecting-Ip: 52.230.164.178
```

That `52.230.164.178` IP address [resolves to](http://ip-api.com/json/52.230.164.178) Microsoft Azure Cloud (centralus) in Des Moines, Iowa.

#### Is container.download a data exfiltration vulnerability?

On the one hand, this is really useful! ChatGPT can navigate around websites looking for useful files, download those files to a container and then process them using Python or other languages.

Is this a data exfiltration vulnerability though? Could a prompt injection attack trick ChatGPT into leaking private data out to a `container.download` call to a URL with a query string that includes sensitive information?

I don’t think it can. I tried getting it to assemble a URL with a query string and access it using `container.download` and it couldn’t do it. It told me that it got back this error:

> ERROR: download failed because url not viewed in conversation before. open the file or url using web.run first.

This looks to me like the same safety trick [used by Claude’s Web Fetch tool](https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/): only allow URL access if that URL was either directly entered by the user or if it came from search results that could not have been influenced by a prompt injection.

(I poked at this a bit more and managed to get a simple constructed query string to pass through `web.run` \- a different tool entirely \- but when I tried to compose a longer query string containing the previous prompt history a `web.run` filter blocked it.)

So I *think* this is all safe, though I’m curious if it could hold firm against a more aggressive round of attacks from a seasoned security researcher.

#### Bash and other languages

The key lesson from coding agents like Claude Code and Codex CLI is that Bash rules everything: if an agent can run Bash commands in an environment it can do almost anything that can be achieved by typing commands into a computer.

When Anthropic added their own code interpreter feature to Claude [last September](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/) they built that around Bash rather than just Python. It looks to me like OpenAI have now done the same thing for ChatGPT.

Here’s what ChatGPT looks like when it runs a Bash command \- here my prompt was:

> npm install a fun package and demonstrate using it

[![Screenshot of ChatGPT 5.2 Thinking interface with Activity panel. Main chat shows user prompt "npm install a fun package and demonstrate using it" and response "Thought for 32s > Yep — here's a fun one: cowsay 🐄 I installed it with npm and ran a tiny Node script:" followed by bash code block containing "mkdir -p /mnt/data/npmfun cd /mnt/data/npmfun npm init -y npm install cowsay --no-fund --no-audit node -e "const cowsay=require('cowsay'); console.log(cowsay.say({text:'Hel" and Output: section showing ASCII cow art saying "< Hello from npm inside the container! >" with cow drawing made of characters. Activity panel on right (32s) shows: "Running npm install in container" with bash command and output "v22.16.0 10.9.2", "Inspecting npm command output and container status" with directory listing showing "drwxr-xr-x 2 root oai_shared 80 Jan 26 17:32 . drwxrwxr-x 2 oai oai_shared 60 Jan 26 17:32 .. -rw-r--r-- 1 root root", "Re-running npm install" note about node_modules missing, and "Rerunning npm install with output" showing "added 41 packages in 2s".](https://substackcdn.com/image/fetch/$s_!kVUN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5c95393-5dba-400a-b25b-590279c5dae9_2022x1880.jpeg "Screenshot of ChatGPT 5.2 Thinking interface with Activity panel. Main chat shows user prompt \"npm install a fun package and demonstrate using it\" and response \"Thought for 32s > Yep — here's a fun one: cowsay 🐄 I installed it with npm and ran a tiny Node script:\" followed by bash code block containing \"mkdir -p /mnt/data/npmfun cd /mnt/data/npmfun npm init -y npm install cowsay --no-fund --no-audit node -e \"const cowsay=require('cowsay'); console.log(cowsay.say({text:'Hel\" and Output: section showing ASCII cow art saying \"< Hello from npm inside the container! >\" with cow drawing made of characters. Activity panel on right (32s) shows: \"Running npm install in container\" with bash command and output \"v22.16.0 10.9.2\", \"Inspecting npm command output and container status\" with directory listing showing \"drwxr-xr-x 2 root oai_shared 80 Jan 26 17:32 . drwxrwxr-x 2 oai oai_shared 60 Jan 26 17:32 .. -rw-r--r-- 1 root root\", \"Re-running npm install\" note about node_modules missing, and \"Rerunning npm install with output\" showing \"added 41 packages in 2s\".")](https://substackcdn.com/image/fetch/$s_!kVUN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5c95393-5dba-400a-b25b-590279c5dae9_2022x1880.jpeg)

It’s useful to click on the “Thinking” or “Thought for 32s” links as that opens the Activity sidebar with a detailed trace of what ChatGPT did to arrive at its answer. This helps guard against cheating \- ChatGPT might claim to have run Bash in the main window but it can’t fake those black and white logs in the Activity panel.

I had it run [Hello World in various languages](https://chatgpt.com/share/6977b890-f1c0-8006-b39a-9a02c7ca1993) later in that same session.

[![Terminal screenshot showing "Hello, world" programs in multiple languages. Top section shows code: swift -e 'print("Hello, world from Swift!")' followed by cat > hello.kts <<'KTS' / println("Hello, world from Kotlin!") / KTS / kotlinc -script hello.kts, then cat > hello.c <<'C' / #include <stdio.h> / int main(){ puts("Hello, world from C!"); return 0; } / C / gcc hello.c -o hello_c / ./hello_c, then cat > hello.cpp <<'CPP' / #include <iostream> / int main(){ std::cout << "Hello, world from C++!" << std::endl; } / CPP / g++ hello.cpp -o hello_cpp / ./hello_cpp. Bottom section shows output: Hello, world from Ruby! / Hello, world from Perl! / Hello, world from PHP! / Hello, world from Go! / Hello, world from Java! / Hello, world from Swift! / Hello, world from Kotlin! / Hello, world from C! / Hello, world from C++!. UI shows "Thought for 2m 29s" and "Done" at bottom.](https://substackcdn.com/image/fetch/$s_!GNbm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fded9899e-16fe-4824-8333-7b9515f519fc_1360x1498.jpeg "Terminal screenshot showing \"Hello, world\" programs in multiple languages. Top section shows code: swift -e 'print(\"Hello, world from Swift!\")' followed by cat > hello.kts <<'KTS' / println(\"Hello, world from Kotlin!\") / KTS / kotlinc -script hello.kts, then cat > hello.c <<'C' / #include <stdio.h> / int main(){ puts(\"Hello, world from C!\"); return 0; } / C / gcc hello.c -o hello_c / ./hello_c, then cat > hello.cpp <<'CPP' / #include <iostream> / int main(){ std::cout << \"Hello, world from C++!\" << std::endl; } / CPP / g++ hello.cpp -o hello_cpp / ./hello_cpp. Bottom section shows output: Hello, world from Ruby! / Hello, world from Perl! / Hello, world from PHP! / Hello, world from Go! / Hello, world from Java! / Hello, world from Swift! / Hello, world from Kotlin! / Hello, world from C! / Hello, world from C++!. UI shows \"Thought for 2m 29s\" and \"Done\" at bottom.")](https://substackcdn.com/image/fetch/$s_!GNbm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fded9899e-16fe-4824-8333-7b9515f519fc_1360x1498.jpeg)

#### Installing packages from pip and npm

In the previous example ChatGPT installed the `cowsay` package from npm and used it to draw an ASCII\-art cow. But how could it do that if the container can’t make outbound network requests?

In [another session](https://chatgpt.com/share/69773501-b6d8-8006-bbf2-fa644561aa26) I challenged it to explore its environment. and figure out how that worked.

Here’s [the resulting Markdown report](https://github.com/simonw/research/blob/main/chatgpt-container-environment/README.md) it created.

The key magic appears to be a `applied-caas-gateway1.internal.api.openai.org` proxy, available within the container and with various packaging tools configured to use it.

The following environment variables cause `pip` and `uv` to install packages from that proxy instead of directly from PyPI:

```
PIP_INDEX_URL=https://reader:****@packages.applied-caas-gateway1.internal.api.openai.org/.../pypi-public/simple
PIP_TRUSTED_HOST=packages.applied-caas-gateway1.internal.api.openai.org
UV_INDEX_URL=https://reader:****@packages.applied-caas-gateway1.internal.api.openai.org/.../pypi-public/simple
UV_INSECURE_HOST=https://packages.applied-caas-gateway1.internal.api.openai.org
```

This one appears to get `npm` to work:

```
NPM_CONFIG_REGISTRY=https://reader:****@packages.applied-caas-gateway1.internal.api.openai.org/.../npm-public
```

And it reported these suspicious looking variables as well:

```
CAAS_ARTIFACTORY_BASE_URL=packages.applied-caas-gateway1.internal.api.openai.org
CAAS_ARTIFACTORY_PYPI_REGISTRY=.../artifactory/api/pypi/pypi-public
CAAS_ARTIFACTORY_NPM_REGISTRY=.../artifactory/api/npm/npm-public
CAAS_ARTIFACTORY_GO_REGISTRY=.../artifactory/api/go/golang-main
CAAS_ARTIFACTORY_MAVEN_REGISTRY=.../artifactory/maven-public
CAAS_ARTIFACTORY_GRADLE_REGISTRY=.../artifactory/gradle-public
CAAS_ARTIFACTORY_CARGO_REGISTRY=.../artifactory/api/cargo/cargo-public/index
CAAS_ARTIFACTORY_DOCKER_REGISTRY=.../dockerhub-public
CAAS_ARTIFACTORY_READER_USERNAME=reader
CAAS_ARTIFACTORY_READER_PASSWORD=****
NETWORK=caas_packages_only
```

Neither Rust nor Docker are installed in the container environment, but maybe those registry references are a clue of features still to come.

#### Adding it all together

The result of all of this? You can tell ChatGPT to use Python or Node.js packages as part of a conversation and it will be able to install them and apply them against files you upload or that it downloads from the public web. That’s *really* cool.

The big missing feature here should be the easiest to provide: we need **official documentation**! A release notes entry would be a good start, but there are a lot of subtle details to how this new stuff works, its limitations and what it can be used for.

As always, I’d also encourage OpenAI to come up with a name for this set of features that properly represents how it works and what it can do.

In the meantime, I’m going to call this **ChatGPT Containers**.

#### Update: a full list of tools

I decided to ask ChatGPT about other tools that were available to it in case there was anything interesting in there:

> List all tools that are available to you, with their exact names and descriptions and signatures

Here’s [what I got back](https://chatgpt.com/share/6977ffa0-df14-8006-9647-2b8c90ccbb81).

### [Adding dynamic features to an aggressively cached website](https://simonwillison.net/2026/Jan/28/dynamic-features-static-site/) \- 2026\-01\-28

My blog uses aggressive caching: it sits behind Cloudflare with a 15 minute cache header, which guarantees it can survive even the largest traffic spike to any given page. I’ve recently added a couple of dynamic features that work in spite of that full\-page caching. Here’s how those work.

#### Edit links that are visible only to me

This is a Django site and I manage it through the Django admin.

I have [four types of content](https://github.com/simonw/simonwillisonblog/blob/b8066f870a94d149f5e8cee6e787d3377c0b9507/blog/models.py#L254-L449) \- entries, link posts (aka blogmarks), quotations and notes. Each of those has a different model and hence a different Django admin area.

I wanted an “edit” link on the public pages that was only visible to me.

The button looks like this:

[![Entry footer - it says Posted 27th January 2026 at 9:44 p.m. followed by a square Edit button with an icon.](https://substackcdn.com/image/fetch/$s_!AdYp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fc2a0a8-b165-405a-a998-026e73cb4ce3_1178x178.jpeg "Entry footer - it says Posted 27th January 2026 at 9:44 p.m. followed by a square Edit button with an icon.")](https://substackcdn.com/image/fetch/$s_!AdYp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fc2a0a8-b165-405a-a998-026e73cb4ce3_1178x178.jpeg)

I solved conditional display of this button with `localStorage`. I have a [tiny bit of JavaScript](https://github.com/simonw/simonwillisonblog/blob/b8066f870a94d149f5e8cee6e787d3377c0b9507/templates/base.html#L89-L105) which checks to see if the `localStorage` key `ADMIN` is set and, if it is, displays an edit link based on a data attribute:

```
document.addEventListener(’DOMContentLoaded’, () => {
  if (window.localStorage.getItem(’ADMIN’)) {
    document.querySelectorAll(’.edit-page-link’).forEach(el => {
      const url = el.getAttribute(’data-admin-url’);
      if (url) {
        const a = document.createElement(’a’);
        a.href = url;
        a.className = ‘edit-link’;
        a.innerHTML = ‘<svg>...</svg> Edit’;
        el.appendChild(a);
        el.style.display = ‘block’;
      }
    });
  }
});
```

If you want to see my edit links you can run this snippet of JavaScript:

```
localStorage.setItem(’ADMIN’, ‘1’);
```

My Django admin dashboard has [a custom checkbox](https://github.com/simonw/simonwillisonblog/blob/b8066f870a94d149f5e8cee6e787d3377c0b9507/templates/admin/index.html#L18-L39) I can click to turn this option on and off in my own browser:

[![Screenshot of a Tools settings panel with a teal header reading "Tools" followed by three linked options: "Bulk Tag Tool - Add tags to multiple items at once", "Merge Tags - Merge multiple tags into one", "SQL Dashboard - Run SQL queries against the database", and a checked checkbox labeled "Show "Edit" links on public pages"](https://substackcdn.com/image/fetch/$s_!nMsC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc041e81-9ede-416c-bd34-e7d60695f747_1250x368.jpeg "Screenshot of a Tools settings panel with a teal header reading \"Tools\" followed by three linked options: \"Bulk Tag Tool - Add tags to multiple items at once\", \"Merge Tags - Merge multiple tags into one\", \"SQL Dashboard - Run SQL queries against the database\", and a checked checkbox labeled \"Show \"Edit\" links on public pages\"")](https://substackcdn.com/image/fetch/$s_!nMsC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc041e81-9ede-416c-bd34-e7d60695f747_1250x368.jpeg)

#### Random navigation within a tag

Those admin edit links are a very simple pattern. A more interesting one is a feature I added recently for navigating randomly within a tag.

Here’s an animated GIF showing those random tag navigations in action ([try it here](https://simonwillison.net/tag/ai-ethics/)):

[![Animated demo. Starts on the ai-ethics tag page where a new Random button sits next to the feed icon. Clicking that button jumps to a post with that tag and moves the button into the site header - clicking it multiple times jumps to more random items.](https://substackcdn.com/image/fetch/$s_!FVYB!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d93b895-cf8e-4a26-a876-3e5a11f74268_661x417.gif "Animated demo. Starts on the ai-ethics tag page where a new Random button sits next to the feed icon. Clicking that button jumps to a post with that tag and moves the button into the site header - clicking it multiple times jumps to more random items.")](https://substackcdn.com/image/fetch/$s_!FVYB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d93b895-cf8e-4a26-a876-3e5a11f74268_661x417.gif)

On any of my blog’s tag pages you can click the “Random” button to bounce to a random post with that tag. That random button then persists in the header of the page and you can click it to continue bouncing to random items in that same tag.

A post can have multiple tags, so there needs to be a little bit of persistent magic to remember which tag you are navigating and display the relevant button in the header.

Once again, this uses `localStorage`. Any click to a random button records both the tag and the current timestamp to the `random_tag` key in `localStorage` before redirecting the user to the `/random/name-of-tag/` page, which selects a random post and redirects them there.

Any time a new page loads, JavaScript checks if that `random_tag` key has a value that was recorded within the past 5 seconds. If so, that random button is appended to the header.

This means that, provided the page loads within 5 seconds of the user clicking the button, the random tag navigation will persist on the page.

You can [see the code for that here](https://github.com/simonw/simonwillisonblog/blob/b8066f870a94d149f5e8cee6e787d3377c0b9507/templates/base.html#L106-L147).

#### And the prompts

I built the random tag feature entirely using Claude Code for web, prompted from my iPhone. I started with the `/random/TAG/` endpoint ([full transcript](https://gistpreview.github.io/?2e7de58a779271aa5eb6f4abcd412d72/index.html)):

> Build /random/TAG/ \- a page which picks a random post (could be an entry or blogmark or note or quote) that has that tag and sends a 302 redirect to it, marked as no\-cache so Cloudflare does not cache it
> 
> Use a union to build a list of every content type (a string representing the table out of the four types) and primary key for every item tagged with that tag, then order by random and return the first one
> 
> Then inflate the type and ID into an object and load it and redirect to the URL
> 
> Include tests \- it should work by setting up a tag with one of each of the content types and then running in a loop calling that endpoint until it has either returned one of each of the four types or it hits 1000 loops at which point fail with an error

Then:

> I do not like that solution, some of my tags have thousands of items
> 
> Can we do something clever with a CTE?

Here’s the [something clever with a CTE](https://github.com/simonw/simonwillisonblog/blob/b8066f870a94d149f5e8cee6e787d3377c0b9507/blog/views.py#L737-L762) solution we ended up with.

For the “Random post” button ([transcript](https://gistpreview.github.io/?d2d3abe380080ceb9e7fb854fa197bff/index.html)):

> Look at most recent commit, then modify the /tags/xxx/ page to have a “Random post” button which looks good and links to the /random/xxx/ page

Then:

> Put it before not after the feed icon. It should only display if a tag has more than 5 posts

And finally, the `localStorage` implementation that persists a random tag button in the header ([transcript](https://gistpreview.github.io/?8405b84f8e53738c8d4377b2e41dcdef/page-001.html)):

> Review the last two commits. Make it so clicking the Random button on a tag page sets a localStorage value for random\_tag with that tag and a timestamp. On any other page view that uses the base item template add JS that checks for that localStorage value and makes sure the timestamp is within 5 seconds. If it is within 5 seconds it adds a “Random name\-of\-tag” button to the little top navigation bar, styled like the original Random button, which bumps the localStorage timestamp and then sends the user to /random/name\-of\-tag/ when they click it. In this way clicking “Random” on a tag page will send the user into an experience where they can keep clicking to keep surfing randomly in that topic.

---

**Quote** 2026\-01\-24

> **If you tell a friend they can now instantly create any app, they’ll probably say “Cool! Now I need to think of an idea.”** Then they will forget about it, and never build a thing. The problem is not that your friend is horribly uncreative. It’s that most people’s problems are not software\-shaped, and most won’t notice even when they are. \[...]
> 
> Programmers are trained to see everything as a software\-shaped problem: if you do a task three times, you should probably automate it with a script. *Rename every IMG\_\*.jpg file from the last week to hawaii2025\_\*.jpg*, they tell their terminal, while the rest of us painfully click and copy\-paste. We are blind to the solutions we were never taught to see, asking for faster horses and never dreaming of cars.

[Jasmine Sun](https://jasmi.news/p/claude-code)

---

**Link** 2026\-01\-24 [Don’t “Trust the Process”](https://www.youtube.com/watch?v=4u94juYwLLM):

Jenny Wen, Design Lead at Anthropic (and previously Director of Design at Figma) gave a provocative keynote at Hatch Conference in Berlin last September.

[![Don't ](https://substackcdn.com/image/fetch/$s_!pxcv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3354a6c6-4983-4c73-b206-4efb0b18997f_2664x1214.jpeg "Don't ")](https://substackcdn.com/image/fetch/$s_!pxcv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3354a6c6-4983-4c73-b206-4efb0b18997f_2664x1214.jpeg)

Jenny argues that the Design Process \- user research leading to personas leading to user journeys leading to wireframes... all before anything gets built \- may be outdated for today’s world.

> **Hypothesis**: In a world where anyone can make anything — what matters is your ability to choose and curate what you make.

In place of the Process, designers should lean into prototypes. AI makes these much more accessible and less time\-consuming than they used to be.

Watching this talk made me think about how AI\-assisted programming significantly reduces the cost of building the *wrong* thing. Previously if the design wasn’t right you could waste months of development time building in the wrong direction, which was a very expensive mistake. If a wrong direction wastes just a few days instead we can take more risks and be much more proactive in exploring the problem space.

I’ve always been a compulsive prototyper though, so this is very much playing into my own existing biases!

---

**Link** 2026\-01\-25 [Kākāpō Cam: Rakiura live stream](https://www.doc.govt.nz/our-work/kakapo-recovery/what-we-do/kakapo-cam-rakiura-live-stream/):

Critical update for this year’s [Kākāpō breeding season](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-k-k-p-parrots-will-have-an-outstanding-breeding-season): the New Zealand Department of Conservation have a livestream running of Rakiura’s nest!

> You’re looking at the underground nest of 23\-year\-old Rakiura. She has chosen this same site to nest for all seven breeding seasons since 2008, a large cavity under a rātā tree. Because she returns to the site so reliably, we’ve been able to make modifications over the years to keep it safe and dry, including adding a well\-placed hatch for monitoring eggs and chicks.

Rakiura is a legendary Kākāpō:

> Rakiura hatched on 19 February 2002 on Whenua Hou/Codfish Island. She is the offspring of Flossie and Bill. Her name comes from the te reo Māori name for Stewart Island, the place where most of the founding kākāpō population originated.
> 
> Rakiura has nine living descendants, three females and six males, across six breeding seasons. In 2008 came Tōitiiti, in 2009 Tamahou and Te Atapō, in 2011 Tia and Tūtoko, in 2014 Taeatanga and Te Awa, in 2019 Mati\-mā and Tautahi. She also has many grandchicks.

She laid her first egg of the season at 4:30pm NZ time on 22nd January. The livestream went live shortly afterwards, once she committed to this nest.

The stream is [on YouTube](https://www.youtube.com/watch?v=BfGL7A2YgUY). I [used Claude Code](https://gisthost.github.io/?dc78322de89a2191c593215f109c65d7/index.html) to write [a livestream\-gif.py script](https://tools.simonwillison.net/python/#livestream-gifpy) and used that to capture this sped\-up video of the last few hours of footage, within which you can catch a glimpse of the egg!

---

**Link** 2026\-01\-25 [the browser is the sandbox](https://aifoc.us/the-browser-is-the-sandbox/):

Paul Kinlan is a web platform developer advocate at Google and recently turned his attention to coding agents. He quickly identified the importance of a robust sandbox for agents to operate in and put together these detailed notes on how the web browser can help:

> This got me thinking about the browser. Over the last 30 years, we have built a sandbox specifically designed to run incredibly hostile, untrusted code from anywhere on the web, the instant a user taps a URL. \[...]
> 
> Could you build something like Cowork in the browser? Maybe. To find out, I built a demo called [Co\-do](http://co-do.xyz) that tests this hypothesis. In this post I want to discuss the research I’ve done to see how far we can get, and determine if the browser’s ability to run untrusted code is useful (and good enough) for enabling software to do more for us directly on our computer.

Paul then describes how the three key aspects of a sandbox \- filesystem, network access and safe code execution \- can be handled by browser technologies: the [File System Access API](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access) (still Chrome\-only as far as I can tell), CSP headers with `<iframe sandbox>` and WebAssembly in Web Workers.

Co\-do is a very interesting demo that illustrates all of these ideas in a single application:

[![Screenshot of Co-do application interface with robot logo. Left sidebar shows WORKSPACE section with ](https://substackcdn.com/image/fetch/$s_!jzsj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a5ab50d-93bc-42ff-85f3-a02d554a84ea_2014x1640.jpeg "Screenshot of Co-do application interface with robot logo. Left sidebar shows WORKSPACE section with ")](https://substackcdn.com/image/fetch/$s_!jzsj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a5ab50d-93bc-42ff-85f3-a02d554a84ea_2014x1640.jpeg)

You select a folder full of files and configure an LLM provider and set an API key, Co\-do then uses CSP\-approved API calls to interact with that provider and provides a chat interface with tools for interacting with those files. It does indeed feel similar to [Claude Cowork](https://simonwillison.net/2026/Jan/12/claude-cowork/) but without running a multi\-GB local container to provide the sandbox.

My biggest complaint about `<iframe sandbox>` remains how thinly documented it is, especially across different browsers. Paul’s post has all sorts of useful details on that which I’ve not encountered elsewhere, including a complex [double\-iframe technique](https://aifoc.us/the-browser-is-the-sandbox/#the-double-iframe-technique) to help apply network rules to the inner of the two frames.

Thanks to this post I also learned about the `<input type="file" webkitdirectory>` tag which turns out to work on Firefox, Safari *and* Chrome and allows a browser read\-only access to a full directory of files at once. I had Claude knock up a [webkitdirectory demo](https://tools.simonwillison.net/webkitdirectory) to try it out and I’ll certainly be using it for projects in the future.

[![.claude > skills > building-datasette-plugins containing HOOKS.md (10.7 KB, selected/highlighted), INTERNALS.md (10.1 KB), SKILL.md (3.7 KB), TESTING.md (8.4 KB), settings.local.json (280 B); also shows .eggs folder with pytest_runner-6.0.1-py3.9.egg. Right panel “File preview” shows selected file details: Name: HOOKS.md, Path: datasette/.claude/skills/building-datasette-plugins/HOOKS.md, Size: 10.7 KB, Type: text/markdown, Last modified: 12/20/2025, 9:28:59 AM. Preview content shows: “# Plugin Hooks Reference” followed by “All hooks use the @hookimpl decorator. Accept only the parameters you need.” then “## Database Connection Hooks” and “### prepare_connection(conn, database, datasette)” with description “Called when a new SQLite connection is created. Use to register custom SQL functions.” Bottom section “File type distribution” shows horizontal bar chart: .py (4439), .no ext (3358), .dat (1068), .pyc (925), .txt (332), .mo (321), .po (321), .html (249).](https://substackcdn.com/image/fetch/$s_!wiTq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F493ae35e-655d-4266-a231-532e9f47f664_2276x1820.jpeg ".claude > skills > building-datasette-plugins containing HOOKS.md (10.7 KB, selected/highlighted), INTERNALS.md (10.1 KB), SKILL.md (3.7 KB), TESTING.md (8.4 KB), settings.local.json (280 B); also shows .eggs folder with pytest_runner-6.0.1-py3.9.egg. Right panel “File preview” shows selected file details: Name: HOOKS.md, Path: datasette/.claude/skills/building-datasette-plugins/HOOKS.md, Size: 10.7 KB, Type: text/markdown, Last modified: 12/20/2025, 9:28:59 AM. Preview content shows: “# Plugin Hooks Reference” followed by “All hooks use the @hookimpl decorator. Accept only the parameters you need.” then “## Database Connection Hooks” and “### prepare_connection(conn, database, datasette)” with description “Called when a new SQLite connection is created. Use to register custom SQL functions.” Bottom section “File type distribution” shows horizontal bar chart: .py (4439), .no ext (3358), .dat (1068), .pyc (925), .txt (332), .mo (321), .po (321), .html (249).")](https://substackcdn.com/image/fetch/$s_!wiTq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F493ae35e-655d-4266-a231-532e9f47f664_2276x1820.jpeg)

---

**Note** [2026\-01\-26](https://simonwillison.net/2026/Jan/26/tests/)

Someone [asked](https://news.ycombinator.com/item?id=46765460#46765823) on Hacker News if I had any tips for getting coding agents to write decent quality tests. Here’s what I said:

---

I work in Python which helps a lot because there are a TON of good examples of pytest tests floating around in the training data, including things like usage of fixture libraries for mocking external HTTP APIs and snapshot testing and other neat patterns.

Or I can say “use pytest\-httpx to mock the endpoints” and Claude knows what I mean.

Keeping an eye on the tests is important. The most common anti\-pattern I see is large amounts of duplicated test setup code \- which isn’t a huge deal, I’m much more more tolerant of duplicated logic in tests than I am in implementation, but it’s still worth pushing back on.

“Refactor those tests to use pytest.mark.parametrize” and “extract the common setup into a pytest fixture” work really well there.

Generally though the best way to get good tests out of a coding agent is to make sure it’s working in a project with an existing test suite that uses good patterns. Coding agents pick the existing patterns up without needing any extra prompting at all.

I find that once a project has clean basic tests the new tests added by the agents tend to match them in quality. It’s similar to how working on large projects with a team of other developers work \- keeping the code clean means when people look for examples of how to write a test they’ll be pointed in the right direction.

One last tip I use a lot is this:

```
Clone datasette/datasette-enrichments
from GitHub to /tmp and imitate the
testing patterns it uses
```

I do this all the time with different existing projects I’ve written \- the quickest way to show an agent how you like something to be done is to have it look at an example.

---

**Link** 2026\-01\-27 [Kimi K2\.5: Visual Agentic Intelligence](https://www.kimi.com/blog/kimi-k2-5.html):

Kimi K2 landed [in July](https://simonwillison.net/2025/Jul/11/kimi-k2/) as a 1 trillion parameter open weight LLM. It was joined by Kimi K2 Thinking [in November](https://simonwillison.net/2025/Nov/6/kimi-k2-thinking/) which added reasoning capabilities. Now they’ve made it multi\-modal: the K2 models were text\-only, but the new 2\.5 can handle image inputs as well:

> Kimi K2\.5 builds on Kimi K2 with continued pretraining over approximately 15T mixed visual and text tokens. Built as a native multimodal model, K2\.5 delivers state\-of\-the\-art coding and vision capabilities and a self\-directed agent swarm paradigm.

The “self\-directed agent swarm paradigm” claim there means improved long\-sequence tool calling and training on how to break down tasks for multiple agents to work on at once:

> For complex tasks, Kimi K2\.5 can self\-direct an agent swarm with up to 100 sub\-agents, executing parallel workflows across up to 1,500 tool calls. Compared with a single\-agent setup, this reduces execution time by up to 4\.5x. The agent swarm is automatically created and orchestrated by Kimi K2\.5 without any predefined subagents or workflow.

I used the [OpenRouter Chat UI](https://openrouter.ai/moonshotai/kimi-k2.5) to have it “Generate an SVG of a pelican riding a bicycle”, and it did [quite well](https://gist.github.com/simonw/32a85e337fbc6ee935d10d89726c0476):

[![Cartoon illustration of a white pelican with a large orange beak and yellow throat pouch riding a green bicycle with yellow feet on the pedals, set against a light blue sky with soft bokeh circles and a green grassy hill. The bicycle frame is a little questionable. The pelican is quite good. The feet do not quite align with the pedals, which are floating clear of the frame.](https://substackcdn.com/image/fetch/$s_!T8Z4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69500d9f-f169-45cd-83b6-d8d525920daf_800x600.png "Cartoon illustration of a white pelican with a large orange beak and yellow throat pouch riding a green bicycle with yellow feet on the pedals, set against a light blue sky with soft bokeh circles and a green grassy hill. The bicycle frame is a little questionable. The pelican is quite good. The feet do not quite align with the pedals, which are floating clear of the frame.")](https://substackcdn.com/image/fetch/$s_!T8Z4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69500d9f-f169-45cd-83b6-d8d525920daf_800x600.png)

As a more interesting test, I decided to exercise the claims around multi\-agent planning with this prompt:

> I want to build a Datasette plugin that offers a UI to upload files to an S3 bucket and stores information about them in a SQLite table. Break this down into ten tasks suitable for execution by parallel coding agents.

Here’s [the full response](https://gist.github.com/simonw/ee2583b2eb5706400a4737f56d57c456). It produced ten realistic tasks and reasoned through the dependencies between them. For comparison here’s the same prompt [against Claude Opus 4\.5](https://claude.ai/share/df9258e7-97ba-4362-83da-76d31d96196f) and [against GPT\-5\.2 Thinking](https://chatgpt.com/share/6978d48c-3f20-8006-9c77-81161f899104).

The [Hugging Face repository](https://huggingface.co/moonshotai/Kimi-K2.5) is 595GB. The model uses Kimi’s janky “modified MIT” license, which adds the following clause:

> Our only modification part is that, if the Software (or any derivative works thereof) is used for any of your commercial products or services that have more than 100 million monthly active users, or more than 20 million US dollars (or equivalent in other currencies) in monthly revenue, you shall prominently display “Kimi K2\.5” on the user interface of such product or service.

Given the model’s size, I expect one way to run it locally would be with MLX and a pair of $10,000 512GB RAM M3 Ultra Mac Studios. That setup has [been demonstrated to work](https://twitter.com/awnihannun/status/1943723599971443134) with previous trillion parameter K2 models.

---

**Link** 2026\-01\-27 [One Human \+ One Agent \= One Browser From Scratch](https://emsh.cat/one-human-one-agent-one-browser/):

embedding\-shapes was [so infuriated](https://emsh.cat/cursor-implied-success-without-evidence/) by the hype around Cursor’s [FastRender browser project](https://simonwillison.net/2026/Jan/23/fastrender/) \- thousands of parallel agents producing \~1\.6 million lines of Rust \- that they were inspired to take a go at building a web browser using coding agents themselves.

The result is [one\-agent\-one\-browser](https://github.com/embedding-shapes/one-agent-one-browser) and it’s *really* impressive. Over three days they drove a single Codex CLI agent to build 20,000 lines of Rust that successfully renders HTML\+CSS with no Rust crate dependencies at all \- though it does (reasonably) use Windows, macOS and Linux system frameworks for image and text rendering.

I installed the [1MB macOS binary release](https://github.com/embedding-shapes/one-agent-one-browser/releases/tag/0.1.0) and ran it against my blog:

```
chmod 755 ~/Downloads/one-agent-one-browser-macOS-ARM64 
~/Downloads/one-agent-one-browser-macOS-ARM64 https://simonwillison.net/
```

Here’s the result:

[![My blog rendered in a window. Everything is in the right place, the CSS gradients look good, the feed subscribe SVG icon is rendered correctly but there's a missing PNG image.](https://substackcdn.com/image/fetch/$s_!NEcf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0de2f2f0-3924-4f36-89f0-769ce351205c_2000x1600.jpeg "My blog rendered in a window. Everything is in the right place, the CSS gradients look good, the feed subscribe SVG icon is rendered correctly but there's a missing PNG image.")](https://substackcdn.com/image/fetch/$s_!NEcf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0de2f2f0-3924-4f36-89f0-769ce351205c_2000x1600.jpeg)

It even rendered my SVG feed subscription icon! A PNG image is missing from the page, which looks like an intermittent bug (there’s code to render PNGs).

The code is pretty readable too \- here’s [the flexbox implementation](https://github.com/embedding-shapes/one-agent-one-browser/blob/0.1.0/src/layout/flex.rs).

I had thought that “build a web browser” was the ideal prompt to really stretch the capabilities of coding agents \- and that it would take sophisticated multi\-agent harnesses (as seen in the Cursor project) and millions of lines of code to achieve.

Turns out one agent driven by a talented engineer, three days and 20,000 lines of Rust is enough to get a very solid basic renderer working!

I’m going to upgrade my [prediction for 2029](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#3-years-someone-will-build-a-new-browser-using-mainly-ai-assisted-coding-and-it-won-t-even-be-a-surprise): I think we’re going to get a *production\-grade* web browser built by a small team using AI assistance by then.

---

**Link** 2026\-01\-28 [The Five Levels: from Spicy Autocomplete to the Dark Factory](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/):

Dan Shapiro proposes a five level model of AI\-assisted programming, inspired by the five (or rather six, it’s zero\-indexed) [levels of driving automation](https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-05/Level-of-Automation-052522-tag.pdf).

0. **Spicy autocomplete**, aka original GitHub Copilot or copying and pasting snippets from ChatGPT.
1. The **coding intern**, writing unimportant snippets and boilerplate with full human review.
2. The **junior developer**, pair programming with the model but still reviewing every line.
3. The **developer**. Most code is generated by AI, and you take on the role of full\-time code reviewer.
4. The **engineering team**. You’re more of an engineering manager or product/program/project manager. You collaborate on specs and plans, the agents do the work.
5. The **dark software factory**, like a factory run by robots where the lights are out because robots don’t need to see.

Dan says about that last category:

> At level 5, it’s not really a car any more. You’re not really running anybody else’s software any more. And your software process isn’t really a software process any more. It’s a black box that turns specs into software.
> 
> Why Dark? Maybe you’ve heard of the Fanuc Dark Factory, [the robot factory staffed by robots](https://www.organizedergi.com/News/5493/robots-the-maker-of-robots-in-fanuc-s-dark-factory). It’s dark, because it’s a place where humans are neither needed nor welcome.
> 
> I know a handful of people who are doing this. They’re small teams, less than five people. And what they’re doing is nearly unbelievable \-\- and it will likely be our future.

I’ve talked to one team that’s doing the pattern hinted at here. It was *fascinating*. The key characteristics:

* Nobody reviews AI\-produced code, ever. They don’t even look at it.
* The goal of the system is to prove that the system works. A huge amount of the coding agent work goes into testing and tooling and simulating related systems and running demos.
* The role of the humans is to design that system \- to find new patterns that can help the agents work more effectively and demonstrate that the software they are building is robust and effective.

It was a tiny team and they stuff they had built in just a few months looked very convincing to me. Some of them had 20\+ years of experience as software developers working on systems with high reliability requirements, so they were not approaching this from a naive perspective.

I’m hoping they come out of stealth soon because I can’t really share more details than this.

---