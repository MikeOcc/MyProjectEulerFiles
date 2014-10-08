from Functions import RofPrimes
k = 2**50

mx = 33554432
primes = RofPrimes(2,mx)

square_primes=[]

for i in primes:
  square_primes.append(i*i)
 
def p193():
    def scf(max_prod, square_primes, previous=1, start=0):
        tot = 0
        for pos in xrange(start, len(square_primes)):
            sq = square_primes[pos]
            if sq * previous >= max_prod:
                break
            tot += max_prod / sq / previous - scf(max_prod, square_primes, sq * previous, pos + 1)
        return tot
    print k - scf(k - 1, square_primes)
 
if __name__ == "__main__":
    p193()