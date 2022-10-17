base_a = 1
base_b = 1
a = 1
b = 1
toggle = True
is_2022 = False
best = (1,2021)
while not is_2022:
    print(f"a={base_a} b={base_b}")
    print("-------------")
    while b <= 2022:
        print(a)
        c = a + b
        a = b
        b = c
        if a == 2022:
            print(f"found 2022, a={base_a} b={base_b}")
            is_2022=True
            break
    # if toggle:
    #     base_b += 1
    # else:
    #     base_a += 1
    base_b+=1
    a,b = base_a,base_b
    toggle = not toggle
#

# suma = 10000
# rok = 2022
# best = (rok, 0)
#
# for i in range(rok+1):
# 	y = rok
# 	x = i
# 	while x > 0 and y > x:
# 		x, y = y-x, x
# 	if x + y < suma:
# 		suma = x + y
# 		best = (x, y)
#
# print(suma, best)
