import tkinter as tk
from tkinter import messagebox
import hangman


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.game = hangman.Hangman()
        self.setup_ui()

    def setup_ui(self):
        self.word_label = tk.Label(
            self.root, text=self.game.render(), font=("Helvetica", 16)
        )
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts remaining: {self.game.attempts}",
            font=("Helvetica", 14),
        )
        self.attempts_label.pack(pady=5)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.letter_entry = tk.Entry(self.input_frame, width=5, font=("Helvetica", 14))
        self.letter_entry.pack(side=tk.LEFT, padx=5)

        self.guess_button = tk.Button(
            self.input_frame,
            text="Guess",
            command=self.make_guess,
            font=("Helvetica", 14),
        )
        self.guess_button.pack(side=tk.LEFT, padx=5)

    def make_guess(self):
        letter = self.letter_entry.get().strip().lower()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        found = self.game.guess(letter)
        self.word_label.config(text=self.game.render())
        self.attempts_label.config(text=f"Attempts remaining: {self.game.attempts}")

        if found:
            messagebox.showinfo(
                "Correct Guess", f"The letter '{letter}' is in the word!"
            )
        else:
            messagebox.showinfo(
                "Incorrect Guess", f"The letter '{letter}' is not in the word."
            )

        if self.game.is_won():
            messagebox.showinfo(
                "Game Over",
                f"Congratulations! You've guessed the word: {self.game.word}",
            )
            self.root.quit()
        elif self.game.is_lost():
            messagebox.showinfo(
                "Game Over", f"Game over! The correct word was: {self.game.word}"
            )
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
