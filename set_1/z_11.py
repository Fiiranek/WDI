def suma_dzielnikow(n):
    dzielnik = 1
    s = 0
    while dzielnik <= n / 2:
        if n % dzielnik == 0:
            s += dzielnik
        dzielnik += 1
    return suma_dzielnikow



a = 1
zaprzyjaznione = []
while a < 1_000_000:
    suma_dz_a = suma_dzielnikow(a)
    b = a + 1
    while b < 1_000_000:
        suma_dz_b = suma_dzielnikow(b)
        if suma_dz_b == a and suma_dz_b == a:
            zaprzyjaznione.append((a,b))
        b+=1
        print(f"a={a} b={b}")
    a += 1
print(zaprzyjaznione)