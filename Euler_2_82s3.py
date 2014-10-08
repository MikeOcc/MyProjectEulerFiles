rows = [[int(n) for n in s.split(',')] for s in open('matrix82test.txt').readlines()]
nrows = len(rows)-1

tmp=[0]*len(rows)


for i in range(0,nrows+1) :
  tmp[i] = rows[i][nrows];  
  #print i,nrows,tmp[i]  

print tmp

for i in range(nrows -1,-1,-1):   #(int i = nrows - 2; i >= 0; i--) {
               
  # Traverse down
  tmp[0] += rows[0][i];

  for j in range(1, nrows) :
    tmp[j] = min(tmp[j-1] + rows[j][i], tmp[j] + rows[j][i]);

                
   #Traverse up
  for j in range(nrows-1,-1,-1):  #  (int j = nrows - 2; j >= 0; j--) {
    tmp[j] = min(tmp[j], tmp[j+1] + rows[j][i]);  
  
  
# #start counting from end of col 
# for i in range(nrows, -1, -1):
  # for j in range(nrows, -1, -1):
  
        # if (i==nrows and j==nrows): continue    #these 4 lines check for out-of-bounds conditions

        # # if last column only check next row
        # if (j==nrows): 
          # minx = min(rows[i+1][j],rows[i-1][j])
          # print i,j,rows[i+1][j], minx

        # # if last row only check val of column to right
        # elif (i==nrows): 
          # minx = min(rows[i][j+1] ,rows[i-1][j]   )
          # print i,j,rows[i][j+1],rows[i-1][j], minx

        # # min value for right and for down
        # else:
          # minx = min(rows[i+1][j], rows[i][j+1], rows[i][j-1])
          # print i,j,rows[i+1][j], rows[i][j+1], rows[i][j-1],minx
        # rows[i][j] += minx
 
print "Answer to PE82 = ", min(tmp)
print
# for i in range(nrows+1):
  # for j in range(nrows+1):
    # print rows[i][j],
  # print