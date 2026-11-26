

from tools import generate_password, get_current_time, roll_dice


print("Current_time: "+get_current_time())
print(f"Rolled dice value: {roll_dice()}")
print(f"Password: {generate_password(4)}")