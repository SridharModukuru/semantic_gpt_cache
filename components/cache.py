import redis
import json

from components.gemini_embed import get_embedding
from components.groq_api import ask_groq
from components.utils import cosine_similarity

# make sure redis is running as a docker container or on any server 
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

similarity_threshold = 0.9

def check_cache(question,similarity_threshold):
    if question =="clear cache":
        r.flushdb()
        print("Cleared current Redis DB")
        return "Cache Cleared",True

    query_embedding = get_embedding(question)


    # check all the embeddings in vectordb, until similarity threshold is met

    for key in r.scan_iter("embed:*"): # indexes of all embeddings
        data = json.loads(r.get(key)) # get embedding
        stored_embedding = data['embedding']
        similarity = cosine_similarity(query_embedding, stored_embedding)
        if similarity >= similarity_threshold:
            print("✅ Found in cache:", key)
            return data['answer'], True

    answer = ask_groq(question)

    r.set(f"embed:{r.dbsize()}", json.dumps({ # using dbsize as index to store at
        "question": question,
        "embedding": query_embedding,
        "answer": answer
    }))
    print("stored new answer in cache.")
    return answer, False
