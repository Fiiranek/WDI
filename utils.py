""" Contains functions commonly used in algorithms"""

import math


def digits_number(n: int):
    if n == 0: return 1
    digits_counter = 0
    while n > 0:
        n //= 10
        digits_counter += 1
    return digits_counter


def is_prime(n):
    if n < 2: return False
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


if __name__ == "__main__":
    fraction(3, 5)
