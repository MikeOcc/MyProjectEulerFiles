#
#
# Euler Problem 284
#
#
from time import time
import string

digs = "0123456789abcdef"
digslist = map(None,digs)
digsval = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

def conv(n,b1,b2):

    # convert from the source base to the target base; work in decimal in between
    the_exp = 0
    dec_val = 0
    for idx1 in range(len(n)-1,-1,-1):
        dec_val += digslist.index(n[idx1]) * (b1**the_exp)
        the_exp += 1

    #print digslist
    #print

    # now convert from decimal to the target base

    target_list = []
    cur_val = dec_val
    done = False
    while cur_val > 0:
        the_rem = cur_val % b2
        target_list.append(digslist[the_rem])
        cur_val /= b2

    target_list.reverse()
    target_val = ''
    for the_char in target_list:
        target_val += the_char

    #return dec_val, target_val
    return target_val


def isSS(n):

  ns = n**2
  v1 = conv(str(n),10,14)
  v2 = conv(str(ns),10,14)
  l = len(v1)
  v2a = v2[-l:]
  if v1 == v2a:
    #print "hit", v1, v2, n%(2**l), n%(7**l)
    return v2
  else:
    return '0'

def SumDigs(numstr):
  summ = 0
  for v in numstr:
   summ += digsval[v]
  return summ


st = time()

seed1 = '7'
BigSum = 7 + 1
L= 0
for m in xrange(1,284):
  #print m, seed1
  found = False
  for n1 in xrange(1,100000):
    newpref = conv(str(n1),10,14)
    #print "newpref",newpref,newpref+seed1
    newseed = newpref+seed1
    newseed10 = conv(newseed,14,10)
    #print "newseed", newseed
    newseedtry = isSS(int(newseed10))
    if newseedtry != '0':
       L = len(newseed)
       V = SumDigs(newseed)
       BigSum += V
       #print m,n1,newseed, SumDigs(newseed)
       print m,n1,newseed,L,V
       seed1 = newseed
       found = True
       break
  if found == False:
    print "Ran out of Loops",m;exit()
  if L == 9: break

seed1 = '8'
BigSum += 8
for m in xrange(1,1000):
  #print m, seed1
  found = False
  for n1 in xrange(1,100000):
    newpref = conv(str(n1),10,14)
    #print "newpref",newpref,newpref+seed1
    newseed = newpref+seed1
    newseed10 = conv(newseed,14,10)
    #print "newseed", newseed
    newseedtry = isSS(int(newseed10))
    if newseedtry != '0':
       L = len(newseed)
       V = SumDigs(newseed)
       BigSum += V
       #print m,n1,newseed, SumDigs(newseed)
       print m,newseed,L,V
       seed1 = newseed
       found = True
       break
  if found == False:
    print "Ran out of Loops",m;exit()
  if L == 9: break


print "BigSum is", BigSum
print "BigSum in Base 14 is", conv(str(BigSum),10,14)
print "Process time is ", time()-st



