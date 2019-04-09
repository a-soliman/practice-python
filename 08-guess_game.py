'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random


def game():
    rand_num = random.randint(1, 10)
    tryes = 0

    while(True):
        guess = input("guesss a number from 1 to 9: ")

        if guess == "exit":
            break

        guess = int(guess)
        tryes += 1

        if (guess == rand_num):
            print("congrats..")
            break

        if guess < rand_num:
            print("up")

        else:
            print("down")

    print(tryes)


game()
