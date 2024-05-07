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


import random
moves = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if choice>2:
  print("You enetered an invalid number. ")
else:
  print(moves[choice])
  rand_choice = random.randint(0,2)
  print(f"Computer chose:\n{moves[rand_choice]}")
  if choice==rand_choice:
    print("It's a draw.")
  elif choice==0 and rand_choice==2:
    print("You win.")
  elif choice < rand_choice:
    print("You lose.")
  elif choice==2 and rand_choice==0:
    print("You lose.")
  elif choice > rand_choice:
    print("You win.")
