#
# Begoner
#

wordArray =  eval('[' + open("words.txt").readlines()[ 0 ] + ']')   # eval( '[' + open("words.txt").readlines()[ 0 ] + ']' )

print wordArray

print type(wordArray)

triangleNums, sumOfWords =  [ i * ( i + 1 ) / 2 for i in xrange( 0, 30 ) ], 0
def getValue( word, total = 0 ):
        print word
        for i in word: 
          
          total += ord( i ) - 64
        return total
for i in wordArray:
        if ( getValue( i ) in triangleNums ): sumOfWords += 1 
print sumOfWords


#
# Or
#

wordArray,triangleNums, sumOfWords = eval( '[' + open("words.txt").readlines()[ 0 ] + ']' ), [ i * ( i + 1 ) / 2 for i in xrange( 0, 30 ) ], 0
len( [ i for i in [ reduce( lambda x, y: x + ord( y ) - 64, i, 0 ) for i in wordArray ] if i in triangleNums ] )
