#Recursion
#Lab1.1 The Factorial Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#int(input("...")) รับค่าข้อมูลแบบตัวเลข integer
number = int(input("Enter factorial number: "))
print(factorial(number))
