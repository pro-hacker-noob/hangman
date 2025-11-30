word = "string"
word_len = len(word)


def hide(word=word):
    return "_" * len(word)


curr = hide()


def guess(letter, curr, word):
    letter = letter.lower()
    word = word.lower()
    if letter not in word:
        return False
    result = curr[:]

    for i, ch in enumerate(word):
        if ch == letter:
            result[i] = letter

    return result
