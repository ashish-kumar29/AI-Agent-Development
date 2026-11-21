from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
print("hello, world!")
  
client = OpenAI(
       base_url=os.getenv("BASE_URL"),
       api_key=os.getenv("GEMINI_API_KEY")
)
print("="*40)
print("My Personal AI Assistant")
print("="*40)
while True:
       user_input = input("You: ")
       if user_input.lower() in ["exit", "quit"]:
              print("Exiting the AI Assistant. Goodbye!")
              break
       response= client.chat.completions.create(
              model=os.getenv("MODEL"),
              messages=[
                     {
                            "role": "user",
                            "content": user_input
                     }
              ]
       )
       print("AI Assistant:", response.choices[0].message.content)