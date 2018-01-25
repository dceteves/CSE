'''
1. word bank
2. random item selection to guess
3. Take in a letter and add it to a list of letters_guessed
4. hide and reveal letters
5. win/lose condition
'''
import random
import string

word_bank = ["special", "computer", "python", "programming", "burger",
             "tablet", "pycharm", "github", "edison", "javascript"]
guesses = 10
guessesTaken = []
# random_word = random.choice(word_bank)
random_word = "programming"
random_word = random_word.lower()
wordList = list(random_word)
input("Press enter to play Hangman")
display_wordList = []
while guesses != 0:

    print(wordList)
    print(display_wordList)
    print(''.join(display_wordList))
    if len(wordList) == 0:
        break
    guess = input("Guess a letter >")
    guessesTaken.append(guess)
    for letter in wordList:
        if guess == letter:
            display_wordList.append(guess)
        else:
            if letter != "*":
                display_wordList.append("*")









