from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def get_embedding(text):
    
    """
    using googlegenaiEmbedding for embedding the user query and llm responce to check similarity.
    """

    return embedding_model.embed_query(text)
