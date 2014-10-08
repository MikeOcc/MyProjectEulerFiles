#
#
# Euler Problem 236
#
#

from Functions import gcd
'''
A=[5248,1312,2624,5760,3936]
B=[640,1888,3776,3776,5664]


u0=1476;v0=1475
'''

LIMIT = 1000

i,j,k,t,t2,g,s,s2=0,0,0,0,0,0,0,0

for i in xrange(1,LIMIT+1):
   for j in xrange(1,LIMIT+1):
      for k in xrange(1,LIMIT+1):

         t = 6372*(41*i+205*j+5*k)
         t2 = 205*(90*i+5310*j+59*k)
         g = gcd(t,t2)
         t /= g
         t2 /= g
         s = int(t**.5)
         if s*s == t:
            s2 = int(t2**.5)
            if (s2*s2 == t2 and s*41 > 59*s2 and s*i <= 37760 and s*j <= 11328 and s*k <= 339840):
               print i,j,k,s,s2

