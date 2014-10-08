
#rows = [[int(n) for n in s.split(',')] for s in open('matrix82.txt').readlines()]

rows = [[int(n) for n in s.split(',')] for s in open('matrix82test.txt').readlines()]

nrows = len(rows)
 
for i in range(nrows):   #row
  for j in range(nrows):     #col
    if (i==nrows and j==nrows): continue    #these 4 lines check for out-of-bounds conditions

    if i==0:
      if j != nrows-1:
        print i,j
        minx=min(rows[i][j+1],rows[i+1][j] )
      else:
        minx=rows[i+1][j]
    elif i==nrows-1:
      print "&", i,j
      if j != nrows-1:
	    minx=min(rows[i][j+1],rows[i-1][j] )
      else:
        minx=rows[i-1][j]      	

    else:
      print i,j
      if j != nrows-1:
        minx = min(rows[i+1][j],rows[i-1][j], rows[i][j+1] )
      else:
        minx = min(rows[i+1][j],rows[i-1][j])
    rows[i][j] += minx
 
print "Sum of PE82 = ", rows[nrows-1][nrows-1]