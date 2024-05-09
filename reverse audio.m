[x,f]=audioread("/home/rguktrkvalley/c.wav");
[y,f1]=audioread("/home/rguktrkvalley/Sports.wav");
du=(length(x)/f)+(length(y)/f1);
t=linspace(0,du,length(x)+length(y));
k=x+y;
plot(t,k);