#
#
#
from decimal import Decimal
a = 3.86619826

x=a

for y in xrange(1,987654321+1):
   x *=a
   rm = x - int(x)
   x = x%10**10
   x += rm

print y,Decimal(x)