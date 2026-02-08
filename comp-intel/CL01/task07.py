# (1) Import the numpy and matplotlib.pyplot module.
import numpy as np
import matplotlib.pyplot as plt

# (2) Use them to plot the sine curve between 0 and 20 (in 0.1 steps).
x = np.arange(0, 20, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Curve (0 to 20)")
plt.show()