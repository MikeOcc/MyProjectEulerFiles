#
#
#  Euler Problem 386
#
#
from collections import defaultdict
from Functions import divisors,RetFact
from collections import defaultdict
#,FactorSieve
from time import time

def FactorSieve(n):
  
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

st=time()

N = 10**8

print "Factoring Integers..."
#f = FactorSieve(N)
print "Done"
# for i in f:
  # print f[i]

summ = 0
# for i in xrange(1,N+1):
  # sl=len(set(f[i]))
  # if f[i]==[i] or sl==1:
    # summ+=1
    # continue
  
  # if sl==2:
    # summ+=2
    # continue

  # summ +=sl
def canAdd(s,y):
  #canAdd=True
  for z in s:
    if y>z:
      if y/z==(1.0 * y)/z:
        return False
    else:
      if z/y==(1.0 * z)/y:
        return False
  return True

d = divisors(120120)

x=[]
s=set(x) 
s2=set(x)

for x in d:

  z = RetFact(x)
  S = set(z)
  summ = 0
  for SS in S:
    summ += z.count(SS)
  if summ == 4:
    print x


# for x in d:
  # z = RetFact(x)
  # two = z.count(2)
  # zz = x/(2**two)
  # zzz = 3**(two+1)*zz
  # if zzz>(120120/4):
    # print x,two, zz,z


# for i in xrange(126,2,-1):
  # s = set([d[i]])
  # for j in xrange(i-1,1,-1):
    #if d[j]%5==0:continue
    # if canAdd(s,d[j]):
      # s=s.union(set([d[j]]))
  # for j in xrange(127,2,-1):
    #if d[j]%5==0:continue
    # if (d[j] not in s) and canAdd(s,d[j]):
      # s=s.union(set([d[j]]))
	  
  # if len(s)>len(s2):
    # s2=s
	
print len(s2)
print sorted(s2)
print

for x in s2:
  print x, set(RetFact(x))
	
# print summ
print "time elapsed", time()-st


