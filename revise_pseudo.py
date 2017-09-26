'''
secret_number = generate a random number between 0 and 100
  guess = -1
  while secret_number != guess
    guess = get a guess input from player
    if guess < secret_number
     say “your guess is low”
    else if guess > secret_number
      say “your guess is high”
   else
      say “you guessed right!”
    end if
  end while
 '''
import random

secret_number = random.randint(0, 100)
tries = 0
guess = -1
print("Guess the number! It's an integer between 0 and 100, inclusive:")
while secret_number != guess:
    guess =  input(">")

    while not guess.isdigit() or int(guess) > 100 or int(guess) < 0:
        print("Oops! Your guess must be an integer between 0 and 100 inclusive:")
        guess = input(">")

    guess = int(guess)
    if guess < secret_number:
        print("Sorry, that guess was too low, try again.")
    elif guess > secret_number:
        print("Sorry, that guess was too high, try again.")
    else:
        print("{} is correct! You win!".format(secret_number))
        break

    if tries == 9:
        print("The number was {}. You lose. Better luck next time!".format(secret_number))
        break
    tries += 1
