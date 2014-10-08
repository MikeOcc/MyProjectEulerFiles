# First load the file and sort it.
import os
import sys
sys.path.append('/python')
os.curdir='/python'

x = eval( '[' + open( 'names.txt' ).readlines()[ 0 ] + ']' )
x.sort()
 
# Then calculate what is needed.
 
print reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )

u=sum ([ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ])
print "sum =",u



# junk u=sum ([ sum[ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ])

print "sum =",u