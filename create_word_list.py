import random

try:
    file_path = "top_english_nouns_lower_10000.txt"
    output_path = "filtered_word_list.txt"
    with open(file_path, "r") as file:
        content = file.read()
        word_list = content.splitlines()
        for i in range(len(word_list)):
            if len(word_list[i]) >= 5:
                with open(output_path, "a") as output_file:
                    output_file.write(word_list[i].strip() + "\n")


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
