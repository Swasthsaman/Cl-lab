from matplotlib import pyplot as pt
import numpy as np
t=np.arange(0,1,0.01)
#f=2
#pt.plot(t,x)
dict={"c1":[2,5],"c2":(3,4),"c3":(7,8)}
print(dict)
#print(dict["Sin1"[0]])
print("Choose any Sinusoid to print")
pl=input("Enter: ")
if(dict[pl]):
	x=dict[pl][1]*np.cos(2*np.pi*dict[pl][0]*t)
	pt.plot(t,x)
	pt.xlabel("Time")
	pt.ylabel("Amplitude")
	pt.title("Cos Wave")
	pt.show()
else:
 	print("Enter the name os the key only.")
	
