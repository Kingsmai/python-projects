import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)
x = np.arccos(np.sin(theta)) * np.cos(theta)
y = np.arccos(np.sin(theta)) * np.sin(theta)

plt.plot(x, y, c='r')
plt.show()