with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

X = 1
begin = False
i = 0
ciclo = 1
register = 0
while i < len(lines):
    if ciclo in [20, 60, 100, 140, 180, 220]:
        register += X*ciclo
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

print(register)