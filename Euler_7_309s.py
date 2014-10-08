
from Functions import gcd

def p309(N = 10**6):
    lll = [[] for w in xrange(N)]
    for s in xrange(1, int(N**0.5) + 500):
        for t in xrange(1 + (s&1), s, 2):
            if s*s + t*t >= N:
                break
            if gcd(s, t) == 1:
                for l in xrange(1, N/(s*s + t*t) + 1 - ((N%(s*s + t*t)) == 0)):
                    a = 2*l*s*t
                    b = l*(s*s - t*t)
                    lll[a].append(b)
                    lll[b].append(a)
    count = 0
    for ll in lll:
        for i, a in enumerate(ll):
            for b in ll[:i]:
                if (a*b) % (a+b) == 0:
                    print a,b
                    count += 1
    return count



print p309()