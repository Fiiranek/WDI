n = int(input())
s = 1
num = 1
k = 0
while s < n:
    s += num
    num += 2
    k += 1
print(k)
