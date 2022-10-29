import math


def sito_erastostenesa(n):
    t = [True for _ in range(n)]
    t[0] = t[1] = False
    for i in range(2, math.isqrt(n)):
        if t[i]:
            for j in range(i * i, n):
                t[j] = False
    for k in range(n):
        if t[k]: print(k)


sito_erastostenesa(100000)
