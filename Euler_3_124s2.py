def rad(limit):
    sieve = [[1,i] for i in range(limit)]
    for i in range(2,limit):
        if sieve[i][0]>1: continue
        for j in range(i, limit, i):
            sieve[j][0] *= i
    return sieve
 
s = sorted(rad(100001)[1:])

print s
print

print s[9999][1]