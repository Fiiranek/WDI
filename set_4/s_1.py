def ulam_matrix(n: int):  # n must be odd
    num = 1
    t = [[0 for _ in range(n)] for _ in range(n)]
    i = j = n // 2
    k = 0
    counter = 1
    while num <= n ** 2:
        for a in range(counter):
            t[i][j] = num
            num += 1
            if k == 0:
                j += 1
            elif k == 1:
                i -= 1
            elif k == 2:
                j -= 1
            else:
                i += 1
        k += 1
        if k > 3: k = 0
        if k % 2 == 0:
            counter += 1
    for row in t:
        print(row)


ulam_matrix(3)
