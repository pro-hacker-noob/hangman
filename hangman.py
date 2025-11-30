word = "string"
word_len = len(word)


def hide(word=word):
    return "_" * word_len


curr = hide()


def guess(letter, curr):
    letter = letter.lower()
    return "".join(word[i] if word[i].lower() == letter else curr[i] for i in range(n))
