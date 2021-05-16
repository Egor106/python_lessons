from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(i, rep=False):
    n = nouns.copy()
    adv = adverbs.copy()
    adj = adjectives.copy()
    joke_list = []
    min_len = min(n, adv, adj)
    while i and len(min_len):
        num = randrange(len(min_len))
        if rep:
            joke_list.append(f"{n.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            joke_list.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        i -= 1
    return joke_list

print(get_jokes(10))
