  # starts the os
from replit import db
if input("update users? ").strip().lower() == "y":
  for user in db["users"]:
    # update users with new info
    print(user)
    db["users"][user] = {"password" : db["users"][user]["password"], "casino" : {"casino tokens" : 0, "casino highscore" : 0}, "battleship" : {"boards" : {"Pboard" : [], "Cboard" : []}},  "ships" : {"Prow" : 0, "Pcol" : 0, "Crow" : 0, "Ccol" : 0}}
    print(db["users"][user])
    input()
import OS