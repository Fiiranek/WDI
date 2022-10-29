import random

n = int(input())

t = [0 for _ in range(n)]
for i in range(n):
    t[i] = random.randint(1, 1000)
for i in range(n):
    num = t[i]
    odd_digit_counter = 0
    while num > 0:
        digit = num % 10
        num //= 10
        if digit % 2 != 0: odd_digit_counter += 1
    if odd_digit_counter < 1:
        print('NIE')
        exit()
print('TAK')
