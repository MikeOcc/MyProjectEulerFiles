#
#
#

def FactorSieve(n):
  from collections import defaultdict
  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
           f[i].append(p)
       if f[p]==[]:f[p]=[p]
  return f

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # recurrence formula for length by amount1 and amount2 Tony Veijalainen 2010
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    amount1 = n-10
    amount2 = 6

    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
             ## can you make recurrence formula for whole reciprocal?
            sieve[i*i//2::i] = [False] * (amount1//amount2+1)
        amount1-=4*i+4
        amount2+=4

    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]


def nCr(N,r):     # from scipy.comb(), but MODIFIED!  Binomial Functions.
    if (r > N) or (N < 0) or (r < 0):
        return 0L
    N,r = map(long,(N,r))
    top = N
    val = 1L
    while (top > (N-r)):
        val *= top
        top -= 1
    n = 1L
    while (n < r+1L):
        val /= n
        n += 1
    return val



def IsPrime(startnumber):
 
  if startnumber==2: return True
  if startnumber<2: return False
  
  startnumber*=1.0
 
  if startnumber/2==int(startnumber/2):
     return False


  for divisor in range(3,int(startnumber**0.5)+1,2):
      if startnumber/divisor==int(startnumber/divisor):
          return False
          
  return True

def primes0(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]


def RofPrimes(m,n): 
#
#  return a range of primes
#
  if ((n<=m) or (n<2) or (m<2)): return []

  elif m==2 and n==2: return [2]
    #elif n<2: return []
    #s=range(3,n+1,2)
#  if m%2==0:
#    s=range(3,n+1,2)
#  else:
  s=range(3,n+1,2)
  
  if m%2==0:cutoff = s.index(m+1)
  else: cutoff = s.index(m)

  mroot = n ** 0.5
  half=(n+1)/2-1
  i=0
  r=3  #m
  while r <= mroot:
    
    if s[i]:
      j=(r*r-3)/2
      #print i, j, s, len(s), half
      s[j]=0
      while j<half:
        s[j]=0
        j+=r
    i=i+1
    r=2*i+3

  if m>2:
    
    s=s[cutoff:]    
    x = [x for x in s if x]
    
    #print cutoff
    
  else:
    x = [2]+[x for x in s if x]
  
  return x


###

def IsPalindrome(n):
  
  # ]
  nn = str(n)[::-1]

  return (int(nn) == n)

###
  IsPal = True
  nn = str(n)
  nlen = len(nn)

  #if nlen==2:   

  IsOdd = False
  if nlen/2*2 != len:
    IsOdd=True

  if IsOdd:
    tlen = (nlen-1)/2
  else:
    tlen = nlen /2

  for i in range(0,tlen+1):
    if nn[i] != nn[-i-1]:
       IsPal = False
       break

  return IsPal
###

def RevNumber(n):

  
#  nn = str(n)[::-1]

  return int(str(n)[::-1])


def PowerSum(npower,nthlevel):

    n=npower;m=nthlevel
    powerSum = 0
    prev=0

    if m==0 or m==1: return 0
    m-=1
    facts={}
    facts[0]=0
    for i in range(0,m):
       z = n**i
       facts[i+1] = z + facts[i]
       print facts[i]

    print facts
    powerSum=sum(facts[i] for i in xrange(m+1)) 
      
 
#1 , 2+1+1, 4+2+1 + 2+1 + 1,  8+4+2+1 + 4+2+1 + 2+1 + 1
#(1, 4, 11, 26) 
# reduce(lambda x,y:n*x+y,range(0,3))

    return powerSum


	
def gcd(a,b):
  if b==0:
     return a
  else:
     return gcd(b, a%b)


def gcdtwo(a, b):

    if a == 0:
       return b

    while not b==0:
        if a > b:
           a -= b
        else:
           b -= a
    return a


def IsPanDig(n):
  haszero = False
  nstr = str(n)
  lstr = len(str(n))
  sumdig = 1

  for i in range(0,lstr):
    if nstr[i]=="0":
      haszero = True
    else:
      sumdig = sumdig * int(nstr[i])

  if haszero: lstr = lstr -1
  print "sumdig,lstr", sumdig, nstr, lstr  

  if sumdig == factorial(lstr):return True
  return False

def RetFact(n):
  #from time import time
  #st = time()
  ndiv = n
  factlist=[ ]
 
  ctr = 2
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(ctr)==0:
      factlist.append(ctr)
      ndiv /= (ctr)
    else:
      ctr +=1
  #print "process time",time()-st
  return factlist


def RetFact2(n):
  from time import time
  st = time()
  ndiv = n
  factlist=[ ]
  powlist=[ ]
  ctr = 2
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(ctr)==0:
      factlist.append(ctr)
      ndiv /= (ctr)
    else:
      ctr +=1
  print "process time",time()-st
  return factlist   




def appendEs2Sequences(sequences,es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):

    return reduce(appendEs2Sequences,lists,[])


def primefactors(n):
  
    i = 2
    while i<=n**.5:   #sqrt(n):
        if n%i==0:
            l = primefactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]      # n is prime



def factorGenerator(n):
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[map(lambda x:k**x,range(0,factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors






def d(p1,p2):
  dx = p1[0]-p2[0]
  dy = p1[1]-p2[1]
  return (dx**2 + dy**2)**.5


  
# from collections import defaultdict
# from functools import reduce
# from itertools import combinations
# from operator import mul

def Factor(n):

  n += 1
  f = collections.defaultdict(list)
  t = range(n)

  for p in xrange(2, n):
     if p not in f:
       t[p] = p - 1
       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
         f[i].append(k)
         t[i] = t[i] * (p - 1) // p
  return f, t


  
#import gmpy2

def factorialMod(n, modulus):
    ans=1
 

    for i in range(1,modulus-n):
        ans = (ans * i) % modulus
    ans = gmpy2.invert(ans, modulus)

    #Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
    if n % 2 == 0:
        ans = -1*ans + modulus
    return ans % modulus
	

#______________________________

if __name__ == "__main__":

  testfunc = 4

  if testfunc==1:
     x= IsPalindrome(198717891)
     y= IsPalindrome(12)
     print x, y

  elif testfunc==2:
     print RofPrimes(500000)
   
  elif testfunc==3:
     print PowerSum(2,4)

  elif testfunc==4:
     print RetFact(1888117678800)
#1888117678800
#5065186134317