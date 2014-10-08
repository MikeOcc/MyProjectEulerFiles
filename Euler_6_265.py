#
#
#  Euler problem 265
#
#
from math import log10
from itertools import combinations,permutations
from time import time

def ib(n):

  '''
  val = 0
  n = n[::-1]
  for i in xrange(len(n)):
     if n[i]=="1":
        val += 2**i
  '''
  return int(n,2)

def bi(n,l=5):
  bitlist = []
  m = n
  while 1:
    if n == 0:
      return "0"*l
      #break
    elif m == 1:
      bitlist.append(1)
      break
    else:
      dig = int(log10(m)/log10(2))
      if dig >= 1:
        bitlist.append(dig+1)
      amt = 2**dig
      m -= amt
      if m == 0:
        break
  mx = max(bitlist)
  #if mx!=l:
  #  l=mx
  val = ["0"]*l
  for v in bitlist:
    val[l-v]= "1"
  val = "".join(val)
  return val 

def uniq(s):

  l=[]
  for i in xrange(32):
    if i< 28:
      p = s[i:i+5]
    else:
     p = s[i:i+5]+s[:(i-27)] 
    if p in l:
      #print "ooops",i,p
      return False
    else:
      l.append(p)
  return True


#################
 
chunks=[]

for i in xrange(1,16):
  a = bi(i,4)
  chunks.append(a)
  #print i, a

#chunks.append("0101")
#chunks.append("1001")

print chunks

a = combinations(chunks,7)
st=time()
summ = 0
ctr=0
slist=[]
slist2=[]
for b in a:
  #print b
  #c = ["0000"]
  #for d in b:
  #  c.append(d)
  #c.append("1111")
  f = permutations(b)
  for e in f:
    g ="0000"+ "".join(e) 
    #print g
    if g[0:5] != "00000":
      g = "0" + g[0:31]
    #print g
    if uniq(g):
      if g not in slist2:
        print "!!!!",g
        slist.append( ib(g))
        ctr+=1
        slist2.append(g)

print

#slist = list(set(slist))
print "summ is", sum(slist)
print "num of solns is",ctr
print "process time is", time()-st






