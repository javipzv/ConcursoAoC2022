with open('input.txt', 'r') as f:
    lines = f.readlines()


punctuation = 0
for move in lines:
    if "X" in move:
        if "A" in move:
            punctuation += 3
        elif "B" in move:
            punctuation += 1
        else:
            punctuation += 2
    elif "Y" in move:
        if "A" in move:
            punctuation += 1 + 3
        elif "B" in move:
            punctuation += 2 + 3
        else:
            punctuation += 3 + 3 
    else:
        if "A" in move:
            punctuation += 2 + 6
        elif "B" in move:
            punctuation += 3 + 6
        else:
            punctuation += 1 + 6

print(punctuation)