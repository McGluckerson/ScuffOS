import OS
from apps import maze_levels

def maze(user):
	print("Welcome to maze!")
	print("Input q to quit")
	print("there are 4 levels")
	print("if you enter a level that dosnt exist the program will crash becuase im too lazy to fix it :)")
	OS.on_enter()
	OS.clear()

	maze = []

	level_selected = input("Level #: ")

	if level_selected == "q":
		print("quiting maze")
		OS.on_enter()
		OS.os_commands(user)

	level_selected = int(level_selected)

	player_pos = [maze_levels.levels[level_selected]["player_starting_pos"][0], maze_levels.levels[level_selected]["player_starting_pos"][1]]
	def setup():
		row = 1
		for x in range(20):
			maze.append(maze_levels.levels[level_selected]["layout"][row - 1])
			row += 1
		maze[player_pos[0] - 1][player_pos[1] - 1] = "+"

	def print_maze():
		for i in range(20):
			print(" ".join(maze[i]))

	setup()
	print_maze()

	while 1 == 1:
		move = input("").lower()
		if move == "w" and maze[player_pos[0] - 1 - 1][player_pos[1] - 1] != "X":
			maze[player_pos[0] - 1][player_pos[1] - 1] = " "
			player_pos[0] -= 1
		elif move == "s" and maze[player_pos[0] - 1 + 1][player_pos[1] - 1] != "X":
			maze[player_pos[0] - 1][player_pos[1] - 1] = " "
			player_pos[0] += 1	
		elif move == "a" and maze[player_pos[0] - 1][player_pos[1] - 1 - 1] != "X":
			maze[player_pos[0] - 1][player_pos[1] - 1] = " "
			player_pos[1] -= 1
		elif move == "d" and maze[player_pos[0] - 1][player_pos[1] - 1 + 1] != "X":
			maze[player_pos[0] - 1][player_pos[1] - 1] = " "
			player_pos[1] += 1
		elif move == "q":
			print("quiting maze")
			OS.on_enter()
			OS.os_commands(user)

		OS.clear()
		if maze[player_pos[0] - 1][player_pos[1] - 1] == "O":
			print("you reached the exit!")
			OS.on_enter()
			OS.clear()
			print("quiting maze")
			OS.on_enter()
			OS.os_commands(user)
			maze(user)
		maze[player_pos[0] - 1][player_pos[1] - 1] = "+"
		print_maze()