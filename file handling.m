t=linspace(-2,2,2000);
u=linspace(-2,2,2000);
sq=[zeros(1,500),2*ones(1,1000),zeros(1,500)];
K=2;
N=[1,3,7,19,49,70];
for n=1:6;
 an=[];
 for m=1:N(n)
 an=[an,2*K*sin(m*pi/2)/(m*pi)];
 end;
 fN=K/2;
 for m=1:N(n)
 fN=fN+an(m)*cos(m*pi*t/2);
 end;
 nq=int2str(N(n));
 subplot(3,2,n);
 plot(u,sq,'r','LineWidth',2);
 hold on;
 plot(t,fN,'LineWidth',2);
 hold off;
 axis([-2 2 -0.5 2.5]);
 grid;
 xlabel('time');
 ylabel('y_N(t)');
 title(['N=',nq]);
end;
