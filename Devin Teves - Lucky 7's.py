from random import randint
rounds = 0
money = 15
highest = 0
while money != 0:
    die, die2 = randint(0, 6), randint(0, 6)
    rounds += 1
    print("Round %s!" % rounds)
    if die + die2 == 7:
        money += 4
        print("You won money! \nYou have $%s. \n" % money)
    elif die + die2 != 7:
        money -= 1
        print("You lost money! You rolled %s. \nYou have $%s. \n" % (die + die2, money))
    if money > highest:
        highest = money
    print(highest)
print("You ran out of money! It took you %s rounds until you lost all of your money. "
      "\nYour highest was $%s.\nGame over." % (rounds, highest))
