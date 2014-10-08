#
#  decypher cipher.txt
#
#
from string import *
from itertools import *

a2z = range(97,123)
abc = combinations(a2z,3)

f = open("cipher1.txt","r")

x=f.readlines()
x = str(x[0]).strip(' ').split(',')

#print type(x)
print
ctr=0

#print len(x)
z = 100*"0"

numctr=list(z)
for i in xrange(len(numctr)):
  numctr[i]=0
  
#print "!!", type(numctr[0])

#print "nm", type(numctr), len(numctr)
#print numctr

for i in xrange(0,len(x)):
  ctr+=1 
  #print ctr,crypts
  #c=chr(int(i))
  #a,c,b = x[i],x[i+1],x[i+2]
  print i ,x[i]
  numctr[int(x[i])] = numctr[int(x[i])] +1

print

for i in xrange(len(numctr)):
  print i,numctr[i]

print "#---------------------"
ctr=0


abc = (ord('g'),ord('o'),ord('d'))


print "key =", chr(abc[0])+chr(abc[1])+chr(abc[2])
ctr+=1
str1 = ""
for i in xrange(0,len(x)):
    if i%3==0:str1 += chr(abc[0]^int(x[i]))
    if i%3==1:str1 += chr(abc[1]^int(x[i]))
    if i%3==2:str1 += chr(abc[2]^int(x[i]))


print ctr,":",str1
sum1=0

for j in xrange(0,len(str1)):
  #print ord(str1[j])
  sum1 += ord(str1[j])

print "the sum John's msgs is" , sum1


"""
for a in range(97,123):
  for b in range(97,123):
    for c in range(97,123):

      crypt = (a,b,c)

      print "key =", chr(crypt[0])+chr(crypt[1])+chr(crypt[2])
      ctr+=1
      str1 = ""
      for i in xrange(0,50):
        if i%3==0:str1 += chr(crypt[0]^int(x[i]))
        if i%3==1:str1 += chr(crypt[1]^int(x[i]))
        if i%3==2:str1 += chr(crypt[2]^int(x[i]))
      print ctr,":",str1
"""



f.close()
