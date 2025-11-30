import random

try:
    file_path = "top_english_nouns_lower_10000.txt"

    with open(file_path, "r") as file:
        content = file.read()
        word_list = content.splitlines()
        chosen_word = word_list[random.randint(0, len(word_list) - 1)]
    print(chosen_word)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
