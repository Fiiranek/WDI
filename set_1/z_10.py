def czy_doskonala(n):
    suma = 0
    dzielnik = 1

    while dzielnik <= n / 2:
        if n % dzielnik == 0:
            suma += dzielnik
        dzielnik += 1
    if suma == n:
        return True
    return False


print(czy_doskonala(6))
print(czy_doskonala(28))
print(czy_doskonala(20))
