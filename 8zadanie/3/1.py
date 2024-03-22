from itertools import product 


letters = "привет"
list_letters = sorted(letters)


list_words = []
for word in product(list_letters, repeat = 5):  # создание массива из всех возможных слов
    word = "".join(word)
    list_words.append(word)


new_list_words = []
for i in range(len(list_words)):  # создание массива без каждого третьего и пятого слова
    if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
        new_list_words.append(list_words[i])
        

k = 1
for word in new_list_words:
    if "и" not in word and "е" not in word:  # проверка на отсутствие гласных
        res = k
    k+=1


print(res)
