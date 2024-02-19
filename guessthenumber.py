import random
import math

def number_guessing():
    
    print("Welcome to the number guessing game! Let's begin")
    lower = int(input("Enter the initial range"))
    high = int(input("Enter the end range"))
    n = random.randint(lower,high)

    print("\n\tYou've only ", round(math.log(high - lower + 1, 2)),"chances to guess the integer!\n")
    count = 0

    while count < math.log(high - lower + 1, 2):
        guess = int(input("Enter you guessed number"))
        if n == guess:
            print(f"Hurraay!! You made the right guess after {count} trials!")
            break
        elif n < guess:
            print("Try Again! You guessed higher")
        elif n > guess:
            print("Try Again! You guessed lower")
        count += 1

    if n != guess:
        print(f"Oops!! The number is {n}. Better luck next time!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing()
    else:
        print("Thanks for playing!")
    
    try:
        if lower > high:
            raise ValueError("Lower bound must be smaller than upper bound")
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please enter valid integers for the range")
        number_guessing()


def computer_guess():
    print("Now let the computer guess your magic number")
    low = 1
    high = int(input("Enter a number as upper limit"))
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

if __name__ == "__main__":
    number_guessing()
    computer_guess()
