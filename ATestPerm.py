#
#
#
#
#
#
from math import log
def base3int(x):
    x = int(x)
    exponents = range(int(log(x, 3)), -1, -1)
    for e in exponents:
        d = int(x // (3 ** e))
        x -= d * (3 ** e)
        yield d


###################################

for i in xrange(1000,20000):
  #z = base3int(i)
  num = [] 
  for y in base3int(i):
    num.append(str(y))
  num1 = "".join(num)
  print int(num1)