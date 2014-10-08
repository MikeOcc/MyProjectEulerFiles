from itertools import count, combinations
from math import sqrt
import time
 
def is_prime(n):
	for p in primes:
		if p * p > n:
			return True
		elif n % p == 0:
			return False
	return True
 
def make_primes(n):
	m = int(sqrt(n + 0.5))
	for p in xrange(3, m + 1, 2):
		if is_prime(p):
			primes.append(p)
 
	a = [ 0 ] * ((n + 15) / 16)
	for p in primes:
		if p * p > n:
			break
		if p == 2:
			continue
		for k in xrange(3 * p, n + 1, 2 * p):
			a[k>>4] |= 1 << (k & 15)
 
	for k in xrange((m + 1) / 2 * 2 + 1, n + 1, 2):
		if (a[k>>4] & (1 << (k & 15))) == 0:
			primes.append(k)
 
def gen_divisor(f, k = 0):
	if k == len(f):
		yield 1
	else:
		p = f[k]
		e_max = f[k+1]
		for e in xrange(e_max + 1):
			n = p ** e
			for d in gen_divisor(f, k + 2):
				yield n * d
 
def is_tatami_free(a, b):
	if a > b:
		a, b = b, a
 
	n = b / a
	begin = a * n + n + 2
	end = a * (n + 1) - n - 2
	return begin <= b and b < end
 
def value(f):
	return reduce(mul, map(lambda k: f[k] ** f[k+1], range(0, len(f), 2)))
 
def gen_rectangle(f):
	s = value(f)
	n = 1
	for k in range(1, len(f), 2):
		n *= f[k] + 1
	if n >= N * 2 - 1:
		for a in gen_divisor(f):
			b = s / a
			if a <= b:
				yield a, b
 
def T(f):
	counter = 0
	for a, b in gen_rectangle(f):
		if is_tatami_free(a, b):
			counter += 1
	return counter
 
def gen_exp(n):
	if n == 1:
		yield [ ]
	else:
		for d in range(1, n):
			for a in gen_exp(n / (d + 1)):
				yield [ d ] + a
 
def add(x, y):
	return x + y
 
def mul(x, y):
	return x * y
 
def num_divs(a):
	return reduce(mul, map(lambda x: x + 1, a))
 
def number(a, ary_p):
	return reduce(mul, map(lambda t: t[0] ** t[1], zip(ary_p, a)))
 
def make_fac(a, ary_p):
	return reduce(add, map(lambda t: [ t[0], t[1] ], zip(ary_p, a)))
 
def gen_ary_primes(n, offs):
	for ary_k in combinations(range(n + offs - 1), n - 1):
		ary_k = ary_k + ( n + offs - 1, )
		yield map(lambda k: primes[k], ary_k)
 
def gen_factorize(ndivmin, ndivmax, p_offs):
	for a in gen_exp(ndivmax):
		n = num_divs(a)
		if n < ndivmin:
			continue
		for ary_p in gen_ary_primes(len(a), p_offs):
			yield make_fac(a, ary_p)
 
def min2(a, b):
	if a < 0:
		return b
	elif b < 0:
		return a
	else:
		return min(a, b)
 
def gen_prime_index(n1, n2):
	for a in gen_exp(n2 - 1):
		if num_divs(a) >= n1:
			yield a
 
def value2(ary_exp, ary_index):
	return reduce(mul, map(lambda t: primes[t[0]] ** t[1],
										zip(ary_index, ary_exp)))
 
def gen_next_index(a):
	for k in range(len(a) - 1):
		if a[k+1] > a[k] + 1:
			yield a[:k] + (a[k] + 1, ) + a[k+1:]
	yield a[:-1] + (a[-1] + 1, )
 
def make_fac2(ae, ai):
	return reduce(add, map(lambda t: [ primes[t[1]], t[0] ], zip(ae, ai)), [ ])
 
def gen_fac(ary_exp, min_s):
	stack = [ tuple(range(len(ary_exp))) ]
	finished = set(stack)
	while len(stack):
		ary_index = stack.pop()
		finished.add(ary_index)
		n = value2(ary_exp, ary_index)
		if n < min_s:
			yield make_fac2(ary_exp, ary_index), n
			for a in gen_next_index(ary_index):
				if a not in finished:
					stack.append(a)
 
def calc_min_size2_core(ary_exp, min_s0):
	min_s = -1
	min_n = -1
	for f, n in gen_fac(ary_exp, min_s0):
		min_n = min2(min_n, n)
		if T(f) == N:
			min_s = min2(min_s, n)
	return min_s, min_n
 
def calc_min_size2(min_s):
	n = N * 2 - 1
	while True:
		min_n = -1
		for a in gen_prime_index(n, n * 2):
			s, min_num = calc_min_size2_core(a, min_s)
			min_s = min2(s, min_s)
			min_n = min2(min_num, min_n)
 
		if min_s < min_n or min_n == -1:
			break
 
		n *= 2
 
	return min_s
 
def calc_min_size_core(ndivmin, p_offs):
	ndivmax = ndivmin * 2
	min_s = -1
	min_n = -1
	for f in gen_factorize(ndivmin, ndivmax, p_offs):
		s = value(f)
		if min_n == -1 or s < min_n:
			print f, s
		min_n = min2(min_n, s)
		if T(f) == N:
			min_s = min2(min_s, s)
	return min_s, min_n
 
def update_history(t, stack, s):
	if t not in s:
		stack.append(t)
		s.add(t)
 
def calc_min_size():
	min_s = -1
	stack = [ (N * 2 - 1, 0) ]
	finished = set(stack)
	while len(stack):
		n, offs = stack.pop(0)
		s, limit = calc_min_size_core(n, offs)
		if s != -1:
			min_s = s
			break
		if min_s == -1 or limit < min_s:
			update_history((n, offs + 1), stack, finished)
			update_history((n * 2, offs), stack, finished)
			min_s = min2(s, min_s)
 
	return calc_min_size2(min_s)
 
N = 200
primes = [ 2 ]
make_primes(100000)
print calc_min_size()