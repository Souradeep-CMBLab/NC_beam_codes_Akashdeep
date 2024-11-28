clear all

%% K1 
%load -ascii wmap_hybrid_beam_maps_K1_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_K1_7yr_v4_t0;

%% Ka1
%load -ascii wmap_hybrid_beam_maps_Ka1_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_Ka1_7yr_v4_t0;

%% Q1
%load -ascii wmap_hybrid_beam_maps_Q1_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_Q1_7yr_v4_t0;

%% Q2
%load -ascii wmap_hybrid_beam_maps_Q2_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_Q2_7yr_v4_t0;

%% V2
%load -ascii wmap_hybrid_beam_maps_V2_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_V2_7yr_v4_t0;

%% W1
%load -ascii wmap_hybrid_beam_maps_W1_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_W1_7yr_v4_t0;

%% W2
%load -ascii wmap_hybrid_beam_maps_W2_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_W2_7yr_v4_t0;

%% W3
%load -ascii wmap_hybrid_beam_maps_W3_7yr_v4_t0.txt
%B = wmap_hybrid_beam_maps_W3_7yr_v4_t0;

%% W4
load -ascii wmap_hybrid_beam_maps_W4_7yr_v4_t0.txt
B = wmap_hybrid_beam_maps_W4_7yr_v4_t0;

%%
M = max(max(B));
[c r]= find(B==M);
brc1 = 0;
brc2 = 0;
brc3 = 0;
brs1 = 0;
brs2 = 0;
brs3 = 0;
br1 = 0;
br0 = 0;
alp = 0;%-1.22173048;
for i=1:600
    for j=1:600
        x = j-r;
        y = i-c;
        if(x==0 && y==0)
            continue;
        end
        theta = sqrt(x*x+y*y);
        cosphi = x/theta;        
        sinphi = y/theta;
        theta = theta*(12/600)*(pi/180);   

%        brc = brc + sin(theta)*cosphi*B(i,j)*cos(alp) + sin(theta)*sinphi*B(i,j)*sin(alp);
%        brs = brs - sin(theta)*cosphi*B(i,j)*sin(alp) + sin(theta)*sinphi*B(i,j)*cos(alp);
%        br0 = br0 + cos(theta)*B(i,j);

        brs1 = brs1 + cos(2*theta)*sinphi*sinphi*B(i,j);
        brs2 = brs2 + cos(theta)*sinphi*cosphi*B(i,j);
        brs3 = brs3 + (3*cosphi*cosphi-1)*B(i,j);   

        brc1 = brc1 + sin(2*theta)*sinphi*sinphi*B(i,j);
        brc2 = brc2 + sin(theta)*sinphi*cosphi*B(i,j);        

        br1 = br1 + B(i,j);
    end
end

surf(B,'FaceColor','red','EdgeColor','none')
camlight left; lighting phong

fprintf('b^{2}_{-2} = %f + %fi \n',(1/4)*sqrt(15/2/pi)*brs1/br1,(1/4)*sqrt(15/2/pi)*brc1/br1)
fprintf('b^{2}_{-1} = %f + %fi \n',(1/2)*sqrt(15/2/pi)*brs2/br1,(1/2)*sqrt(15/2/pi)*brc2/br1)
fprintf('b^{2}_{0} = %f \n',(1/4)*sqrt(5/pi)*brs3/br1)
fprintf('b^{2}_{1} = %f + %fi \n',-(1/2)*sqrt(15/2/pi)*brs2/br1,(1/2)*sqrt(15/2/pi)*brc2/br1)
fprintf('b^{2}_{2} = %f - %fi \n',(1/4)*sqrt(15/2/pi)*brs1/br1,(1/4)*sqrt(15/2/pi)*brc1/br1)