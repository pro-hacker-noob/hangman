import random

try:
    file_path = "filtered_word_list.txt"
    with open(file_path, "r") as file:
        content = file.read()
        word_list = content.splitlines()
        word = random.choice(word_list).strip()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    word = "ERROR"


def hide(word):
    return ["_"] * len(word)


current_state = hide(word)


def guess(letter, word, current_state=current_state):
    letter = letter.lower()
    word = word.lower()

    result = current_state[:]
    found = False

    for i, ch in enumerate(word):
        if ch == letter:
            result[i] = letter
            found = True

    return result, found


def render(current_state):
    return " ".join(current_state)


def is_won(current_state):
    return "_" not in current_state


def input_letter():
    while True:
        letter = input("Enter a letter: ").strip().lower()
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
    attempts = 6
    current_state = hide(word)

    print("Welcome to Hangman!")
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
