#
#  Euler 162
#
from Functions import nCr



n1=1

for i in range(1,17):
  n1*=13

n2=16**15*15
print n1,n2,n2-n1

print len(str(n1)),len(str(n2-1))