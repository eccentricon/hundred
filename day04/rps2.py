"""The classic rock-paper-scissors game.

1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock.

Start: https://replit.com/@appbrewery/rock-paper-scissors-start
Solution: https://replit.com/@appbrewery/rock-paper-scissors-end

https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
"""
import random

ROCK = 0
PAPER = 1
SCISSORS = 2

rules = """
1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock.
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

throws = [rock, paper, scissors]
throw_names = ["rock", "paper", "scissors"]

user_throw = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if user_throw > SCISSORS:
    user_throw = SCISSORS
elif user_throw < ROCK:
    user_throw = ROCK

print(f"You chose {throw_names[user_throw]}.")
print(throws[user_throw])

computer_throw = random.randint(ROCK, SCISSORS)

print(f"Computer chose {throw_names[computer_throw]}.")
print(throws[computer_throw])

WIN = "You win! 😺"
LOSE = "You lose. 😿"
DRAW = "Draw! 🙀"

#       0/0   0/1  0/2     1/0   1/1   1/2    2/0  2/1   2/2
#       R/R   R/P  R/S     P/R   P/P   P/S    S/R  S/P   S/S
map = [[DRAW, WIN, LOSE], [LOSE, DRAW, WIN], [WIN, LOSE, DRAW]]

print(map[computer_throw][user_throw])
print(rules)
