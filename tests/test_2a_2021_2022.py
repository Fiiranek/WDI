def zbw_4(x):
    t = [False for _ in range(4)]
    while x > 0:
        r = x % 4
        t[r] = True
        x //= 4
    return t


def zgodne(a, b):
    zbw_4_a = zbw_4(a)
    zbw_4_b = zbw_4(b)
    for i in range(4):
        if zbw_4_a[i] != zbw_4_b[i]: return False
    return True


def solve(T: list):
    N = len(T)
    c_max = 0
    i = 0
    while i < N:
        j = i + 1
        spr = True
        c = 0
        while j < N and spr:
            if not zgodne(T[i], T[j]):
                spr = False
            else:
                # print(f"elementy za pozycjach {i} {j} są takie same")
                j += 1
                c += 1
        c_max = max(c_max, c + 1)
        i += 1
    print(c_max)


solve([13, 23, 13, 33, 33, 33, 58, 23, 23, 23, 23, 23], )
