# This is an adaptation to the solution for problem 67.
# Same algorithm, just different input format and minimizing
# instead of maximizing.
 
global rec 
rec = []

def find_min_sum(input):
	""" Read the rectangle in input file and find the MINIMUM
	sum from top to bottom only going down down or right.
	It uses a simple bottom-up dynamic programming algorithm:
	The MINIMUM sum at any sub-rectangle is the top-left element of the
	sub-rectangle added to the MINIMUM sum of the sub-rectangles below
	and right of it. """
 
	rec = []
 
	file = open(input, "r")
	for line in file:
		rec.append(map(lambda s: int(s), line.split(",")))
 
	h = len(rec)
	w = len(rec[0])	# asumed rectangular
 
	for i in xrange(h - 1, -1, -1):	# from the bottom up
 
		# from right to left, order matters here
		for j in xrange(w - 1, -1, -1):
 
			if j == (w - 1):
				if i == (h - 1):
					# bottom-right corner
					pass
				else:
					# right edge
					rec[i][j] = rec[i][j] + rec[i + 1][j]
			elif i == (h - 1):
				# bottom edge
				rec[i][j] = rec[i][j] + rec[i][j + 1]
			else:
				# other elements
				rec[i][j] = rec[i][j] + min(rec[i + 1][j], rec[i][j + 1])

	print
	print
	for i in xrange(80):
		for j in xrange(80):
			print rec[i][j],
		print
		print
	print
 
	return rec[0][0]	# the top-left of the rectangle, the MINIMUM sum
 
 
print "The largest sum going down the recangle is ", find_min_sum("matrix.txt")

