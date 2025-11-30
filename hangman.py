import random

try:
    file_path = "filtered_word_list.txt"
    with open(file_path, "r") as file:  # open the file in read mode
        content = file.read()
        word_list = content.splitlines()  # read words from the file into a list
        word = random.choice(word_list).strip()  # select a random word from the list
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    word = "ERROR"  # Fallback word if file not found


def hide(word):
    return ["_"] * len(
        word
    )  # returns a list of underscores representing hidden letters


current_state = hide(word)


def guess(
    letter, word, current_state=current_state
):  # returns updated current_state and whether the letter was found
    letter = letter.lower()
    word = word.lower()

    result = current_state[:]  # list copy
    found = False

    for i, ch in enumerate(word):  # iterate through each character in the word
        if ch == letter:
            result[i] = letter
            found = True

    return (
        result,
        found,
    )  # return updated current_state and whether the letter was found
