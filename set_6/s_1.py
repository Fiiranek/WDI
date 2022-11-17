import utils
def rev(n):
    x = list(reversed(str(n)))
    k = ""
    for i in x: k+= i
    return k

def liczby(n,w):
    if n == 0:
        w = int(rev(w))
        print(f"n={n} w={w}")

        if utils.is_prime(w):
            print(w)
    else:
        liczby(n//10,w*10 + n % 10)
        liczby(n//10,w)
liczby(9713,0)


