#
#
#
#
#
from time import time

def S(n):

  if n == 0:
    return 290797
  else:
    return (S(n-1)**2) % 50515093
st = time()

S0 = 290797
tot = 0
temp = S0
tot2 = S0
S = [290797]

for i in xrange(0,20):
  S.append((S[i]**2)% 50515093)
print 
print S
print
lim = 20
for i in xrange(1,lim+1):
  for j in xrange(i,lim+1):
    if j<i: continue

    A = min(S[i:j+1])
    print i,j,":",A
    tot += A

print tot

print "process time", time() - st
  



