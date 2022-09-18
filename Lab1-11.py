#Lab1.11 Exponent value of 'a' to the power 'b'
def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

print(power(9,3))
