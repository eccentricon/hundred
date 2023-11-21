#!/usr/bin/env python

# Treasure Island (alternative implementation)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

alive = True
status = "You found the treasure! You win!"

print("You're at a crossroad. Where do you want to go?")
cmd = input("[Hint: Type \"(l)eft\" or \"(r)ight\"]: ").lower()
if (cmd[0] == "l"):
  print("You've come to a lake. There is an island in the middle of the lake.")
  cmd = input("[Hint: Type \"(w)ait\" to wait for a boat, or \"(s)wim\" to swim across]: ").lower()
else:
  status = "You fell into a hole. Game over."
  alive = False
  
if (alive and cmd[0] == "w"):
  print("You arrive at the island unharmed. There is a house with 3 doors.", 
        "One red, one yellow and one blue. Which colour do you choose?")
  cmd = input("[Hint: Type \"(r)ed\", \"(y)ellow\", or \"(b)lue\"]: ").lower()
elif (alive):
  status = "You get attacked by an angry trout. Game over."
  alive = False

if (alive and cmd[0] == "b"):
  status = "You enter a room of beasts. Game over."
elif (alive and cmd[0] == "r"):
  status = "It's a room full of fire. Game over."
elif (alive and cmd[0] != "y"):
  status = "You chose a door that doesn't exist. Game over."

print(status)