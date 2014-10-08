#
# 354
#

#cellcnt = {}
#slopes=[]


a = 3**.5
b = 1.5


def Ring(n):

  maxd = n * a
  if n%2 ==0:
    mind = n * b
  else:
    mind = ((n * b)**2 + (a/2)**2)**.5

  num = 6 * n

  if mind==maxd:
    lst = [mind]
  else:
    lst = []
    if n%2==0:strt = 0;offset = 0
    else: strt = 1;offset = -.5

    for j in xrange(strt,n):
      val = ((n*b)**2 + ((a)*j+offset*a)**2)**.5
      if val > maxd:break
      #print "!",n, j, val
      lst.append(val)
    if maxd not in lst:lst.append(maxd)

  return maxd,mind,num,lst

for i in xrange(64150030,64150031):
  print i,Ring(i)