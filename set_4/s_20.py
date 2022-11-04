def sum_row(t: list, row_index: int):
    return sum(t[row_index])


def sum_column(t: list, col_index: int, N: int):
    x = 0
    for i in range(N):
        x += t[i][col_index]
    return x


def towers(t: list, N: int):
    t_sum_max = 0
    for i in range(N ** 2):
        print("-----------------------")
        for j in range(i + 1, N ** 2):
            r1 = i // N
            c1 = i % N

            r2 = j // N
            c2 = j % N
            t_sum = 0
            if r1 == r2:
                t_sum = sum_row(t, r1) + sum_column(t, c1, N) + sum_column(t, c2, N) - 2 * t[r1][c1] - 2 * t[r2][c2]
            elif c1 == c2:
                t_sum = sum_column(t, c1, N) + sum_row(t, r1) + sum_row(t, r2) - 2 * t[r1][c1] - 2 * t[r2][c2]
            else:
                t_sum = sum_column(t, c1, N) + sum_column(t, c2, N) + sum_row(t, r1) + sum_row(t, r2) - (2 * t[r1][c1] +
                                                                                                         2 * t[r2][c2] +
                                                                                                         t[r1][c2] +
                                                                                                         t[r2][c1])
            t_sum_max = max(t_sum_max, t_sum)
    print(t_sum_max)


test_board = [
    [1, 1, 1, 2, 3],
    [4, 1, 4, 5, 6],
    [1, 1, 0, 1, 9],
    [3, 4, 1, 3, 9],
    [7, 6, 6, 8, 8]
]
towers(test_board, 5)
