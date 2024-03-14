import random

def choose_word():
    words = ["python", "hangman", "game", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1

    if attempts == 0:
        print("You ran out of attempts! The word was:", word)

if __name__ == "__main__":
    hangman()