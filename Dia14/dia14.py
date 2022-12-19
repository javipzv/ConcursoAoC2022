import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

map = [["."]*1000 for i in range(1000)]

for rock in lines:
    xy = re.findall("[0-9]*,[0-9]*", rock)
    x_old, y_old = None, None
    for value in xy:
        x, y = value.split(",")
        x, y = int(x), int(y)
        if x_old is None:
            map[y][x] = "#"
        else:
            if x > x_old:
                aux_x = x
                while aux_x >= x_old:
                    map[y][aux_x] = "#"
                    aux_x -= 1
            elif x < x_old:
                aux_x = x
                while aux_x <= x_old:
                    map[y][aux_x] = "#"
                    aux_x += 1
            elif y > y_old:
                aux_y = y
                while aux_y >= y_old:
                    map[aux_y][x] = "#"
                    aux_y -= 1
            elif y < y_old:
                aux_y = y
                while aux_y <= y_old:
                    map[aux_y][x] = "#"
                    aux_y += 1
        
        x_old, y_old = x, y

blocks = 0
max_y = 0
while True:
    try:
        y, x = (0, 500)
        while True:
            if map[y + 1][x] == ".":
                y = y + 1
                continue
            elif map[y + 1][x - 1] == ".":
                x = x - 1
                continue
            elif map[y + 1][x + 1] == ".":
                x = x + 1
                continue
            map[y][x] = "o"
            blocks += 1
            break
    except IndexError:
        break

print(blocks)