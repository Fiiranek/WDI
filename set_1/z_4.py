def pierw_calkowitoliczbowy(n):
    suma = 0
    l = 1
    k = 0
    while suma < n:
        suma += l
        l += 2
        k += 1
    return k


print(pierw_calkowitoliczbowy(81))
print(pierw_calkowitoliczbowy(9))
print(pierw_calkowitoliczbowy(1))
