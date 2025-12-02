import random


class Hangman:
    HIDDEN_LETTER = "_"

    def __init__(self):
        try:
            file_path = "filtered_word_list.txt"
            with open(file_path, "r") as file:
                content = file.read()
                self.word_list = content.splitlines()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            self.word_list = ["error"]
        except Exception as e:
            print(f"An error occurred: {e}")
            self.word_list = ["error"]

        self.word = self.get_word()
        self.attempts = 6
        self.current_state = self.hide()

    def get_word(self):
        return random.choice(self.word_list).strip().lower()

    def hide(self):
        return [self.HIDDEN_LETTER if ch != " " else " " for ch in self.word]

    def guess(self, letter):
        found = False
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.current_state[i] = letter
                found = True
        if not found:
            self.attempts -= 1
        return found

    def render(self):
        return " ".join(self.current_state)

    def is_won(self):
        return self.HIDDEN_LETTER not in self.current_state

    def is_lost(self):
        return self.attempts <= 0
