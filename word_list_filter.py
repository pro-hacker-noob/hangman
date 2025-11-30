file_path = "top_english_nouns_lower_10000.txt"
with open(file_path, "r") as file:
    content = file.read()
    word_list = content.splitlines()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip()
        if len(word_list[i]) >= 5:
            print(word_list[i])
