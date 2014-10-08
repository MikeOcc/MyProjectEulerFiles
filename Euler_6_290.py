from Functions import RetFact

def d(k):

  r = 0
  while k:
    r, k = r + k % 10, k / 10
    #if r>23: return -1
  return r
  
cnt = 0

for i in xrange(0,1000):

  if d(i) == d(i*137):
    print i, i*137, RetFact(i)
    cnt +=1
	
print "count:",i,cnt  #,RetFact(cnt)
