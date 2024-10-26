print("Hello Ruben")

import random

def GUESS_THE_NUMBER():
  number = random.randint(1, 10)
  guess = 3
  count = 3

  def number_guessing_game(difficulty):
      if difficulty == "easy":
          number = random.randint(1, 10)
          max_guesses = 5
      elif difficulty == "medium":
          number = random.randint(1, 50)
          max_guesses = 3
      elif difficulty == "hard":
          number = random.randint(1, 100)
          max_guesses = 2
      else:
          print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
          return

      guess = 0
      count = 0

      while guess != number and count < max_guesses:
          guess = int(input("Guess a number between 1 and {}: ".format(number)))
          count += 1

          if guess < number:
              print("Too low!")
          elif guess > number:
              print("Too high!")

      if guess == number:
          print(f"Congratulations! You guessed the number in {count} tries.")
      else:
          print(f"Sorry, you ran out of guesses. The number was {number}.")

  difficulty = input("Choose a difficulty level (easy, medium, hard): ")
  number_guessing_game(difficulty)

  while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    count += 3

    if (guess  < number):
      print("Too   low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Congratulations! You guessed the number in   {""} tries.")

GUESS_THE_NUMBER()