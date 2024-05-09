import numpy as np
import matplotlib.pyplot as plt
t = np.arange(1, 10)
x = np.sin(2 * np.pi * t)
y = np.cos(2 * np.pi * t)
fig, axs = plt.subplots(1, 2)
axs[0].plot(t, x)
axs[0].set_title('Sine Wave')
axs[1].plot(t, y)
axs[1].set_title('Cosine Wave')
plt.tight_layout()
plt.show()

