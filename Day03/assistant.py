from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
print("hello, world!")
  
client = OpenAI(
       base_url=os.getenv("BASE_URL"),
       api_key=os.getenv("API_KEY")  
)
print("="*40)
print("My Personal AI Assistant")
print("="*40)
message = []
roles = {
       "1": "You are a friendly school teacher. Explain concepts in simple words and using real life examples",
       "2": "You are a senior python developer. Explain topics in simple words and and using simple codes. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "3": "You are experienced travel guide. Try to tell about places to visit, foods to recommend and travel tips. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "4": "You are a professional interviewer. Ask questions, evaluate the answer and provide feedback and then ask next question. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "5": "You are a motivational speaker. Try to encourage people and cheers for life and give practical advice. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer"
}
print("Choose a system prompt for the AI Assistant (or press Enter to skip): ")
print("1: Teacher")
print("2: Senior developer")
print("3: Travel Guide")
print("4: Interviewer")
print("5: Motivational Speaker")
role = input("Choose Assistant")
message.append({
       "role": "system",
       "content": roles.get(role,"You are a friendly AI assistant")
})
print(message)
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
# for message in message:
#        print(f"{message['role'].title()}: {message['content']}")