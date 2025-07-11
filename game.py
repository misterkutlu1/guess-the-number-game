#
# A simple "Guess the Number" game.
#

import random # We need this to generate a random number

def guess_the_number():
    """The main function for the Guess the Number game."""

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0

    print("--- Welcome to Guess the Number! ---")
    print("I have selected a secret number between 1 and 100.")
    print("Can you guess what it is?\n")

    # The main game loop
    while True:
        try:
            # Ask the player for their guess
            guess_str = input("Enter your guess: ")
            
            # Convert the player's input string into an integer
            guess = int(guess_str)
            
            # Increment the number of attempts
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # The player guessed correctly!
                print(f"\nCongratulations! You guessed the number!")
                print(f"The secret number was {secret_number}.")
                print(f"It took you {attempts} attempts.")
                break # Exit the loop since the game is over

        except ValueError:
            # This runs if the player enters text that is not a number
            print("Oops! That's not a valid number. Please enter a number.")

    print("\n--- Thanks for playing! ---")

# This line makes sure the game runs when the script is executed
if __name__ == "__main__":
    guess_the_number()
