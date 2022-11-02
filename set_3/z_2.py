import utils


def compare_digits(n_1, n_2):
    t_1 = [False for _ in range(64)]
    t_2 = [0 for _ in range(64)]

    while n_1 > 0:
        t_1[n_1 % 10] = True
        n_1 //= 10
    while n_2 > 0:
        t_2[n_2 % 10] = True
        n_2 //= 10
    for i in range(10):
        if t_1[i] != t_2[i]: return False
    return True


print(compare_digits(1000, 1000))
print(compare_digits(1000, 1002))
print(compare_digits(12, 123456789))
