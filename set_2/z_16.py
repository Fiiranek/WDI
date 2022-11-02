def is_smith_number(n):
    d, k = 2, n
    n_digits_sum = 0
    while k > 0:
        n_digits_sum += k % 10
        k //= 10
    factors_digits_sum = 0
    while n > 1:
        while n % d == 0:
            factor = d
            n //= d
            while factor > 0:
                factors_digits_sum += factor % 10
                factor //= 10
        d += 1
    return n_digits_sum == factors_digits_sum


print(is_smith_number(24))
print(is_smith_number(85))
