n = int(input("Podaj liczbe: "))

dzielnik = 1

while dzielnik <= n / 2:
    if n % dzielnik == 0:
        print(dzielnik)
    dzielnik += 1
