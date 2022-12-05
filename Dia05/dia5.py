with open('input.txt', 'r') as f:
    lines = f.readlines()

dict_nums = {n:list(range(2, 35, 4))[n-1] for n in range(1, 10)}
dict_nums = {v:k for k, v in dict_nums.items()}
dict_lists = {n:[] for n in range(1, 10)}

for i in range(7, -1, -1):
    for crate in lines[i]:
        if crate != "[" and crate != "]" and crate != " " and crate != "\n":
            index = lines[i].index(crate) + 1
            dict_lists[dict_nums[index]] += [crate]
            lines[i] = lines[i].replace(crate, "0", 1)

for mystr in lines[10:]:
    if len(mystr) > 19:
        quantity, From, To = int(mystr[5:7]), int(mystr[13]), int(mystr[18])
    else:
        quantity, From, To = int(mystr[5]), int(mystr[12]), int(mystr[17])
    for time in range(quantity):
        last = dict_lists[From][-1]
        del dict_lists[From][-1]
        dict_lists[To].append(last)

for lists in dict_lists.values():
    print(lists[-1], end="")