letters = ["a","b","c"]
for letter in letters:
    print(letter)

letters = ["a","b","c"]
for letter in enumerate(letters):
    print(letter)

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0],letter[1])

letters = ["a", "b", "c"]
items = (0,"a")
index,letter = items
for index, letter in enumerate(letters):
    print(index,letter)

letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index,letter)
