koszt_min = 10**10
def król_r(T,k,w=0,koszt=0):
    global koszt_min
    if w == 8:
        koszt_min = min(koszt,koszt_min)
    else:
        if k > 0: król_r(T,k+1,w+1,koszt+T[w][k])
        if k < 7: król_r(T,k-1,w+1,koszt+T[w][k])
        król_r(T,k,w+1,koszt+T[w][k])


def król(T,k):
    global koszt_min
    koszt_min = 10**10
    król_r(T,k)
    return koszt_min