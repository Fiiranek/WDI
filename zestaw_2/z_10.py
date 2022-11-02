n = int(input())
a_prev = 2
i = 2

while True:
    a = 3 * a_prev + 1
    if n % a == 0:
        print('TAK')
        break
    a_prev = a
    # if a >