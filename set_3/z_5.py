i = 0
t = [0 for _ in range(64)]
while True:
    n = int(input())
    if n == 0: break
    t[i] = n
    i += 1
t.sort(reverse=True)
print(t[9])
