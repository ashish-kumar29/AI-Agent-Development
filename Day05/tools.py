

from datetime import datetime
from pathlib import Path
import random
import secrets
import string


def get_current_time():
       return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def roll_dice():
       return random.randint(1,6)

def generate_password(length=12):
       characters = (
              string.ascii_letters +
              string.digits +
              string.punctuation
       )
       password = ""
       for _ in range(length):
              password += secrets.choice(characters)
       return password

def read_text_files(filename):
       file_path = Path(__file__).parent.parent / filename
       try:
              with open(filename, "r", encoding="utf-8") as file:
                     return file.read()
       except FileNotFoundError:
              return "Error File not found"