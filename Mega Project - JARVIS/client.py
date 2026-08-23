import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a Virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(completion.choices[0].message.content)