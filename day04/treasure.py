line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

# Impl #1
# col = position[0].lower()
# row = position[1]
# if col == 'a':
#   map_col = 0
# elif col == 'b':
#   map_col = 1
# else:
#   map_col = 2

# if row == '1':
#   map_row = 0
# elif row == '2':
#   map_row = 1
# else:
#   map_row = 2

# map[map_row][map_col] = 'X'

# Impl #2
letter = position[0].lower()
letter_index = "abc".index(letter)
number_index = int(position[1]) - 1

print(f"letter_index={letter_index}")
print(f"number_index={number_index}")
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
