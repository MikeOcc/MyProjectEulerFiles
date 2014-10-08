
import fractions, operator, functools, math, collections

n = 10 ** 18

c = list(range(int(n ** (1 / 3.)) + 1))

t = 0

for x in range(2, int(math.sqrt(len(c))) + 1):
    if c[x] == x:
        for y in range(2 * x, len(c), x):
            c[y] = min(c[y], x)

def factor(x):
    factors = []
    while x != 1:
        p = c[x]
        e = 0
        while not x % p:
            x //= p
            e += 1
        factors += [(p, e)]
    return factors

primes = [x for x in range(2, len(c)) if c[x] == x]

q = []

def kk(pp, idx, v):
    if v * pp[-1] >= n:
        return
    global q
    if len(pp) >= 2:
        q += [pp]
    for i in range(idx + 1, len(primes)):
        if v * primes[i] ** 3 >= n:
            break
        kk(pp + [primes[i]], i, v * primes[i] * primes[i])

for i, p in enumerate(primes):
    kk([p], i, p ** 2)

r = []

for pp in q:
    k = True
    y = collections.defaultdict(int)
    ee = collections.defaultdict(int)
    for p in pp:
        ee[p] = 2
        y[p] = 1
    for p in pp:
        for a, b in factor(p - 1):
            y[a] += b
    for a, b in y.items():
        if b < 2 and a not in pp:
            k = False
            break
    if k:
        r += [pp]
        
del q

def achilles(ee):
    return functools.reduce(fractions.gcd, (e for p, e in ee.items())) == 1


def rec(e, y, pp, idx, prod):
    if prod >= n:
        return
    if idx == len(pp):
        if achilles(e) and achilles(y):
            global t
            t += 1
        return
    rec(e, y, pp, idx + 1, prod)
    e[pp[idx]] += 1
    y[pp[idx]] += 1
    rec(e, y, pp, idx, prod * pp[idx])
    e[pp[idx]] -= 1
    y[pp[idx]] -= 1
            
for pp in r:
    y = collections.defaultdict(int)
    ee = collections.defaultdict(int)
    for p in pp:
        ee[p] = 2
        y[p] = 1
        for a, b in factor(p - 1):
            y[a] += b
    for p in pp:
        if y[p] == 1:
            y[p] += 1
            ee[p] += 1
    rec(ee, y, pp, 0, functools.reduce(operator.mul, (p ** e for p, e in ee.items())))

print(t)