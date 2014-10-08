#
#
# Euler 350
#
#

from Functions import RetFact

'''
def gcd(a,b):
  if b==0:
     return a
  else:
     return gcd(b, a%b)
'''

def gcd(a,b):
  if b==0:
     return a
  else:
     return gcd(b, a%b)


print gcd(6,4)


def lcm(lst):
  s = set()
  for l in lst:
    F = RetFact(l)
    for f in F:
      s.add(f)
  lcm=1
  print s
  for i in s:
    lcm *=i
  return lcm 

print lcm([2,6,4])

exit()


G=10
L=100

x=range(1,101)
ctr = 0
for i in x:
  for j in x:
    if j>=i and gcd(i,j)>G:
     ctr+=1

print ctr





