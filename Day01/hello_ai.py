from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
print("hello, world!")
  
client = OpenAI(
       base_url=os.getenv("BASE_URL"),
       api_key=os.getenv("API_KEY")
)
message = [
       {
       "role": "user",
        "content": "Hello, AI Assistant!, are you ollama or gemini?"
       }
]
response= client.chat.completions.create(
       model=os.getenv("MODEL"),
       messages=message
)
print("AI Assistant:", response.choices[0].message.content)