from openai import OpenAI
import os
from dotenv import load_dotenv

from tools_manager import execute_tool
from tools import generate_password, get_current_time, roll_dice
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
file_content=""
roles = {
       "1": "You are a friendly school teacher. Explain concepts in simple words and using real life examples",
       "2": "You are a senior python developer. Explain topics in simple words and and using simple codes. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "3": "You are experienced travel guide. Try to tell about places to visit, foods to recommend and travel tips. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "4": "You are a professional interviewer. Ask questions, evaluate the answer and provide feedback and then ask next question. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "5": "You are a motivational speaker. Try to encourage people and cheers for life and give practical advice. If anything asked out of this context, dont tell the answer and  tell it is out of scope and can't answer",
       "6": """You are given a document.
              Answer the user's question using only the information present in documeny.
              If the answer is not available, say:
                     'I could not find that information in the document' 
              Document:
              {}"""
}
print("Choose a system prompt for the AI Assistant (or press Enter to skip): ")
print("1: Teacher")
print("2: Senior developer")
print("3: Travel Guide")
print("4: Interviewer")
print("5: Motivational Speaker")
print("6: Answer questions based on some document")
role = input("Choose Assistant")
assistant_req = 5
if role=="6":
       assistant_req, file_content = execute_tool("file")
print(file_content)
if not assistant_req:
       print(file_content)
content = roles.get(role,"You are a friendly AI assistant").format(file_content)
message.append({
       "role": "system",
       "content": content
})

print(message)
while True:
       user_input = input("You: ")
       if user_input.lower() in ["exit", "quit"]:
              print("Exiting the AI Assistant. Goodbye!")
              break
       calculated_response = ""
       if not assistant_req:
              calculated_response = execute_tool(user_input)
       if calculated_response:
              print(calculated_response)
              continue
       message.append({
              "role": "user",
              "content": user_input
       })
       print(f"user input: {user_input}")
       response= client.chat.completions.create(
              model=os.getenv("MODEL"),
              messages=message     
       )
       print("AI Assistant:", response.choices[0].message.content)
       message.append({
              "role": "assistant",
              "content": response.choices[0].message.content
       })
# for message in message:
#        print(f"{message['role'].title()}: {message['content']}")