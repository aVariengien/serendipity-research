# Trying out llama.cpp's new vision support

*Plus Gemini 2.0 image creation via their API*

Published: 2025-05-11
Source: https://simonw.substack.com/p/trying-out-llamacpps-new-vision-support

---

In this newsletter:

* Trying out llama.cpp's new vision support

Plus 11 links and 3 quotations and 1 TIL and 3 notes

### [Trying out llama.cpp's new vision support](https://simonwillison.net/2025/May/10/llama-cpp-vision/) \- 2025\-05\-10

This [llama.cpp server vision support via libmtmd](https://github.com/ggml-org/llama.cpp/pull/12898) pull request \- via [Hacker News](https://news.ycombinator.com/item?id=43943047) \- was merged earlier today. The PR finally adds full support for vision models to the excellent [llama.cpp](https://github.com/ggml-org/llama.cpp) project. It's documented [on this page](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md), but the more detailed technical details are [covered here](https://github.com/ggml-org/llama.cpp/tree/master/tools/mtmd#multimodal-support-in-llamacpp). Here are my notes on getting it working on a Mac.

`llama.cpp` models are usually distributed as `.gguf` files. This project introduces a new variant of those called `mmproj`, for multimodal projector. `libmtmd` is the new library for handling these.

You can try it out by compiling `llama.cpp` from source, but I found another option that works: you can download pre\-compiled binaries from the [GitHub releases](https://github.com/ggml-org/llama.cpp/releases).

On macOS there's an extra step to jump through to get these working, which I'll describe below.

**Update**: it turns out the [Homebrew package](https://formulae.brew.sh/formula/llama.cpp) for `llama.cpp` turns things around *extremely* quickly. You can run `brew install llama.cpp` or `brew upgrade llama.cpp` and start running the below tools without any extra steps.

I downloaded the `llama-b5332-bin-macos-arm64.zip` file from [this GitHub release](https://github.com/ggml-org/llama.cpp/releases/tag/b5332) and unzipped it, which created a `build/bin` directory.

That directory contains a bunch of binary executables and a whole lot of `.dylib` files. macOS wouldn't let me execute these files because they were quarantined. Running this command fixed that for the `llama-mtmd-cli` and `llama-server` executables and the `.dylib` files they needed:

```
sudo xattr -rd com.apple.quarantine llama-server llama-mtmd-cli *.dylib
```

Now I can run an interactive terminal LLM session using this command:

```
./llama-mtmd-cli -hf unsloth/gemma-3-4b-it-GGUF:Q4_K_XL
```

The first time this runs it fetches four files from [unsloth/gemma\-3\-4b\-it\-GGUF](https://huggingface.co/unsloth/gemma-3-4b-it-GGUF) \- a quantized copy of Google DeepMind's [Gemma 3 4B](https://huggingface.co/google/gemma-3-4b-pt) \- and stores them in `~/Library/Caches/llama.cpp`:

```
2.4G unsloth_gemma-3-4b-it-GGUF_gemma-3-4b-it-UD-Q4_K_XL.gguf
217B unsloth_gemma-3-4b-it-GGUF_gemma-3-4b-it-UD-Q4_K_XL.gguf.json
812M unsloth_gemma-3-4b-it-GGUF_mmproj-F16.gguf
203B unsloth_gemma-3-4b-it-GGUF_mmproj-F16.gguf.json
```

Once they've downloaded an interactive session starts. You can chat directly with the model or use the `/image path-to-image.jpg` command to load an image into the context.

I loaded in [a pelican photo](https://static.simonwillison.net/static/2025/pelican-no-hat.jpg) and prompted "describe it" and got back this:

> It’s a striking photograph of a brown pelican standing in shallow water on a sandy beach. Here's a breakdown of what I see:
> 
> * **Subject:** The main focus is a large brown pelican. It’s standing with its wings fully extended, creating a dramatic pose.
> * **Pose:** The pelican is in a slightly awkward, almost comical stance, with its legs planted firmly in the wet sand and its wings spread wide. It looks like it might be preparing to take off or is simply enjoying the water.
> * **Color \& Texture:** The pelican is a rich, dark brown with lighter markings on its wings and head. The sand is a muted beige color, and the water reflects the sunlight, creating a shimmering effect. You can see the texture of the sand and the ripples in the water.
> * **Lighting:** The lighting appears to be bright and sunny, casting shadows and highlighting the details of the pelican's feathers.
> * **Background:** The background is blurred, suggesting a shallow depth of field, which keeps the focus on the pelican. It appears to be a beach scene.
> * **Overall Impression:** The image has a dynamic feel due to the pelican’s pose and the movement implied by the water. It’s a well\-composed shot that captures a moment of wildlife in its natural habitat.
> 
> Do you want me to zoom in on a particular detail, or perhaps tell you more about pelicans?

Not bad for a 3\.2GB model running on my laptop!

[![Screenshot of the terminal session showing the response quoted above.](https://substackcdn.com/image/fetch/$s_!F4lr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff013041a-3ef3-460c-a488-e20db7fb24c9_1504x1394.jpeg "Screenshot of the terminal session showing the response quoted above.")](https://substackcdn.com/image/fetch/$s_!F4lr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff013041a-3ef3-460c-a488-e20db7fb24c9_1504x1394.jpeg)

#### Running llama\-server

Even more fun is the `llama-server` [command](https://github.com/ggml-org/llama.cpp/tree/master/tools/server#llamacpp-http-server). This starts a localhost web server running on port 8080 to serve the model, with both a web UI and an OpenAI\-compatible API endpoint.

The command to run it is the same:

```
./llama-server -hf unsloth/gemma-3-4b-it-GGUF:Q4_K_XL
```

Now visit

http://localhost:8080

in your browser to start interacting with the model:

[![screenshot of llama.cpp web UI - I've added a photo of some pelicans and the prompt decsribe these creatures, it came back with the following: Okay, let's describe these beautiful birds!  These are Brown Pelicans (Pelecanus occidentalis).  Here's a breakdown of their key features, based on the image:      Appearance: They are large, brown birds with distinctive long, pointed bills. Their plumage is a rich, chocolate brown, with lighter underparts. They have large, webbed feet.     Posture: As you can see, they're standing together on a concrete embankment, likely near the water's edge. They're in a somewhat huddled or attentive stance.     Size: They are quite large birds – adults can have a wingspan of up to 6.5 feet (2 meters).     Behavior: Pelicans are known for their unique feeding technique, where they plunge-dive into the water to scoop up fish with their pouches.  In the image, you can see:      A group of 6-7 Brown Pelicans.     A single bird in the foreground, slightly out of focus, showing a more detailed view of their feathers and feet.  Where they are: The presence of these birds suggests they are likely in a coastal or wetland environment – perhaps a bay, estuary, or near a large body of water.  Do you want me to delve deeper into any specific aspect of these birds, such as their habitat, diet, or conservation status? On the right is a Conversations sidebar with three other conversations listed.](https://substackcdn.com/image/fetch/$s_!aSxC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdba53ea8-c8f0-4729-a81e-cb25783ca683_2030x1962.jpeg "screenshot of llama.cpp web UI - I've added a photo of some pelicans and the prompt decsribe these creatures, it came back with the following: Okay, let's describe these beautiful birds!  These are Brown Pelicans (Pelecanus occidentalis).  Here's a breakdown of their key features, based on the image:      Appearance: They are large, brown birds with distinctive long, pointed bills. Their plumage is a rich, chocolate brown, with lighter underparts. They have large, webbed feet.     Posture: As you can see, they're standing together on a concrete embankment, likely near the water's edge. They're in a somewhat huddled or attentive stance.     Size: They are quite large birds – adults can have a wingspan of up to 6.5 feet (2 meters).     Behavior: Pelicans are known for their unique feeding technique, where they plunge-dive into the water to scoop up fish with their pouches.  In the image, you can see:      A group of 6-7 Brown Pelicans.     A single bird in the foreground, slightly out of focus, showing a more detailed view of their feathers and feet.  Where they are: The presence of these birds suggests they are likely in a coastal or wetland environment – perhaps a bay, estuary, or near a large body of water.  Do you want me to delve deeper into any specific aspect of these birds, such as their habitat, diet, or conservation status? On the right is a Conversations sidebar with three other conversations listed.")](https://substackcdn.com/image/fetch/$s_!aSxC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdba53ea8-c8f0-4729-a81e-cb25783ca683_2030x1962.jpeg)

It miscounted the pelicans in [the group photo](https://static.simonwillison.net/static/2025/pelican-group.jpg), but again, this is a *tiny* 3\.2GB model.

With the server running on port 8080 you can also access the OpenAI\-compatible API endpoint. Here's how to do that using `curl`:

```
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Describe a pelicans ideal corporate retreat"}
    ]
  }' | jq
```

I built a new plugin for LLM just now called [llm\-llama\-server](https://github.com/simonw/llm-llama-server) to make interacting with this API more convenient. You can use that like this:

```
llm install llm-llama-server
llm -m llama-server 'invent a theme park ride for a pelican'
```

Or for vision models use `llama-server-vision`:

```
llm -m llama-server-vision 'describe this image' -a https://static.simonwillison.net/static/2025/pelican-group.jpg
```

The LLM plugin uses the streaming API, so responses will stream back to you as they are being generated.

[![Animated terminal session. $ llm -m llama-server 'invent a theme park ride for a pelican' Okay, this is a fun challenge! Let's design a theme park ride specifically for a pelican – a majestic, diving bird. Here’s my concept:  Ride Name: “Pelican’s Plunge”   Theme: Coastal Exploration & Underwater Discovery  Target Audience: Families with children (8+ recommended), animal lovers, and those who enjoy a mix of thrills and gentle exploration.  Ride Type: A partially submerged, rotating “pod” experience with a focus on simulated dives and underwater views.  Ride Mechanics:  1. The Pod: Guests ride in a large, semi-circular pod shaped like a stylized, open-mouthed pelican’s beak.  It’s made of reinforced, transparent acrylic and has comfortable seating inside. The pod can hold around 8-10 people.  2. The Launch: Guests board the pod and are positioned facing forward. The ride begins with a slow, gentle rise up a ramp, mimicking the pelican’s ascent from the water.   3. The "Dive" Sequence: This is the core of the ride.  The pod enters a large, darkened chamber that simulates the ocean floor.     * Rotating Simulation: The pod begins to rotate slowly, mimicking a pelican diving into the water.     * Water Effects:  The chamber is filled with realistic, moving water – created by a sophisticated system of pumps, jets, and screens. This creates the illusion of being surrounded by the ocean.    * Projection Mapping:  Powerful projection mapping is used on the walls and floor to create stunning underwater visuals: schools of fish, coral reefs, kelp forests, and even glimpses of marine life like sharks (safely projected, of course!).    * “Dive” Trigger:  At specific points in the rotation, the pod will perform a short, controlled “dive” – a sudden drop that creates a feeling of speed and the sensation of plunging into the water.  Sensors detect the speed of the rotation and trigger these dives.  4. Underwater Exploration: After the initial dive, the pod continues its rotation, offering increasingly detailed views of the projected underwater scenes.      * Interactive Elements (Optional):  Small, strategically placed screens could display sonar-like visuals, allowing guests to “scan” the environment and reveal hidden creatures or details.  5. The Ascent & Return: The ride gradually slows, bringing the pod back to the surface. As it rises, the projections shift to show a sunny coastline and seabirds flying overhead. The pod returns to the loading area.   Theming & Atmosphere:  * Sound Design: Immersive sound effects – waves crashing, seabirds calling, underwater ambience – are crucial. * Lighting: Dynamic lighting that shifts with the projections and the "dive" sequences. * Pelican Props:  Realistic pelican statues and props are integrated throughout the queue and surrounding area. * Educational Element: Small informational panels explain pelican behavior, conservation efforts, and the importance of marine ecosystems.  Why this works for a pelican:  * Mimics Natural Behavior: The ride accurately reflects a pelican’s primary activity – diving for fish. * Visually Engaging: The combination of water effects, projection mapping, and rotation creates a captivating and immersive experience. * Family-Friendly Thrill: The “dive” sequences provide a moderate thrill without being overly intense. * Educational Value: It promotes awareness and appreciation for these amazing birds and the marine environment.    ---  Further Development Ideas:  * Different "Dive Routes": Create multiple routes through the underwater environment, each with a different theme (e.g., a coral reef route, a deep-sea route, a pelican’s feeding ground route). * Animatronic Pelican: A large animatronic pelican could “greet” guests as they board the pod. * Smell Integration: Subtle scents of saltwater and seaweed could enhance the immersion.    Would you like me to brainstorm a specific element of the ride further, such as:  *   The projection mapping details? *   The technical aspects of the water effects? *   A unique interactive element? ](https://substackcdn.com/image/fetch/$s_!3Ew7!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2145248-1892-45b4-8c8c-fe3f3c0bf61e_824x412.gif "Animated terminal session. $ llm -m llama-server 'invent a theme park ride for a pelican' Okay, this is a fun challenge! Let's design a theme park ride specifically for a pelican – a majestic, diving bird. Here’s my concept:  Ride Name: “Pelican’s Plunge”   Theme: Coastal Exploration & Underwater Discovery  Target Audience: Families with children (8+ recommended), animal lovers, and those who enjoy a mix of thrills and gentle exploration.  Ride Type: A partially submerged, rotating “pod” experience with a focus on simulated dives and underwater views.  Ride Mechanics:  1. The Pod: Guests ride in a large, semi-circular pod shaped like a stylized, open-mouthed pelican’s beak.  It’s made of reinforced, transparent acrylic and has comfortable seating inside. The pod can hold around 8-10 people.  2. The Launch: Guests board the pod and are positioned facing forward. The ride begins with a slow, gentle rise up a ramp, mimicking the pelican’s ascent from the water.   3. The \"Dive\" Sequence: This is the core of the ride.  The pod enters a large, darkened chamber that simulates the ocean floor.     * Rotating Simulation: The pod begins to rotate slowly, mimicking a pelican diving into the water.     * Water Effects:  The chamber is filled with realistic, moving water – created by a sophisticated system of pumps, jets, and screens. This creates the illusion of being surrounded by the ocean.    * Projection Mapping:  Powerful projection mapping is used on the walls and floor to create stunning underwater visuals: schools of fish, coral reefs, kelp forests, and even glimpses of marine life like sharks (safely projected, of course!).    * “Dive” Trigger:  At specific points in the rotation, the pod will perform a short, controlled “dive” – a sudden drop that creates a feeling of speed and the sensation of plunging into the water.  Sensors detect the speed of the rotation and trigger these dives.  4. Underwater Exploration: After the initial dive, the pod continues its rotation, offering increasingly detailed views of the projected underwater scenes.      * Interactive Elements (Optional):  Small, strategically placed screens could display sonar-like visuals, allowing guests to “scan” the environment and reveal hidden creatures or details.  5. The Ascent & Return: The ride gradually slows, bringing the pod back to the surface. As it rises, the projections shift to show a sunny coastline and seabirds flying overhead. The pod returns to the loading area.   Theming & Atmosphere:  * Sound Design: Immersive sound effects – waves crashing, seabirds calling, underwater ambience – are crucial. * Lighting: Dynamic lighting that shifts with the projections and the \"dive\" sequences. * Pelican Props:  Realistic pelican statues and props are integrated throughout the queue and surrounding area. * Educational Element: Small informational panels explain pelican behavior, conservation efforts, and the importance of marine ecosystems.  Why this works for a pelican:  * Mimics Natural Behavior: The ride accurately reflects a pelican’s primary activity – diving for fish. * Visually Engaging: The combination of water effects, projection mapping, and rotation creates a captivating and immersive experience. * Family-Friendly Thrill: The “dive” sequences provide a moderate thrill without being overly intense. * Educational Value: It promotes awareness and appreciation for these amazing birds and the marine environment.    ---  Further Development Ideas:  * Different \"Dive Routes\": Create multiple routes through the underwater environment, each with a different theme (e.g., a coral reef route, a deep-sea route, a pelican’s feeding ground route). * Animatronic Pelican: A large animatronic pelican could “greet” guests as they board the pod. * Smell Integration: Subtle scents of saltwater and seaweed could enhance the immersion.    Would you like me to brainstorm a specific element of the ride further, such as:  *   The projection mapping details? *   The technical aspects of the water effects? *   A unique interactive element? ")](https://substackcdn.com/image/fetch/$s_!3Ew7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2145248-1892-45b4-8c8c-fe3f3c0bf61e_824x412.gif)

---

**Link** 2025\-05\-07 [astral\-sh/ty](https://github.com/astral-sh/ty):

Astral have been working on this "extremely fast Python type checker and language server, written in Rust" [quietly but in\-the\-open](https://simonwillison.net/2025/Jan/29/charlie-marsh/) for a while now. Here's the first alpha public release \- albeit [not yet announced](https://news.ycombinator.com/item?id=43918484#43919354) \- as [ty](https://pypi.org/project/ty/) on PyPI (nice [donated](https://news.ycombinator.com/item?id=43918484#43920112) two\-letter name!)

You can try it out via [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) like this \- run the command in a folder full of Python code and see what comes back:

```
uvx ty check
```

I got zero errors for my recent, simple [condense\-json](https://github.com/simonw/condense-json) library and a *ton* of errors for my more mature [sqlite\-utils](https://sqlite-utils.datasette.io/) library \- [output here](https://gist.github.com/simonw/a13e1720b03e23783ae668eca7f6f12a).

It really is *fast*:

```
cd /tmp
git clone https://github.com/simonw/sqlite-utils
cd sqlite-utils
time uvx ty check
```

Reports it running in around a tenth of a second (0\.109 total wall time) using multiple CPU cores:

```
uvx ty check  0.18s user 0.07s system 228% cpu 0.109 total
```

Running `time uvx mypy .` in the same folder (both after first ensuring the underlying tools had been cached) took around 7x longer:

```
uvx mypy .  0.46s user 0.09s system 74% cpu 0.740 total
```

This isn't a fair comparison yet as ty still isn't feature complete in comparison to mypy.

---

**Link** 2025\-05\-07 [llm\-prices.com](https://www.llm-prices.com/):

I've been maintaining a simple LLM pricing calculator since [October last year](https://github.com/simonw/tools/commits/main/llm-prices.html). I finally decided to split it out to its own domain name (previously it was hosted at `tools.simonwillison.net/llm-prices`), running on Cloudflare Pages.

[![Screenshot of the llm-prices.com site - on the left is a calculator interface for entering number of input tokens, output tokens and price per million of each. On the right is a table of models and their prices, sorted cheapest first.](https://substackcdn.com/image/fetch/$s_!SDkw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F264e8202-ab06-4238-af33-afd8828e6cd6_1028x594.jpeg "Screenshot of the llm-prices.com site - on the left is a calculator interface for entering number of input tokens, output tokens and price per million of each. On the right is a table of models and their prices, sorted cheapest first.")](https://substackcdn.com/image/fetch/$s_!SDkw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F264e8202-ab06-4238-af33-afd8828e6cd6_1028x594.jpeg)

The site runs out of my [simonw/llm\-prices](https://github.com/simonw/llm-prices) GitHub repository. I ported [the history](https://github.com/simonw/llm-prices/commits/b45e8f9c718c4ad3ab50b906a2c3882cbcffcb5b/index.html) of the old `llm-prices.html` file using a vibe\-coded bash script that I forgot to save anywhere.

I rarely use AI\-generated imagery in my own projects, but for this one I found an excellent reason to use GPT\-4o image outputs... to generate the favicon! I dropped a screenshot of the site into ChatGPT (o4\-mini\-high in this case) and asked for the following:

> design a bunch of options for favicons for this site in a single image, white background

[![A 3x3 grid of simple icon concepts: green coins/circles, a green price tag with dollar sign, a calculator with dollar sign, a calculator with plus sign, a blue chat bubble with three dots, a green brain icon, the letters "AI" in dark gray, a document with finger pointing at it, and green horizontal bars of decreasing size.](https://substackcdn.com/image/fetch/$s_!dsyw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cff4789-126a-40ff-b2be-6e9d6e8ff3ac_1024x1024.jpeg "A 3x3 grid of simple icon concepts: green coins/circles, a green price tag with dollar sign, a calculator with dollar sign, a calculator with plus sign, a blue chat bubble with three dots, a green brain icon, the letters \"AI\" in dark gray, a document with finger pointing at it, and green horizontal bars of decreasing size.")](https://substackcdn.com/image/fetch/$s_!dsyw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cff4789-126a-40ff-b2be-6e9d6e8ff3ac_1024x1024.jpeg)

I liked the top right one, so I cropped it into Pixelmator and made a 32x32 version. Here's what it looks like in my browser:

[![A cropped web browser showing the chosen favicon - it's a calculator with a dollar sign overlapping some of the keys.](https://substackcdn.com/image/fetch/$s_!u-qb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F263df0fe-aa35-4547-847b-06fab6c4b99a_1038x496.png "A cropped web browser showing the chosen favicon - it's a calculator with a dollar sign overlapping some of the keys.")](https://substackcdn.com/image/fetch/$s_!u-qb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F263df0fe-aa35-4547-847b-06fab6c4b99a_1038x496.png)

I added a new feature just now: the state of the calculator is now reflected in the `#fragment-hash` URL of the page, which means you can link to your previous calculations.

I implemented that feature using [the new gemini\-2\.5\-pro\-preview\-05\-06](https://simonwillison.net/2025/May/6/gemini-25-pro-preview/), since that model boasts improved front\-end coding abilities. It did a pretty great job \- here's how I prompted it:

```
llm -m gemini-2.5-pro-preview-05-06 -f https://www.llm-prices.com/ -s 'modify this code so that the state of the page is reflected in the fragmenth hash URL - I want to capture the values filling out the form fields and also the current sort order of the table. These should be respected when the page first loads too. Update them using replaceHistory, no need to enable the back button.'
```

Here's [the transcript](https://gist.github.com/simonw/9d4e15b58ccfaca9e08747225cb69fa2) and [the commit updating the tool](https://github.com/simonw/llm-prices/commit/c9eee704d070d119e6c342d9a7ab6c41d09550dd), plus [an example link](https://www.llm-prices.com/#it=5883&ot=16087&ic=1.25&oc=10&sb=input&sd=descending) showing the new feature in action (and calculating the cost for that Gemini 2\.5 Pro prompt at 16\.8224 cents, after [fixing the calculation](https://simonwillison.net/2025/May/8/llm-gemini-0191/).)

---

**Link** 2025\-05\-07 [Medium is the new large](https://mistral.ai/news/mistral-medium-3):

New model release from Mistral \- this time closed source/proprietary. Mistral Medium claims strong benchmark scores similar to GPT\-4o and Claude 3\.7 Sonnet, but is priced at $0\.40/million input and $2/million output \- about the same price as GPT 4\.1 Mini. [For comparison](https://www.llm-prices.com/), GPT\-4o is $2\.50/$10 and Claude 3\.7 Sonnet is $3/$15\.

The model is a vision LLM, accepting both images and text.

More interesting than the price is the deployment model. Mistral Medium may not be open weights but it is very much available for self\-hosting:

> Mistral Medium 3 can also be deployed on any cloud, including self\-hosted environments of four GPUs and above.

Mistral's other announcement today is [Le Chat Enterprise](https://mistral.ai/news/le-chat-enterprise). This is a suite of tools that can integrate with your company's internal data and provide "agents" (these look similar to Claude Projects or OpenAI GPTs), again with the option to self\-host.

Is there a new open weights model coming soon? This note tucked away at the bottom of the Mistral Medium 3 announcement seems to hint at that:

> With the launches of [Mistral Small](https://mistral.ai/news/mistral-small-3-1) in March and Mistral Medium today, it's no secret that we're working on something 'large' over the next few weeks. With even our medium\-sized model being resoundingly better than flagship open source models such as Llama 4 Maverick, we're excited to 'open' up what's to come :)

I released [llm\-mistral 0\.12](https://github.com/simonw/llm-mistral/releases/tag/0.12) adding support for the new model.

---

**Link** 2025\-05\-07 [Create and edit images with Gemini 2\.0 in preview](https://developers.googleblog.com/en/generate-images-gemini-2-0-flash-preview/):

Gemini 2\.0 Flash has had image generation capabilities for a while now, and they're now available via the paid Gemini API \- at 3\.9 cents per generated image.

According to [the API documentation](https://ai.google.dev/gemini-api/docs/image-generation) you need to use the new `gemini-2.0-flash-preview-image-generation` model ID and specify `{"responseModalities":["TEXT","IMAGE"]}` as part of your request.

Here's an example that calls the API using `curl` (and fetches a Gemini key from the `llm keys get` store):

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-preview-image-generation:generateContent?key=$(llm keys get gemini)" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Photo of a raccoon in a trash can with a paw-written sign that says I love trash"}
      ]
    }],
    "generationConfig":{"responseModalities":["TEXT","IMAGE"]}
  }' > /tmp/raccoon.json
```

Here's [the response](https://gist.github.com/simonw/d96f4adb9cd0933e17fb5771b43d681a). I got Gemini 2\.5 Pro [to vibe\-code me](https://gist.github.com/simonw/6363ace77bbac08c6ad05857b3bd9ad2) a new [debug tool](https://tools.simonwillison.net/gemini-image-json) for visualizing that JSON. If you visit that tool and click the "Load an example" link you'll see the result of the raccoon image visualized:

[![Render JSON from Gemini Image Generation tool. Paste Gemini JSON here: a bunch of JSON with a base64 encoded PNG. Then buttons to Load an example, or a really big (40MB) example or Render JSON. The Rendered Content shows a photograph of a raccoon in an open top bin holding a sign that says I heart trash.](https://substackcdn.com/image/fetch/$s_!xrKZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14b094d5-2bcb-4d7c-9f43-38e27fee9a8c_1388x2628.jpeg "Render JSON from Gemini Image Generation tool. Paste Gemini JSON here: a bunch of JSON with a base64 encoded PNG. Then buttons to Load an example, or a really big (40MB) example or Render JSON. The Rendered Content shows a photograph of a raccoon in an open top bin holding a sign that says I heart trash.")](https://substackcdn.com/image/fetch/$s_!xrKZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14b094d5-2bcb-4d7c-9f43-38e27fee9a8c_1388x2628.jpeg)

The other prompt I tried was this one:

> Provide a vegetarian recipe for butter chicken but with chickpeas not chicken and include many inline illustrations along the way

The result of that one was a [41MB JSON file](https://gist.github.com/simonw/55894032b2c60b35f320b6a166ded493)(!) containing 28 images \- which presumably cost over a dollar since images are 3\.9 cents each.

Some of the illustrations it chose for that one were somewhat unexpected:

[![Text reads: "* ½ teaspoon Kashmiri chili powder (or paprika for milder flavor)" followed by a group photo of people in formal attire with black suits and light blue ties standing in rows outdoors, then "* ½ cup heavy cream (or coconut cream for vegan option)" followed by a close-up image of dried cumin seeds or similar brown spice.](https://substackcdn.com/image/fetch/$s_!Rr2C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5548d941-082f-40b8-8d1a-818d3176e5de_1396x1646.jpeg "Text reads: \"* ½ teaspoon Kashmiri chili powder (or paprika for milder flavor)\" followed by a group photo of people in formal attire with black suits and light blue ties standing in rows outdoors, then \"* ½ cup heavy cream (or coconut cream for vegan option)\" followed by a close-up image of dried cumin seeds or similar brown spice.")](https://substackcdn.com/image/fetch/$s_!Rr2C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5548d941-082f-40b8-8d1a-818d3176e5de_1396x1646.jpeg)

If you want to see that one you can click the "Load a really big example" link in [the debug tool](https://tools.simonwillison.net/gemini-image-json), then wait for your browser to fetch and render the full 41MB JSON file.

The most interesting feature of Gemini (as with GPT\-4o images) is the ability to accept images as inputs. I tried that out with [this pelican photo](https://static.simonwillison.net/static/2025/pelican-no-hat.jpg) like this:

```
cat > /tmp/request.json << EOF
{
  "contents": [{
    "parts":[
      {"text": "Modify this photo to add an inappropriate hat"},
      {
        "inline_data": {
          "mime_type":"image/jpeg",
          "data": "$(base64 -i pelican.jpg)"
        }
      }
    ]
  }],
  "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
}
EOF

# Execute the curl command with the JSON file
curl -X POST \
  'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-preview-image-generation:generateContent?key='$(llm keys get gemini) \
  -H 'Content-Type: application/json' \
  -d @/tmp/request.json \
  > /tmp/out.json
```

And now the pelican is wearing a hat:

[![A pelican with its wings outstretched wearing an inappropriate pink bowler hat. The hat looks a little bit pasted on. ](https://substackcdn.com/image/fetch/$s_!1m9M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fa80459-5832-45bd-8753-88a258fddcf4_1024x680.jpeg "A pelican with its wings outstretched wearing an inappropriate pink bowler hat. The hat looks a little bit pasted on. ")](https://substackcdn.com/image/fetch/$s_!1m9M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fa80459-5832-45bd-8753-88a258fddcf4_1024x680.jpeg)

---

**Link** 2025\-05\-07 [Introducing web search on the Anthropic API](https://www.anthropic.com/news/web-search-api):

Anthropic's [web search](https://simonwillison.net/2025/Mar/20/claude-can-now-search-the-web/) (presumably still [powered by Brave](https://simonwillison.net/2025/Mar/21/anthropic-use-brave/)) is now also available through their API, in the shape of a new [web search tool](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool) called `web_search_20250305`.

You can specify a maximum number of uses per prompt and you can also pass a list of disallowed or allowed domains, plus hints as to the user's current location.

Search results are returned in a format that looks similar to the [Anthropic Citations API](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/).

It's charged at $10 per 1,000 searches, which is a little more expensive than what the [Brave Search API](https://brave.com/search/api/) charges ($3 or $5 or $9 per thousand depending on how you're using them).

I couldn't find any details of additional rules surrounding storage or display of search results, which surprised me because both [Google Gemini](https://ai.google.dev/gemini-api/docs/grounding/search-suggestions#requirements) and [OpenAI](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat#output-and-citations) have these for their own API search results.

---

**Link** 2025\-05\-08 [llm\-gemini 0\.19\.1](https://github.com/simonw/llm-gemini/releases/tag/0.19.1):

Bugfix release for my [llm\-gemini](https://github.com/simonw/llm-gemini) plugin, which was recording the number of output tokens (needed to calculate the price of a response) incorrectly for the Gemini "thinking" models. Those models turn out to return `candidatesTokenCount` and `thoughtsTokenCount` as two separate values which need to be added together to get the total billed output token count. Full details in [this issue](https://github.com/simonw/llm-gemini/issues/75).

I spotted this potential bug in [this response log](https://gist.github.com/simonw/87a59e7f5c12274d65e2ac053b0eacdb#token-usage) this morning, and my concerns were confirmed when Paul Gauthier wrote about a similar fix in Aider in [Gemini 2\.5 Pro Preview 03\-25 benchmark cost](https://aider.chat/2025/05/07/gemini-cost.html), where he noted that the $6\.32 cost recorded to benchmark Gemini 2\.5 Pro Preview 03\-25 was incorrect. Since that model is no longer available (despite [the date\-based model alias persisting](https://simonwillison.net/2025/May/6/gemini-25-pro-preview/)) Paul is not able to accurately calculate the new cost, but it's likely a lot more since the Gemini 2\.5 Pro Preview 05\-06 benchmark cost $37\.

I've gone through my [gemini tag](https://observablehq.com/@simonw/blog-to-newsletter) and attempted to update my previous posts with new calculations \- this mostly involved increases in the order of 12\.336 cents to 16\.316 cents ([as seen here](https://simonwillison.net/2025/May/6/gemini-25-pro-preview/)).

---

**Quote** 2025\-05\-08

> *But I’ve also had my own quiet concerns about what \[vibe coding] means for early\-career developers. So much of how I learned came from chasing bugs in broken tutorials and seeing how all the pieces connected, or didn’t. There was value in that. And maybe I’ve been a little protective of it.   
>   
> A mentor challenged that. He pointed out that debugging AI generated code is a lot like onboarding into a legacy codebase, making sense of decisions you didn’t make, finding where things break, and learning to trust (or rewrite) what’s already there. That’s the kind of work a lot of developers end up doing anyway.*

[Ashley Willis](https://ashley.dev/posts/what-even-is-vibe-coding/)

---

**Quote** 2025\-05\-08

> *Microservices only pay off when you have real scaling bottlenecks, large teams, or independently evolving domains. Before that? You’re paying the price without getting the benefit: duplicated infra, fragile local setups, and slow iteration.*

[Oleg Pustovit](https://nexo.sh/posts/microservices-for-startups/)

---

**Link** 2025\-05\-08 [Reservoir Sampling](https://samwho.dev/reservoir-sampling/):

Yet another outstanding interactive essay by Sam Rose ([previously](https://simonwillison.net/tags/sam-rose/)), this time explaining how reservoir sampling can be used to select a "fair" random sample when you don't know how many options there are and don't want to accumulate them before making a selection.

> Reservoir sampling is one of my favourite algorithms, and I've been wanting to write about it for years now. It allows you to solve a problem that at first seems impossible, in a way that is both elegant and efficient.

I appreciate that Sam starts the article with "No math notation, I promise." Lots of delightful widgets to interact with here, all of which help build an intuitive understanding of the underlying algorithm.

[![Animated demo. As a slider moves from left to right the probability of cards drawn from a deck is simulated. Text at the bottom reads Anything older than 15 cards ago is has a less than 0.01% chance of being held when I stop.](https://substackcdn.com/image/fetch/$s_!RI6h!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5db3ad92-4b9f-41e9-98a3-3a7f032c254e_506x463.gif "Animated demo. As a slider moves from left to right the probability of cards drawn from a deck is simulated. Text at the bottom reads Anything older than 15 cards ago is has a less than 0.01% chance of being held when I stop.")](https://substackcdn.com/image/fetch/$s_!RI6h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5db3ad92-4b9f-41e9-98a3-3a7f032c254e_506x463.gif)

Sam shows how this algorithm can be applied to the real\-world problem of sampling log files when incoming logs threaten to overwhelm a log aggregator.

The dog illustration is [commissioned art](https://samwho.dev/dogs/) and the MIT\-licensed code is [available on GitHub](https://github.com/samwho/visualisations/tree/main/reservoir-sampling).

---

**Quote** 2025\-05\-08

> `If Claude is asked to count words, letters, and characters, it thinks step by step before answering the person. It explicitly counts the words, letters, or characters by assigning a number to each. It only answers the person once it has performed this explicit counting step. [...]``If Claude is shown a classic puzzle, before proceeding, it quotes every constraint or premise from the person’s message word for word before inside quotation marks to confirm it’s not dealing with a new variant. [...]``If asked to write poetry, Claude avoids using hackneyed imagery or metaphors or predictable rhyming schemes.`

[Claude's system prompt](https://www.dbreunig.com/2025/05/07/claude-s-system-prompt-chatbots-are-more-than-just-models.html)

---

**Link** 2025\-05\-08 [SQLite CREATE TABLE: The DEFAULT clause](https://www.sqlite.org/lang_createtable.html#the_default_clause):

If your SQLite create table statement includes a line like this:

```
CREATE TABLE alerts (
    -- ...
    alert_created_at text default current_timestamp
)
```

`current_timestamp` will be replaced with a UTC timestamp in the format `2025-05-08 22:19:33`. You can also use `current_time` for `HH:MM:SS` and `current_date` for `YYYY-MM-DD`, again using UTC.

Posting this here because I hadn't previously noticed that this defaults to UTC, which is a useful detail. It's also a strong vote in favor of `YYYY-MM-DD HH:MM:SS` as a string format for use with SQLite, which [doesn't otherwise provide](https://www.sqlite.org/lang_datefunc.html) a formal datetime type.

---

**Link** 2025\-05\-09 [Gemini 2\.5 Models now support implicit caching](https://developers.googleblog.com/en/gemini-2-5-models-now-support-implicit-caching/):

I just spotted a `cacheTokensDetails` key in the token usage JSON while running a [long chain of prompts](https://gist.github.com/simonw/1383565aac316d68cc29f289e33b2e51) against Gemini 2\.5 Flash \- despite not configuring caching myself:

`{"cachedContentTokenCount": 200658, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 204082}], "cacheTokensDetails": [{"modality": "TEXT", "tokenCount": 200658}], "thoughtsTokenCount": 2326}`

I went searching and it turns out Gemini had a massive upgrade to their prompt caching earlier today:

> Implicit caching directly passes cache cost savings to developers without the need to create an explicit cache. Now, when you send a request to one of the Gemini 2\.5 models, if the request shares a common prefix as one of previous requests, then it’s eligible for a cache hit. We will dynamically pass cost savings back to you, providing the same 75% token discount. \[...]
> 
> To make more requests eligible for cache hits, we reduced the minimum request size for 2\.5 Flash to 1024 tokens and 2\.5 Pro to 2048 tokens.

Previously you needed to both explicitly configure the cache *and* pay a per\-hour charge to keep that cache warm.

This new mechanism is so much more convenient! It imitates how both [DeepSeek](https://simonwillison.net/2024/Aug/14/deepseek-context-caching/) and [OpenAI](https://simonwillison.net/2024/Oct/2/not-digital-god/#prompt-caching-aka-the-big-price-drop) implement prompt caching, leaving Anthropic as the remaining large provider who require you to [manually configure prompt caching](https://simonwillison.net/2024/Aug/14/prompt-caching-with-claude/) to get it to work.

Gemini's explicit caching mechanism is still available. [The documentation](https://ai.google.dev/gemini-api/docs/caching) says:

> Explicit caching is useful in cases where you want to guarantee cost savings, but with some added developer work.

With implicit caching the cost savings aren't possible to predict in advance, especially since the cache timeout within which a prefix will be discounted isn't described and presumably varies based on load and other circumstances outside of the developer's control.

**Update**: DeepMind's [Philipp Schmid](https://twitter.com/_philschmid/status/1920772470543397281):

> There is no fixed time, but it's should be a few minutes.

---

**Link** 2025\-05\-09 [sqlite\-utils 4\.0a0](https://github.com/simonw/sqlite-utils/releases/tag/4.0a0):

New alpha release of [sqlite\-utils](https://sqlite-utils.datasette.io/), my Python library and CLI tool for manipulating SQLite databases.

It's the first 4\.0 alpha because there's a (minor) backwards\-incompatible change: I've upgraded the `.upsert()` and `.upsert_all()` methods to use SQLIte's [UPSERT](https://www.sqlite.org/lang_upsert.html) mechanism, `INSERT INTO ... ON CONFLICT DO UPDATE`. Details in [this issue](https://github.com/simonw/sqlite-utils/issues/652).

That feature was added to SQLite in version 3\.24\.0, released 2018\-06\-04\. I'm pretty cautious about my SQLite version support since the underlying library can be difficult to upgrade, depending on your platform and operating system.

I'm going to leave the new alpha to bake for a little while before pushing a stable release. Since this is a major version bump I'm going to [take the opportunity](https://github.com/simonw/sqlite-utils/issues/656) to see if there are any other minor API warts that I can clean up at the same time.

---

**Note** [2025\-05\-09](https://simonwillison.net/2025/May/9/private-issues/)

I had some notes in a GitHub issue thread in a private repository that I wanted to export as Markdown. I realized that I could get them using a combination of several recent projects.

Here's what I ran:

```
export GITHUB_TOKEN="$(llm keys get github)"                                             
llm -f issue:https://github.com/simonw/todos/issues/170 \
  -m echo --no-log | jq .prompt -r > notes.md
```

I have a GitHub personal access token stored in my LLM keys, for use with Anthony Shaw's [llm\-github\-models](https://github.com/tonybaloney/llm-github-models) plugin.

My own [llm\-fragments\-github](https://github.com/simonw/llm-fragments-github) plugin expects an optional `GITHUB_TOKEN` environment variable, so I set that first \- here's [an issue](https://github.com/simonw/llm-fragments-github/issues/11) to have it use the `github` key instead.

With that set, the `issue:` fragment loader can take a URL to a private GitHub issue thread and load it via the API using the token, then concatenate the comments together as Markdown. Here's [the code for that](https://github.com/simonw/llm-fragments-github/blob/87555488805ffc973b5fb45aa51eac83be2c839f/llm_fragments_github.py#L92-L126).

Fragments are meant to be used as input to LLMs. I built a [llm\-echo](https://github.com/simonw/llm-echo) plugin recently which adds a fake LLM called "echo" which simply echos its input back out again.

Adding `--no-log` prevents that junk data from being stored in my [LLM log database](https://llm.datasette.io/en/stable/logging.html).

The output is JSON with a `"prompt"` key for the original prompt. I use `jq .prompt` to extract that out, then `-r` to get it as raw text (not a `"JSON string"`).

... and I write the result to `notes.md`.

---

**Link** 2025\-05\-10 [TIL: SQLite triggers](https://til.simonwillison.net/sqlite/sqlite-triggers):

I've been doing some work with SQLite triggers recently while working on [sqlite\-chronicle](https://github.com/simonw/sqlite-chronicle), and I decided I needed a single reference to exactly which triggers are executed for which SQLite actions and what data is available within those triggers.

I wrote this [triggers.py](https://github.com/simonw/til/blob/main/sqlite/triggers.py) script to output as much information about triggers as possible, then wired it into a TIL article using [Cog](https://cog.readthedocs.io/). The Cog\-powered source code for the TIL article [can be seen here](https://github.com/simonw/til/blob/main/sqlite/sqlite-triggers.md?plain=1).

---

**Note** [2025\-05\-10](https://simonwillison.net/2025/May/10/poker-face/) Poker Face season two just started on Peacock (the US streaming service). It's my favorite thing on TV right now. I've started threads on MetaFilter FanFare for episodes [one](https://fanfare.metafilter.com/26073/Poker-Face-The-Game-Is-a-Foot), [two](https://fanfare.metafilter.com/26075/Poker-Face-Last-Looks) and [three](https://fanfare.metafilter.com/26077/Poker-Face-Whack-a-Mole).

---

**Note** [2025\-05\-11](https://simonwillison.net/2025/May/11/tap-dancer/) Achievement unlocked: tap danced in the local community college dance recital.

---