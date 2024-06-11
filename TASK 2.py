
import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number {} correctly in {} attempts.".format(secret_number, attempts))
            break

if __name__ == "__main__":
    guess_number()
