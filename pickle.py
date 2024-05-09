import numpy as np
from matplotlib import pyplot as plt
import pickle
f=open('file.pkl','wb')
f1=5 
t=np.arange(0,0.01,1)
x=np.sin(2*np.pi*f1*t)
pickle.dump(x,f)
f.close()
f=open('file.pkl','rb')
a=pickle.load(f)
b=pickle.load(f)
print(a,b)
f.close()
f=open('file.pkl','rb')
