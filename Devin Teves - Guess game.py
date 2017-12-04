from random import randint

guesses = 5
number = randint(0, 50)
guess = input("I'm thinking of a number between 1 and 50. What is my number? >")

while guesses != 0:
    if guess == number:
        print("That's my number! You win.")
        break
    else:
        if int(guess) < number:
            guesses -= 1
            guess = input("That's too low. Try again. \nGuesses left: %s >" % guesses)
        elif int(guess) > number:
            guesses -= 1
            guess = input("That's too high. Try again. \nGuesses left: %s >" % guesses)
        elif str(guess) != int(guess):
            guess = input("That's not a number! Try again. >")

print("You ran out of guesses! My number was %s. \nGame over." % number)




