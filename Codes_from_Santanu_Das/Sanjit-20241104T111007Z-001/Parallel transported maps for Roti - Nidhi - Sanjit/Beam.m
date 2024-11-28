clc
clear all
close all
for i = 1:300
    for j = 1:300
        thx = (i-150)*(3.0/300)*(pi/180);
        thy = (j-150)*(3.0/300)*(pi/180);
        V(i,j) = exp(-0.5*(thx/0.002347048167)^2 -0.5*(thy/0.002083988462)^2);
        W(i,j) = exp(-0.5*(thx/0.00175215334)^2 -0.5*(thy/0.00160587506)^2);        
    end
end

fp = fopen('W1.txt','w');
fp1 = fopen('V1.txt','w');
for i = 1:300
    for j = 1:300
        fprintf(fp1,'%e  ',V(j,i));
        fprintf(fp,'%e  ',W(j,i));        
    end
end
fclose(fp);
fclose(fp1);

load -ascii WBlm.d
WS = WBlm(:,3);
l = WBlm(:,1);
WS = WBlm(:,3);

ll = 1:1000;
WCN = spline(l,WC,ll);
WSN = spline(l,WS,ll);



