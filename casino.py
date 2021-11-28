import OS
from random import randint

def casino(user):
  print("opening 'casino'")
  print("")
  print("...")
  print("")
  OS.on_enter()

  print("Welcome to the casino!")
  print("enter 'help' for commands")

  # 50/50
  def bet(amount):
    print("")
    print("...")
    print("")
    if randint(0, 1) == 1:
      print("you won " + str(amount) + " tokens")
      OS.on_enter()
      return amount
    else:
      print("you lost " + str(amount) + " tokens")
      OS.on_enter()
      return -amount


  # 50/50
  def double_or_nothing(amount):
    print("")
    print("...")
    print(" ")

    if randint(0, 1) == 1:
        if input("you win! double? ").strip().lower() in OS.yes_words:
            amount *= 2
            return double_or_nothing_part_2(amount)
        else:
            return amount
    else:
        print("you lost " + str(amount) + " tokens")
        OS.on_enter()
        return -amount


  # 66/33
  def double_or_nothing_part_2(amount):
    print("")
    print("...")
    print("")

    if randint(0, 2) == 1:
        print("you lost " + str(amount) + " tokens")
        OS.on_enter()
        return -amount
    else:
        if input("you win! double? ").strip().lower() in OS.yes_words:
            amount *= 2
            return double_or_nothing(amount)
        else:
            print("you won " + str(amount) + " tokens")
            OS.on_enter()
            return amount


  # white jack
  def white_jack(amount):
    print("")

    pc1 = randint(1, 10)
    pc2 = randint(1, 10)

    dp1 = randint(1, 10)
    dp2 = randint(1, 10)

    print("")
    print("...")
    print("")

    print("You and the dealer have 2 cards. You want more than the dealer")
    print("your cards are: " + str(pc1) + " and " + str(pc2))
    print("dealers card are: " + str(dp1) + " and ?")

    if (input("double? ").strip().lower() in OS.yes_words):
        amount *= 2
        if (pc1 + pc2) > (dp1 + dp2):
            print("you have more! you win!")
            OS.on_enter()
            return amount
        else:
            print("you have less! you lose!")
            OS.on_enter()
            return -amount
    else:
        if (pc1 + pc2) > (dp1 + dp2):
            print("you have more! you win!")
            OS.on_enter()
            return amount
        else:
            print("you have less! you lose!")
            OS.on_enter()
            return -amount

  def slot_assigner(rng_slots):
    if rng_slots in range(1, 40):
      return "+"
    elif rng_slots in range(41, 80):
      return "-"
    elif rng_slots in range(81, 90):
      return "="
    elif rng_slots in range (91, 96):
      return "@"
    elif rng_slots in range(97, 99):
      return "x"
    elif rng_slots in range(100, 100):
      return "$"
    else:
      return "error"
      print("error 'slot_rng' was " + rng_slots)
      OS.on_enter()

  def slots():
    OS.clear()
    print("")
    print("...")
    print("")
    slot_rng1 = randint(1, 100)
    slot1 = slot_assigner(slot_rng1)
    slot_rng2 = randint(1, 100)
    slot2 = slot_assigner(slot_rng2)
    slot_rng3 = randint(1, 100)
    slot3 = slot_assigner(slot_rng3)
    slot_list = [slot1, slot2, slot3]
    print(slot_list)
    numofplus = 0
    numofmin = 0
    numofeq = 0
    numofAt = 0
    numofX = 0
    numofCash = 0

    # counts how may times symbols occur
    for slot in slot_list:
      if slot == "+":
        numofplus += 1
      elif slot == "-":
        numofmin += 1
      elif slot == "=":
        numofeq += 1
      elif slot == "@":
        numofAt += 1
      elif slot == "x":
        numofX += 1
      elif slot == "$":
        numofCash += 1

    # returns reward based on symbols
    if numofplus == 2:
      return 1
    elif numofplus == 3:
      return 5
    elif numofmin == 2:
      return 10
    elif numofmin == 3:
      return 20
    elif numofeq == 2:
      return 50
    elif numofeq == 3:
      return 100
    elif numofAt == 2:
      return 200
    elif numofAt == 3:
      return 500
    elif numofX == 2:
      return 1000
    elif numofX == 3:
      return 10000
    elif numofCash == 2:
      return 100000
    elif numofCash == 3:
      return 1000000
    else:
      return 0

  while OS.db["users"][user]["casino"]["casino tokens"] > 0:
    OS.clear()
    print("you have " + str(OS.db["users"][user]["casino"]["casino tokens"]) + " tokens")
    if OS.db["users"][user]["casino"]["casino tokens"] > OS.db["users"][user]["casino"]["casino highscore"]:
      print("new high score!")
      OS.db["users"][user]["casino"]["casino highscore"] = OS.db["users"][user]["casino"]["casino tokens"]
    command_casino = input("enter command: ").strip().lower()

    if command_casino == "help":
        print("")
        print("Commands:")
        print("'bet': 50/50 bet.'")
        print(
            "'dor': double or nothing. like bet but you can double your bet. After winning the first bet your chances of winning are 75% instead of 50%"
        )
        print("'wj': white jack (scuffed black jack)")
        print("'quit': quits the program")

    # bet
    elif command_casino == "bet":
        amount = input("amount: ").strip()
        if amount.isnumeric():
          amount = int(amount)
          if amount <= OS.db["users"][user]["casino"]["casino tokens"]:
            OS.db["users"][user]["casino"]["casino tokens"] += bet(amount)
          else:
            print("you dont have enough")
            OS.on_enter()
        else:
          print("'amount' must be an integer")
          OS.on_enter()

    # double or nothing
    elif command_casino == "dor":
        amount = input("amount: ").strip()
        if amount.isnumeric():
          amount = int(amount)
          if amount <= OS.db["users"][user]["casino"]["casino tokens"]:
            OS.db["users"][user]["casino"]["casino tokens"] += double_or_nothing(amount)
          else:
            print("you dont have enough")
            OS.on_enter()
        else:
          print("'amount' must be an integer")
          OS.on_enter()

    # scuffed black jack (white jack)
    elif command_casino == "wj":
        amount = input("amount: ").strip()
        if amount.isnumeric():
          amount = int(amount)
          if amount <= OS.db["users"][user]["casino"]["casino tokens"]:
            OS.db["users"][user]["casino"]["casino tokens"] += white_jack(amount)
          else:
            print("you dont have enough")
            OS.on_enter()
        else:
          print("'amount' must be an integer")
          OS.on_enter()

    # slots
    elif command_casino == "slots":
      if OS.db["users"][user]["casino"]["casino tokens"] >= 10:
        if input("'slots' costs 10 tokens. Play slots? ").strip().lower() in OS.yes_words:
          OS.db["users"][user]["casino"]["casino tokens"] -= 10
          slot_amount_won = slots()
          OS.db["users"][user]["casino"]["casino tokens"] += int(slot_amount_won)
          print("you won " + str(slot_amount_won) + " tokens")
          OS.on_enter()
        else:
          print("cancelled")
          OS.on_enter()
      else:
        print("you need 10 tokens to play")

    elif command_casino == "quit":
      OS.os_commands(user)
    else:
        print("invalid command")
        OS.on_enter()
  else:
    OS.clear()
    print("no more tokens")
    if input("Play again? ").strip().lower() in OS.yes_words:
      OS.db["users"][user]["casino"]["casino tokens"] = 100
      casino(user)
    else:
      OS.os_commands(user)