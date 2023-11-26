"""Banker Roulette"""
import random

names_string = input("Names: ")
# Convert the input into an array seperating
# each name in the input by a comma and space.
names = names_string.split(", ")

index = random.randint(0, (len(names) - 1))
print(f"{names[index]} is going to buy the meal today!")
