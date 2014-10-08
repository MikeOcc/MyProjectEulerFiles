import heapq
from gmpy import next_prime, is_prime
 
class HeapIter(object):
    def __init__(self, *iters):
	self.iters = [(i.next(), i) for i in iters]
	heapq.heapify(self.iters)
 
    def __iter__(self):
	return self
 
    def next(self):
	if not self.iters:
	    raise StopIteration
	ret, it = heapq.heappop(self.iters)
	heapq.heappush(self.iters, (it.next(), it))
	return ret, it
 
    def add(self, it):
	heapq.heappush(self.iters, (it.next(), it))
 
def sq(q):
    assert is_prime(q)
    p = 2
    while True:
	if p != q:
	    yield p*p*q*q*q
	p = int(next_prime(p))
 
def squbes():
    last_prime = 2
    last_it = sq(last_prime)
    h = HeapIter(last_it)
 
    for s, it in h:
	yield s
	if it == last_it:
	    last_prime = int(next_prime(last_prime))
	    last_it = sq(last_prime)
	    h.add(last_it)
 
def is_primeproof(x):
    st = str(x)
    for i in range(len(st)):
        for d in range(10):
            stn = st[:i] + str(d) + st[i+1:]
	    if is_prime(int(stn)) and not stn.startswith('0'):
		return False
    return True
 
 
if __name__ == '__main__':
    from itertools import islice
    p200 = (x for x in squbes() if '200' in str(x) and is_primeproof(x))
    print list(islice(p200, 199, 200))[0]