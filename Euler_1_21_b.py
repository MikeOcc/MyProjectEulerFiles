def sOD(x):
	from math import sqrt
	s = 1
	for i in range(2, int(sqrt(x)) + 1):
		if (x % i == 0):
			s += i
			s += x / i
	return s


def findSum():
	
	sum = 0
	for i in range(1, 10000):
		x = sOD(i)
		if (sOD(x) == i):
			if (i != x):
				sum += i
	return sum

if __name__ == "__main__":
  print findSum()