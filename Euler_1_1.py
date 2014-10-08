
from math import *

sum = 0
temp = 0
temp2 = 0
diff = 0
diff2 = 0
sum2 = 0
diff3 = 0
temp3 = 0
ctr = 0

for i in range(1,1000):
     #print i
     if (i%3==0 or i%5==0):
     #if (i%3==0):
        #ctr = ctr + 1
        sum = sum + i
        diff = sum - temp
        diff2 = diff - temp2
        diff3 = diff3 + diff2 
        temp3 = diff2
        if ((ctr)%3 == 0): diff3 = diff2
        ctr = ctr + 1
        temp2 = diff
        temp = sum
        sum2 = sum2 + diff2
       
 
        if ((ctr)%3 == 0):
           print i, sum, diff, diff2, diff3    
        else:
           print i, sum, diff, diff2
           #xyzygy = 0
     else:
       print i, sum, diff, diff2
       #xyzygy = 0
print "The sum is ", sum

#  5, 3, 4, 4, 3, 5, 3, 6
#  6, 6, 8, 5, 8, 6, 6
#  3-2-1, 3-1-2, 3-3-2, 1-3-1, 2-3-3, 2-1-3, 1-2-3