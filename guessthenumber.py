import random
import math

def number_guessing():
    
    print("Welcome to the number guessing game! Let's begin")
    lower = int(input("Enter the initial range"))
    high = int(input("Enter the end range"))
    n = random.randint(lower,high)

    print("\n\tYou've only ", round(math.log(high - lower + 1, 2)),"chances to guess the integer!\n")
    count = 0
    guess = int(input("Enter you guessed number"))

    while True:
        count+=1
        if n < guess:
            print("Try Again! You guessed higher")
        elif n > guess:
            print("Try Again! You guessed lower")
        else:
            print(f"Hurraay!! You made the right guess after {count} trials!")
            break
        
        if count >= math.log(high - lower + 1, 2):
            print(f"Oops!! The number is {n}. Better luck next time! ")
            break

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

if __name__ == "__main__":
    number_guessing()