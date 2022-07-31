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

print('Game Rules\n1. Rock wins against Scissors.\n2. Scissors win against Paper.\n3. Paper win against Rock.')

user_input = int(input('What do you choose, type 0 for Rock, 1 for Paper and 2 for Scissors : '))

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)

comp_input = random.randint(0, 2)
print(f'computer selected : {comp_input}')

if comp_input == 0:
    print(rock)
elif comp_input == 1:
    print(paper)
elif comp_input == 2:
    print(scissors)

if user_input == 0 and comp_input == 2:
    print('computer chose Scissors, you won')
elif user_input == 2 and comp_input == 1:
    print('computer chose Paper, you won')
elif user_input == 1 and comp_input == 0:
    print('computer chose Rock, you won')
elif user_input == 1 and comp_input == 2:
    print('computer chose Scissors, you lost')
elif user_input == 2 and comp_input == 0:
    print('computer chose Rock, you lost')
elif user_input == 0 and comp_input == 1:
    print('computer chose Paper, you lost')
elif user_input == comp_input:
    print('computer chose the same. it is a tie')
else:
    print()
