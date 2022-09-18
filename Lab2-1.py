#Dynamic Arrays and Amortization
import sys                      #provides getsizeof function
data = []
number = int(input("Enter number: "))   
for k in range(number):         #NOTE: must fix choice of n
    a = len(data)               #number of elements
    b = sys.getsizeof(data)     #actual size in bytes
    print('Length: {0:9d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)           #increse length by one




#Explaination of this Fancier Output Formatting code of python
"""
0: | 1: | 2:  => The position in the arg list from which to get 
                 the value.  The order can be anything you want, and
                 you can repeat values, e.g. '{2:...} {0:...} {1:...} {0:...}' 

2 | 3 | 4     => The minimum width of the field in which to display 
                 the value.  Right justified by default for numbers.


d             => The value must be an integer and it will displayed in 
                 base 10 format (v. hex, octal, or binary format)
"""
"""
x = 1
y = 2
z = 3
print('\n{0:2d} {1:3d} {2:4d}'.format(x,y,z))
print('{2:2d} {1:3d} {0:4d}'.format(x,y,z))
print('{2:2d} {1:3d} {0:4d}'.format(x,y,z))
print('{2:2d} {1:3d} {0:4d}'.format(x,y,z))
print('{2:5d} {1:5d} {0:5d}'.format(x,y,z))
print('{2:2d}\n {0:3d}\n {1:4d}'.format(x,y,z))
print('{2:10d} {1:10d} {0:10d}'.format(x,y,z))
print('{2:1f} {1:10f} {0:10d}'.format(x,y,z))
print('{2:1d} {1:10d} {0:10f}'.format(x,y,z))
"""
