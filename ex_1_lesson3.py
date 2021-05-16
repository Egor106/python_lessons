numbers = {"zero": "ноль", "one": "один", "two": "два", "three": "три",
           "four": "четыре", "five": "пять","six": "шесть", "seven": "семь",
           "eight": "восемь", "nine": "девять", "ten": "десять"}
def num_translate(word):
    return numbers.get(word)
print(num_translate(input("Введите число для перевода:")))
