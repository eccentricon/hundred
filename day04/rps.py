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

if computer_throw == user_throw:
    print("Draw! 🙀")
elif computer_throw == ROCK and user_throw == SCISSORS:
    print("You lose. 😿")
elif computer_throw == SCISSORS and user_throw == PAPER:
    print("You lose. 😿")
elif computer_throw == PAPER and user_throw == ROCK:
    print("You lose. 😿")
else:
    print("You win! 😺")
print(rules)
