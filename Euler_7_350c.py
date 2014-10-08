#
#
# Euler 350
#
#
from itertools import permutations, combinations
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

#print GCD([11])
#exit()


G=10
L=100

x=range(10,101)
sl = set()
ans=[]
ctr = 0

for i in x:
  for j in x:
    for k in x:
      for m in x:
       for o in x:
         for p in x:
           s = i,j,k,m,o,p
           lst = list(s)
           print s,GCD(lst),LCM(lst)
           ans.append(lst)
           if GCD(lst)>=G and LCM(lst)<=L: 
             print s, set(s), GCD(lst),LCM(lst)
             ctr+=1
             sl.add(tuple(sorted(set(sorted(lst)))))



print ctr

print
print 
print ctr
print
sl= sorted(sl)
print sl
print 
print len(sl)
print
print ans
print
ctr3=0
for a in sl:
  ctr2=0
  for b in ans:
     if a == tuple(sorted(set(b))):
        ctr2+=1
  print a, ctr2
  ctr3+=ctr2

print
print ctr3




