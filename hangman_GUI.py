import tkinter as tk
import hangman


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.minsize(400, 200)

        self.game = hangman.Hangman()
        self.setup_ui()

        self.root.bind("<Return>", self.on_enter)

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.word_label = tk.Label(
            self.main_frame,
            text=self.game.render(),
            font=("Helvetica", 16),
            anchor="center",
        )
        self.word_label.pack(pady=10, fill="x")

        self.attempts_label = tk.Label(
            self.main_frame,
            text=f"Attempts remaining: {self.game.attempts}",
            font=("Helvetica", 14),
            anchor="center",
        )
        self.attempts_label.pack(pady=5, fill="x")

        self.input_frame = tk.Frame(self.main_frame)
        self.input_frame.pack(pady=10)

        self.letter_entry = tk.Entry(
            self.input_frame, width=5, font=("Helvetica", 14), justify="center"
        )
        self.letter_entry.pack(side=tk.LEFT, padx=5)
        self.letter_entry.focus_set()

        self.guess_button = tk.Button(
            self.input_frame,
            text="Guess",
            command=self.make_guess,
            font=("Helvetica", 14),
        )
        self.guess_button.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(
            self.main_frame,
            text="Type a letter and press Guess or Enter.",
            font=("Helvetica", 12),
            anchor="center",
        )
        self.status_label.pack(pady=5, fill="x")

    def on_enter(self, event):
        self.make_guess()

    def make_guess(self):
        letter = self.letter_entry.get().strip().lower()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            self.status_label.config(text="Please enter a single letter (a–z).")
            return

        found = self.game.guess(letter)
        self.word_label.config(text=self.game.render())
        self.attempts_label.config(text=f"Attempts remaining: {self.game.attempts}")

        if found:
            self.status_label.config(text=f"The letter '{letter}' is in the word.")
        else:
            self.status_label.config(text=f"The letter '{letter}' is not in the word.")

        if self.game.is_won():
            self.status_label.config(
                text=f"Congratulations! You've guessed the word: {self.game.word}"
            )
            # Disable input after game ends
            self.letter_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.root.after(1500, self.root.quit)
        elif self.game.is_lost():
            self.status_label.config(
                text=f"Game over! The correct word was: {self.game.word}"
            )
            self.letter_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.root.after(1500, self.root.quit)


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
