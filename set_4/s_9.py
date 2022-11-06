def find_odd_square(T: list[list], k: int):
    N = len(T)
    for size in range(3, N, 2):
        step = size // 2
        for i in range(size // 2, N - (size // 2)):
            for j in range(size // 2, N - (size // 2)):
                corners_product = T[i - step][j - step] * T[i - step][j + step] * T[i + step][j + step] * T[i + step][
                    j - step]
                if corners_product == k:
                    return True, (i, j)

    return False


print(find_odd_square(
    [
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [100, 2, 100, 2, 100],
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
    ], 16
))

print(find_odd_square(
    [
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [100, 2, 100, 2, 100],
        [100, 100, 100, 100, 100],
        [100, 2, 100, 2, 100],
    ], 16
))
