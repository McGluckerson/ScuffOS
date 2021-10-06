import OS
from random import randint

def battleship(user):
  print("opening 'battleship'")
  print("")
  print("...")
  print("")

  def setup(user):
    for i in range(5):
      # player attacks player board and cpu attacks cpu board
      OS.info[user]["battleship"]["boards"]["Pboard"].append(["O"] * 5)
      OS.info[user]["battleship"]["boards"]["Cboard"].append(["O"] * 5)

  setup(user)

  def print_board(board):
    OS.clear()
    for i in range(5):
      print(" ".join(board[i]))

  # assigns ship to random point on board
  Pship_row = randint(1, 5) - 1
  Pship_col = randint(1, 5) - 1
  Cship_row = randint(1, 5) - 1
  Cship_col = randint(1, 5) - 1

  for nothing in range(9999999999999999999999999999999999999999):
    OS.on_enter()
    OS.clear()
    print("your turn")
    OS.on_enter()

    print_board(OS.info[user]["battleship"]["boards"]["Pboard"])

    guess_row = input("guess row: ").strip()
    guess_col = input("guess col: ").strip()

    if guess_row.isnumeric() and guess_col.isnumeric():
      guess_row = int(guess_row) - 1
      guess_col = int(guess_col) - 1

      if guess_row == Pship_row and guess_col == Pship_col:
        print("Hit!")
        print("You win")
        if input("play again? ").strip().lower() in OS.yes_words:
          battleship(user)
      elif guess_row not in range(0, 5) or guess_col not in range(0, 5):
        print("thats not on the board!")
      elif OS.info[user]["battleship"]["boards"]["Pboard"][guess_row][guess_col] == "X":
        print("you already guessed there")
      else:
        print("miss!")
        OS.info[user]["battleship"]["boards"]["Pboard"][guess_row][guess_col] = "X"

      OS.on_enter()
      OS.clear()
      print("cpu's turn")
      OS.on_enter()
      OS.clear()

      print_board(OS.info[user]["battleship"]["boards"]["Cboard"])

      cpu_guess_row = randint(0, 5) - 1
      cpu_guess_col = randint(0, 5) - 1
      if cpu_guess_row == Cship_row and cpu_guess_col == Cship_col:
        print("Hit!")
        print("You lose")
        if input("play again? ").strip().lower() in OS.yes_words:
          battleship(user)
      elif guess_row not in range(0, 5) or guess_col not in range(0,5):
        print("thats not on the board!")
      elif OS.info[user]["battleship"]["boards"]["Cboard"][cpu_guess_row][cpu_guess_col] == "X":
        print("you already guessed there")
      else:
        print("miss!")
        OS.info[user]["battleship"]["boards"]["Cboard"][guess_row][guess_col] = "X"

  print_board(OS.info[user]["battleship"]["boards"]["Pboard"])