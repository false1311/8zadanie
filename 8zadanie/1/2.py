from itertools import product
letters = "смешкилоп"


res = 0
for word in product(letters, repeat = 5):
    word = "".join(word)
    if len(set(word)) == len(word):  # проверка на остутствие повторяющихся букв
        if word.count("е") + word.count("и") + word.count("о") == 3:  # проверка на максимальное количество гласных
            res += 1


print(res)

