#Lab1.12 Find  the Greatest Common Divisor (GCD) of two integers
def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)
print(Recurgcd(6,39))

