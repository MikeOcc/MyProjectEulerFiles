
sum1 = 0

for i in range(1,1001):sum1 = sum1 + i**i


print "result = ", str(sum1)[-10:]



#  or

print

print str(sum((i**i)%10**10 for i in range(1,1001)))[-10:]

print

print str(sum(((i%10**10)**i%(10**10)) for i in range(1,1001)))[-10:]

print