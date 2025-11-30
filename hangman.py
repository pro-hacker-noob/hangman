word = "string"


def hide():
    return "_" * len(word)


curr = hide()

n = len(word)


def guess(letter, curr):
    letter = letter.lower()
    return "".join(word[i] if word[i].lower() == letter else curr[i] for i in range(n))
