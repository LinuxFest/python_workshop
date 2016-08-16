"""NumPy Arrays"""
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

b = [1, 2, 3, 4]
print(b)

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.float64)
print(c, c.shape, c.size)

# 'd' is short type for float64
zeros = np.zeros((3, 3), 'd')
print(zeros)

normal = np.random.standard_normal((2, 4))
print(normal)

a = np.random.standard_normal((2, 3))
b = np.random.standard_normal((2, 3))
print(np.vstack([a, b]))
print(np.hstack([a, b]))

np.save('save.npy', a)
a_loaded = np.load('save.npy')
print(a_loaded)
