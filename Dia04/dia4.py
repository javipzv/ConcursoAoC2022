with open('input.txt', 'r') as f:
    lines = f.readlines()

overlappings = 0
for pair in lines:
    sections = pair.replace("\n", "").split(",")
    sec1, sec2 = sections[0].split("-"), sections[1].split("-")
    set1 = set(list(range(int(sec1[0]), int(sec1[1]) + 1)))
    set2 = set(list(range(int(sec2[0]), int(sec2[1]) + 1)))
    if set1.issubset(set2) or set2.issubset(set1):
        overlappings += 1

print(overlappings)