import utils


# problem 1
def solve_1(T: list):
    N = len(T)
    index_max = -1
    for i in range(N):
        il = 1
        for j in range(i):
            if utils.is_prime(T[j]):
                il *= T[j]
        if T[i] == il:
            if index_max == -1:
                index_max = i
            if T[i] > T[index_max]:
                index_max = i
    if index_max >= 0: return index_max
    return None


# problem 2
def solve_2(N):
    for b in range(2, 17):
        number = N
        if utils.is_prime(digits_product(N, b)):
            return b
        k = utils.num_len(number)
        multi = 10 ** (k - 1)
        for i in range(k - 1):
            first_digit = number // multi
            number -= first_digit * multi
            number *= 10
            number += first_digit
            if utils.is_prime(digits_product(N, b)):
                return b
    return None


def digits_product(n: int, b: int):
    prod = 1
    while n > 0:
        r = n % b
        n //= b
        prod *= r
    return prod


print(solve_1([2, 3, 6, 17, 19, 323]))
print(solve_1([20, 20, 40]))

print(solve_2(1428))
print(solve_2(16))
