from random import randint

# imports programs
import battleship
import casino

yes_words = ["yes", "y"]

# programs used when logged in
def os_commands(user):
  print("")
  print("...")
  print("")
  commands = {"help" : "shows list of commands"}

  command = input("enter command: ").strip().lower()
  
  if command == "help":
    print(commands)
  elif command == "battleship":
    battleship.battleship(user)
  elif command == "casino":
    casino.casino(user)
  else:
    print("invalid command")
    os_commands(user)

users = {"user1" : "password1", "user2" : "password2"}

def login():
  # checks if user exists
  user_login = input("enter user: ")
  if user_login in users:
    print("user found!")
  else:
    print("user does not exist")
    login()

  # checks if password mathes
  password_login = input("enter password: ")
  if users[user_login] == password_login:
    print("logging into " + user_login)
    os_commands(user_login)
  else:
    print("password does not match!")
    login()

login()
