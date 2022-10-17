def nwd_niezoptylamizowany(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def nwd(a,b):
    while b > 0:
        pom = b
        b = a%b
        a = pom
    return a

# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
print(nwd(10, 5))
print(nwd(nwd(27, 3), 9))


