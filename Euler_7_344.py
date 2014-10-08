#
#
#
#
#

from itertools import combinations

def fibo(n):
  #if n ==0:return 0
  if n ==1:return 2
  if n ==2:return 3
  return fibo(n-2) + fibo(n-1)

coins = [0]*10

coins[1]=1
coins[4]=1
coins[6]=1
coins[7]=2
coins[9]=1
#print coins
coins = [0]*10
x = combinations(range(0,9),2)
  
for y in x:
    coins[y[0]] = 1
    coins[y[1]] = 1
    cf = False
    while cf == False:
      Z = combinations(range(9),1)
      
      if coins[Z] == 0:
        coins[Z]=1
        break
      X = reduce(lambda x,y: x^y, coins)
    print X

