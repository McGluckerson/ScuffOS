from replit import db
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

def high_score_printer(user):
  print(user + "'s high scores:")

def user_info(user):
  print(db["users"][user])
  on_enter()
  os_commands(user)

# programs used when logged in
def os_commands(user):
  clear()
  commands = {"help" : "shows list of commands", "user info" : "prints user info", "logout" : "logs user out" , "battleship" : "opens the game battleship", "casino" : "opens the casino game"}

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
  elif command == "user info":
    user_info(user)
  elif command == "battleship":
    clear()
    battleship.battleship(user)
  elif command == "casino":
    clear()
    casino.casino(user)
    os_commands(user)
  elif command == "logout":
    logout(user)
  elif command == "print user database" and user == "admin":
    print("there are " + len(db["users"]) + " users!")
    print(db["users"].keys())
    on_enter()
    os_commands(user)
  elif command == "database":
    # add database info to print
    print(len(db))
    on_enter()
    os_commands(user)
  else:
    print("invalid command")
    on_enter()
    os_commands(user)

users = {"admin" : "debug", "user2" : "password2"}

def login():
  clear()
  # checks if user exists
  user_login = input("enter user: ")
  if user_login in db["users"]:
    print("user found!")
  else:
    print("user does not exist")
    on_enter()
    login()

  # checks if password matches
  password_login = input("enter password: ")
  if db["users"][user_login]["password"] == password_login:
    print("logging into " + user_login)
    if user_login == "admin":
      print("debug tools unlocked")
    on_enter()
    clear()
    os_commands(user_login)
  else:
    print("password does not match!")
    on_enter()
    clear()
    login()

def add_user():
  new_user = input("user name: ")
  new_password = input("user password: ")
  db["users"][new_user] = {"password" : new_password, "casino" : {"casino tokens" : 0, "casino highscore" : 0}, "battleship" : {"boards" : {"Pboard" : [], "Cboard" : []},  "ships" : {"Pship_row" : 0, "Pship_col" : 0, "Cship_row" : 0, "Cship_col" : 0}}}
  print("user added!")
  print("user: " + new_user)
  print("password: " + new_password)
  on_enter()
  clear()
  start_screen()

def start_screen():
  print("type 'help' for list of commands")
  start_command = input("command: ").strip().lower()
  if start_command == "help":
    print("'login', 'add user'")
    start_screen()
  elif start_command == "login":
    login()
  elif start_command == "add user":
    add_user()

start_screen()