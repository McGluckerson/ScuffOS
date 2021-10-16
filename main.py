  # starts the os
from replit import db
import os
if input("update users? ").strip().lower() == "y":
  for user in db["users"]:
    # update users with new info
    print(user)
    db["users"][user] = {"password" : db["users"][user]["password"], "casino" : {"casino tokens" : 0, "casino highscore" : 0}, "battleship" : {"boards" : {"Pboard" : [], "Cboard" : []},  "ships" : {"Pship_row" : 0, "Pship_col" : 0, "Cship_row" : 0, "Cship_col" : 0}}}
    print(db["users"][user])
    input()
    clear_type = 'clear'
    if os.name in ('nt', 'dos'): # changes clear type to work with windows if running
      clear_type = 'cls'
  os.system(clear_type)
import OS