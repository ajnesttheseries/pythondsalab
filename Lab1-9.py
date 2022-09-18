#Lab1.9 Harmonic Sum of n-1
def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(9))
print(harmonic_sum(6))
