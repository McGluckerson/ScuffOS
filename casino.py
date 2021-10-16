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
        # STILL RETURNS ERROR IF NOTHING ENTERED!
        # NEEDS FIXING!
        if amount.isnumeric:
          amount = int(amount)
          if amount <= OS.db["users"][user]["casino"]["casino tokens"]:
            OS.db["users"][user]["casino"]["casino tokens"] += white_jack(amount)
          else:
            print("you dont have enough")
            OS.on_enter()
        else:
          print("'amount' must be an integer")
          OS.on_enter()

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