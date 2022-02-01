from replit import db
import os

# imports programs
import battleship
import casino

yes_words = ["yes", "y"]

# function for programs and os to use
def clear():
	clear_type = 'clear'
	if os.name in ('nt', 'dos'): # changes clear type to work with windows if running windows
		clear_type = 'cls'
	os.system(clear_type)
def on_enter():
	literaly_nothing_ok = input("'Enter' to continue")

def logout(user):
	print("goodbye" + user)
	on_enter
	login()

def high_score_printer(user):
	print(user + "'s high scores:")
	print("casino: " + str(db["users"][user]["casino"]["casino highscore"]))

def user_info(user):
	print("password: " + db["users"][user]["password"])
	print("casino tokens: " + str(db["users"][user]["casino"]["casino tokens"]))
	on_enter()
	os_commands(user)

def search_db(user):
	clear()
	print("Check Data Base Format Guide on how to enter key path")
	key_path = input("Enter key path: ")
	try:
		eval(key_path)
		key_path_valid = True
	except:
		print("key path invalid")
		on_enter()
		os_commands(user)
	if key_path.endswith('["password"]'):
		print("no XD")
		on_enter()
		os_commands(user)
	else:
		clear()
		if key_path_valid:
			if type(eval(key_path)) is str:
				print(key_path + ":")
				print(eval(key_path))
		on_enter()
		os_commands(user)

# programs used when logged in
def os_commands(user):
	clear()
	commands = {"help" : "shows list of commands", "user info" : "prints user info", "highscores": "shows your highscores", "search database" : "lets the user search the databse including user information", "battleship" : "opens the game battleship", "casino" : "opens the casino game", "logout" : "returns to login"}

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
	elif command == "search database":
		search_db(user)
	elif command == "battleship":
		clear()
		battleship.battleship(user)
	elif command == "casino":
		clear()
		casino.casino(user)
		os_commands(user)
	elif command == "logout":
		start_screen()
	elif command == "print number of users" and user == "admin":
		print("there are " + len(db["users"]) + " users!")
		print(db["users"])
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
	db["users"][new_user] = {"password" : new_password, "casino" : {"casino tokens" : 0, "casino highscore" : 0}, "battleship" : {"boards" : {"Pboard" : [], "Cboard" : []},	"ships" : {"Pship_row" : 0, "Pship_col" : 0, "Cship_row" : 0, "Cship_col" : 0}}}
	if input("confirm? ") in yes_words:
		clear()
		if new_user not in db["users"]:
			print("user added!")
			print("user: " + new_user)
			print("password: " + new_password)
		else:
			print("user already exists ¯\_(ツ)_/¯")
	else:
		print("cancelled")
	on_enter()
	clear()
	start_screen()

def start_screen():
	clear()
	start_command = input("login or add user? ").strip().lower()
	if start_command == "login":
		login()
	elif start_command == "add user":
		add_user()
	else:
		print("invalid command")
		on_enter()
		start_screen()

start_screen()