from math import floor

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

dict_inspections = {i:0 for i in range(8)}
dict_monkeys = {i:[] for i in range(8)}

for i in range(0, len(lines), 7):
    items = list(map(int, lines[i + 1][18:].split(", ")))
    dict_monkeys[i/7] += items

for j in range(1, 21):
    monkey_num = 0
    for i in range(0, len(lines), 7):
        for item in dict_monkeys[i/7]:
            dict_inspections[i/7] += 1
            if lines[i+2][25:] == "old":
                num = item
            else:
                num = int(lines[i+2][25:])
            if "*" in lines[i+2]:
                result = item * num
            else:
                result = item + num
            if floor(result/3) % int(lines[i+3][21:]) == 0:
                dict_monkeys[int(lines[i+4][29])] += [floor(result/3)]
            else:
                dict_monkeys[int(lines[i+5][30])] += [floor(result/3)]
        
            index = dict_monkeys[monkey_num].index(item)
            dict_monkeys[monkey_num][index] = 0
        dict_monkeys[monkey_num] = list(filter(lambda x: x != 0, dict_monkeys[monkey_num]))
        monkey_num += 1

max1 = max(dict_inspections.values())
dict_inspections = {k:v for k,v in dict_inspections.items() if v != max1}
max2 = max(dict_inspections.values())
print(max1*max2)