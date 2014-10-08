#
#
#  Euler 118
#

from itertools import combinations,permutations
from time import time
from Euler import miller_rabin

st = time()

d = {}

d[1]=['2','3','5','7']
l = [1,2,3,4,5,6,7,8,9]
for w in xrange(2,10):
  d[w]=[]

for i in xrange(2,9):

  x = combinations(l,i)

  for p in x:

    xx = permutations(p)
  
    for xxx in xx:
      qp = ''.join(str(i) for i in xxx)
      n = int(qp)
      if len(qp)!=len(set(qp)):continue
      if miller_rabin(n): 
        #print n
        d[i]+= [qp]

ctr=0

a1 = d[1]
b1 = d[2]
c1 = d[3]
d1 = d[4]
e1 = d[5]
f1 = d[6]
g1 = d[7]
h1 = d[8]

zz,zz1,zz2,zz3,zz4,zz5,zz6,zz7='','','','','','','',''
for q in [1,0]:
  for o in [0,1]:
    for n in [0,1]:  # 6s
      for m in [0,1]: # 5s
         for l in [0,1,2]: # 4s
           for k in [0,1,2,3]: # 3s  
             for j in [0,1,2,3,4]: # 2s
               for i in [1,0,2,3,4]: # 1s
                 if i+j*2+k*3+l*4+m*5+n*6+o*7+q*8 != 9:continue
                 print i,j,k,l,m,n,o,q
			 
                 a = combinations(a1,i)
                 for aa in a:
                   zz = ''.join(aa)
                   b = combinations(b1,j)
                   for bb in b:
                     zz1=''.join(bb)
                     c = combinations(c1,k)
                     for cc in c:
                       zz2=''.join(cc)
                       d = combinations(d1,l)
                       for dd in d:
                         zz3=''.join(dd)
                         e = combinations(e1,m)
                         for ee in e:
                           zz4=''.join(ee)
                           f = combinations(f1,n)
                           for ff in f:
                             zz5=''.join(ff)
                             g = combinations(g1,o)
                             for gg in g:
                               zz6=''.join(gg)
                               h = combinations(h1,q)
                               for hh in h:
                                 zz7=''.join(hh)
                                 pandig = zz+zz1+zz2+zz3+zz4+zz5+zz6+zz7
                                 if len(set(pandig))==9:
                                   #print pandig,":",i,j,k,l,m,n,o,q
                                   ctr+=1

print ctr

print time() - st


