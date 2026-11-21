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
message = []
while True:
       user_input = input("You: ")
       if user_input.lower() in ["exit", "quit"]:
              print("Exiting the AI Assistant. Goodbye!")
              break
       message.append({
              "role": "user",
              "content": user_input
       })
       response= client.chat.completions.create(
              model=os.getenv("MODEL"),
              messages=message     
       )
       print("AI Assistant:", response.choices[0].message.content)
       message.append({
              "role": "AI Assistant",
              "content": response.choices[0].message.content
       })
for message in message:
       print(f"{message['role'].title()}: {message['content']}")