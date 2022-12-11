with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
space = [["."]*39 for i in range(6)]

X = 1
begin = False
i = 0
ciclo, row = 0, 0

while i < len(lines):
    if ciclo in list(range(X-1, X+2)):
        space[row][ciclo] = "#"
    if ciclo % 40 == 0 and ciclo != 0:
        row += 1
        ciclo = 0
        continue
    if lines[i][0:4] == 'noop':
        i += 1
    elif lines[i][0:4] == 'addx':
        if begin:
            begin = False
            X += int(lines[i][5:])
            i += 1
        else:
            begin = True
    ciclo += 1

for row in space:
    for i in row:
        print(i, end=" ")
    print()
