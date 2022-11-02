import random

n = int(input())

t = [0 for _ in range(n)]
for i in range(n):
    t[i] = random.randint(1, 1000)
for i in range(n):
    num = t[i]
    is_even_digit = False
    while num > 0:
        digit = num % 10
        num //= 10
        if digit % 2 == 0:
            is_even_digit=True
            break
    if not is_even_digit:
        print('TAK')
        exit()

        exit()
print('NIE')
