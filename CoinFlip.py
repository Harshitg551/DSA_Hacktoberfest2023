import random

def play_game():
    print("Welcome to the Coin Flip Game!")

    while True:
        user_guess = input("Guess heads or tails (enter 'h' for heads or 't' for tails, or 'q' to quit): ").lower()

        if user_guess == 'q':
            print("Thank you for playing. Goodbye!")
            return

        if user_guess not in ['h', 't']:
            print("Invalid input. Please try again.")
            continue

        # Simulate a coin flip
        coin_result = random.choice(['h', 't'])

        print("Flipping the coin...")

        # Display the result
        print("The coin landed on:", 'heads' if coin_result == 'h' else 'tails')

        # Check if the player's guess matches the result
        if user_guess == coin_result:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed incorrectly.")

if __name__ == "__main__":
    play_game()
