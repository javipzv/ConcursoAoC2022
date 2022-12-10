with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
#lines = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']

class Knot():
    def __init__(self, row: int, index: int, positions_set) -> None:
        self.row: int = row
        self.index: int = index
        self.positions_set = positions_set

def needs_move(A: Knot, B: Knot):
    return (abs(A.index - B.index) > 1) or (abs(A.row - B.row) > 1)

T = Knot(0, 0, set())
H = Knot(0, 0, set())

T.positions_set.add((T.row, T.index))

for move in lines:
    if move[0] == 'U':
        H.row = H.row - int(move[2:])
        if needs_move(H, T):
            if H.index != T.index:
                if H.index > T.index:
                    T.index = T.index + 1
                elif H.index < T.index:
                    T.index = T.index - 1
            t_rows = T.row
            for i in range(abs(t_rows - H.row) - 1):
                T.row -= 1
                T.positions_set.add((T.row, T.index))

    elif move[0] == 'D':
        H.row = H.row + int(move[2:])
        if needs_move(H, T):
            if H.index != T.index:
                if H.index > T.index:
                    T.index = T.index + 1
                elif H.index < T.index:
                    T.index = T.index - 1
            t_rows = T.row
            for i in range(abs(t_rows - H.row) - 1):
                T.row += 1
                T.positions_set.add((T.row, T.index))

    elif move[0] == 'R':
        H.index = H.index + int(move[2:])
        if needs_move(H, T):
            if H.row != T.row:
                if H.row > T.row:
                    T.row = T.row + 1
                elif H.row < T.row:
                    T.row = T.row - 1
            t_index = T.index
            for i in range(abs(H.index - t_index) - 1):
                T.index += 1
                T.positions_set.add((T.row, T.index))

    elif move[0] == 'L':
        H.index = H.index - int(move[2:])
        if needs_move(H, T):
            if H.row != T.row:
                if H.row > T.row:
                    T.row = T.row + 1
                elif H.row < T.row:
                    T.row = T.row - 1
            t_index = T.index
            for i in range(abs(t_index - H.index) - 1):
                T.index -= 1
                T.positions_set.add((T.row, T.index))
            
print(len(T.positions_set))
