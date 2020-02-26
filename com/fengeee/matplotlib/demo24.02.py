import math
import matplotlib.pyplot as plt
import numpy

X = numpy.linspace(0, 2 * numpy.pi, 100)
Y = numpy.cos(X)
plt.plot(X, Y)
Y = numpy.sin(X)
plt.plot(X, Y)
plt.show()
