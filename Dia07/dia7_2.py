import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

class Dir():
    def __init__(self, name: str, size: int, childs: list, parent) -> None:
        self.name = name
        self.size = size
        self.childs = childs
        self.parent = parent

class Tree():
    def __init__(self, root: Dir) -> None:
        self.root = root
        self.actual_dir: Dir

root_dir = Dir(name="/", size=0, childs=[], parent=None)
mytree = Tree(root=root_dir)
mytree.actual_dir = mytree.root

for command in lines[1:]:
    if command[2:4] == "cd":
        if command[5:7] == "..":
            mytree.actual_dir = mytree.actual_dir.parent
            continue
        mydir = [dir for dir in mytree.actual_dir.childs if dir.name == command[5:]]
        if not mydir:
            newdir = Dir(name=command[5:], size=0, childs=[], parent=mytree.actual_dir)
            mytree.actual_dir.childs.append(newdir)
            mytree.actual_dir = newdir
        else:
            mytree.actual_dir = mydir[0]

    elif command[2:4] == "ls":
        continue

    elif command[:3] == "dir":
        newdir = Dir(name=command[4:], size=0, childs=[], parent=mytree.actual_dir)
        mytree.actual_dir.childs.append(newdir)

    else:
        file_size = int(re.findall("[0-9]+", command)[0])
        mytree.actual_dir.size += file_size
        parent_dir = mytree.actual_dir.parent
        while parent_dir is not None:
            parent_dir.size += file_size
            parent_dir = parent_dir.parent

def get_min_needed(mytree: Dir, needed):
    def aux(main_dir: Dir, needed: int, min: int):
        if main_dir.size > needed and main_dir.size < min:
            min = main_dir.size
        for child in main_dir.childs:
            min = aux(child, needed, min)
        return min
    return aux(mytree.root, needed, mytree.root.size)
    
needed = mytree.root.size - (70000000 - 30000000)
print(get_min_needed(mytree, needed))