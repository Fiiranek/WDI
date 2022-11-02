import utils


def mix_numbers(a: int, b: int, mask: int):
    number = 0
    mult = 1

    while mask > 0 or a > 0:
        # print(f"mask_bin={bin(mask).replace('0b','')}, mask={mask}, a={a}, b={b}")
        if mask % 2 == 0:
            digit = a % 10
            a //= 10
        else:
            digit = b % 10
            b //= 10
        number += mult * digit
        mult *= 10

        mask //= 2

    return number


def validate_mask(a: int, b: int, mask: int):
    counter_a = len(str(a))
    counter_b = len(str(b))
    while mask > 0:
        if mask % 2 == 0:
            counter_a -= 1
        else:
            counter_b -= 1
        mask //= 2
    return counter_a >= 0 and counter_b == 0


def main(a: int, b: int):
    p = 0
    for mask in range(2 ** (len(str(a)) + len(str(b)))):
        if validate_mask(a, b, mask) and utils.is_prime(mix_numbers(a, b, mask)):
            p += 1
            print(mix_numbers(a, b, mask))
    print('PIERWSZYCH:',p)


main(123, 75)
