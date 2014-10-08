from math import factorial
import sys
import math


def problem171():
	facts =[factorial(x) for x in range(21)]
	def permuteAdd(curr, nums):
		nums= [0] * (20-len(nums)) + nums
		size = len(nums)
		count = 0
		run = 0
		results = []
		for i in range(size):
			if run == nums[i]:
				count += 1
			else:
				if count > 0:
					results.append((run,count))
				count = 1
				run = nums[i]
		if count > 0:
			results.append((run,count))
		perms = reduce(lambda x,y: x/facts[y[1]],results,facts[size])
		digitsum = sum([perms*y[0]*y[1] for y in results])/size
		num = (int("1"*size)*digitsum + curr) % 1000000000
		return int(num)
	seed = []
	for i in range(9*9*20+1):
		seed.append([])
	seed[0].append([])
	for i in range(1,10):
		sys.stdout.write(str(i))
		sys.stdout.flush()
		for j in range(i*i,len(seed)):
			for s in seed[j-i*i]:
				if len(s) < 20:
					seed[j].append(s[:]+[i])

	seed = [seed[i*i] for i in range(int(math.sqrt(len(seed)-1))+1)]
	digitsum = 0
	for s in seed:
		for nums in s:
			digitsum = permuteAdd(digitsum, nums)
	print "#171",digitsum
			
problem171()