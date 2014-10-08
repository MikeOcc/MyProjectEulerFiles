#
#
#  Euler Problem 112
#
#

def bouncy(n):

  n1 = list(str(n))
  nlen = len(n1)

  tmp = 0
  for i in xrange(nlen-1):
    if n1[i+1]>=n1[i]:
      tmp+=1
  if tmp==nlen-1:
    return 1    #  inc

  tmp = 0
  for i in xrange(nlen-1):
    if n1[i+1]<=n1[i]:
      tmp+=1
  if tmp==nlen-1:
    return -1   # dec.

  return 0     #  bouncy

#############
'''
print bouncy(11)
print bouncy(99998887111)
print bouncy(157)
print bouncy(15393)
'''
tot = 10000000
numb = 0
for j in xrange(1,tot+1):
  if bouncy(j)==0:numb+=1
  if (numb*100)/j==99:
     print "yeah!",j, numb
     break
     
print 
print (numb*100)/j

