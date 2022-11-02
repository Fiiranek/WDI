def check_if_every_row_includes_minimum_one_number_containing_only_odd_digits(t: list):
    for row in t:
        counter = 0
        for number in row:
            if check_if_number_contains_only_odd_digits(number): counter += 1
        if counter < 1: return False
    return True


def check_if_number_contains_only_odd_digits(n: int):
    while n > 0:
        digit = n % 10
        if digit % 2 == 0: return False
        n //= 10
    return True


print(check_if_every_row_includes_minimum_one_number_containing_only_odd_digits(
    [
        [11, 22],
        [23, 45]
    ]
))

print(check_if_every_row_includes_minimum_one_number_containing_only_odd_digits(
    [
        [11, 22],
        [23, 55]
    ]
))
