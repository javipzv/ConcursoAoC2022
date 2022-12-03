from math import ceil
with open('input.txt', 'r') as f:
    lines = f.readlines()

lower = list(map(chr, range(97, 123)))
dict_letras = {n:lower.index(n)+1 for n in lower}

priorities_sum = 0
for rucksack in lines:
    mitad = ceil((len(rucksack) - 2) / 2)
    first_compartment = rucksack[:mitad]
    second_compartment = rucksack[mitad:-1]
    for letter in first_compartment:
        if letter in second_compartment:
            if letter in lower:
                sum = dict_letras[letter]
            else:
                sum = dict_letras[letter.lower()]+26
            priorities_sum += sum
            break

print(priorities_sum)