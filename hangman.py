import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'The solution is {chosen_word}.')


display = []

for _ in range(word_length):
    display += "_"

# Create a variable and name it negative. The code will loop until it becomes positive. If it becomes positive, the game is over, either lost (not done yet) or won.
end_game = False
live = 6
while not end_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess != chosen_word:
        live -= 1
        if live == 0:
            end_game = True
            print('You lose.')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print('You win.')
