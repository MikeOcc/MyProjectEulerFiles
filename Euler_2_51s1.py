from Functions import RofPrimes
from bisect import bisect

def prob51(): 

  primes=RofPrimes(10000,1000000)

# test primes in list of primes under 10Meg 
  for p in primes: 
    if p < 10000: continue 
    s = str(p) 
   
    for c in '012': 
     
     if s.count(c) not in (3,6,9): continue 
     losers = [] 
     winners = [] 
     
     for d in '0123456789': 
       n = int(s.replace(c,d)) 
       # see if candidate family member is prime 

       if d >= c and n == primes[bisect(primes,n)-1]: 
         winners.append(n) 
       else: 
         losers.append(n) 

# if more than 2 losers, then can't be a 
# family of eight primes 
     if len(losers) > 2: break 
  
  return winners 
  
print prob51()