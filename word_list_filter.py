file_path = "top_english_nouns_lower_10000.txt"
output_path = "filtered_word_list.txt"
with open(file_path, "r") as file:
    content = file.read()
    word_list = content.splitlines()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip()
        if len(word_list[i]) >= 5:
            with open(output_path, "w") as output_file:
                output_file.write(word_list[i] + "\n")
