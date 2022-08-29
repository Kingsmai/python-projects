import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi / 2, np.pi / 2, 1000)
y1 = np.power(np.cos(x), 0.5) * np.cos(200 * x) + np.power(np.absolute(x), 0.5) -0.7
y2 = np.power(4 - np.power(x, 2), 0.01)

plt.plot(x, y1 * y2, c='r')
plt.show()