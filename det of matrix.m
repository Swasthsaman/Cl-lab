%x = linspace(0, 2*pi, 100);
%y = sin(x);
%plot(x, y);
%figure;
x=linspace(0,2*pi,100000000000000);
a=cos(2*x);
b=sin(2*x);
c=2*sin(x);
plot(x,a+b+c);