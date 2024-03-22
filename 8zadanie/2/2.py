letters = "актуш"


k = 1
res = []
for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    word = letter1 + letter2 + letter3 + letter4 + letter5
                    if str(k)[-1] == "9" and word[0] == "т" and word.count("у") >= 1 and word.count("к") == 0 and word.count("н") == 0:
                        res.append(k)
                    k += 1

print(res[0])