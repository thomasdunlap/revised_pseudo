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

secret_number = random.randint(1,100)
tries = 0
guess = -1
print("Guess the number! It's an integer between 1 and 100, inclusive:")
for _ in range(10):
    guess =  input(">")

    while not guess.isdigit() or int(guess) > 100 or int(guess) < 1:
        print("Oops! Your guess must be an integer between 1 and 100 incluse:")
        guess = input(">")

    if int(guess) == secret_number:
        print("{} is correct! You did it!".format(secret_number))
        break
    if tries == 9:
        print("The number was {}. Better luck next time!".format(secret_number))
        break
    print("Sorry! Try again!")
    tries += 1
