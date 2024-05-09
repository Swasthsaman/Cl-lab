import numpy as np
from matplotlib import pyplot as plt
t=np.arrange(0,1,0.01)
sin_dict={
    's1':[2,5],
    's2':[5,10],
    's3':[3,7],
    's4':[10,12],
    's5':[1,2],}
k=input('Enter sinusoidal key to generate')
if sin_dict:
            x=sin_dict[k][0]*np.sin(2*np.pi*sin_dict[k][1]*t)
plt.plot(t,x)
plt.show()

