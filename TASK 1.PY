import random

def display_hangman(tries):
    """Returns a hangman drawing based on the number of tries."""
    hangman_graphics = [
        '''
           ------
           |    |
                |
                |
                |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
                |
                |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
           |    |
                |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
          /|    |
                |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
         =========
        ''', '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
         =========
        '''
    ]
    return hangman_graphics[tries]

def choose_word():
    """Selects a random word from a predefined list."""
    words = ["python", "hangman", "programming", "developer", "computer", "science", "artificial", "intelligence"]
    return random.choice(words)

def play_hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")
    word = choose_word()  # Select a random word
    word_letters = set(word)  # Set of unique letters in the word
    guessed_letters = set()  # Set of letters that the player has guessed
    correct_guesses = set()  # Set of correctly guessed letters
    tries = 0  # Number of incorrect guesses
    max_tries = 6  # Maximum number of incorrect guesses allowed

    while tries < max_tries and correct_guesses != word_letters:
        # Display current state of the word
        word_display = [letter if letter in correct_guesses else '_' for letter in word]
        print(f"Word: {' '.join(word_display)}")
        print(f"Incorrect guesses left: {max_tries - tries}")
        print(display_hangman(tries))

        # Ask the player for a guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            tries += 1
            print(f"Sorry, '{guess}' is not in the word.")

    if correct_guesses == word_letters:
        print(f"Congratulations! You've guessed the word '{word}'.")
    else:
        print(f"Game over! The word was '{word}'.")
        print(display_hangman(tries))

# Run the game
if __name__ == "__main__":
    play_hangman()
