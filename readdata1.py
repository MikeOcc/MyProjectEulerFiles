import sys
import os
os.curdir = '/python'
f = open('read1.txt','r')
g = open('write1.txt','w')

#x=f.read()

#print f.readline()


i = 1
ctr=0
#for line in x:
#  print line
for i in range(0,1000000):
  
  x = f.readline()
  #z = x.count("0")
  #print z
  if x.count("0") <1:
    ctr+=1
    y = str(ctr) + ") 0" + x[-10:]
    g.write(y)

f.close()

g.close()

print "The number of #s is ",ctr

print "this is the end of the program"