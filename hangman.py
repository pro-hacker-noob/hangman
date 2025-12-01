import random

HIDDEN_LETTER = "_"

try:
    file_path = "filtered_word_list.txt"
    with open(file_path, "r") as file:
        content = file.read()
        word_list = content.splitlines()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    word = "ERROR"
    print("Using default word 'ERROR' for the game.")
except Exception as e:
    print(f"An error occurred: {e}")
    word = "ERROR"
    print("Using default word 'ERROR' for the game.")


def get_word():
    return random.choice(word_list).strip().lower()


def hide(word):
    global HIDDEN_LETTER
    return [HIDDEN_LETTER if ch != " " else " " for ch in word]


def guess(letter, word, current_state):

    result = current_state[:]
    found = False

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                result[i] = letter
                found = True

    return result, found


def render(current_state):
    return " ".join(current_state)


def is_won(current_state):
    return HIDDEN_LETTER not in current_state


def input_letter():
    while True:
        letter = input("Enter a letter: ").strip().lower()
        if letter.strip().lower() == "exit":
            print("Exiting the game. Goodbye!")
            exit()
        if len(letter) == 1 and letter.isalpha():
            return letter
        print("Invalid input. Please enter a single letter.")


def turn(word, current_state, attempts):
    print("\nCurrent state: " + render(current_state))
    letter = input_letter()
    new_state, found = guess(letter, word, current_state)

    if found:
        print(f"The letter '{letter}' is in the word.")
    else:
        print(f"the letter '{letter}' is not in the word.")
        attempts -= 1

    return attempts, new_state


def is_lost(attempts):
    return attempts <= 0


def main():
    word = get_word()
    attempts = 6
    current_state = hide(word)

    print("Welcome to Hangman! type 'exit' to quit the game anytime.")
    print(f"You have {attempts} attempts to guess the word.")

    while not is_won(current_state) and not is_lost(attempts):
        print(f"\nAttempts remaining: {attempts}")
        attempts, current_state = turn(word, current_state, attempts)

    if is_won(current_state):
        print(f"\nCongratulations You've guessed the word: {word}")
    else:
        print(f"\nGame over The correct word was: {word}")


if __name__ == "__main__":
    main()
