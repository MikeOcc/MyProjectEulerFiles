def fact(n):
        return reduce(lambda x,y:x*y,range(1,n+1),1)
 
n = 5
r = (n-1)/2
p = [1]+[0]*r
for k in range(n+1):
  for i in range(r, 0, -1):
    p[i] += k*p[i-1]

print p
print "Answer to PE121 = ", fact(n+1) / sum(p)