import math
from time import time
def prime(n):
    """Checks number is prime or not"""
    bol = True
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i == 0):
            bol = False
    if(bol):
        return True
    else:
        return False

def eq(p1,p2):
    """Euclid algorithm"""
    a = 1
    b = 0
    c = 0
    d = 1
    x = p1
    y = p2
    if(p1 < 0):
        x = p1*(-1)
        a = -1
    if(p2 < 0):
        y = p2*(-1)
        d = -1
    while(True):
        if(x == 1):
            return(a,b)
        if(y == 1):
            return(c,d)
        if(x > y):
            q = x/y
            x = x%y
            a = a-c*q
            b = b-d*q
        else:
            q = y/x
            y = y%x
            c = c-a*q
            d = d-b*q


def chinese_rem(arr,):
    """Solves x = ai(mod pi) (ai,pi)are stored in an array"""
    N = 1
    e = []
    sol = 0
    for x in arr:
        N *= x[1]
    for x in arr:
        e.append(eq(x[1],N/x[1])[1]*N/x[1])
    for i in xrange(len(arr)):
        sol += arr[i][0]*e[i]
    return(sol%N)

def base(n,p):
    t = p
    u = n
    while(n/t != 0):
        t *= p
    t /= p
    arr = []
    while (t != 0):
        arr.append(u/t)
        u = u%t
        t /= p
    return arr

def C(a,b,p):
    if(a < b):
        return 0
    n = 1
    d = 1
    for i in range(b+1,a+1):
        n = (n*i)%p
    for i in range(1,a-b+1):
        d = (d*i)%p
    return (n*eq(d,-p)[0])%p
    
st = time()
n = 10**18
m = 10**9
total = 0
parr = []
dic = {}

for i in range(1000,5000):
    if(prime(i)):
        parr.append(i)

for i in xrange(len(parr)):
    p = parr[i]
    A = base(n,p)
    B = base(m,p)
    A = A[-len(B):]
    #print A,B,p
    X = 1
    for ind in range(len(A)):
        X *= C(A[ind],B[ind],p)
    dic[p] = X

for i in xrange(len(parr)):
    p = parr[i]
    print p
    X = dic[p]
    for j in xrange(i+1, len(parr)):
        q = parr[j]
        Y = dic[q]
        T = chinese_rem([X,p],[Y,q])
        for k in xrange(j+1,len(parr)):
            r = parr[k]
            Z = dic[r]
            total += chinese_rem([(T,p*q),(Z,r)])

print total
print "process time -",time()-st