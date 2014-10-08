#
#  Euler Problem 305
#
#
from string import find

h = []

for i in xrange(1,14):
  h.append(3**i)

print
print h

s = ""

for i in xrange(1,200000000):  #17000000):
  s += str(i)


print 
#print s
print len(s)
print s[80:81]
print s[270:272]
print s[111111364: 111111368]
print s[-10:]
print
summ=0
kmax=13
for k in range(1,kmax+1): #  (1,kmax+1):
  z=3**k
  zz=str(z)
  i = 0
  pp = []
  for j in xrange(z):
    x=find(s,zz,i)
    i=x+1
    pp.append(i)
  summ += i
  print k,z,i  #,pp

print "Sum of f(n) for i=1 to",kmax,"is",summ

print
print
'''
prev = 0
for vv in pp:
  print vv-prev,
  prev=vv

print
print sum(pp)
print
#print s[30009:31210]
'''