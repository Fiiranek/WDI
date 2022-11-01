def fun(n: int):
    for i in range(10 ** (n - 1), (10 ** n) - 1):
        num = i
        total = 0
        while num > 0:
            digit = num % 10
            num //= 10
            total += digit ** n
        if total == i: print(total)


fun(3)
