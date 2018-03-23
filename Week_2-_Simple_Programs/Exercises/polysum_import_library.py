# import math library for tan and pi function only
from math import tan, pi


def polysum(n, s):
    perimeter = n*s # perimeter is the number of sides times length
    area = (.25*n*s**2)/(tan(pi/n)) # call tan function without having to write math.tan

    sum_of_polygon = round(perimeter**2 + area, 4) # use the round function to round to 4 decimal places

    return sum_of_polygon

print(polysum(79, 64))