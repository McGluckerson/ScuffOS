import os

# imports programs
import battleship
import casino

yes_words = ["yes", "y"]

# function for programs and os to use
def clear():
  clear_type = 'clear'
  if os.name in ('nt', 'dos'): # changes clear type to work with windows if running
    clear_type = 'cls'
  os.system(clear_type)
def on_enter():
  signal = input("'Enter' to continue")

def logout(user):
  print("goodbye" + user)
  on_enter
  login()

high_scores = {"user1" : {"battleship" : "N/A", "casino" : 0}, "user2" : {"battleship" : "N/A", "casino" : 0}}

def high_score_printer(user):
  print(user + "'s high scores:")
  print(high_scores[user])

# programs used when logged in
def os_commands(user):
  clear()
  commands = {"help" : "shows list of commands", "battleship" : "opens the game battleship", "casino" : "opens the casino game"}

  command = input("enter command: ").strip().lower()
  
  if command == "help":
    print(commands)
    on_enter()
    os_commands(user)
  if command == "highscores":
    clear()
    high_score_printer(user)
    on_enter()
    os_commands(user)
  elif command == "battleship":
    clear()
    battleship.battleship(user)
  elif command == "casino":
    clear()
    casino.casino(user)
  else:
    print("invalid command")
    on_enter()
    os_commands(user)

users = {"user1" : "password1", "user2" : "password2"}

def login():
  clear()
  # checks if user exists
  user_login = input("enter user: ")
  if user_login in users:
    print("user found!")
  else:
    print("user does not exist")
    on_enter()
    login()

  # checks if password mathes
  password_login = input("enter password: ")
  if users[user_login] == password_login:
    print("logging into " + user_login)
    on_enter()
    clear()
    os_commands(user_login)
  else:
    print("password does not match!")
    on_enter()
    clear()
    login()

login()