import math
import numpy

epsilon = 1e-4

def functionate(x):
    return pow(math.e,-x) + pow(x,2) - 2

def find_boundary_next(x,val):
    if numpy.sign(functionate(x)) == numpy.sign(functionate(val)):
        return x
    else:
        return val

def find_x_next(a,b):
    return (a + b)/2


def find_function_root(a, b):
    if functionate(a) * functionate(b) >= 0:
        print("No value in this segment!")
        return

    iter_n = int(math.log((b-a)/epsilon,2))
    print("Number of iterations: " ,iter_n)
    temp_a = a
    temp_b = b

    for i in range(iter_n + 1):
        new_x = find_x_next(temp_a,temp_b)
        print("x on iter ", i, "  ->   ", new_x, " and the f(x)  ->  ",functionate(new_x))
        temp_a = find_boundary_next(new_x, temp_a)
        temp_b = find_boundary_next(new_x, temp_b)


find_function_root(1, 2)