def mul(c1,c2):
    r = [c1[i]+c1[i-1] for i in xrange(len(c1)-1,0,-1)]+[c1[0]]
    result = []
    for i in range(len(c2)):
        result.append(sum(map(lambda x,y: x*y,r,c2)))
        r.insert(0,r[-1])
        r.pop()
        r[-1] -= r[0]
    return result
 
def power(c,n,mod = None):
    if n == 1:
        result = c
    elif n % 2 == 0:
        new= power(c,n/2,mod)
        result = mul(new,new)
    else:
        result= mul(c,power(c,n-1,mod))
    if mod != None:
        result = [i % mod for i in result]
    print c,n,mod,result
    return result
 
size = 2000
n = [1]*size
c = [1] + [0]*(size-1)
print mul(power(c,10**18,20092010),n)[-1] % 20092010