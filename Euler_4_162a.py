#
#
# Euler 160
#
#
from Functions import nCr

summ = 0

for i in xrange(14):
  z =  2*(i+2)*(i+1)*16**i
  summ += z
  print z
 
print summ

summ2 =0

for i in xrange(13):
  #z = 13*(i+3)*(i+2)*(i+1)*16**i
  z = 16*nCr(i+3,3)*16**i
  summ2 += z
  print z

print 
print summ2
summ3=0

for k in xrange(3,17):
  summ3+=15*16**(k-1)-15**(k)-(2*14)*15**(k-1)+(13*14**(k-1))+2*14**k-13**k

# for i in xrange(3,17):
  # summ2 +=43 * 15**(i - 1)* 13**i
# print

# summ -=summ2

print summ3