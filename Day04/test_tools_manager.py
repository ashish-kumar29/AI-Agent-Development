from tools_manager import execute_tool


print(execute_tool("Roll a dice"))
print(execute_tool("What is today date"))
print(execute_tool("Generate a random password"))
print(execute_tool("What is python"))
if execute_tool("What is python") == None:
       print("AI Assistant will help")