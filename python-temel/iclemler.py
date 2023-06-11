x = list(range(-10, 11, 1))
y = [i * i for i in x]

print(x)
print(y)

import matplotlib.pyplot as plt

plt.plot(x,y)
