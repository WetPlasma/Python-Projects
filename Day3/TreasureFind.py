print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input("Your choice: ").lower()

if choice1 == "left":
  print("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  choice2 = input("Your choice: ").lower()
  if choice2 == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    choice3 = input("Your choice: ").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  elif choice2 == "swim":
    print("You get attacked by an angry trout. Game Over.")
  else:
    print("You fell into a hole. Game Over.")
elif choice1 == "right":
  print("You come to a cave. Do you go 'in' or 'around' the cave?")
  choice2 = input("Your choice: ").lower()
  if choice2 == "in":
    print("You found the treasure! You Win!")
  elif choice2 == "around":
    print("You fall into a bottomless pit. Game Over.")
  else:
    print("You chose an invalid option. Game Over.")
else:
  print("You chose an invalid option. Game Over.")
