#
#  Euler Problem 41
#
#  find the largest n-digit pandigital prime

from Functions import IsPrime
from time import time

st = time()

highpan = 7654321

def PanDig(n):

  nset = set(str(n))

  for m in range(1,8):
    if str(m) not in nset: return False

  return True

for i in range(highpan, 6999999,-1):
   if PanDig(i) and IsPrime(i):
     print "Pandigital Prime Found! n=",i 
     break

print "Process time is", time()-st