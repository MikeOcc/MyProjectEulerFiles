#
#
#  Euler Problem 153
#
#

from Functions import RetFact, divisors,IsPrime

summ = 6

for n in xrange(3, 6):

   if IsPrime(n):
     
     print n,n%4
     if n%4==1 :
       pass
     else:
       summ += (n+1)
   else:
     d = divisors(n)
     print n,d
     summ +=sum(d)

print
print summ

#
# 6    20   1 ,6, 3, 
# 7     8   1 ,7
# 8    29
# 9    13
# 10   56
# 11   12
# 17   
