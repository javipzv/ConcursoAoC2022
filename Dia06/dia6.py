with open('input.txt', 'r') as f:
    lines = f.readlines()

for i in range(len(lines[0])):
    myset = {i for i in lines[0][i:i+4]}
    if len(myset) == 4:
        index = i + 4
        break

print(index)
