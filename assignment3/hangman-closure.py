# Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        word_progress = ""

        for character in secret_word:
            if character in guesses:
                word_progress += character
            else:
                word_progress += "_"

        print(word_progress)

        return all(character in guesses for character in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    hangman = make_hangman(secret_word)

    guessed = False

    while not guessed:
        letter = input("Guess a letter: ").lower()
        guessed = hangman(letter)

    print("You guessed the word!")
