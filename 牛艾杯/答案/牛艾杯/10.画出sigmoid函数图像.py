import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

x = np.arange(-5,5,0.01)
y = 1/(1+np.exp(-x))
plt.plot(x,y)
plt.show