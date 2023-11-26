#!/usr/bin/env python
"""100 Days of Coding: Day 4 examples."""

# import random

# # Random integers between 1 and 10, inclusive
# random_int = random.randint(1, 10)
# print(random_int)

# # Random float between 0.0 and 1.0, exclusive
# random_float = random.random()
# print(random_float)

# # Random float between 0.0 and 5.0
# random_float = random.random() * 5
# print(random_float)

# U.S. states in order of admission
states = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

print(states[0])
print(states[1])
print(states[-1])
print(states)
print("type(states): ", type(states))

states.append("Theodoria")
print(states)
