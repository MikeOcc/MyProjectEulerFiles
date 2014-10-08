#
#
# Euler 350
#
#
from itertools import combinations, permutations

def gcd(a,b):
   """Return greatest common divisor using Euclid's Algorithm."""
   while b:      
	a, b = b, a % b
   return a

def lcm(a,b):
   """
   Return lowest common multiple."""
   return (a*b)/gcd(a,b)

def GCD(terms):
   "Return gcd of a list of numbers."
   return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
   "Return lcm of a list of numbers."   
   return reduce(lambda a,b: lcm(a,b), terms)

print GCD([10,20,40,80,100])
print LCM([10,20,50,100])
#exit()

#if GCD(lst)>=G and LCM(lst)<=L: 

G=10
L=100
N=3

ctr = L-G + 1



for i in xrange(G,L+1):     #L/2+1):
  lsti=[]
  for k in xrange(1,N):
      
      x=combinations(range(i*2,L+2,i),k)
      for y in x:
        print "!",y
        lst=[i]
        for z in y:
          lst.append(z)
          if lst not in lsti and (GCD(lst)>=G and LCM(lst))<=L:
            print lst
            lsti.append(lst)
            ctr += 6


#print lst
print ctr