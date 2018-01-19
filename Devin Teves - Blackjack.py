import random
total_value = 0
oponent_total_value = 0


while total_value != 21 or oponent_total_value != 21:
    card = random.randint(1, 13)
    if card < 11:
        total_value += card
        input("You drew a %s. Total value: %s \nType 'end' to end your turn. >" % (card, total_value))
    else:
        if card == 11:
            total_value += 10
            input("You drew a jack. Total value: %d \nType 'end' to end your turn. >" % (total_value))
        elif card == 12:
            total_value += 10
            input("You drew a queen. Total value: %d \nType 'end' to end your turn. >" % (total_value))
        elif card == 13:
            total_value += 10
            input("You drew a king. Total value: %d \nType 'end' to end your turn. >" % (total_value))
        elif card == 1:
            choice = input("You drew an ace. Would you like 1, or 11? \n>")
            if choice == 1:
                total_value += 1
            else:
                total_value += 11
                input("Total value: %d \nType 'end' to end your turn. >" % (total_value)    )

    oponent_card = random.randint(1, 14)
    if oponent_card >= 11:
        oponent_total_value += oponent_card
        print("Your oponent drew a %d. Their total value: %d" %(oponent_card, oponent_total_value))
    else:
        if oponent_card == 11:
            oponent_total_value += 10
        elif oponent_card == 12:
            oponent_total_value += 10
        elif oponent_card == 13:
            oponent_total_value += 10
        elif oponent_card == 1:
            if oponent_total_value <= 10:
                oponent_total_value += 11
            else:
                oponent_total_value += 1
        else:
            oponent_total_value += card

  # if total_value == 21:
  #   print(")




