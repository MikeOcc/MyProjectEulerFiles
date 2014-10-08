###
#  
# Project Euler Problem 28: Find the sum of both diagonals in a 1001 by 1001 spiral
#
###

n = 500  # nth ring number, 0th Ring is sole digit 1
# S = 2*n+1 =>Spiral number  (n=2 => 3 x 3 Spiral, n=3 => 5 x 5, etc.)

sum = 1  # (0th Ring number is counted once though in both diagonals)
prev = 1

for i in range(1,n+1):   # Count thru 500 rings
    S = 2 * i + 1      # Get spiral #
    trsn = S**2        # Number of top right Spiral (ie. nth Ring)
                       # p = 4 * (S - 1) => Count of #'s in nth ring perimeter (2 * S) + 2 * (S -2)
    brsn = trsn - 3 * (S-1)  # Bottom right Spiral #, 3/4 of p
    sdnr = (trsn +brsn) * 2  # sum of corner #'s in nth ring. (3+5+7+9==2*(9+3)
    print i,")","sdnr", sdnr, prev, sdnr - prev
    prev = sdnr
    sum += sdnr        # total corner #s of all the rings  

print "Sum of both diagonals in a",S,"by",S," Spiral = ", sum
