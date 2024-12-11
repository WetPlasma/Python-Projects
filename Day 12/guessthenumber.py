import random

def play_guess_the_number():
  """Plays a 'Guess the Number' game with three difficulty levels."""

  print("Welcome to Guess the Number!")
  difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
  number = random.randint(1, 100)


  attempts = 0
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'medium':
    attempts = 7
  elif difficulty == 'hard':
    attempts = 5
  else:
    print("Invalid difficulty. Defaulting to easy.")
    attempts = 10

  for i in range(attempts):
    guess = int(input(f"Guess a number between 1 and 100 (attempt {i+1}/{attempts}): "))
    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Congratulations! You guessed the number {number} in {i+1} attempts.")
      return
  print(f"You ran out of attempts. The number was {number}")
play_guess_the_number()
