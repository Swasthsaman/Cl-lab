N=128;
f1=150;
f2=300;
fs=8000;
n=0:N-1;
x1=sin(2*pi*(f1/fs)*n);
x2=cos(2*pi*(f2/fs)*n);
y1=x1;
y2=x2;
figure(1);
subplot(3,3,1);
plot(n,x1);
grid;
title('signal x1(t)');
subplot(3,3,2);
plot(n,y1);
grid;
title('signal y1(t)');
subplot(3,3,3);
plot(n,x2);
grid;
title('signal x2(t)');
subplot(3,3,4);
plot(n,y2);
grid;
title('signal y2(t)');
%signal delay
x1d=[zeros(1,20),x1(1:N-20)];
subplot(3,3,5);
plot(n,x1d);
grid;
title('delayed x1d(n),[x1(n-20)]');