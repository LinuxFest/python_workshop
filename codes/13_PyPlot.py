import numpy as np
import matplotlib.pyplot as pp

x = np.linspace(0, 10, 40)
print(x)
sinx = np.sin(x)
cosx = np.cos(x)

pp.plot(x, sinx)
pp.show()

pp.plot(x, sinx, 'x')
pp.plot(x, cosx, 'o')
pp.show()

y = sinx * cosx
z = cosx ** 2 - sinx ** 2
pp.plot(x, y)
pp.plot(x, z)
pp.legend(['sin(x) cos(x)', 'cos(x)^2 - sin(x)^2'])
pp.show()

print(np.dot(sinx, cosx))

print(np.outer(sinx, cosx))
