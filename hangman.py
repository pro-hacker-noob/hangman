# The secret word players are trying to guess.
word = "string"


def hide(word):
    """
    Create the initial hidden version of the word.
    Each character in the word is replaced with an underscore.
    
    Returns a LIST (not a string) because we want to easily
    replace characters later when the player guesses correctly.
    """
    return ["_"] * len(word)


# Create the starting "hidden" version of the word.
# Example: "string" -> ["_", "_", "_", "_", "_", "_"]
curr = hide(word)


def guess(letter, curr, word):
    """
    Updates the current progress ('curr') based on a guessed letter.
    
    - letter: the character the player guessed
    - curr: the current revealed state of the word (list of chars)
    - word: the actual secret word
    
    Returns:
        (updated_curr, found)
        updated_curr → the new state of the word after applying the guess
        found → True if the letter exists in the word, otherwise False
    """

    # Normalize everything to lowercase so guesses aren't case-sensitive.
    letter = letter.lower()
    word = word.lower()

    # Make a copy so we don't accidentally change the caller's list.
    result = curr[:]
    found = False  # Tracks whether the guessed letter was in the word.

    # Loop through each character in the secret word.
    for i, ch in enumerate(word):

        # If the guessed letter is found, reveal it in the result list.
        if ch == letter:
            result[i] = letter
            found = True  # Mark that the guess was correct.

    # Return both the updated word progress + whether the guess was successful.
    return result, found
