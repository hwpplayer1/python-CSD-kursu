points = [(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)]

x, y = zip(*points)

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
