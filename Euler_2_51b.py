###
# Problem 51 of Project Euler
###
from time import time
from math import *

from Functions import RofPrimes

def findMults(n,m):

  #if n == 56993: print "YEAH"
  retval = 0
  s=[0,0,0,0,0,0,0,0,0,0]
  nstr = str(n)
  nlen = len(str(n))
  nstr = nstr[:nlen-1]
  #nlen = len(str(n))

  for i in range(0,len(nstr)):
     s[int(nstr[i])] += 1
 
  #print s
 
  for j in range(0,len(s)):
     if s[j]>m-1:
       retval += (j+1)*s[j]

  #print retval

  return retval

#################################
st = time()
x=RofPrimes(100000,1000000)

#print x
print "number of primes searched:",len(x)
print
print "________________"

y=[]
z=[]
ctr=0
for i in range(0,len(x)):

  m=2

  if findMults(x[i],m)>m-1:
    temp=str(x[i])
    if len(temp)<6:continue
 
    temp2 = temp[1:2]+temp[3:4]+temp[5:]
    zz =  temp[0:1]+temp[2:3]+temp[4:5]

    if len(set(zz))==1:
      y.append(temp)

      #print ctr,y[ctr]
      ctr+=1

      z.append(temp2)
      
print

"""
#print y
for i in range(0,len(y)):
   
  print i,z[i],"<",y[i]

print
"""
print "&&&&&&&&&&&&&&&&&&&&&&"

setz= list(set(z))
#print z.count('563')

for k in xrange(len(setz)):
   u= z.count(setz[k])
   if u==8:
     samedigs = setz[k]
     print k,":",u,":",setz[k]
print "&&&&&&&&&&&&&&&&&&&&&&"
print

zanswer=0
for i in range(0,len(y)):
   
  if z[i]==samedigs:
     print y[i]
     if zanswer==0:zanswer=y[i]

print
print "The smallest prime of the 8 family primes is", zanswer
print
print "Process time is",time()-st

