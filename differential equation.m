t=-10:0.1:10;
y1=sin(t);
y2=cos(t);
subplot(121),plot(t,y1),title('sinewave');grid on
subplot(122),plot(t,y2),title('coswave');grid on
%--------------------linearity property---------------%
y3=2*y1;
y4=3*y2;
y5=y3+y4;
y6=t.*y5;
y7=t.*y3;
y8=t.*y4;
y9=y7+y8;
e=(y6)-(y9);
figure,subplot(2,2,1),plot(t,y6),title('T[a1*x1(t)+a2*x2(t)]');grid on
subplot(2,2,2),plot(t,y9),title('a1*T[x1(t)]+a2*T[x2(t)]');grid on
%--------------------time invariant property---------------%
Y2=sin(t-2);
Y3=t.*Y2;
Y4=(t-2).*sin(t-2);
figure,plot(t,Y3,'b--'),title('time invariant');grid on ,text(10*10^5,20,'level2')
hold; plot(t,Y4,'r--'),legend('T[x(t-2)]','y(t-2)',-1)
