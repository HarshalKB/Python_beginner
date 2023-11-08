import random

rps = [" ", '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''', '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

computer = random.randint(1, 3)
print('''
Welcome to rock-paper-scissors game.
Type 1 for rock, 2 for paper and 3 for scissors.
''')
player = int(input())
print(f'''
You chose:
{rps[player]}
And Computer chose:
{rps[computer]}
''')
if player == computer:
    print("It's a draw.")
elif player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
    print("You Win!")
else:
    print("You Lose!")
