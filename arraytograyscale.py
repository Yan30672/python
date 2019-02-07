import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,0,255,0])
x.reshape(2,2)
plt.gray()
plt.imshow(x)
