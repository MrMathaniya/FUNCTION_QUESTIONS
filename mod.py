import random
number=random.randint(1,100)
guess=int(input("Guess a number between 1 and 100: "))
if number==guess:
    print("Yes, you've guessed right")
else:
    print("Nope, you guessed wrong try again\n"
          "The number was",number)