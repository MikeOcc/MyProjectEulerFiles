from Functions import RetFact

def d(k):

  r = 0
  while k:
    r, k = r + k % 10, k / 10
    if r>23: return -1
  return r
  
cnt = 0
for j in xrange(8,10):
  for i in xrange(0,10**j,23):

    if d(i) == 23:
      print i
      cnt +=1
	
  print j,cnt  #,RetFact(cnt)
