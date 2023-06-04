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

choices_list = [rock, paper, scissors]

cpu_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'"))


print ("You choose: \n" + choices_list[player_choice])
print ("Computer choose:\n" + choices_list[cpu_choice])

if (player_choice == 0 and cpu_choice == 2) or (player_choice == 1 and cpu_choice == 0) or (player_choice == 2 and cpu_choice == 1):
  print ("You win")
elif player_choice == cpu_choice:
  print("Spare")
else:
  print("You lose")
