#!/usr/bin/env python

# Treasure Island

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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You're at a crossroad. Where do you want to go?")
cmd = input("[Hint: Type \"left\" or \"right\"]: ").lower()
if (cmd[0] == "l"):
  print("You've come to a lake. There is an island in the middle of the lake.")
  cmd = input("[Hint: Type \"wait\" to wait for a boat, or \"swim\" to swim across]: ").lower()
  if (cmd[0] == "w"):
    print("You arrive at the island unharmed. There is a house with 3 doors.", 
          "One red, one yellow and one blue. Which colour do you choose?")
    cmd = input("[Hint: Type \"red\", \"yellow\", or \"blue\"]: ").lower()
    if (cmd[0] == "y"):
      status = "You found the treasure! You win!"
    elif (cmd[0] == "b"):
      status = "You enter a room of beasts. Game over."
    elif (cmd[0] == "r"):
      status = "It's a room full of fire. Game over."
    else:
      status = "You chose a door that doesn't exist. Game over."
  else:
    status = "You get attacked by an angry trout. Game over."
else:
  status = "You fell into a hole. Game over."

print(status)