

from math import sqrt
N = 10**3
print
print "calculating strong rep units for N<=",N,"..."
M={}
tot = 1
n = 1
while 1:
  rep = 2**n-1
  if rep>=N:break
  #tot+=rep
  print n,rep
  try:
    M[rep]+=1
  except KeyError:
    M[rep]=1
  n+=1

b1 = int((-1 + sqrt(1 - (4*(1-N))))/2.)

b=3
while b<b1+1:
  print "base:",b

  rep = 1
  n=1
  while rep <= N:
    rep += b**n
    if rep>=N:
       break
    else:
       print n,rep
       try:
         M[rep]+=1
       except KeyError:
         M[rep]=1

    n+=1
  b+=1
   # if rep>=N:
   #   break
   


#print 
#print M
'''
for i in xrange(len(M)):
    try:
       if M[i]>1:
         print i
         tot +=i
    except KeyError:
       pass
'''

for key in M:

  if M[key]>1:
     print "!",key, M[key]
     tot +=key

print "Sum for all strong repunits is",tot
print

for key in M:
  if key> b1+1 and M[key]==1:
    print "!",key, M[key]
    tot +=key

print "tot",tot


