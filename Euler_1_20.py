#
# Find the sum of the digits in the number 100!
#

start = 100

sum = 1

i = 1

for i in range(1,101):
  sum = sum * i 
  

print "10! is ",sum

sumstr = str(sum)
print sumstr

sum2 = 0

len1 = len(sumstr)

for i in range (0,len1):
  sum2 = sum2 + int(sumstr[i])
  print i,int(sumstr[i]), sum2


print "Sum is ",  sum2