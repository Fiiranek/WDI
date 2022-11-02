# Wersja bardzie zwarta.
def sito(n):  # liczby pierwsze <= n
    """Sito Eratostenesa - liczby pierwsze nie większe od n."""
    L = [0] + n * [1]
    for p in range(2, n):
        q = p * p
        if q > n:
            break
        if L[p] == 1:
            for i in range(q, n + 1, p):
                L[i] = 0
    return [i for i in range(1, n + 1) if L[i] == 1]


def sum_p(n):
    suma = 0
    for cyfra in str(n):
        suma += int(cyfra) ** len(str(n))
    return suma


l_pierwsze = sito(1_000_000)
for l_pierwsza in l_pierwsze:
    if l_pierwsza == sum_p(l_pierwsza):
        print(l_pierwsza)
