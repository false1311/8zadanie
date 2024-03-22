letters = "привет"


list_words = []
for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    word = letter1 + letter2 + letter3 + letter4 + letter5
                    list_words.append(word)  # добавление в массив всех слов


new_list_words = []
for i in range(len(list_words)):  # создание массива без каждого третьего и пятого слова
    if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
        new_list_words.append(list_words[i])
        

res = 0
k = 1
for word in new_list_words:
    if "и" not in word and "е" not in word:  # проверка на отсутствие гласных
        res = k
    k+=1


print(res)