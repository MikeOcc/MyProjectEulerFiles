from time import time
st=time()
import re

count = 0
for s in open('roman.txt','r'):
  #print s," ",
  l = len(s)
  s = re.sub('IIII','IV',s)
  s = re.sub('XXXX','XL',s)
  s = re.sub('CCCC','CD',s)
  s = re.sub('VIV','IX',s)
  s = re.sub('LXL','XC',s)
  s = re.sub('DCD','CM',s)
  count += l - len(s)
  #print s
print
print count,time()-st