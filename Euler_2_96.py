#
#
#  Euler Problem 96
#
#
from string import strip

def solve(g):

  cnt=[0]*10
  print # "cnt",cnt
  for row in xrange(9):
    for col in xrange(9):
       v=g[row][col]
       #print v
       cnt[v]+=1
  
  print cnt 

  for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print
  print

  p = [ [0 for z in range(9) ] for x in range(9)]  
  for row in xrange(9):
    for col in xrange(9):
       if g[row][col]>0:
          p[row][col]=-1
       else:
          p[row][col]=range(1,10)
  '''
  for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]
  '''

  for z in xrange(20):

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         for i in xrange(9):
           if g[row][i] in p[row][col]: 
             t = p[row][col]
             t.remove(g[row][i])   
             p[row][col]=t
         for i in xrange(9):
           if g[i][col] in p[row][col]: 
             t = p[row][col]
             t.remove(g[i][col])   
             p[row][col]=t
   print
   '''
   for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]
   '''
   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1 and len(p[row][col])==1:
        g[row][col]=p[row][col][0]
        p[row][col]=-1
   '''
   for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]
   '''

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         for i in xrange(9):
           if g[row][i] in p[row][col]: 
             t = p[row][col]
             t.remove(g[row][i])   
             p[row][col]=t
         for i in xrange(9):
           if g[i][col] in p[row][col]: 
             t = p[row][col]
             t.remove(g[i][col])   
             p[row][col]=t
   print
   for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print

   print
   '''
   for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]
    print
   '''

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1 and len(p[row][col])==1:
        g[row][col]=p[row][col][0]
        p[row][col]=-1
   print

   for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         for i in xrange(9):
           if g[row][i] in p[row][col]: 
             t = p[row][col]
             t.remove(g[row][i])   
             p[row][col]=t
         for i in xrange(9):
           if g[i][col] in p[row][col]: 
             t = p[row][col]
             t.remove(g[i][col])   
             p[row][col]=t

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1 and len(p[row][col])==1:
        g[row][col]=p[row][col][0]
        p[row][col]=-1
   print

   for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print


   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         for i in xrange(9):
           if g[row][i] in p[row][col]: 
             t = p[row][col]
             t.remove(g[row][i])   
             p[row][col]=t
         for i in xrange(9):
           if g[i][col] in p[row][col]: 
             t = p[row][col]
             t.remove(g[i][col])   
             p[row][col]=t

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1 and len(p[row][col])==1:
        g[row][col]=p[row][col][0]
        p[row][col]=-1
   print
   for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print

  for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]

S = [ [ [idx for idx in range(50) ] for row in range(9)] for col in range(9)]

f = open('sudoku.txt','r')

ctr=-1
ctr1=0
for x0 in f.readlines():
  #
  x = x0.strip()
  #print len(x0)
  #print x0
  if x[0]=="G":
   #print x
   ctr+=1
   ctr1=0
   continue
  else:
    for y in xrange(0,9):
      z = x[y]
      #print ctr,ctr1,y,z
      S[ctr1][y][ctr] = int(z)
    ctr1+=1

print
for i in xrange(2,3):

  g = [ [0 for z in range(9) ] for x in range(9)]

  for row in xrange(9):
    for col in xrange(9):
       g[row][col] = S[row][col][i]

  print g
  solve(g)
    
  print
  print
