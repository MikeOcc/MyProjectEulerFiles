#
#
#  Euler 156
#
#




def f(d):
  s = 0
  n = 0
  x = 0
  d1 = str(d)
  while 1:
    n+=1
    ns = str(n)
    #if "1" in ns:
    x += ns.count('1')
    if x == n:
      s+=n
      print n,s
      
    if x >= 22786974071:
           #21675862961
      break

  return s

print f(1)