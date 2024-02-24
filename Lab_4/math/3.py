import math

n = int(input("number of sides: "))
a = int(input("the length of a side: "))
print (f'Area is: {int(n/4 * a**2 / math.tan(math.pi / n))}')