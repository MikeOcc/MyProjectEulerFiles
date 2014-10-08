#
#  Euler Problem 76
#

target = 100
ns = range(1,target+1)
ways = [1]+[0]*target
 
for n in ns:
  for i in range(n, target+1):
    ways[i] += ways[i-n]
    print n,i, ways[i-n],ways[i]
 
print "Answer to PE76 = ", ways[target]
