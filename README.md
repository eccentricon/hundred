# 100 Days of Code: The Complete Python Pro Bootcamp for 2023

https://www.udemy.com/course/100-days-of-code/

## Day 4

### Random module

- https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

```
import random

# Random integers between 1 and 10, inclusive
random_int = random.randint(1, 10)
print(random_int)

# Random float between 0.0 and 1.0, exclusive
random_float = random.random()
print(random_float)

# Random float between 0.0 and 5.0
random_float = random.random() * 5
print(random_float)
```

### Lists

https://docs.python.org/3/tutorial/datastructures.html

```
states = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    # etc.
  ]

print(states[0])
print(states[1])
print(states[-1])
print(states)
print("type(states): ", type(states))

states.append("Theodoria")
```