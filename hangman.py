# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter.\n").lower()

display = []
for letter in chosen_word:
    if letter == guess:
        display += [guess]
    else:
        display += ['_']
print(display)
