import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
diagram = [rock, paper, scissors]

myscore = int(input(
    "What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))

print(f"You chose:\n{diagram[myscore]}")


number = int(random.randint(0, 2))
print(f"The computer chose:\n{diagram[number]}")

if myscore == number:
    print("It's a draw. Try again.")
elif myscore == 0 and number == 1:
    print("You lose!")
elif myscore == 0 and number == 2:
    print("You win!")
elif myscore == 1 and number == 0:
    print("You win!")
elif myscore == 1 and number == 2:
    print("You lose!")
elif myscore == 2 and number == 0:
    print("You lose!")
elif myscore == 2 and number == 1:
    print("You win!")
