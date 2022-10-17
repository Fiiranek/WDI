def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwd_modulo(a,b):
    while b != 0:
        pom = b
        b = a % b
        a = pom

    return a

print(nwd(10, 5))
print(nwd(nwd(27, 3), 9))
print(nwd_modulo(10,5))


