word = "string"

def hide(word):
    return ["_"] * len(word)

curr = hide(word)

def guess(letter, curr, word):
    letter = letter.lower()
    word = word.lower()

    result = curr[:]  # list copy
    found = False

    for i, ch in enumerate(word):
        if ch == letter:
            result[i] = letter
            found = True

    return result, found

