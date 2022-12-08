with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

# Edge trees
visible_on_edge = 2*len(lines[0]) + 2*len(lines) - 4

# Interior trees
def visible_from_top(list, index, row, value):
    visible = True
    for trees in list[row-1::-1]:
        if not int(trees[index]) < value:
            visible = False
            break
    return visible

def visible_from_below(list, index, row, value):
    visible = True
    for trees in list[row+1:]:
        if not int(trees[index]) < value:
            visible = False
            break
    return visible

def visible_from_left(list, index, row, value):
    visible = True
    for tree in list[row][index-1::-1]:
        if not int(tree) < value:
            visible = False
            break
    return visible

def visible_from_right(list, index, row, value):
    visible = True
    for tree in list[row][index + 1:]:
        if not int(tree) < value:
            visible = False
            break
    return visible

def is_visible(list, index, row, value):
    return visible_from_top(list, index, row, value) or visible_from_below(list, index, row, value) or visible_from_right(list, index, row, value) or visible_from_left(list, index, row, value)

visible_inside = 0
row = 0
for trees in lines[1:-1]:
    index = 0
    row += 1
    for tree in trees[1:-1]:
        index += 1
        if is_visible(lines, index, row, int(tree)):
            visible_inside += 1

print(visible_on_edge + visible_inside)

