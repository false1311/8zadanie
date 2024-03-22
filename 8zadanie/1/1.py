from itertools import permutations
letters = "смешкилоп"
#list_letters = sorted(letters, reverse=True)


res = 0
for word in permutations(letters, 5):
    word = "".join(word)
    if word.count("е") + word.count("и") + word.count("о") == 3:
        res += 1


print(res)

