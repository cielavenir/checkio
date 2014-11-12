#eh, copied from referee.py

from random import choice

FIRST = "X"
X = "X"
O = "O"
E = "."
D = "D"
SIZE = 3
EMPTY_FIELD = ("...", "...", "...")

def weight_bot(weight_dict):
    def f(grid, mark):
        nonlocal weight_dict
        enemy_mark = X if mark == O else O
        work_weights = {
            E: weight_dict["empty"],
            X: weight_dict["own"] if mark == X else weight_dict["enemy"],
            O: weight_dict["own"] if mark == X else weight_dict["enemy"],
        }
        tr_grid = list(zip(*grid))
        empties = [(x, y) for x in range(SIZE) for y in range(SIZE) if grid[x][y] == E]
        if not empties:
            return None, None
        best_cell, best_weight = empties[0], 0
        for x, y in empties:
            rows = [grid[x], tr_grid[y]]
            if x == y:
                rows.append([grid[i][i] for i in range(SIZE)])
            if x == SIZE - y - 1:
                rows.append([grid[i][SIZE - i - 1] for i in range(SIZE)])
            weight = 0
            for work_row in rows:
                if X in work_row and O in work_row:
                    continue
                weight += sum(work_weights[el] for el in work_row)
            if weight > best_weight:
                best_cell, best_weight = (x, y), weight
            elif weight == best_weight:
                best_cell, best_weight = choice([(x, y), best_cell]), weight
        return best_cell
    return f

x_and_o=lambda grid, your_mark: weight_bot({"empty": 1, "own": 1, "enemy": 2})(grid,your_mark)