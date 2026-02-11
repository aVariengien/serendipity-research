# Qwen2.5-Coder-32B is an LLM that can code well that runs on my Mac

*Plus Visualizing local election results with Datasette, Observable and MapLibre GL*

Published: 2024-11-13
Source: https://simonw.substack.com/p/qwen25-coder-32b-is-an-llm-that-can

---

In this newsletter:

* Qwen2\.5\-Coder\-32B is an LLM that can code well that runs on my Mac
* Visualizing local election results with Datasette, Observable and MapLibre GL

Plus 9 links and 4 quotations

### **[Qwen2\.5\-Coder\-32B is an LLM that can code well that runs on my Mac](https://simonwillison.net/2024/Nov/12/qwen25-coder/) \- 2024\-11\-12**

There's a whole lot of buzz around the new [Qwen2\.5\-Coder Series](https://qwenlm.github.io/blog/qwen2.5-coder-family/) of open source (Apache 2\.0 licensed) LLM releases from Alibaba's Qwen research team. On first impression it looks like the buzz is well deserved.

Qwen claim:

> Qwen2\.5\-Coder\-32B\-Instruct has become the current SOTA open\-source code model, matching the coding capabilities of GPT\-4o.

That's a *big* claim for a 32B model that's small enough that it can run on my 64GB MacBook Pro M2\. The Qwen published scores look impressive, comparing favorably with GPT\-4o and Claude 3\.5 Sonnet (October 2024\) edition across various code\-related benchmarks:

