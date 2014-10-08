#
#
# Euler Problem 93
#
#

from itertools import combinations, permutations

def f(n):

  l=[]
  a,b,c,d=n[0],n[1],n[2],n[3]
  ops = ["+","*","/","-"]

  opset = permutations(ops,3)

  for O in opset:
    s1,s2,s3=O[0],O[1],O[2]

    try:
      e = eval("((a"+s1+"b)"+s2+"c)"+s3+"d") #((a*b)-c)+d
    except:
      e=0

    try:
      f = eval("(a"+s1+"b)"+s2+"(c"+s3+"d)")   #(a*b)-(c+d)
    except:
      f=0

    try:
      g = eval("(a"+s1+"(b"+s2+"c))"+s3+"d")  #(a*(b-c))+d
    except:
      g=0

    try:
      h = eval("a"+s1+"((b"+s2+"c)"+s3+"d)")  #a*((b-c)+d)
    except:
      h=0

    try:
      i = eval("a"+s1+"(b"+s2+"(c"+s3+"d))")  #a*(b-(c+d))
    except:
      i=0

    l.append(e)
    l.append(f)
    l.append(g)
    l.append(h)
    l.append(i)

  return l

#  "((a"+s1+"b)"+s2+"c)"+s3+"d"

N = [1,2,3,4,5,6,7,8,9]


S1 = combinations(N,4)
ctr=0
max1,max2=0,0
maxs=()
for S in S1:

  L=[]
  S0=S
  print "!",S
  print
  X = permutations(S0,4)

  for x in X:
    y = f(x)
    for z in y:
      if z!=0 and abs(z) not in L:L.append(abs(z))
  print sorted(L)
  if len(L)>max1:
    max1 = len(L)
    max2 = L
    maxs = S


print
print max1,sorted(max2),maxs








