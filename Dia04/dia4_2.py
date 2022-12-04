with open('input.txt', 'r') as f:
    lines = f.readlines()
#lines = ['2-4,6-8\n', '2-3,4-5\n', '5-7,7-9\n', '2-8,3-7\n', '6-6,4-6\n', '2-6,4-8\n']
overlappings = 0
for pair in lines:
    sections = pair.replace("\n", "").split(",")
    sec1, sec2 = sections[0].split("-"), sections[1].split("-")
    set1 = set(list(range(int(sec1[0]), int(sec1[1]) + 1)))
    set2 = set(list(range(int(sec2[0]), int(sec2[1]) + 1)))
    union = set1 & set2
    if len(union) >= 1:
        print(union, 'founded')
        overlappings += 1
    else:
        print(union, 'not')

print(overlappings)