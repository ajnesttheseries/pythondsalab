#Lab1.8 Sum of the Positive Integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

print(sum_series(9))
print(sum_series(16))
