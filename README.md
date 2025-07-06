
SEMANTIC GPT CACHE:

Smart caching system for LLMs using semantic similarity.
Saves time and API calls by avoiding cached prompts through vector-based matching using cosine similarity.

Objective:

in the world of artificial intelligence, llms have been the most used across organizations
and to no ones surprize they arent that cheap
in order to maintain balance between the quality and expense, the idea of caching responces is done
however the balnce mentioned here can be knob using similarity threshold parameter.

workflow :


tools:
groq - for llm
gemini -embedings
redis - vectordb cloud storeage

run using docker:
--empty

run: set up .env
python main.py

...

![alt text](image.png)
