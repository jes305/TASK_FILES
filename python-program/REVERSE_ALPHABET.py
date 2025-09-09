# reverse only alphabets in strings without changing position


def revlet(text):
    letters = []
    for ch in text:
        if ch.isalpha():
            letters.append(ch)
    result = "  "
    for ch in text:
        if ch.isalpha():
            result += letters.pop()
        else:
            result += ch
    return result
print(revlet("abcdefgh"))  






