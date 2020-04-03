from scipy import integrate


def f(x, a, b):
    return a * x + b


v, err = integrate.quad(f, 1, 2, args=(-1, 1))

print(v) # v is the result
print(err) # err is the absolute error
