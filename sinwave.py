import numpy as np
f=open("/home/rguktrkvalley/empt.txt",mode="w+")
t=np.arange(0,1,0.01)
x=np.sin(2*np.pi*12*t)
d=f.write(str(x))
print(d)

