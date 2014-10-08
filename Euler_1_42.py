#
#  Euler problem 42
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are
# triangle words?
#

from os import curdir
from string import split, replace
#from operator import mul
#from array import array
from math import sqrt
from time import time

st = time()

curdir = "/python"


f = open('words.txt','r') # Number pasted to file.

y = replace(f.read(),'"','')

#print type(y)

z = split(y,",")

#print type(z)

zlen = len(z)

#print type(z[10])

totsum = 0

for i in range(0,zlen):  #for line in f:

  nword = list(z[i])
  sumTri = sum( ord(x)-64 for x in nword)
  #  now check to see if # is triangle

  trinum = round((-1. + sqrt(1. + 8.*sumTri))/2.,3)
  if trinum == int(trinum):
    # triangle number, thus triangle word found
    totsum +=1
    print totsum,")", z[i], "T(",int(trinum),") =",sumTri

f.close()

print "Total number of Triangle Words is", totsum

print "Process time is", time() - st