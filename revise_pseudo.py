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
while guess != secret_number and tries <= 10:
    guess =  int(raw_input('Guess the number!\n>'))
    if guess == secret_number:
        print('You did it!')
        break
    print(Sorry)
    tries += 1
