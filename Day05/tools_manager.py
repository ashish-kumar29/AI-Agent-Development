

from tools import generate_password, get_current_time, read_text_files, roll_dice


def execute_tool(user_input):
       if "date" in user_input.lower():
              return f"Current date is {get_current_time()}"
       elif "dice" in user_input.lower():
              return f"Dice rolled value is {roll_dice()}"
       elif "password" in user_input.lower():
              return f"New generated password: {generate_password()}"
       elif "file" in user_input.lower():
              print("hello")
              content = read_text_files("Notes/the_life_of_aarav_mehta_20mb.txt")
              assistant_req = True
              if "error" in content.lower():
                     assistant_req = False
              return assistant_req, content
       else:
              return None
       