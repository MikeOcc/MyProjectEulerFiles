def sum_s(x):

  return x*(2*x+1)*(x+1)//6

SUM = 0
END = 10**15
i = 1
while i <= END:
  mult = END//i
  next_i = END//mult+1
  SUM += mult * (sum_s(next_i-1) - sum_s(i-1))
  i = next_i
  SUM %= 10**9

print(SUM%10**9)