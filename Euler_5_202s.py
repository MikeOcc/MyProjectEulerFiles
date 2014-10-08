import math

def multiplesInSequence(start,end,factor,step):
    # Return the number of elements of the arithmetic sequence start +
    # step * i which are <=end and which are divisible by factor
    x=start/factor
    x*=factor
    if x < start: x+=factor
    while (x-start) % step != 0 and x<end: x+=factor
    if x> end: return 0
    if x==end: return 1
    y=x+factor
    i=1
    while (y-x) % step != 0 and y<=end:
        y+=factor
        i+=1
    if y>end: 
        return i-1
    return 1 + (end-x)/(factor*i)

def permuteItems(iterable):
    l=list(iterable)
    current=[]
    perms=[]
    recPerm(current,l,perms)
    return perms

def recPerm(current,items,perms):
    if len(items)==1:
        current.append(items[0])
        perms.append(list(current))
        current.pop()
        perms.append(list(current))
    else:
        current.append(items[0])
        recPerm(current,items[1:],perms)
        current.pop()
        recPerm(current,items[1:],perms)

def findSmallPrimeDivisors(t):
    primes=set()
    if t & 1 == 0:
        primes.add(2)
        t/=2
    top=1+int(math.sqrt(t))
    for n in xrange(3,top,2):
        if t % n == 0:
            residues=set((n % p for p in primes))
            if 0 not in residues: primes.add(n)
    return primes

def findPrimeDivisors(t):
    if t==1: return set()
    primes=findSmallPrimeDivisors(t)
    if len(primes)==0:
        primes.add(t)
    else:
        x=t
        for p in primes:
            while x % p ==0: x/=p
        primes=primes.union(findPrimeDivisors(x))
    return primes

def countPaths(R):
    if R&1==0: return 0
    end=(R+3)/2
    start=(R+3)/4
    sum=end
    m3=end % 3
    if m3==1: end-=2
    elif m3==2: end-=1
    else: return 0
    if sum & 1 == 0:
        step=6
        if end & 1 ==0: end -=3
    else:
        step=3
    numsteps=1+(end-start)/step
    primes=findPrimeDivisors(sum)
    if 2 in primes: primes.remove(2)
    primes=list(primes)
    primes.sort()
    # Begin with the number of steps in the sequence start + step * i
    # which are <= end
    count=numsteps
    # Now use inclusion-exclusion to count the number of elements of
    # the sequence which are divisible by some factor of sum
    for primeSet in permuteItems(primes):
        m=1
        for p in primeSet: m*=p
        if m==1: continue
        n=multiplesInSequence(start,end,m,step)
        if len(primeSet) & 1 == 0: count+=n
        else: count-=n
    return 2 * count


print countPaths(12017639147)
