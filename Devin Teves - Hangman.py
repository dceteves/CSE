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
guesses_taken = []
random_word = random.choice(word_bank)
# random_word = "programming"
random_word.lower()
wordlist = []
display_wordlist = []
for letter in random_word:
    wordlist.append(letter)
    display_wordlist.append("*")

input("Press enter to play Hangman")

while guesses != 0:
    print(wordlist)
    print(display_wordlist)
    print(''.join(display_wordlist))
    if len(wordlist) == 0:
        break
    guess = input("Guess a letter >")
    guesses_taken.append(guess)
    for letter in wordlist:
        if guess == letter:
            wordlist.remove(guess)
        display_wordlist[random_word.index(guess)] = guess










