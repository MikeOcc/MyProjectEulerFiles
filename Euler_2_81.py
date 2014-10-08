#
#
# Euler Problem 81
#
#[s]

f = open('matrix.txt')

ar=[[0 for col in range(80)] for row in range(80)]

#print ar
#print
#print ar[6][20]


x = f.readlines()
i=0
for y in x:
  
  z = y.strip().split(",")
  j=0
  for v in z:
    
    ar[i][j]=v
    j+=1

  i+=1
print 
'''
for i in xrange(80):
  print
  for j in xrange(80):
    print ar[i][j],
  print
print
'''
summ,i,j=int(ar[79][79]),79,79
while 1:

  print "!",i,j,

  if i>0 and j>0:
    valx = ar[i][j-1]
    valy = ar[i-1][j]
    if int(valx)<int(valy):
      j-=1
      summ+=int(valx)
      print valx,summ
    else:
      i-=1
      summ+=int(valy)
      print valy,summ
  elif i==0 and j>0:
    j-=1
    valx = ar[i][j]
    summ+=int(valx)
    print valx,summ
  elif j==0 and i>0:
    i-=1
    valy = ar[i][j]
    summ+=int(valy)
    print valy,summ
  else:  
    summ+=int(ar[0][0])
    print ar[0][0],summ
    break

print "Answer is ",summ



