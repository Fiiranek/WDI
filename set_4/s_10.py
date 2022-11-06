def solve(T: list[list[int]]):
    N = len(T)
    for row_index in range(N):
        if not check_0_in_row(T, row_index): return False
    for col_index in range(N):
        if not check_0_in_col(T, col_index): return False
    return True


def check_0_in_col(T: list[list[int]], col_index):
    for i in range(len(T)):
        if T[i][col_index] == 0:
            return True
    return False


def check_0_in_row(T: list[list[int]], row_index):
    for i in range(len(T[row_index])):
        if T[row_index][i] == 0:
            return True
    return False


print(solve(
    [[1, 2, 0],
     [0, 2, 1],
     [3, 0, 1]]
))

print(solve(
    [[1, 2, 1],
     [0, 2, 1],
     [3, 0, 1]]
))
