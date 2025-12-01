try:
    file_path = "top_english_nouns_lower_10000.txt"
    file_path = "filtered_word_list.txt"

    with open(file_path, "r") as file:
        content = file.read().strip()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


counts = {}

for char in content:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1
sorted_counts = sorted(counts.items(), key=lambda x: x[1])
print(sorted_counts)
