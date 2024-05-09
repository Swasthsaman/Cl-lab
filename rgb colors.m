inputImage='input image.jpg';
imageData=imread('1.jpg');
redVector=imageData(:,:,1);
greenVector=imageData(:,:,2);
blueVector=imageData(:,:,3);
csvwrite('red_component.csv', redVector(:));
csvwrite('green_component.csv',greenVector(:));
csvwrite('blue_component.csv', blueVector(:));
disp('Red,green,blue components saved successfully as csv files.');
