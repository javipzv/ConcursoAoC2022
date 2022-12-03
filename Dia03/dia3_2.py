from math import ceil
with open('input.txt', 'r') as f:
    lines = f.readlines()

lower = list(map(chr, range(97, 123)))
dict_letras = {n:lower.index(n)+1 for n in lower}

priorities_sum = 0
for i in range(0, len(lines), 3):
    for letter in lines[i][:-1]:
        if (letter in lines[i+1][:-1]) and (letter in lines[i+2][:-1]):
            if letter in lower:
                sum = dict_letras[letter]
            else:
                sum = dict_letras[letter.lower()]+26
            priorities_sum += sum
            break

print(priorities_sum)