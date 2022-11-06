import utils


def solve_1(x):
    n = len(str(x))
    prime_max = 0
    for M in range(n):
        for N in range(n):
            x_new = cut(M, N, x)
            print(x_new)
            if utils.is_prime(x_new) and unique_digits(x_new):
                prime_max = max(prime_max,x_new)
    return prime_max

def cut(M, N, x):
    for i in range(N):
        x //= 10
    num_len = len(str(x))
    for j in range(M):
        multiplier = 10 ** (num_len - 1)
        d = x // multiplier
        x -= d * multiplier
        num_len -= 1
    return x


def unique_digits(x):
    t = [False for i in range(10)]
    while x > 0:
        digit = x % 10
        x //= 10
        if t[digit]: return False
        t[digit] = True
    return True

print(solve_1(1202742516))