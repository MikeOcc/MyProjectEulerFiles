#
#
# Euler Problem 81
#
#[s]

f = open('matrix.txt')

data=[[0 for col in range(80)] for row in range(80)]

#print ar
#print
#print ar[6][20]


x = f.readlines()
i=0
for y in x:
  
  z = y.strip().split(",")
  j=0
  for v in z:
    
    data[i][j]=int(v)
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

for i in range(78,-1,-1):
  print i,data[79][i],data[i][79]
print
for i in range(78,-1,-1):
 #print i,data[79][i]
 data[79][i] += data[79][i+1]
 data[i][79] += data[i+1][79]
 print i,data[79][i],data[i][79]
print
print i,data[79][i],data[i][79]
print "!",data[0][0]

#For each cell, add which ever is lower, the cell to the right, or the cell below
for i in range(78,-1,-1):
 for j in range(78,-1,-1):
  #data[i][j] += data[i][j+1] if (data[i][j+1] < data[i+1][j]) else data[i+1][j]
  print i,j,":",i+1,j+1
  if (data[i][j+1] < data[i+1][j]):
    data[i][j] += data[i][j+1]
    print "sideways"
  else:
    data[i][j] += data[i+1][j]
    print "updown"
print data[0][0]



