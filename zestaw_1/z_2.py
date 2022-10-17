year = 2022
best = [1, year - 1]
for x in range(1, year + 1):
    for y in range(1, year + 1):
        a = y
        b = x
        while b < year + 1:
            if b == year:
                if sum([x, y]) < sum(best): best = [x, y]
            c = a + b
            b = a
            a = c
print(best)
