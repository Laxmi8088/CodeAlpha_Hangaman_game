import random

def play_hangman():
    words = ["python", "developer", "computer", "keyboard", "software"]

    word_to_guess = random.choice(words)

    guessed_letters = set()

    max_incorrect_guesses = 6
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print("=" * 40)
    print(f"I have selected a random word. You have {max_incorrect_guesses} incorrect guesses allowed.")
    print("Good luck!\n")

    while incorrect_guesses < max_incorrect_guesses:

        display_word = []

        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        current_progress = " ".join(display_word)

        print(f"Word: {current_progress}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word:
            print("\n" + "=" * 40)
            print(f"Congratulations! You won! The word was '{word_to_guess}'.")
            print("=" * 40)
            break

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        print("-" * 30)

    else:
        print("\n" + "=" * 40)
        print(f"Game Over! You ran out of guesses. The word was '{word_to_guess}'.")
        print("=" * 40)

if __name__ == "__main__":
    play_hangman()