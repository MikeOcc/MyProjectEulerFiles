###
# Problem 51 of Project Euler
###

from math import *

from Functions import RofPrimes

def findMults(n,m):

  #if n == 56993: print "YEAH"
  retval = 0
  s=[0,0,0,0,0,0,0,0,0,0]
  nstr = str(n)
  nlen = len(str(n))
  nstr = nstr[:nlen-1]
  nlen = len(str(n))

  for i in range(0,len(nstr)):
     s[int(nstr[i])] += 1
 
  #print s
 
  for j in range(0,len(s)):
     if s[j]>m-1:
       retval += (j+1)*s[j]

  #print retval

  return retval

#################################

x=RofPrimes(10000,1000000)

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
    #temp = temp[:1]+temp[2:3]+temp[4:]
    #temp2 = temp[:2]+temp[4:]
    #zz = temp[2:4]
    #temp2 = temp[0:1]+temp[3:] 
    #zz = temp[1:3] 
    #temp2 = temp[3:] 
    #zz = temp[0:3]
    #temp2 = temp[1:2]+temp[4:] 
    #zz =  temp[0:1]+temp[2:4]
    #temp2 = temp[2:3]+temp[5:] 
    #zz =  temp[1:2]+temp[3:5]
    temp2 = temp[1:2]+temp[3:4]+temp[5:] 
    zz =  temp[0:1]+temp[2:3]+temp[4:5]

    if len(set(zz))==1:
      y.append(temp)

      #temp =str(x[i])
      #print temp[4:]
      print ctr,y[ctr]
      ctr+=1

      z.append(temp2)
      #if set(temp2=='87'

print
print "&&&&&&&&&&&&&&&&&&&&&&"
'''
print y
for i in range(0,len(y)):
   
  print i,z[i],"<",y[i]

print
'''
print "&&&&&&&&&&&&&&&&&&&&&&"

setz= list(set(z))
print z.count('563')

for k in xrange(len(setz)):
   u= z.count(setz[k])
   if u>5:
     print k,":",u,":",setz[k]

