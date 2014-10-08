rows = [[int(n) for n in s.split(',')] for s in open('matrix82test.txt').readlines()]
nrows = len(rows)-1


#start counting from end of col 
for i in range(nrows, -1, -1):
  for j in range(nrows, -1, -1):
  
        if (i==nrows and j==nrows): continue    #these 4 lines check for out-of-bounds conditions

        # if last column only check next row
        if (j==nrows): minx = rows[i+1][j]

        # if last row only check val of column to right
        elif (i==nrows): minx = rows[i][j+1]

        # min value for right and for down
        else: minx = min(rows[i+1][j], rows[i][j+1])

        rows[i][j] += minx
 
print "Answer to PE81 = ", rows[0][0]
print
 
print "Answer to PE81 = ", rows[0][0]
print
for i in range(nrows+1):
  for j in range(nrows+1):
    print rows[i][j],
  print