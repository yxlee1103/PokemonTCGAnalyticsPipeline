# Pokemon Trading Card Game(TCG) Analytics Pipeline
After YouTuber Logan Paul purchased a Pikachu card for a staggering $5.275 million, you might be wondering if any of your vintage Pokemon cards hold significant value. 
It's crucial to note that not every Pokemon card commands high value – rarity and being out of print contribute significantly to value appreciation. 
Another influencing factor is grading, cards evaluated by agencies like PSA or Beckett proving more valuable than ungraded ones. Factors such as condition, edges, corners, and printing quality being pivotal in determining their worth. 
Cards in mint condition, boasting crisp edges, sharp corners, and vibrant, unfaded imagery, are more likely to hold their value. <br /> 

## Description
Now, let's explore the possibility of purchasing a raw card, having it graded by PSA or Beckett and sell it for a profit. Additionally, let's identify which card offers the most favourable return rate. 
In this project, we'll utilize **Google Cloud Services** to construct a Pokemon TCG analytics pipeline, from retrieving data via the API, storing and processing the data, to crafting a Looker Studio dashboard.

## Getting Started
### Architecture
![Architecture](https://github.com/yxlee1103/PokemonTCGAnalyticsPipeline/assets/33648886/fd04a2ca-822f-4cbc-b471-5b65224788a1)

### Process
1. Retrieving data from Pokemon TCG API with Python
2. Storing Data in GCS
3. Creating a Cloud Trigger 
4. Orchestrating a Dataflow Job for Big Query
5. Automating workflows with Cloud Composer
6. Visualizing on Looker Studio
