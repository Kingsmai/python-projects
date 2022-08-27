import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2, 300)
x2 = np.linspace(0, -2, 300)

y11 = (np.power(x1, 2 / 3) + np.power(np.power(x1, 4 / 3) - 4 * np.power(x1, 2) + 4, 0.5)) / 2 - 0.12
y12 = (np.power(x1, 2 / 3) - np.power(np.power(x1, 4 / 3) - 4 * np.power(x1, 2) + 4, 0.5)) / 2
y21 = (np.power(-x2, 2 / 3) + np.power(np.power(-x2, 4 / 3) - 4 * np.power(-x2, 2) + 4, 0.5)) / 2 - 0.12
y22 = (np.power(-x2, 2 / 3) - np.power(np.power(-x2, 4 / 3) - 4 * np.power(-x2, 2) + 4, 0.5)) / 2

plt.plot(x1, y11, c='r')
plt.plot(x1, y12, c='r')
plt.plot(x2, y21, c='r')
plt.plot(x2, y22, c='r')
plt.show()