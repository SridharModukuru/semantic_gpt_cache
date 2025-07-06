import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# set up groq api key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(question):
    """
    using groqapi as llm backup, if similarity_index is not satisfied, then query the qroq llm. 
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant., keep the responces simple and ease."},
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
