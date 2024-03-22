from itertools import product


letters = "актуш"


k = 1
for word in product(letters, repeat = 5):
    word = "".join(word)
    if str(k)[-1] == "9" and word[0] == "т" and word.count("у") >= 1 and word.count("к") == 0 and word.count("н") == 0:
        print(k)
        break
    k += 1
