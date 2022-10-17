def pierw_kw_z_newt(n, eps):
    a = 1
    b = n

    while abs(a - b) >= eps:
        a = (a + b) / 2
        b = n / a
    return a


print(pierw_kw_z_newt(3, 0.0000001))
