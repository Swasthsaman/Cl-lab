[x,f]=audioread("/home/rguktrkvalley/OSR_us_000_0010_8k.wav");
audiowrite('f2.wav',x,2*f);
disp(sizeof(x))
display(f);