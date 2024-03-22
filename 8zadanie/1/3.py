letters = "смешкилоп"
res = 0


for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    word = letter1 + letter2 + letter3 + letter4 + letter5
                    if len(set(word)) == len(word):  # проверка на отсутсвие повторяющихся букв
                        if word.count("е") + word.count("о") + word.count("и") == 3:  # проверка на максимальное количество гласных
                            res += 1


print(res)
