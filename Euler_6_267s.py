import math
 
def bisect_left(f, n):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo+hi)//2
        print(mid, f(mid))
        if f(mid) < 0: lo = mid+1
        else: hi = mid
    return lo
 
niter = 1000
total = 10 ** 9
 
def succ(f):
    def t(n):
        return (1 + 2 * f) ** n * (1 - f) ** (niter - n)
    return t
 
def c(n, m):
    return math.factorial(n) // math.factorial(m) // math.factorial(n - m)
 
def mx(f):
    x = bisect_left(lambda x: succ(f)(x) - total, niter + 1)
    print(x, succ(f)(x))
    return sum(c(niter, k) for k in range(x, niter + 1)) / 2 ** niter
 
print(mx(0.148))