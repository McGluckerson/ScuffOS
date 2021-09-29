import OS
from random import randint

def battleship(user):
  print("opening 'battleship'")
  print("")
  print("...")
  print("")

  board = []

  for i in range(5):
    board.append(["O"] * 5)

  def print_board(board):
    OS.clear()
    for i in range(5):
      print(" ".join(board[i]))

  ship_row = randint(1, 5) - 1
  ship_col = randint(1, 5) - 1

  turns = 5

  while turns > 0:
    print("you have " + str(turns) + " turns left")
    print_board(board)

    guess_row = input("guess row: ").strip()
    guess_col = input("guess col: ").strip()

    if guess_row.isnumeric() and guess_col.isnumeric():
      guess_row = int(guess_row) - 1
      guess_col = int(guess_col) - 1

      if guess_row == ship_row and guess_col ==  ship_col:
        print("Hit!")
        break
      elif guess_row not in range(0, 5) or ship_col not in range(0,5):
        print("thats not on the board!")
      elif board[guess_row][guess_col] == "X":
        print("you already guessed there")
        OS.on_enter()
      else:
        print("miss!")
        board[guess_row][guess_col] = "X"
        OS.on_enter()

      turns -= 1
    else:
      print("guess must be an integer")
      OS.on_enter()
  else:
    print("no more turns")
    if input("Play again? ").strip().lower() in OS.yes_words:
      battleship(user)
    else:
      OS.os_commands(user)

  print_board(board)