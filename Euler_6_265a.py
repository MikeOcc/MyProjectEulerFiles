#
#
#  Euler problem 265
#
#
from math import log10
from itertools import combinations,permutations
from time import time

def ib2(n):
 
  return int(n,2)

def ib(n):
  val = 0
  n = n[::-1]
  for i in xrange(len(n)):
     if n[i]=="1":
        val += 2**i

  return val

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

st = time()

#x = ib("00000110010011101101010001011111")

#print x
#exit()

chunks=[]

for i in xrange(1,16):
  a = bi(i,4)
  chunks.append(a)
  #print i, a

#chunks.append("0101")
#chunks.append("1001")

print chunks

#a = combinations(chunks,7)

#a=permutations([000000000111111111111111])

summ = 0
#sum2 = 0
slist=[]
ctr = 0
u = ib2("0001000100000000000000000")
v = ib2("1111111111111100000000000")

for e in xrange(u,v):
 
    g ="000001"+ bi(e,25) + "1" 
    #print g
    if uniq(g):
      print "!!!!",g
      slist.append( ib(g))
      #sum2 += (ib(g))
      ctr+=1

print

#slist = list(set(slist))
print "summ is", sum(slist)
print "number of solutions is",ctr
print "process time is",time()-st







