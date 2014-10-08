#
#
#
#

from Functions import primes, IsPrime
from itertools import combinations,permutations
from time import time
from Euler import miller_rabin

def is_pandigital(n, s=9): n=str(n);return len(n)==s and not '1234567890'[:s].strip(n)

st = time()

d = {}

d[1]=['','2','3','5','7']
l = [1,2,3,4,5,6,7,8,9]
for w in xrange(2,10):
  d[w]=['']

for i in xrange(2,9):

  x = combinations(l,i)


  for p in x:

    xx = permutations(p)
  
    for xxx in xx:

    #print xxx
      qp = ''.join(str(i) for i in xxx)
      n = int(qp)
      if len(qp)!=len(set(qp)):continue
      if miller_rabin(n):   #IsPrime(n):
        #print n
        d[i]+= [qp]

ctr=0

#print d[8]
#print
#print len(d[8])
#exit()

a1 = d[1]
b1 = d[2]
c1 = d[3]
d1 = d[4]
e1 = d[5]
f1 = d[6]
g1 = d[7]
h1 = d[8]

# for i in xrange(0,5):
  # for j in xrange(0,5):
    # for k in xrange(0,4):  # 3s
      # for l in xrange(0,3): # 4s
         # for m in xrange(0,2): # 5s
           # for n in xrange(0,2): # 6s  
             # for o in xrange(0,2): # 7s
               # for q in xrange(0,2): # 8s
zz,zz1,zz2,zz3,zz4,zz5,zz6,zz7='','','','','','','',''
for q in [1,0]:
  for o in [0,1]:
    for n in [0,1]:  # 6s
      for m in [0,1]: # 5s
         for l in [0,1,2]: # 4s
           for k in [0,1,2,3]: # 3s  
             for j in [0,1,2,3,4]: # 2s
               for i in [0,1,2,3,4]: # 1s
                 if i+j*2+k*3+l*4+m*5+n*6+o*7+q*8 != 9:continue
                 print i,j,k,l,m,n,o,q
                 ctr+=1
                 zz='0'
                 # a1 = d[1]
                 # b1 = d[2]
                 # c1 = d[3]
                 # d1 = d[4]
                 # e1 = d[5]
                 # f1 = d[6]
                 # g1 = d[7]
                 # h1 = d[8]
				 
                 a = combinations(a1,i)
                 b = combinations(b1,j)
                 c = combinations(c1,k)
                 d = combinations(d1,l)
                 e = combinations(e1,m)
                 f = combinations(f1,n)
                 g = combinations(g1,o)
                 h = combinations(h1,q)
                 for aa in a:
                   zz = ''.join(aa)
                   #print "!",aa,zz
                   #print "!",zz
                   for bb in b:
                     zz1=''.join(bb)
                     for cc in c:
                       zz2=''.join(cc)
                       #print "#",zz2,zz1,zz,''.join(cc),i,j,k,l,m,n,o,q
                       for dd in d:
                         zz3=''.join(dd)
                         for ee in e:
                           zz4=''.join(ee)
                           for ff in f:
                             zz5=''.join(ff)
                             #print zz5
                             for gg in g:
                               zz6=''.join(gg)
                               for hh in h:
                                 zz7=''.join(hh)
                                 print "! ",zz+zz1+zz2+zz3+zz4+zz5+zz6+zz7
                                 if len(zz7+zz6+zz5+zz4+zz3+zz2+zz1+zz)==len(set(zz7+zz6+zz5+zz4+zz3+zz2+zz1+zz)) and len(zz7+zz6+zz5+zz4+zz3+zz2+zz1+zz)==10:
                                   #print zz7,zz6,zz1,zz,hh,":",i,j,k,l,m,n,o,q
                                   ctr+=1
                               if len(zz6+zz5+zz4+zz3+zz2+zz1+zz)==len(set(zz6+zz5+zz4+zz3+zz2+zz1+zz)) and len(zz6+zz5+zz4+zz3+zz2+zz1+zz)==10:
                                 #print zz6,zz5,gg,l,j,k,l,m,n,o,q
                                 ctr+=1
                             if len(zz5+zz4+zz3+zz2+zz1+zz)==len(set(zz5+zz4+zz3+zz2+zz1+zz)) and len(zz5+zz4+zz3+zz2+zz1+zz)==10:
                               #print zz5,zz4,ff,l,j,k,l,m,n,o,q
                               ctr+=1
                           if len(zz4+zz3+zz2+zz1+zz)==len(set(zz4+zz3+zz2+zz1+zz)) and len(zz4+zz3+zz2+zz1+zz)==10:
                             #print zz4,zz3,ee,l,j,k,l,m,n,o,q
                             ctr+=1
                         if len(zz3+zz2+zz1+zz)==len(set(zz3+zz2+zz1+zz)) and len(zz3+zz2+zz1+zz)==10:
                           #print zz3,zz2,dd,l,j,k,l,m,n,o,q
                           ctr+=1 
                       if len(zz2+zz1+zz)==len(set(zz2+zz1+zz)) and len(zz2+zz1+zz)==10:
                         #print zz2,zz1,cc,l,j,k,l,m,n,o,q
                         ctr+=1	
                     if len(zz1+zz)==len(set(zz1+zz)) and len(zz1+zz)==10:
                       #print zz1,zz,bb,l,j,k,l,m,n,o,q
                       ctr+=1					
                   #print zz,zz1,zz2,zz3,zz4,zz5,zz6,zz7
print ctr

print time() - st


