with open('input.txt', 'r') as f:
    lines = f.readlines()

for i in range(len(lines[0])):
    myset = {i for i in lines[0][i:i+14]}
    if len(myset) == 14:
        index = i + 14
        break

print(index)
