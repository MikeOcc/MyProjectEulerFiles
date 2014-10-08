#
#  Euler Problem 99
#
#
from math import log
f = open('base_exp.txt')

x=f.readlines()

answer = 0
maxb=0;maxe=0
linenum=0
ctr=0
for y in x:
  ctr+=1
  z = y.strip('\r\n').split(",")
  #print z
  b = int(z[0]);e=int(z[1])
  print b,e
  num = log(b)*e
  if num>answer:
    answer=num
    maxb=b;maxe=e;linenum=ctr

print "the larget number is e^",answer,linenum,b,e
