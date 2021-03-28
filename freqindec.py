def dict(x):
    d = {}
    for letter in x:
        d[letter] = 1 + d.get(letter, 0)
    return d


def most_frequent(str):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    d = dict(letters)
    r = []
    for key in d:
        r.append((d[key], key))
    r.sort(reverse=True)
    for c, letter in r:
        print (letter, c)

most_frequent("missisippi")
