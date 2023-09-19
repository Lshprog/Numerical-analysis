import math
import numpy

epsilon = 1e-4


def phi_of_x(x):
    return pow(2 - pow(math.e, -x), 1 / 2)

def der_phi_of_x(x):
    return pow(math.e, -x) / (2 * pow(2 - pow(math.e, -x), 1 / 2))


def сonvergence_test(init_point, delta, q):
    left_part = abs(phi_of_x(init_point) - init_point)
    right_part = (1 - q) * delta

    if left_part <= right_part:
        return True
    else:
        return False

def find_number_of_iterations(init_point, q):
    upp = abs(phi_of_x(init_point) - init_point)
    btp = (1 - q) * epsilon
    logup = math.log(upp/btp, math.e)
    logbt = math.log(1/q, math.e)
    return int(logup/logbt) + 1


def aitken(arr, n):
    left_part = pow(arr[n] - arr[n-1],2)/abs(2 * arr[n-1] - arr[n] - arr[n-2])
    if left_part < epsilon:
        return True
    return False

def treshold_check(arr, n):
    left_part = abs(arr[n] - arr[n-1])
    right_part = (1-q)*epsilon/q
    if left_part <= right_part:
        return True
    return False

def find_function_root(init_point, delta, q):
    x = init_point
    iterarr = []
    if сonvergence_test(init_point, delta, q):
        number_of_iterations =  find_number_of_iterations(init_point, q)
        for iteration in range(number_of_iterations):
            print(iteration, "  <-  iteration")
            x = phi_of_x(x)
            iterarr.append(x)
            if iteration > 1:
                if aitken(iterarr, iteration) or treshold_check(iterarr, iteration):
                    return x

    return x


init_point = 1.5
delta = 0.5
q = der_phi_of_x(1)

print(сonvergence_test(init_point, delta, q))
print(q)

print("{:.10f}".format(find_function_root(init_point, delta, q)))
