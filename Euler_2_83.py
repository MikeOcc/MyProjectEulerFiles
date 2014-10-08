#
#
# Euler Problem 83
#
#[s]

f = open('matrix.txt')

g=[[0 for col in range(80)] for row in range(80)]

#print ar
#print
#print ar[6][20]


x = f.readlines()
i=0
for y in x:
  
  z = y.strip().split(",")
  j=0
  for v in z:
    
    g[i][j]=int(v)
    j+=1

  i+=1
print 
#############################

print g[0][0],g[0][1]
summ = g[0][0]
d={}
maxr,maxcol=79,79
cr,cc = 0,0
while True:
  if cr == cc== 0:
    a = g[0][1]
    b = g[1][0]
    if a<b:
      cr,cc=0,1
      summ+=a
      d[(cr,cc)]=1
    else:
      cr,cc=1,0
      summ+=b
      d[(cr,cc)]=1	
  elif cr==0 and cc>0 and cc<79:
    a = g[0][cc+1]
    b = g[1][cc]
    if a<b:
      cr,cc=0,cc+1
      summ+=a
      d[(cr,cc)]=1
    else:
      cr,cc=1,cc
      summ+=b
      d[(cr,cc)]=1    
  elif cc==0 and cr>0 and cr<79:
    a = g[cr][1]
    b = g[cr+1][0]
    if a<b:
      cr,cc=cr,1
      summ+=a
      d[(cr,cc)]=1
    else:
      cr,cc=cr+1,0
      summ+=b
      d[(cr,cc)]=1  
  elif cc>0 and cr>0 and cc<79 and cr<79:
    print "cr,cc",cr,cc
    a = (cr,cc-1)
    b = (cr-1,cc)
    c = (cr,cc+1)
    e = (cr+1,cc)
    print a,b,c,e
    if a in d:
      a=10**6
    else:
      a=g[cr][cc-1]

    if b in d:
      b=10**6
    else:
      b=g[cr-1][cc]

    if c in d:
      c=10**6
    else:
      c=g[cr][cr+1]

    if e in d:
      e=10**6
    else:
      e=g[cr+1][cc]

    print a,b,c,e
    zx,zy=cr,cc

    if a==min(a,b,c,e):
      cr,cc=zx,zy-1
    elif b==min(b,c,e):
      cr,cc=zx-1,zy
    elif c==min(c,e):
      cr,cc=zx,zy+1
    else:
      cr,cc=zx+1,zy
    summ+=g[cr][cc]
    d[(cr,cc)]=1
  elif cc==79 and cr<79:
    cr+=1
    summ+=g[cr][cc]
    d[(cr,cc)]=1
  elif cc==79 and cr==79:
    break
  else:
    print cr,cc

print summ