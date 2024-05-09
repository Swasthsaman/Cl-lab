import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
t=np.arange(1,10)
x=np.sin(2*np.pi*t)
y=np.cos(2*np.pi*t)
plt.subplot(1,2,1)
plt.plot(x)
plt.subplot(1,2,2)
plt.plot(y)
