word = "string"


def hide(word):
    return ["_"] * len(word)


current = hide(word)


def guess(letter, curr, word):
    letter = letter.lower()
    word = word.lower()

    result = current[:]  # list copy
    found = False

    for i, ch in enumerate(word):
        if ch == letter:
            result[i] = letter
            found = True

    return result, found
