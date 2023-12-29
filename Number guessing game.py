import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I've picked a random number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        # Get user input
        try:
            user_guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts += 1
    
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing!")

# Run the game
guess_the_number()

