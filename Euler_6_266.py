#
# Problem 266
#
#
global basex

basex=1777

from Functions import IsPrime
from math import floor,sqrt
from itertools import combinations,permutations
BigP = 1

for i in range(2,190):
  if IsPrime(i):
    BigP *= i

#BigP=long(BigP)

qq=1
SQP= BigP**.500000
print "SQP", SQP

print "________________________"

answer = 1
qq=1
factors=[]

for j in range(2,190):
  if not IsPrime(j):continue
  factors.append(j)
answer = 0

print
print factors

print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
print

for i in range(24, 28):

  print "Set of numbers of length i",i

  zz = combinations(factors,i)

  answer0=1
  
  for zzz in zz:
    #print zzz
    for jz in range(len(zzz)):
     answer0*=zzz[jz]
     
    if answer0>SQP:
       #print "Hit!"
       ctr2=0
       while answer0>SQP:
         answer0/=zzz[ctr2]
         ctr2+=1
         if answer0<SQP:
            #print "possible answer",answer0 
            if answer0>answer:
               answer=answer0
               print "i,jz",i,jz,answer
            break
       #break


print BigP,SQP
print answer, answer%10**16,answer%10**10

print BigP/answer



