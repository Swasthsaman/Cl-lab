import numpy as np
from matplot import pyplot as plt
t=nprange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()