""" Contains functions commonly used in algorithms"""

import math


def num_len(n: int):
    if n == 0:
        return 1
    x = 0
    while n > 0:
        x += 1
        n //= 10
    return x


def digits_number(n: int):
    if n == 0: return 1
    digits_counter = 0
    while n > 0:
        n //= 10
        digits_counter += 1
    return digits_counter


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0: return False
        x += 2
        if n % x == 0: return False
        x += 4
    return True


def fraction(n: int, d: int):
    n, d = reduce_fraction(n, d)
    print(n // d, end='')
    n = n % d
    if n > 0:
        print('.', end='')


def reduce_fraction(numerator: int, denominator: int):
    gcf_of_n_and_d = gcf(numerator, denominator)
    numerator, denominator = int(numerator / gcf_of_n_and_d), int(denominator / gcf_of_n_and_d)
    return numerator, denominator


def gcf(a: int, b: int):
    """Greatest common factor"""
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def permutation(arr: list, pos=0):
    if pos == len(arr):
        print(arr)
    else:
        for i in range(pos, len(arr)):
            arr[i], arr[pos] = arr[pos], arr[i]
            permutation(arr, pos + 1)
            arr[i], arr[pos] = arr[pos], arr[i]


def suma_podzielnikow(n):
    i = 2
    suma = 1

    while i * i < n:
        if n % i == 0:
            suma += i + n // i
        i += 1
    print(suma)


suma_podzielnikow(20)


def czy_pierwsza(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    x = 5
    while x * x < n:
        if n % x == 0:
            return False
        x += 2
        if n % x == 0:
            return False
        x += 4
    return True


print(czy_pierwsza(29))
print(czy_pierwsza(13))
print(czy_pierwsza(10))
print(czy_pierwsza(100))
""" Contains functions commonly used in algorithms"""

import math


def num_len(n: int):
    if n == 0:
        return 1
    x = 0
    while n > 0:
        x += 1
        n //= 10
    return x


def digits_number(n: int):
    if n == 0: return 1
    digits_counter = 0
    while n > 0:
        n //= 10
        digits_counter += 1
    return digits_counter


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0: return False
        x += 2
        if n % x == 0: return False
        x += 4
    return True


def fraction(n: int, d: int):
    n, d = reduce_fraction(n, d)
    print(n // d, end='')
    n = n % d
    if n > 0:
        print('.', end='')


def reduce_fraction(numerator: int, denominator: int):
    gcf_of_n_and_d = gcf(numerator, denominator)
    numerator, denominator = int(numerator / gcf_of_n_and_d), int(denominator / gcf_of_n_and_d)
    return numerator, denominator


def gcf(a: int, b: int):
    """Greatest common factor"""
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def permutation(arr: list, pos=0):
    if pos == len(arr):
        print(arr)
    else:
        for i in range(pos, len(arr)):
            arr[i], arr[pos] = arr[pos], arr[i]
            permutation(arr, pos + 1)
            arr[i], arr[pos] = arr[pos], arr[i]


def prime_factors(n):
    k = 2
    while n != 1:
        while n % k == 0:
            print(k)
            n //= k
        k += 1


