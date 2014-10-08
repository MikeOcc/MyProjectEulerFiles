#
#  Problem 206
#
# []

from time import time

def f(n):

  n1 = list(str(n))
  m = ""
  for x in xrange(1,10):
    m+=str(x)+n1[x-1]
  m += "0"

  return int(m)

def f10(n):
  n1 = list(str(n))
  m = "1234567890"
  for x in range(0,20,2):

    if m[x/2] != n1[x]:return False

  return True #  m=="1234567890"


if __name__ == "__main__":
  #a = f(234567890)
  #print a, a**.5
  st = time()

  for i in xrange(101010101,138902663):
    z = str(i)[-1]
    if (z=="7" or z=="3"):
      a = (i*10)**2
      if f10(a):
        print "Hit!", i,a
        break

print
print "The answer is", i*10
print "process time is", time()-st



