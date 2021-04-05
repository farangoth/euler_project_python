alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
solution22 = 0

with open("p022_names.txt", "r") as f:
    names = [name.replace("\"", "") for name in f.read().split(",")]
    names = sorted(names)

    for name in names:
        score_name = 0
        for letter in name:
            score_name += alphabet.index(letter) + 1
        solution22 += (names.index(name) + 1) * score_name

print("Sol22: ", solution22)
