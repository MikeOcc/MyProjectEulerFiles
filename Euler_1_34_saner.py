def findFact(limit):
	facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	#limit = 362880 * 9
	for i in xrange(0, limit):
		total = 0
		stringI = str(i)
		for j in stringI:
			total += facts[int(j)]
		if (total == i):
			print i


if __name__ == "__main__":
  from time import time
  st = time()
  findFact(500000)
  print "Time to process is:",time()-st