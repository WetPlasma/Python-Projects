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


list= [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game!\n")
a=int(input("What will you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
if a>=0 and a<3:
    if a==0:
      print(list[0])
    elif a==1:
      print(list[1])
    elif a==2:
      print(list[2])
    
    c=random.randint(0,2)
    print(f"Computer chose {c}")
    if c==0:
      print(list[0])
    elif c==1:
      print(list[1])
    elif c==2:
      print(list[2])
    
    if a==0 and c==1:
      print("You lose")
    if a==0 and c==2:
      print("You win")
    if a==1 and c==0:
      print("You win")
    if a==1 and c==2:
      print("You lose")
    if a==2 and c==0:
      print("You lose")
    if a==2 and c==1:
      print("You win")
    if a==c:
      print("It's a draw")
else:
  print("You typed an invalid number, you lose!")
