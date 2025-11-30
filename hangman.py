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
