#
#
#  Euler 122
#
#

from Functions import RetFact
from math import log

m={1:1}

# for k in range(2,201):
  # x = 2**k
  # p = log(k)/log(2)
  # if p == int(p): m[k]=int(p)
  # print k, p, x  


for n in range(2,201):
  p = log(n)/log(2)
  if p == int(p):
     m[n]=int(p)
     continue

  l = [1,2]
  steps = 1
  t = 2
  cur = 2
  while t < n:
    t = t * 2
    steps += 1
    if t > n:
      t = t /2
      steps -= 1
      break
    l.append(t)
  print n,t,l	
  
  for i in range(1,len(l)+1):  
    nxt = t + l[-i]
    if nxt <= n:
      steps +=1
      t = nxt
    if t == n: break
  print n,t
  
 
  
  #--------------------
  
  l = [1,2,3]
  steps3 = 2
  t = 3
  cur = 2
  while t < n:
    t = t * 2
    steps3 += 1
    if t > n:
      t = t /2
      steps3 -= 1
      break
    l.append(t)
  print n,t,l	
  
  for i in range(1,len(l)+1):  
    nxt = t + l[-i]
    if nxt <= n:
      steps3 +=1
      t = nxt
    if t == n: break
  print "!:",n,t
  
  if steps3 < steps: steps = steps3
  
  #--------------------------------------
  
  l = [1,2,3,5]
  steps5 = 3
  t = 5
  cur = 2
  while t < n:
    t = t * 2
    steps5 += 1
    if t > n:
      t = t /2
      steps5 -= 1
      break
    l.append(t)
  print n,t,l	
  
  for i in range(1,len(l)+1):  
    nxt = t + l[-i]
    if nxt <= n:
      steps5 +=1
      t = nxt
    if t == n: break
  print "!:",n,t  
  
  if steps5 < steps: steps = steps5
#-----------------------------------------

  l = [1,2,3,5,7]
  steps7 = 4
  t = 7
  
  while t < n:
    t = t * 2
    steps7 += 1
    if t > n:
      t = t /2
      steps7 -= 1
      break
    l.append(t)
  print n,t,l	
  
  for i in range(1,len(l)+1):  
    nxt = t + l[-i]
    if nxt <= n:
      steps7 +=1
      t = nxt
    if t == n: break
  print "!:",n,t  
  
  if steps7 < steps: steps = steps7

#-----------------------------------------

  l = [1,2,3,5,10,15]
  steps7 = 5
  t = 15
  
  while t < n:
    t = t * 2
    steps7 += 1
    if t > n:
      t = t /2
      steps7 -= 1
      break
    l.append(t)
  print n,t,l	
  
  for i in range(1,len(l)+1):  
    nxt = t + l[-i]
    if nxt <= n:
      steps7 +=1
      t = nxt
    if t == n: break
  print "!:",n,t  
  
  if steps7 < steps: steps = steps7
  
  #-----------------------------------------------------
  
  m[n] = steps

  
print 
print m
print

summ = 0
for a in m:
  summ += m[a]
  
print "The sum of m(k) is ", summ
