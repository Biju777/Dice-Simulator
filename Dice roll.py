import random


def dice(min_number, max_number):
    bot_number = random.randint(min_number, max_number)
    print(f"Dice rolling...")
    print(f"The number is {bot_number}")
    # Take input from user if he want to play again.
    again = input("If you want to play again press 'y' or 'n' for exit: ")
    # handle the user input
    if again.lower() == 'y':
        dice(1, 6)

    elif again == 'n':
        exit()


dice(1, 6)
