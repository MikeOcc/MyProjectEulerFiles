#
#
# Euler 350
#
#

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

      s = i,j,k
      lst = list(s)
      #print type(lst),lst
      if GCD(lst)>=G and LCM(lst)<=L: 
        print s,GCD(lst),LCM(lst)
        ans.append(lst)
        ctr+=1
        sl.add(tuple(sorted(set(sorted(lst)))))
        #sl.add(tuple(sorted(lst)))
      #else:
      #  print s,GCD(lst),LCM(lst)
'''

lst=[2]
for i in xrange(4,100,2):
    if GCD(lst)>=G and LCM(lst)<=L: 
        ctr+=1  
    lst.append(i)  
'''
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
