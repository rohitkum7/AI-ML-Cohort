from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # explicitly use your key from .env
)

response = client.chat.completions.create(
    model="gpt-4",  # or gpt-4 if you have access
    messages=[
        {"role": "user", "content": "Now I have created an ai llm, how to create agents out of them"}
    ]
)

print(response.choices[0].message.content)
