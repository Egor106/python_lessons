
def thesaurus(*args):
    names = {}
    for i in sorted(args):
        letters = i[0]
        if letters in names:
            names[letters] += [i]
        else:
            names[letters] = [i]
    return names
print(thesaurus("Иван", "Мария", "Петр", "Илья"))