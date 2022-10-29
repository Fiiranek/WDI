import math


def czy_pierwsza(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0:
            return False
        x += 2
        if n % x == 0:
            return False
        x += 4
    return True

print(czy_pierwsza(29))