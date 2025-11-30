try:
    # Define the input file path and the output file path
    file_path = "top_english_nouns_lower_10000.txt"
    output_path = "filtered_word_list.txt"

    # Open the input file and read its content
    with open(file_path, "r") as file:
        content = file.read()
        # Split the content into a list of words
        word_list = content.splitlines()

        # Iterate through the word list
        for i in range(len(word_list)):
            # Check if the word length is greater than or equal to 5
            if len(word_list[i]) >= 5:
                # Append the word to the output file
                with open(output_path, "a") as output_file:
                    output_file.write(word_list[i].strip() + "\n")

# Handle the case where the input file is not found
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
# Handle any other exceptions that may occur
except Exception as e:
    print(f"An error occurred: {e}")
