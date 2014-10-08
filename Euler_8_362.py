

from Functions import divisors,IsPrime

def IsSF(d):
  v = 0
  D1 = divisors(d)
  D1.remove(1)

  for d1 in D1:
    if d1**.5 == int(d1**.5):
      return False

  return True

summ = 0
for k in xrange(2,101):
  cnt = 0
  D = divisors(k)
  D.remove(1)
  for d in D:

     if IsSF(d): 
       cnt +=1
       print "!",k,d,cnt

  summ += cnt
  print k, cnt


print summ
