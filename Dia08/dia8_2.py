with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

def visible_from_top(list, index, row, value):
    visible = True
    score_trees = 0
    for trees in list[row-1::-1]:
        score_trees += 1
        if not int(trees[index]) < value:
            visible = False
            break
    return visible, score_trees

def visible_from_below(list, index, row, value):
    visible = True
    score_trees = 0
    for trees in list[row+1:]:
        score_trees += 1
        if not int(trees[index]) < value:
            visible = False
            break
        
    return visible, score_trees

def visible_from_left(list, index, row, value):
    visible = True
    score_trees = 0
    for tree in list[row][index-1::-1]:
        score_trees += 1
        if not int(tree) < value:
            visible = False
            break
    return visible, score_trees

def visible_from_right(list, index, row, value):
    visible = True
    score_trees = 0
    for tree in list[row][index + 1:]:
        score_trees += 1
        if not int(tree) < value:
            visible = False
            break
    return visible, score_trees

def is_visible(list, index, row, value):
    return visible_from_top(list, index, row, value)[0] or visible_from_below(list, index, row, value)[0] or visible_from_right(list, index, row, value)[0] or visible_from_left(list, index, row, value)[0]

def calculate_scenic_route(list, index, row, value):
    return visible_from_top(list, index, row, value)[1] * visible_from_below(list, index, row, value)[1] * visible_from_right(list, index, row, value)[1] * visible_from_left(list, index, row, value)[1]

max_scenic_route = 0
row = 0
for trees in lines[1:-1]:
    index = 0
    row += 1
    for tree in trees[1:-1]:
        index += 1
        if is_visible(lines, index, row, int(tree)):
            max_scenic_route = max(max_scenic_route, calculate_scenic_route(lines, index, row, int(tree)))

print(max_scenic_route)