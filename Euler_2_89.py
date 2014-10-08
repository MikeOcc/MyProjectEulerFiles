#
#
#  Euler Problem 89
#
#
from string import rstrip

global RomanNumerals,RomanNumVals

RomanNumerals= {'I':1,'V':5, 'X':10, 'L':50,'C':100 ,'D':500 ,'M':1000}

RomanNumVals=  [1  , 5 , 10 ,  50 ,100, 500, 1000]



def CharSaved(N):

  lenN = len(N)
  l0 = lenN
  if "VIIII" in N:
     lenN-=3
  elif "IIII" in N:lenN-=2

  if "LXXXX" in N:
    lenN-=3
  elif "XXXX" in N:lenN-=2 

  if "DCCCC" in N:
    lenN-=3
  elif "CCCC" in N:lenN-=2 

  return l0 - lenN
  
def CalcVal(N):

  summ = 0
  lenN = len(N)
  for i in xrange(lenN-1):
    y = RomanNumerals[N[i]]
    z = RomanNumerals[N[i+1]]
    if y<z: y = -y
    summ+= y
  summ+= RomanNumerals[N[lenN-1]]
  return summ

##########################
from time import time
st=time()

#RomanNumVals=  [1  , 5 , 10 ,  50 ,100, 500, 1000]

f = open('roman.txt','r')

z=f.readlines()
totnumsaved=0
for x in z:

  #val1 = x.rstrip() 
  numsaved = CharSaved(x); totnumsaved+=numsaved
  #print val1, CalcVal(val1), numsaved


print "The total number of Roman Numerals saved is",totnumsaved
print "Process time is",time()-st




