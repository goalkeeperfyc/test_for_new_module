from scipy import integrate
import numpy as np
import math


def f(x, a, b):
    return a * x + b


v, err = integrate.quad(f, 1, 2, args=(-1, 1))

print(v)  # v is the result
print(err)  # err is the absolute error


def normal_distribution(x, mean, std):
    return 1 / (std * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mean) / std) ** 2)


v2, err2 = integrate.quad(normal_distribution, -np.inf, 0, args=(0, 1))

print(v2)

