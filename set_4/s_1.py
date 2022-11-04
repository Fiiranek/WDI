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


def ulam_matrix_by_garek(n:int):
    x = n
    a = 0
    b = n - 1
    t = [[0 for _ in range(n)] for _ in range(n)]
    while a <= b:
        for j in range(a,b+1):
            t[a][j] = x
            x+=1

        for i in range(a+1,b):
            t[i][b] = x
            x+=1

        for j in range(b,a,-1):
            t[b][j] = x
            x+=1

        for i in range(b,a,-1):
            t[i][a] = x
            x+=1
        a +=1
        b-=1
    print(t)

ulam_matrix(3)
ulam_matrix_by_garek(4)
