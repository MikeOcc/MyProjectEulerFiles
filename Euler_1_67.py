#
#  find maximal sum in triangle.txt
#

from os import curdir
from string import whitespace,strip,replace
from operator import mul
from array import array
from math import *


curdir = "/python"

f = open('triangle.txt','r') # Number pasted to file.

i = 1
ctr=0
#y=zeros(2,int)     #array([100,100,0])

y = [ [0 for col in range(100) ] for row in range(100)]

#for line in x:
#  print line
sumy=0

for i in range(0,100):
  
  x= replace(strip(f.readline())," ",",")
  z = x.split(",")

#  print i,z
  maxy = 0

  for j in range(0,len(z)):

  #print 

    y[i][j]=int(z[j])

    if y[i][j]>maxy:

      maxy=y[i][j]


  print maxy

  sumy += maxy


print "!!!!! sum",sumy
      
 
  #z = x.count("0")
  #print z
  
  #print i, len(z), type(z), z

sum = 0
for i in range(0,99,2):
  zz=""
  vv=0
  wl=0
  vv=0
  wr=0
  vwm = 0
  uu=0
  maxvv=0
  prevvwm=0
  maxi,maxj,maxv = 0,0,0

  for j in range(0,99):
       
    vv = y[i][j]
    wl = y[i-1][j-1]
    wr = y[i+1][j+1]
    vwm=max(wl,wr)+vv
    if vwm>prevvwm:
       maxvv=vv
       prevvmn = vwm
       uu= max(wl,wr)
       maxj,maxv = j,vv
  print i, maxj,maxvv,uu,maxvv+uu
  
  sum += maxvv+uu
print "sum",sum
  

f.close()

