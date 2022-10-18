#!/usr/bin/env python3

# Made By Jaydin Madore
# Made On Oct 18, 2022
# This program checks if the user guessed a number correctly


import random


def main():

    # Assigns a random number from 0-9 to the random_number variable.
    random_number = random.randint(0, 9)

    # Requests the user's guess.
    print("The random number is within the range of 0-9")
    user_guess = input("Enter your guess: ")

    # Tries casting user_guess from string to int.
    try:
        user_guess = int(user_guess)

    # Executed if user_guess cannot be converted to int.
    except ValueError:
        print("You did not enter an integer.")

    # Executed if user_guess is not between 0 and 9
    if user_guess < 0 or user_guess > 9:
        print(f"Invalid guess!\nIt should be between 0 and 9.")
        main()
        # Loops through code until user_guess is an integer
        while not isinstance(user_guess, int):
            print("The random number is within the range of 0-9")
            user_guess = input("Enter your guess: ")

            # Tries casting user_guess from string to int.
            try:
                user_guess = int(user_guess)

                # If user_guess is an integer, the loop is broken
                break
            except ValueError:
                print("Please try again.")

    # Executed if the user guessed correctly.
    if random_number == user_guess:
        print("You guessed correctly!")

    # Executed if the user guessed incorrectly.
    else:
        print(f"You guessed incorrectly. The correct answer was {random_number}")


if __name__ == "__main__":
    main()
