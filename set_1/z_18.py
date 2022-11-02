def pierwiastek(a,n,eps=0.0001):
    x = a
    x_prev = a
    while True:
        pom = x_prev
        x_prev = x
        x = (1/n)*((n-1)*pom + (a/(pom**(n-1))))
        print(x,x_prev)
        if abs(x - x_prev) < eps:
            break
    print(a)
pierwiastek(8,3)