

from tools import generate_password, get_current_time, roll_dice


def execute_tool(user_input):
       if "date" in user_input.lower():
              return f"Current date is {get_current_time()}"
       elif "dice" in user_input.lower():
              return f"Dice rolled value is {roll_dice()}"
       elif "password" in user_input.lower():
              return f"New generated password: {generate_password()}"
       else:
              return None