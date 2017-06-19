import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

step = 0.01

def normal_distribution(x, u, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * cmath.exp(-(x-u)**2 / (2 * sigma**2))

x_range_min = -5
x_range_max = 5

#Plot x axis
x_axis = [m * 0.01 for m in range(x_range_min * 100, x_range_max * 100)]

#Generate input sequence
u = 0
sigma = 0.2
n1 = [normal_distribution(m * 0.01, u, sigma) for m in range(x_range_min * 100, x_range_max * 100)]

u = -2
sigma = 0.5
n2 = [normal_distribution(m * 0.01, u, sigma) for m in range(x_range_min * 100, x_range_max * 100)]

u = 0
sigma = 1.0
n3 = [normal_distribution(m * 0.01, u, sigma) for m in range(x_range_min * 100, x_range_max * 100)]

u = 0
sigma = 5.0
n4 = [normal_distribution(m * 0.01, u, sigma) for m in range(x_range_min * 100, x_range_max * 100)]

#Plot
plt.figure()
plt.plot(x_axis, n1)
plt.plot(x_axis, n2)
plt.plot(x_axis, n3)
plt.plot(x_axis, n4)
plt.show()
