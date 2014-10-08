def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
 
fac = [factorial(i) for i in range(10)]
 
def partitions(n,d = None,start = 1):
    # generates numbers that add up to n, in numerical order
    # d = number of digits, or any number if left out
    # start makes first digit start at 1 instead of 0.
    if d == None:
        i = 0
        sub = None
        while True:
            if sub == None:
                i += 1
                sub_gen = partitions(n,i,start=1)
            else:
                yield sub
            sub = sub_gen.next()
    elif d == 0:
        yield ''
        while True:
            yield None
    else:
        start = max(start,n-(d-1)*9)
        stop = min(9,n)
        for i in range(start,stop+1):
            sub_gen = partitions(n-i,d-1,start=0)
            while True:
                sub = sub_gen.next()
                if sub == None:
                    break
                yield str(i) + sub
        yield None
 
def f(n):
    return sum(fac[int(d)] for d in str(n))
 
def sf(n):
    return sum(int(d) for d in str(f(n)))
 
def g(i):
    n = 1
    while sf(str(n)) != i:
        n += 1
    return n
 
def reverse(n):
    # finds number for which the factorials of digits add up to to n.
    # represents as a list: [-totaldigits, ones, twos, threes...]
    # i.e., 1111223499 is [-10,4,2,1,1,0,0,0,0,2]
    # this guarantees that these representations are ordered properly
    result = []
    for i in range(9,0,-1):
        m,n = divmod(n,fac[i])
        result.append(m)
    result.append(-sum(result))
    return result[::-1]
 
def g2(i):
    # try each number whose digits add up to i
    part = partitions(i)
    best = None # works because any list > None
    while True:
        n = part.next()
        x = reverse(int(n))
        if x > best: 
            best = x
        if x[9] > -best[0]:
            # more nines in x than all digits in best.
            return best
 
def sg(i):
    if i <= 40:
        return sum(int(d) for d in str(g(i)))
    else:
        l = g2(i)
        return sum(l[j]*j for j in range(1,10))
 
print sum(sg(x) for x in range(1,151))