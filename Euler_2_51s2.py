from Functions import primes as genprime
primes = genprime(10**6)
primeset = set(primes)
primeIndex = 0
 
def permu(bag):
	if len(bag) > 0:
		b= replacable_check(bag)
		if b: return b
	check = None
	for i in bag:
		check = permu([j for j in bag if not j == i])
		if check: return check
 
def replacable_check(bag):
	global primes, primeIndex
	p = [c for c in str(primes[primeIndex])]
	for i in bag: p[i] = "*"
	count, replacement = 0, -1
	for i in xrange(10):
		if int(''.join(p).replace("*", str(i))) in primeset:
			count += 1
			if i==0 and p[0]=="*": count -= 1
			elif replacement==-1: replacement = str(i)
	if count >= 8:
		return (''.join(p), primes[primeIndex], ''.join(p).replace("*", replacement))
 
result = None
while primeIndex<len(primes):
	result  = permu( range( len(str(primes[primeIndex]))-1))
	if result: break
	primeIndex += 1
 
if not result: print "no solution found"
else: print "template: %s, prime: %s, smallest in family: %s" % result