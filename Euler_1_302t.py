

stopit =  10**18

#  38775788043632640000
# 229442532802560000

n=1

plist = []
nlist = []
maxn = 2
sum1 = 1

while sum1 <= stopit:
  #print "____________"

  if sum1 >= stopit: break
  sum1 = 1

  n += 1
  nlist.append(n) 

  for i in range(2,n+1):
    sum1 *= i**2
   # print "!!!",i,i**2,sum1
  
  print "nth sum1", n, sum1
  plist.append(sum1)


print plist
print nlist
print sum1, n

