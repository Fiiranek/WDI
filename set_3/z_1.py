def convert_to_system(n, base):
    result = [0 for _ in range(64)]
    i = 0
    while n > 0:
        result[i] = n % base
        n //= base
        i += 1
    for x in range(i - 1, -1, -1):
        print('0123456789ABCDEF'[result[x]], end="")
    # return result


convert_to_system(9, 2)
