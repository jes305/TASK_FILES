# reverse only alphabets in strings without changing position


def revlet(text):
    letters = []
    for ch in text:
        if ch.isalnum():
            letters.append(ch)
            #print(letters[-1::-1])
            
            
    result = "  "
    for ch in text:
        if ch.isalnum():
            result += letters.pop()
        else:
            result += ch
    return result
print(revlet("a2$mrita"))





