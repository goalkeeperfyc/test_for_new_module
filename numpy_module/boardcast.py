import numpy as np

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))

print("x shape is " + str(x.shape))
print("y shape is " + str(y.shape))

try:
    x + y
except ValueError as error_mess:
    print("ValueError: " + str(error_mess))

print("xx shape is " + str(xx.shape))
print("y shape is " + str(y.shape))

print("xx+y shape is " + str((xx+y).shape))
print(xx + y)

print("x shape is " + str(x.shape))
print("z shape is " + str(z.shape))
print("x+z shape is " +str((x+z).shape))

print(x + z)

"""
Broadcasting provides a convenient way of taking the outer product 
(or any other outer operation) of two arrays. 
The following example shows an outer addition operation of two 1-d arrays:
"""

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
a_plus_b = a[:, np.newaxis] + b
print(a_plus_b)
print("the shape of a+b is " + str((a_plus_b).shape))
print("a shape is " + str(a.shape))
print("b shape is " + str(b.shape))
print(a[:, np.newaxis])
print("the shape of a[:, np.newaxis] is " + str(a[:, np.newaxis].shape))
"""
Here the newaxis index operator inserts a new axis into a, 
making it a two-dimensional 4x1 array. 
Combining the 4x1 array with b, which has shape (3,), yields a 4x3 array.
"""