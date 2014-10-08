# Miller-Rabin for primes

from Functions import IsPrime

def miller_rabin_pass(a, n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def IsPrim(n):
    if not miller_rabin_pass(2, n):
        return False
    if not miller_rabin_pass(7, n):
        return False
    if not miller_rabin_pass(61, n):
        return False
    return True


# recursive definition C(n,k,p)=C(n/p,k/p)*C(n%p,k%p,p) for prime p

def c(n,k,p):
    if k==0:
        return 1
    b=1
    for i in xrange(1,k+1):
        b=(b*(n-k+i)*pow(i,p-2,p))%p
    return b

def C(n,k,p):
    b=1
    while n>1:
        t=c(n%p,k%p,p)
        b=(b*t)%p
        n/=p
        k/=p
    return b

# find primes and C(10^18,10^9,p)

cc={}
pp=[]
for i in xrange(1001,5000,2):
    if IsPrime(i):
        p=C(10**18,10**9,i)
        cc[i]=p
        pp.append(i)

# use CRT for solution


def inv(a,b):
    if b==0:
        return (a,1,0)
    (d,s,t)=inv(b,a%b)
    (d,s,t)=(d,t,s-(a/b)*t)
    return (d,s,t)



t=0
for i in xrange(len(pp)-2):
    for j in xrange(i+1,len(pp)-1):
        for k in xrange(j+1,len(pp)):
            a=inv(pp[i]*pp[j],pp[k])
            b=inv(pp[i]*pp[k],pp[j])
            c=inv(pp[j]*pp[k],pp[i])
            t+=(cc[pp[i]]*c[1]*pp[j]*pp[k]+cc[pp[j]]*b[1]*pp[i]*pp[k]+cc[pp[k]]*a[1]*pp[j]*pp[i])%(pp[i]*pp[j]*pp[k])
print t

print inv(17*13,11)