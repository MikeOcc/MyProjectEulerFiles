#
#
#  Euler 145
#
#

def IsOdd(m):

  nlist = list(str(n))
  for a in nlist:
   if int(a)%2==0:return False
  return True



summ = 0

for i in xrange(10**7,10**8):
  #if i%10==0 or 
  n= i + int(str(i)[::-1])
  y = IsOdd(n)
  if y and i%10>0 :
    summ+=1
    print i, n, IsOdd(n)

print "Answer is", summ