#
#  Problem 6 Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
#


if __name__ == '__main__':

  maxpal = 0; maxi = 0; maxj = 0
  sumsq = 0
  sqsum = 0
  diff = 0

  for i in range(1,101, 1):
    sumsq = sumsq + i * i
    sqsum = sqsum + i

  sqsum*=sqsum

  diff = sqsum - sumsq

  print "The sum of the Squares is ", sumsq
  print "The square of the Sums is ", sqsum
  print "The difference is ", diff