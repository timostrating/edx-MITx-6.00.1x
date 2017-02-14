def f(i):
    return i + 2
def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    LCopy = L[:]
    for i in LCopy:
        if g(f(i)) == False:
            L.remove(i)

    if len(L) == 0:
        return -1

    return max(L)


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)