[![In benchmark comparisons, Qwen 2.5 Coder (32B Instruct) outperforms both GPT-4o and Claude 3.5 Sonnet on LiveCodeBench, Spider, and BIRD-SQL metrics, falls behind on MBPP, Aider, and CodeArena, shows mixed results on MultiPL-E, and performs similarly on HumanEval and McEval benchmarks.](https://substackcdn.com/image/fetch/$s_!kRvZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77dc548c-3952-457a-8668-3546ab6a2922_1688x842.jpeg "In benchmark comparisons, Qwen 2.5 Coder (32B Instruct) outperforms both GPT-4o and Claude 3.5 Sonnet on LiveCodeBench, Spider, and BIRD-SQL metrics, falls behind on MBPP, Aider, and CodeArena, shows mixed results on MultiPL-E, and performs similarly on HumanEval and McEval benchmarks.")](https://substackcdn.com/image/fetch/$s_!kRvZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77dc548c-3952-457a-8668-3546ab6a2922_1688x842.jpeg)

How about benchmarks from other researchers? Paul Gauthier's [Aider benchmarks](https://aider.chat/docs/leaderboards/) have a great reputation and [Paul reports](https://twitter.com/paulgauthier/status/1856018124031832236):

> The new Qwen 2\.5 Coder models did very well on aider's code editing benchmark. The 32B Instruct model scored in between GPT\-4o and 3\.5 Haiku.
> 
> 84% 3\.5 Sonnet, 75% 3\.5 Haiku, 74% Qwen2\.5 Coder 32B, 71% GPT\-4o, 69% Qwen2\.5 Coder 14B, 58% Qwen2\.5 Coder 7B
> 
> [![Those numbers as a chart](https://substackcdn.com/image/fetch/$s_!iuvw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbf05420-b5b3-4683-bc9b-76ab414d390c_1818x1088.jpeg "Those numbers as a chart")](https://substackcdn.com/image/fetch/$s_!iuvw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbf05420-b5b3-4683-bc9b-76ab414d390c_1818x1088.jpeg)

That was for the Aider "whole edit" benchmark. The "diff" benchmark [scores well](https://twitter.com/paulgauthier/status/1856042640279777420) too, with Qwen2\.5 Coder 32B tying with GPT\-4o (but a little behind Claude 3\.5 Haiku).

Given these scores (and the [positive buzz on Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1gp84in/qwen25coder_32b_the_ai_thats_revolutionizing/)) I had to try it for myself.

My attempts to run the [Qwen/Qwen2\.5\-Coder\-32B\-Instruct\-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-GGUF) Q8 using [llm\-gguf](https://github.com/simonw/llm-gguf) were a bit too slow, because I don't have that compiled to use my Mac's GPU at the moment.

But both the [Ollama](https://ollama.com/) version *and* the [MLX](https://github.com/ml-explore/mlx) version worked great!

I installed the Ollama version using:

```
ollama pull qwen2.5-coder:32b

```

That fetched a 20GB quantized file. I ran a prompt through that using my [LLM](https://llm.datasette.io/) tool and Sergey Alexandrov's [llm\-ollama](https://github.com/taketwo/llm-ollama) plugin like this:

```
llm install llm-ollama
llm models # Confirming the new model is present
llm -m qwen2.5-coder:32b 'python function that takes URL to a CSV file and path to a SQLite database, fetches the CSV with the standard library, creates a table with the right columns and inserts the data'

```

Here's [the result](https://gist.github.com/simonw/0a47f9e35a50d4e25a47826f4ab75dda). The code worked, but I had to work around a frustrating `ssl` bug first (which wouldn't have been an issue if I'd allowed the model to use `requests` or `httpx` instead of the standard library).

I also tried running it using the Apple Silicon fast array framework MLX using the [mlx\-llm](https://github.com/riccardomusmeci/mlx-llm) library directly, run via [uv](https://github.com/astral-sh/uv) like this:

```
uv run --with mlx-lm \
  mlx_lm.generate \
  --model mlx-community/Qwen2.5-Coder-32B-Instruct-8bit \
  --max-tokens 4000 \
  --prompt 'write me a python function that renders a mandelbrot fractal as wide as the current terminal'

```

That gave me a *very* [satisfying result](https://gist.github.com/simonw/1cc1e0418a04dbd19cd281cf9b43666f) \- when I ran the code it generated in a terminal I got this:

[![macOS terminal window displaying a pleasing mandelbrot fractal as ASCII art](https://substackcdn.com/image/fetch/$s_!e1yt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb3c1ad-f67d-47f9-b61e-80fa7570b348_925x721.jpeg "macOS terminal window displaying a pleasing mandelbrot fractal as ASCII art")](https://substackcdn.com/image/fetch/$s_!e1yt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb3c1ad-f67d-47f9-b61e-80fa7570b348_925x721.jpeg)

MLX reported the following performance metrics:

```
Prompt: 49 tokens, 95.691 tokens-per-sec
Generation: 723 tokens, 10.016 tokens-per-sec
Peak memory: 32.685 GB
```

Let's see how it does on the [Pelican on a bicycle benchmark](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/).

```
llm -m qwen2.5-coder:32b 'Generate an SVG of a pelican riding a bicycle'
```

Here's [what I got](https://gist.github.com/simonw/56217af454695a90be2c8e09c703198a):

[![A jumble of shapes. The pelican has a yellow body, a black head and a weird proboscis kind of thing. The bicycle is several brown overlapping shapes that looks a bit like a tractor.](https://substackcdn.com/image/fetch/$s_!YMil!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc37bec86-d79d-4f41-8e5d-4ba117c8ea15_200x150.svg "A jumble of shapes. The pelican has a yellow body, a black head and a weird proboscis kind of thing. The bicycle is several brown overlapping shapes that looks a bit like a tractor.")](https://substackcdn.com/image/fetch/$s_!YMil!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc37bec86-d79d-4f41-8e5d-4ba117c8ea15_200x150.svg)

Questionable Pelican SVG drawings aside, this is a really promising development. 32GB is just small enough that I can run the model on my Mac without having to quit every other application I'm running, and both the speed and the quality of the results feel genuinely competitive with the current best of the hosted models.

Given that code assistance is probably around 80% of my LLM usage at the moment this is a meaningfully useful release for how I engage with this class of technology.

---

### **[Visualizing local election results with Datasette, Observable and MapLibre GL](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/) \- 2024\-11\-09**

Alex Garcia and myself hosted the first [Datasette Open Office Hours](https://simonwillison.net/2024/Nov/7/datasette-public-office-hours/) on Friday \- a live\-streamed video session where we hacked on a project together and took questions and tips from community members on Discord.

We didn't record this one (surprisingly not a feature that Discord offers) but we hope to do more of these and record them in the future.

This post is a detailed write\-up of what we built during the session.

* [San Mateo County election results](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#san-mateo-county-election-results)
* [Importing CSV data into Datasette](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#importing-csv-data-into-datasette)
* [Modifying the schema](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#modifying-the-schema)
* [Faceting and filtering the table](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#faceting-and-filtering-the-table)
* [Importing geospatial precinct shapes](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#importing-geospatial-precinct-shapes)
* [Enriching that data to extract the precinct IDs](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#enriching-that-data-to-extract-the-precinct-ids)
* [Running a join](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#running-a-join)
* [Creating an API token to access the data](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#creating-an-api-token-to-access-the-data)
* [Getting CORS working](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#getting-cors-working)
* [Working with Datasette in Observable](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#working-with-datasette-in-observable)
* [Visualizing those with MapLibre GL](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#visualizing-those-with-maplibre-gl)
* [Observable Plot](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#observable-plot)
* [Bringing it all together](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#bringing-it-all-together)
* [We'll be doing this again](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/#we-ll-be-doing-this-again)

#### **San Mateo County election results**

I live in El Granada, a tiny town just north of Half Moon Bay in San Mateo County, California.

Every county appears to handle counting and publishing election results differently. For San Mateo County the results are published [on this page](https://smcacre.gov/elections/november-5-2024-election-results), and detailed per\-precinct and per\-candidate breakdowns are made available as a CSV file.

(I optimistically set up a [Git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) for these results in [simonw/scrape\-san\-mateo\-county\-election\-results\-2024](https://github.com/simonw/scrape-san-mateo-county-election-results-2024) only to learn that the CSV is updated just once a day, not continually as the ballots are counted.)

I'm particularly invested in the results of the [Granada Community Services District](http://granada.ca.gov/) board member elections. Our little town of El Granada is in "unincorporated San Mateo County" which means we don't have a mayor or any local officials, so the closest we get to hyper\-local government is the officials that run our local sewage and parks organization! My partner Natalie ran [the candidate forum event](https://til.simonwillison.net/youtube/livestreaming) (effectively the debate) featuring three of the four candidates running for the two open places on the board.

Let's explore the data for that race using Datasette.

#### **Importing CSV data into Datasette**

I ran my part of the demo using [Datasette Cloud](https://www.datasette.cloud/), the beta of my new hosted Datasette service.

I started by using the pre\-configured [datasette\-import](https://github.com/datasette/datasette-import) plugin to import the data from the CSV file into a fresh table:

[![Paste data to create a table - I drag and drop on a CSV file, which produces a preview of the first 100 of 15,589 rows. I click to Upload and a progress bar runs before redirecting me to the resulting table.](https://substackcdn.com/image/fetch/$s_!qIyG!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F954e119b-3912-47ed-813e-e79d9b8ef025_761x779.gif "Paste data to create a table - I drag and drop on a CSV file, which produces a preview of the first 100 of 15,589 rows. I click to Upload and a progress bar runs before redirecting me to the resulting table.")](https://substackcdn.com/image/fetch/$s_!qIyG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F954e119b-3912-47ed-813e-e79d9b8ef025_761x779.gif)

#### **Modifying the schema**

The table imported cleanly, but all of the columns from the CSV were still being treated as text. I used the [datasette\-edit\-schema](https://observablehq.com/@simonw/blog-to-newsletter) plugin to switch the relevant columns to integers so that we could run sums and sorts against them.

(I also noted that I really should add a "detect column types" feature to that plugin!)

[![Edit table data/san_mateo_election_results - an option to rename table and then one to change existing columns, where each column is listed in turn and some have their type select box set to integer instead of the default of text](https://substackcdn.com/image/fetch/$s_!emvU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5818a93-2be5-4c05-878c-041423755498_1484x1748.jpeg "Edit table data/san_mateo_election_results - an option to rename table and then one to change existing columns, where each column is listed in turn and some have their type select box set to integer instead of the default of text")](https://substackcdn.com/image/fetch/$s_!emvU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5818a93-2be5-4c05-878c-041423755498_1484x1748.jpeg)

The resulting 15,589 rows represent counts from individual precincts around the county for each of the races and measures on the ballot, with a row per precinct per candidate/choice per race.

#### **Faceting and filtering the table**

Since I'm interested in the Granada Community Services District election, I applied a facet on "Contest\_title" and then used that to select that specific race.

I applied additional facets on "candidate\_name" and "Precinct name".

[![28 rows where Contest_title = Granada Community Services District Members, Board of Directors. Facets are precinct name (7 choices), candidate name (IRIS GRANT, JANET BRAYER, NANCY MARSH, WANDA BOWLES) and Contest_title](https://substackcdn.com/image/fetch/$s_!ZuON!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb584c84-d18e-4c3d-9359-6a437f3f9e0b_1790x1152.jpeg "28 rows where Contest_title = Granada Community Services District Members, Board of Directors. Facets are precinct name (7 choices), candidate name (IRIS GRANT, JANET BRAYER, NANCY MARSH, WANDA BOWLES) and Contest_title")](https://substackcdn.com/image/fetch/$s_!ZuON!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb584c84-d18e-4c3d-9359-6a437f3f9e0b_1790x1152.jpeg)

This looks right to me: we have 7 precincts and 4 candidates for 28 rows in total.

#### **Importing geospatial precinct shapes**

Those precinct names are pretty non\-descriptive! What does 33001 mean?

To answer that question, I added a new table.

San Mateo County offers [precinct maps](https://smcacre.gov/elections/precinct-maps-pdf) in the form of 23 PDF files. Our precincts are in the "Unincorporated Coastside" file:

[![Screenshot from a PDF - label is Unincorporated Coastside, it shows the area north of Half Moon Bay with a bunch of polygons with numeric identifiers.](https://substackcdn.com/image/fetch/$s_!UYek!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e0f33d8-cb1a-4a58-9720-c920e5ea6029_1356x900.jpeg "Screenshot from a PDF - label is Unincorporated Coastside, it shows the area north of Half Moon Bay with a bunch of polygons with numeric identifiers.")](https://substackcdn.com/image/fetch/$s_!UYek!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e0f33d8-cb1a-4a58-9720-c920e5ea6029_1356x900.jpeg)

Thankfully the county *also* makes that data available as [geospatial data](https://data.smcgov.org/Government/Election-Precincts/g5sj-6zp8/about_data), hosted using Socrata with an option to export as GeoJSON.

[![Socrata interface, Election Precincts updated March 7 2022 - 533 views, 72 downloads, and export dataset modal shows a GeoJSON option to export 783 rows.](https://substackcdn.com/image/fetch/$s_!tfyT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F914f17dd-5bcd-413a-b6cf-65c6788d1acb_1087x682.jpeg "Socrata interface, Election Precincts updated March 7 2022 - 533 views, 72 downloads, and export dataset modal shows a GeoJSON option to export 783 rows.")](https://substackcdn.com/image/fetch/$s_!tfyT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F914f17dd-5bcd-413a-b6cf-65c6788d1acb_1087x682.jpeg)

The `datasette-import` plugin can handle JSON files... and if a JSON file contains a top\-level object with a key that is an array of objects, it will import those objects as a table.

Dragging that file into Datasette is enough to import it as a table with a `properties` JSON column containing properties and a `geometry`JSON columnn with the GeoJSON geometry.

Here's where another plugin kicks in: [datasette\-leaflet\-geojson](https://datasette.io/plugins/datasette-leaflet-geojson) looks for columns that contain valid GeoJSON geometries and... draws them on a map!

[![Datasette precincts table with 783 rows. The properties column contains JSON keys lastupdate, creationda, prencitid, notes and active - the geometry column renders maps with polygons showing the shape of the precinct.](https://substackcdn.com/image/fetch/$s_!C9nW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f0c4fc3-3c38-4ce5-bd41-15ae1e8636d0_911x929.jpeg "Datasette precincts table with 783 rows. The properties column contains JSON keys lastupdate, creationda, prencitid, notes and active - the geometry column renders maps with polygons showing the shape of the precinct.")](https://substackcdn.com/image/fetch/$s_!C9nW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f0c4fc3-3c38-4ce5-bd41-15ae1e8636d0_911x929.jpeg)

So now we can see the shape of the individual geometries.

#### **Enriching that data to extract the precinct IDs**

The `precinctid` is present in the data, but it's tucked away in a JSON object in that `properties`JSON blob. It would be more convenient if it was a top\-level column.

Datasette's [enrichments feature](https://simonwillison.net/2023/Dec/1/datasette-enrichments/) provides tools for running operations against every row in a table and adding new columns based on the results.

My Datasette Cloud instance was missing the [datasette\-enrichments\-quickjs plugin](https://github.com/datasette/datasette-enrichments-quickjs) that would let me run JavaScript code against the data. I used my privileged access on Datasette Cloud to add that plugin to my requirements and restarted the instance to install it.

I used that to run this JavaScript code against every row in the table and saved the output in a new `precinct_id` column:

```
function enrich(row) {
  return JSON.parse(row.properties).precinctid;
}
```

[![Enrich data in precincts. 783 rows selected. JavaScript. Enrich data with a custom JavaScript function. JavaScript function: function enrich(row) { return JSON.stringify(row) + " enriched"; } - Define an enrich(row) JavaScript function taking an object and returning a value. Row keys: properties, geometry. Output mode: store the function result in a single column. Output clumn name: precinct_id. The column to store the output in - will be created if it does not exist. Output column type: text.](https://substackcdn.com/image/fetch/$s_!Vtyg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca7245e5-3e86-4bf5-af7c-4f1477e110b7_1314x926.jpeg "Enrich data in precincts. 783 rows selected. JavaScript. Enrich data with a custom JavaScript function. JavaScript function: function enrich(row) { return JSON.stringify(row) + \" enriched\"; } - Define an enrich(row) JavaScript function taking an object and returning a value. Row keys: properties, geometry. Output mode: store the function result in a single column. Output clumn name: precinct_id. The column to store the output in - will be created if it does not exist. Output column type: text.")](https://substackcdn.com/image/fetch/$s_!Vtyg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca7245e5-3e86-4bf5-af7c-4f1477e110b7_1314x926.jpeg)

This took less than a second to run, adding and populating a new `precinct_id` column for the table.

#### **Running a join**

I demonstrated how to run a join between the election results and the precincts table using the Datasette SQL query editor.

I tried a few different things, but the most interesting query was this one:

```
select
  Precinct_name,
  precincts.geometry,
  total_ballots,
  json_group_object(
    candidate_name,
    total_votes
  ) as votes_by_candidate
from
  election_results 
  join precincts on election_results.Precinct_name = precincts.precinct_id
where 
  Contest_title = "Granada Community Services District Members, Board of Directors"
group by 
  Precinct_name,
  precincts.geometry,
  total_ballots;
```

[![The SQL query returned four columns: Precinct_name, geometry with a map of the precinct, total_ballots with a number and votes_by_candidate with a JSON object mapping each candidate name to their number of votes.](https://substackcdn.com/image/fetch/$s_!Rwis!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46ec0b9b-3c90-4b06-9d6c-3f73f9d768f3_1644x1550.jpeg "The SQL query returned four columns: Precinct_name, geometry with a map of the precinct, total_ballots with a number and votes_by_candidate with a JSON object mapping each candidate name to their number of votes.")](https://substackcdn.com/image/fetch/$s_!Rwis!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46ec0b9b-3c90-4b06-9d6c-3f73f9d768f3_1644x1550.jpeg)

#### **Creating an API token to access the data**

I was nearly ready to hand over to Alex for the second half of our demo, where he would use Observable Notebooks to build some custom visualizations on top of the data.

A great pattern for this is to host the data in Datasette and then fetch it into Observable via the Datasette JSON API.

Since Datasette Cloud instances are private by default we would need to create an API token that could do this.

I used this interface (from the [datasette\-auth\-tokens plugin](https://github.com/simonw/datasette-auth-tokens)) to create a new token with read\-only access to all databases and tables in the instance:

[![Create an API token interface. This token will allow API access with the same abilities as your current user, swillison .Token will be restricted to: all databases and tables: view-database, all databases and tables: view-table, all databases and tables: execute-sql - token is set to read-only and never expires, a list of possible permissions with checkboxes is listed below.](https://substackcdn.com/image/fetch/$s_!oVyJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F435e6a07-d7dd-4029-ad8f-3fd09e32cffd_1178x1002.jpeg "Create an API token interface. This token will allow API access with the same abilities as your current user, swillison .Token will be restricted to: all databases and tables: view-database, all databases and tables: view-table, all databases and tables: execute-sql - token is set to read-only and never expires, a list of possible permissions with checkboxes is listed below.")](https://substackcdn.com/image/fetch/$s_!oVyJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F435e6a07-d7dd-4029-ad8f-3fd09e32cffd_1178x1002.jpeg)

Since we're running a dedicated instance just for Datasette Public Office Hours there's no reason not to distribute that read\-only token in publically accessible code.

#### **Getting CORS working**

Embarrassingly, I had forgotten that we would need CORS headers in order to access the data from an Observable notebook. Thankfully we have another plugin for that: [datasette\-cors](https://datasette.io/plugins/datasette-cors). I installed that quickly and we confirmed that it granted access to the API from Observable as intended.

I handed over to Alex for the next section of the demo.

#### **Working with Datasette in Observable**

Alex started by running a SQL query from client\-side JavaScript to pull in the joined data for our specific El Granada race:

```
sql = `
select
  Precinct_name,
  precincts.geometry,
  Split_name,
  Reporting_flag,
  Update_count,
  Pct_Id,
  Pct_seq_nbr,
  Reg_voters,
  Turn_Out,
  Contest_Id,
  Contest_seq_nbr,
  Contest_title,
  Contest_party_name,
  Selectable_Options,
  candidate_id,
  candidate_name,
  Candidate_Type,
  cand_seq_nbr,
  Party_Code,
  total_ballots,
  total_votes,
  total_under_votes,
  total_over_votes,
  [Vote Centers_ballots],
  [Vote Centers_votes],
  [Vote Centers_under_votes],
  [Vote Centers_over_votes],
  [Vote by Mail_ballots],
  [Vote by Mail_votes],
  [Vote by Mail_under_votes],
  [Vote by Mail_over_votes]
from
  election_results join precincts on election_results.Precinct_name = precincts.precinct_id
where "Contest_title" = "Granada Community Services District Members, Board of Directors"
limit 101;`
```

And in the next cell:

```
raw_data = fetch(
  `https://datasette-public-office-hours.datasette.cloud/data/-/query.json?_shape=array&sql=${encodeURIComponent(
    sql
  )}`,
  {
    headers: {
      Authorization: `Bearer ${secret}`
    }
  }
).then((r) => r.json())
```

Note the `?_shape=array` parameter there, which causes Datasette to output the results directly as a JSON array of objects.

That's all it takes to get the data into Observable. Adding another cell like this confirms that the data is now available:

```
Inputs.table(raw_data)
```

[![An Observable cell running Inputs.table(raw_data) and displaying a table of Precinct_name and geometry columns, with GeoJSON](https://substackcdn.com/image/fetch/$s_!wVWG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67b1b65-0fc8-490b-ad58-01a5366bfb6a_1942x694.jpeg "An Observable cell running Inputs.table(raw_data) and displaying a table of Precinct_name and geometry columns, with GeoJSON")](https://substackcdn.com/image/fetch/$s_!wVWG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67b1b65-0fc8-490b-ad58-01a5366bfb6a_1942x694.jpeg)

#### **Visualizing those with MapLibre GL**

There are plenty of good options for visualizing GeoJSON data using JavaScript in an Observable notebook.

Alex started with [MapLibre GL](https://maplibre.org/maplibre-gl-js/docs/), using the excellent [OpenFreeMap 3D tiles](https://simonwillison.net/2024/Sep/28/openfreemap/):

```
viewof map = {
  const container = html`<div style="height:800px;">`;
  yield container;
  const map = (container.value = new maplibregl.Map({
    container,
    zoom: 2,
    //style: "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
    style: "https://tiles.openfreemap.org/styles/liberty",
    scrollZoom: true
  }));
  yield container;

  map.on("load", function () {
    map.fitBounds(d3.geoBounds(data), { duration: 0 });
    map.addSource("precincts", {
      type: "geojson",
      data: data
    });
    map.addLayer({
      id: "precincts",
      type: "fill",
      source: "precincts",
      paint: {
        "fill-opacity": 0.4,
        "fill-color": [
          "case",
          ["==", ["get", "ratio"], null], "#000000",
          [
            "interpolate",
            ["linear"],
            ["get", "ratio"],
            0.0, "#0000ff",
            0.5, "#d3d3d3",
            1.0, "#ff0000"
          ]
        ]
      }
    });
    map.on("click", "precincts", (e) => {
      const { precinct, ratio } = e.features[0].properties;
      const description = JSON.stringify();

      new maplibregl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(description)
        .addTo(map);
    });
  });
  invalidation.then(() => map.remove());
}
```

[![An Observable cell showing a map of El Granada - a black shape shows the outlines of the precincts.](https://substackcdn.com/image/fetch/$s_!Lc6M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff09b9ae4-f111-4cb5-ab7a-402f1a53832f_2018x1794.jpeg "An Observable cell showing a map of El Granada - a black shape shows the outlines of the precincts.")](https://substackcdn.com/image/fetch/$s_!Lc6M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff09b9ae4-f111-4cb5-ab7a-402f1a53832f_2018x1794.jpeg)

(This is just one of several iterations, I didn't capture detailed notes of every change Alex made to the code.)

#### **Observable Plot**

Observable notebooks come pre\-loaded with the excellent Observable Plot charting library \- Mike Bostock's high\-level charting tool built on top of D3\.

Alex used that to first render the shapes of the precincts directly, without even needing a tiled basemap:

```
Plot.plot({
  width,
  height: 600,
  legend: true,
  projection: {
    type: "conic-conformal",
    parallels: [37 + 4 / 60, 38 + 26 / 60],
    rotate: [120 + 30 / 60, 0],
    domain: data
  },
  marks: [
    Plot.geo(data, {
      strokeOpacity: 0.1,
      fill: "total_votes",
      title: (d) => JSON.stringify(d.properties),
      tip: true
    })
  ]
})
```

The `parallels` and `rotate` options there come from the handy [veltman/d3\-stateplane](https://github.com/veltman/d3-stateplane?tab=readme-ov-file#nad83--california-zone-3-epsg26943) repo, which lists recommended settings for the [State Plane Coordinate System](https://en.wikipedia.org/wiki/State_Plane_Coordinate_System) used with projections in D3\. Those values are for [California Zone 3](https://www.conservation.ca.gov/cgs/rgm/state-plane-coordinate-system).

[![An Observable cell shows six five distinct colored polygons, each for a different precinct. The shape of El Granada is clearly visible despite no other map tiles or labels.](https://substackcdn.com/image/fetch/$s_!qH-W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F826d5345-c399-463c-b041-6ccbea9e3479_2038x1584.jpeg "An Observable cell shows six five distinct colored polygons, each for a different precinct. The shape of El Granada is clearly visible despite no other map tiles or labels.")](https://substackcdn.com/image/fetch/$s_!qH-W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F826d5345-c399-463c-b041-6ccbea9e3479_2038x1584.jpeg)

#### **Bringing it all together**

For the grand finale, Alex combined everything learned so far to build an interactive map allowing a user to select any of the 110 races on the ballot and see a heatmap of results for any selected candidate and option:

[![Animated demo. Choose a contest select - picking different contests updates the map at the bottom. For each contest the candidates or options are shown as radio buttons, and selecting those updates the map to show a heatmap of votes for that candidate in different precincts.](https://substackcdn.com/image/fetch/$s_!oCZd!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef3e1ef5-622e-4660-ae3b-0392d74108da_1016x844.gif "Animated demo. Choose a contest select - picking different contests updates the map at the bottom. For each contest the candidates or options are shown as radio buttons, and selecting those updates the map to show a heatmap of votes for that candidate in different precincts.")](https://substackcdn.com/image/fetch/$s_!oCZd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef3e1ef5-622e-4660-ae3b-0392d74108da_1016x844.gif)

You can try this out in [Alex's notebook](https://observablehq.com/d/2ed2ad2443d7bbb5). Here's the relevant code (Observable cells are divided by `// ---` comments). Note that Observable notebooks are reactive and allow variables to be referenced out of order.

```
// Select the contest
viewof contest = Inputs.select(contests, { label: "Choose a contest" })

// ---

// And the candidate
viewof candidate = Inputs.radio(
  candidates,
  {
    label: "Choose a candidate",
    value: candidates[0]
  }
)

// ---

// Show the map itself
Plot.plot({
  width,
  height: 600,
  legend: true,
  color: { scheme: "blues", legend: true },
  projection: {
    type: "mercator",
    domain: data2
  },
  marks: [
    Plot.geo(data2, {
      strokeOpacity: 0.1,
      fill: "ratio",
      tip: true
    })
  ]
})
# ---
data2 = ({
  type: "FeatureCollection",
  features: raw_data2.map((d) => ({
    type: "Feature",
    properties: {
      precinct: d.Precinct_name,
      total_ballots: d.total_ballots,
      ratio: JSON.parse(d.votes_by_candidate)[candidate] / d.total_ballots
    },
    geometry: JSON.parse(d.geometry)
  }))
})

// ---

raw_data2 = query(
  `select
  Precinct_name,
  precincts.geometry,
  total_ballots,
  json_grop_object(
    candidate_name,
    total_votes
  ) as votes_by_candidate
from
  election_results 
  join precincts on election_results.Precinct_name = precincts.precinct_id
where Contest_title = :contest
group by 
  Precinct_name,
  precincts.geometry,
  total_ballots;`,
  { contest }
)

// ---

raw_data2 = query(
  `select
  Precinct_name,
  precincts.geometry,
  total_ballots,
  json_group_object(
    candidate_name,
    total_votes
  ) as votes_by_candidate
from
  election_results 
  join precincts on election_results.Precinct_name = precincts.precinct_id
where Contest_title = :contest
group by 
  Precinct_name,
  precincts.geometry,
  total_ballots;`,
  { contest }
)

// ---

// Fetch the available contests
contests = query("select distinct Contest_title from election_results").then(
  (d) => d.map((d) => d.Contest_title)
)

// ---

// Extract available candidates for selected contest

candidates = Object.keys(
  JSON.parse(raw_data2[0].votes_by_candidate)
)

// ---

function query(sql, params = {}) {
  return fetch(
    `https://datasette-public-office-hours.datasette.cloud/data/-/query.json?${new URLSearchParams(
      { sql, _shape: "array", ...params }
    ).toString()}`,
    {
      headers: {
        Authorization: `Bearer ${secret}`
      }
    }
  ).then((r) => r.json());
}
```

#### **We'll be doing this again**

This was our first time trying something like this and I think it worked *really* well. We're already thinking about ways to improve it next time:

* I want to record these sessions and make them available on YouTube for people who couldn't be there live
* It would be fun to mix up the format. I'm particularly keen on getting more people involved giving demos \- maybe having 5\-10 minute lightning demo slots so we can see what other people are working on

Keep an eye on this blog or on the [Datasette Discord](https://datasette.io/discord) for news about future sessions.

---

**Link** 2024\-11\-08 [ChainForge](https://www.chainforge.ai/):

I'm still on the hunt for good options for running evaluations against prompts. ChainForge offers an interesting approach, calling itself "an open\-source visual programming environment for prompt engineering".

The interface is one of those boxes\-and\-lines visual programming tools, which reminds me of [Yahoo Pipes](https://en.wikipedia.org/wiki/Yahoo_Pipes).

[![Screenshot of an AI model testing interface showing prompts, commands, and results. Left panel shows example commands and prompt injections. Center shows a Prompt Node with evaluation function checking for 'LOL' responses. Right panel displays a bar chart comparing success rates of prompt injection across models (PaLM2, Claude, GPT4, GPT3.5) with percentages shown on x-axis.](https://substackcdn.com/image/fetch/$s_!UIo8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10948d65-58a4-47d8-a736-42a450e3e46c_1517x576.jpeg "Screenshot of an AI model testing interface showing prompts, commands, and results. Left panel shows example commands and prompt injections. Center shows a Prompt Node with evaluation function checking for 'LOL' responses. Right panel displays a bar chart comparing success rates of prompt injection across models (PaLM2, Claude, GPT4, GPT3.5) with percentages shown on x-axis.")](https://substackcdn.com/image/fetch/$s_!UIo8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10948d65-58a4-47d8-a736-42a450e3e46c_1517x576.jpeg)

It's open source (from a team at Harvard) and written in Python, which means you can run a local copy instantly via `uvx` like this:

```
uvx chainforge serve

```

You can then configure it with API keys to various providers (OpenAI worked for me, Anthropic models returned JSON parsing errors due to a 500 page from the ChainForge proxy) and start trying it out.

The "Add Node" menu shows the full list of capabilities.

[![Left sidebar shows available nodes including TextFields Node, Prompt Node, and various evaluators. Main area shows connected nodes with input fields for Feet of Clay by Terry Pratchett and Rivers of London book one by Ben Aaronovitch, along with an Inspect Node displaying GPT4-mini's response about the opening sentence of Feet of Clay. A Prompt Node on the right queries What is the opening sentence of {book}? with options to query GPT4o-mini and claude-3-haiku models.](https://substackcdn.com/image/fetch/$s_!sAlx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec8a6739-16d9-4bda-950c-8cdafc8b9578_936x791.jpeg "Left sidebar shows available nodes including TextFields Node, Prompt Node, and various evaluators. Main area shows connected nodes with input fields for Feet of Clay by Terry Pratchett and Rivers of London book one by Ben Aaronovitch, along with an Inspect Node displaying GPT4-mini's response about the opening sentence of Feet of Clay. A Prompt Node on the right queries What is the opening sentence of {book}? with options to query GPT4o-mini and claude-3-haiku models.")](https://substackcdn.com/image/fetch/$s_!sAlx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec8a6739-16d9-4bda-950c-8cdafc8b9578_936x791.jpeg)

The JavaScript and Python evaluation blocks are particularly interesting: the JavaScript one runs outside of a sandbox using plain `eval()`, while the Python one still runs in your browser but uses Pyodide in a Web Worker.

---

**Link** 2024\-11\-08 [uv 0\.5\.0](https://github.com/astral-sh/uv/releases/tag/0.5.0):

The first backwards\-incompatible (in minor ways) release after 30 releases [without a breaking change](https://twitter.com/charliermarsh/status/1855015218071355663).

I found out about this release this morning when I [filed an issue](https://github.com/astral-sh/uv/issues/8940) about a fiddly usability problem I had encountered with the combo of `uv` and `conda`... and learned that the *exact* problem had already been fixed in the brand new version!

---

**Quote** 2024\-11\-09

> *This is a very friendly and supportive place where you are surrounded by peers \- we all want to help each other succeed. The golden rule of this server is:  
>   
> **Don't** ever try to impress anyone here with your knowledge! Instead try to impress folks here with your desire to learn, and desire to help others learn.*

[fast.ai Discord Server](https://twitter.com/jeremyphoward/status/1855093111929946582)

---

**Link** 2024\-11\-10 [Everything I've learned so far about running local LLMs](https://nullprogram.com/blog/2024/11/10/):

Chris Wellons shares detailed notes on his experience running local LLMs on Windows \- though most of these tips apply to other operating systems as well.

This is great, there's a ton of detail here and the root recommendations are very solid: Use `llama-server` from [llama.cpp](https://github.com/ggerganov/llama.cpp) and try \~8B models first (Chris likes Llama 3\.1 8B Instruct at Q4\_K\_M as a first model), anything over 10B probably won't run well on a CPU so you'll need to consider your available GPU VRAM.

This is neat:

> Just for fun, I ported llama.cpp to Windows XP and ran [a 360M model](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) on a 2008\-era laptop. It was magical to load that old laptop with technology that, at the time it was new, would have been worth billions of dollars.

I need to spend more time with Chris's favourite models, Mistral\-Nemo\-2407 (12B) and Qwen2\.5\-14B/72B.

Chris also built [illume](https://github.com/skeeto/illume), a Go CLI tool for interacting with models that looks similar to my own [LLM](https://llm.datasette.io/) project.

---

**Link** 2024\-11\-11 [MDN Browser Support Timelines](https://tools.simonwillison.net/mdn-timelines):

I [complained on Hacker News](https://news.ycombinator.com/item?id=42101434#42103439) today that I wished the MDN browser compatibility ables \- like [this one for the Web Locks API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API#browser_compatibility) \- included an indication as to when each browser was released rather than just the browser numbers.

It turns out they do! If you click on each browser version in turn you can see an expanded area showing the browser release date:

[![Animated GIF showing the table, clicking a browser version expands a box showing when it was released](https://substackcdn.com/image/fetch/$s_!_Y7M!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6eef7ee-f89e-499f-85a4-2b0c30a6324a_672x550.gif "Animated GIF showing the table, clicking a browser version expands a box showing when it was released")](https://substackcdn.com/image/fetch/$s_!_Y7M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6eef7ee-f89e-499f-85a4-2b0c30a6324a_672x550.gif)

There's even [an inline help tip](https://github.com/mdn/yari/pull/6777) telling you about the feature, which I've been studiously ignoring for years.

I want to see all the information at once without having to click through each browser. I had a poke around in the Firefox network tab and found <https://bcd.developer.mozilla.org/bcd/api/v0/current/api.Lock.json>\- a JSON document containing browser support details (with release dates) for that API... and it was served using `access-control-allow-origin: *` which means I can hit it from my own little client\-side applications.

I decided to build something with an autocomplete drop\-down interface for selecting the API. That meant I'd need a list of all of the available APIs, and I used GitHub code search to find that in the [mdn/browser\-compat\-data](https://github.com/mdn/browser-compat-data/tree/main/api)repository, in the `api/` directory.

I needed the list of files in that directory for my autocomplete. Since there are just over 1,000 of those the regular [GitHub contents API](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content) won't return them all, so I switched to the [tree API](https://docs.github.com/en/rest/git/trees?apiVersion=2022-11-28#get-a-tree)instead.

Here's [the finished tool](https://tools.simonwillison.net/mdn-timelines) \- [source code here](https://github.com/simonw/tools/blob/main/mdn-timelines.html):

[![Screenshot of browser support timeline. MDN Browser Support Timelines heading, ViewTransition search box, and api.ViewTransition section showing MDN Documentation and Specification links. Timeline shows Standard_track releases: webview_android v111 (Feb 28 2023), chrome v111 (Mar 6 2023), chrome_android v111 (Mar 6 2023), edge v111 (Mar 12 2023), opera v97 (Mar 21 2023), opera_android v75 (May 16 2023), samsunginternet_android v22.0 (Jul 13 2023), safari v18 (Sep 15 2024), safari_ios v18 (Sep 15 2024), webview_ios v18 (Sep 15 2024). Not Supported: firefox, firefox_android, ie, oculus](https://substackcdn.com/image/fetch/$s_!qOu3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdaa6f62-a2f0-4362-a5c7-8a77c89a92b8_1138x1870.jpeg "Screenshot of browser support timeline. MDN Browser Support Timelines heading, ViewTransition search box, and api.ViewTransition section showing MDN Documentation and Specification links. Timeline shows Standard_track releases: webview_android v111 (Feb 28 2023), chrome v111 (Mar 6 2023), chrome_android v111 (Mar 6 2023), edge v111 (Mar 12 2023), opera v97 (Mar 21 2023), opera_android v75 (May 16 2023), samsunginternet_android v22.0 (Jul 13 2023), safari v18 (Sep 15 2024), safari_ios v18 (Sep 15 2024), webview_ios v18 (Sep 15 2024). Not Supported: firefox, firefox_android, ie, oculus")](https://substackcdn.com/image/fetch/$s_!qOu3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdaa6f62-a2f0-4362-a5c7-8a77c89a92b8_1138x1870.jpeg)

95% of the code was written by LLMs, but I did a whole lot of assembly and iterating to get it to the finished state. Three of the transcripts for that:

* [Web Locks API Browser Support Timeline](https://gist.github.com/simonw/1af1cd4f51c3dc2fa84cca0fa4746a7e) in which I paste in the original API JSON and ask it to come up with a timeline visualization for it.
* [Enhancing API Feature Display with URL Hash](https://gist.github.com/simonw/8c71a931921789e11f1d33f09d9ad9ae) where I dumped in a more complex JSON example to get it to show multiple APIs on the same page, and also had it add `#fragment` bookmarking to the tool
* [Fetch GitHub API Data Hierarchy](https://gist.github.com/simonw/d079404506621e8cafaf752f3a0c491a) where I got it to write me an async JavaScript function for fetching a directory listing from that tree API.

---

**Quote** 2024\-11\-11

> *As a junior engineer, there's simply no substitute for getting the first 100K lines of code under your belt. The "start over each day" method will help get you to those 100K lines faster.  
>   
> You might think covering the same ground multiple times isn't as valuable as getting 100K diverse lines of code. I disagree. Solving the same problem repeatedly is actually really beneficial for retaining knowledge of patterns you figure out.  
>   
> You only need 5K perfect lines to see all the major patterns once. The other 95K lines are repetition to rewire your neurons.*

[Grant Slatton](https://grantslatton.com/software-pathfinding#quantity-has-a-quality-all-of-its-own)

---

**Quote** 2024\-11\-11

> *That development time acceleration of 4 days down to 20 minutes… that’s equivalent to about 10 years of Moore’s Law cycles. That is, using generative AI like this is equivalent to computers getting 10 years better overnight.  
>   
> That was a real eye\-opening framing for me. AI isn’t magical, it’s not sentient, it’s not the end of the world nor our saviour; we don’t need to endlessly debate “intelligence” or “reasoning.” It’s just that… computers got 10 years better. The iPhone was first released in 2007\. Imagine if it had come out in 1997 instead. We wouldn’t even know what to do with it.*

[Matt Webb](https://interconnected.org/home/2024/11/11/in-our-time)

---

**Link** 2024\-11\-11 [Binary vector embeddings are so cool](https://emschwartz.me/binary-vector-embeddings-are-so-cool/):

Evan Schwartz:

> Vector embeddings by themselves are pretty neat. Binary quantized vector embeddings are extra impressive. In short, they can *retain 95\+% retrieval accuracy with 32x compression and \~25x retrieval speedup*.

It's so unintuitive how well this trick works: take a vector of 1024x4 byte floating point numbers (4096 bytes \= 32,768 bits), turn that into an array of single bits for \> 0 or \<\= 0 which reduces it to just 1024 bits or 128 bytes \- a 1/32 reduction.

Now you can compare vectors using a simple Hamming distance \- a count of the number of bits that differ \- and yet still get embedding similarity scores that are only around 10% less accurate than if you had used the much larger floating point numbers.

Evan digs into models that this works for, which include OpenAI's `text-embedding-3-large` and the small but powerful `all-MiniLM-L6-v2`.

---

**Link** 2024\-11\-11 [How I ship projects at big tech companies](https://www.seangoedecke.com/how-to-ship/):

This piece by Sean Goedecke on shipping features at larger tech companies is fantastic.

> Why do so many engineers think shipping is easy? I know it sounds extreme, but I think many engineers do not understand what shipping even is inside a large tech company. What does it mean to ship? It does not mean deploying code or even making a feature available to users. Shipping is a social construct within a company. Concretely, that means that **a project is shipped when the important people at your company believe it is shipped**.

Sean emphasizes communication, building confidence and gaining trust and the importance of deploying previews of the feature (for example using feature flags) as early as possible to get that crucial internal buy\-in and feedback from other teams.

> I think a lot of engineers hold off on deploys essentially out of fear. If you want to ship, you need to do the exact opposite: you need to deploy as much as you can as early as possible, and you need to do the scariest changes as early as you can possibly do them. Remember that you have the most end\-to\-end context on the project, which means **you should be the least scared of scary changes**.

---

**Link** 2024\-11\-12 [Ars Live: Our first encounter with manipulative AI](https://arstechnica.com/ai/2024/11/join-ars-live-nov-19-to-dissect-microsofts-rogue-ai-experiment/):

I'm participating in a live conversation with Benj Edwards on 19th November reminiscing over that incredible time back in February last year [when Bing went feral](https://simonwillison.net/2023/Feb/15/bing/).

[![A promotional image for an Ars Technica live chat event: NOVEMBER 19TH, 4:00 PM ET / 3:00 PM CT features the orange Ars Technica logo and event title Bing Chat: Our First Encounter with Manipulative AI. Below A LIVE CHAT WITH are headshots and details for two speakers: Simon Willison (Independent Researcher, Creator of Datasette) and Benj Edwards (Senior AI Reporter, Ars Technica). The image shows STREAMING LIVE AT YOUTUBE.COM/@ARSTECHNICA at the bottom.](https://substackcdn.com/image/fetch/$s_!58Xu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15032298-aec4-4b8a-a021-a8b82fe1759e_1368x1382.jpeg "A promotional image for an Ars Technica live chat event: NOVEMBER 19TH, 4:00 PM ET / 3:00 PM CT features the orange Ars Technica logo and event title Bing Chat: Our First Encounter with Manipulative AI. Below A LIVE CHAT WITH are headshots and details for two speakers: Simon Willison (Independent Researcher, Creator of Datasette) and Benj Edwards (Senior AI Reporter, Ars Technica). The image shows STREAMING LIVE AT YOUTUBE.COM/@ARSTECHNICA at the bottom.")](https://substackcdn.com/image/fetch/$s_!58Xu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15032298-aec4-4b8a-a021-a8b82fe1759e_1368x1382.jpeg)

---

**Link** 2024\-11\-13 [django\-plugin\-django\-debug\-toolbar](https://github.com/tomviner/django-plugin-django-debug-toolbar):

Tom Viner built a plugin for my [DJP Django plugin system](https://djp.readthedocs.io/) that configures the excellent [django\-debug\-toolbar](https://django-debug-toolbar.readthedocs.io/) debugging tool.

You can see everything it sets up for you [in this Python code](https://github.com/tomviner/django-plugin-django-debug-toolbar/blob/0.3.2/django_plugin_django_debug_toolbar/__init__.py): it configures installed apps, URL patterns and middleware and sets the `INTERNAL_IPS` and `DEBUG` settings.

Here are Tom's [running notes](https://github.com/tomviner/django-plugin-django-debug-toolbar/issues/1) as he created the plugin.

---

**Link** 2024\-11\-13 [Ollama: Llama 3\.2 Vision](https://ollama.com/blog/llama3.2-vision):

Ollama released version 0\.4 [last week](https://github.com/ollama/ollama/releases/tag/v0.4.0) with support for Meta's first Llama vision model, [Llama 3\.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/).

If you have Ollama installed you can fetch the 11B model (7\.9 GB) like this:

```
ollama pull llama3.2-vision

```

Or the larger 90B model (55GB download, likely needs \~88GB of RAM) like this:

```
ollama pull llama3.2-vision:90b

```

I was delighted to learn that Sukhbinder Singh had [already contributed](https://github.com/taketwo/llm-ollama/pull/15) support for [LLM attachments](https://simonwillison.net/2024/Oct/29/llm-multi-modal/) to Sergey Alexandrov's [llm\-ollama](https://github.com/taketwo/llm-ollama)plugin, which means the following works once you've pulled the models:

```
llm install --upgrade llm-ollama
llm -m llama3.2-vision:latest 'describe' \
  -a https://static.simonwillison.net/static/2024/pelican.jpg

```

> This image features a brown pelican standing on rocks, facing the camera and positioned to the left of center. The bird's long beak is a light brown color with a darker tip, while its white neck is adorned with gray feathers that continue down to its body. Its legs are also gray.
> 
> In the background, out\-of\-focus boats and water are visible, providing context for the pelican's environment.

That's not a bad description [of this image](https://static.simonwillison.net/static/2024/pelican.jpg), especially for a 7\.9GB model that runs happily on my MacBook Pro.

---

**Quote** 2024\-11\-13

> *This tutorial exists because of a particular quirk of mine: I love to write tutorials about things as I learn them. This is the backstory of [TRPL](https://doc.rust-lang.org/stable/book/), of which an ancient draft was "[Rust for Rubyists](https://github.com/steveklabnik/rust_for_rubyists)." You only get to look at a problem as a beginner once, and so I think writing this stuff down is interesting. It also helps me clarify what I'm learning to myself.*

[Steve Klabnik](https://steveklabnik.github.io/jujutsu-tutorial/)

---