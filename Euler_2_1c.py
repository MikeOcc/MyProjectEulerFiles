from math import *
from Functions import RofPrimes

def findMults(n,m):


  retval = 0
  s=[0,0,0,0,0,0,0,0,0,0]
  nstr = str(n)
  
  for i in range(0,len(nstr)):
     s[int(nstr[i])] += 1
 
  #print s
 
  for j in range(0,len(s)):
     if s[j]>m-1:
       retval += (j+1)*s[j]

  #print retval

  return retval


x=RofPrimes(10000,200000)

print x
print
print "________________"

for i in range(0,len(x)):

  m=3

  if findMults(x[i],m)>m-1:
    temp =str(x[i])
    print temp[4:]
    if temp[5:6]=='33' :
      print "hit!",x[i]



