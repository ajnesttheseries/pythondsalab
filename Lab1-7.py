#Lab1.7 Sum of a Non-Negative Integer
def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

print(sumDigits(678))
print(sumDigits(79))

