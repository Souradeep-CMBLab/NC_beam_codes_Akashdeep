#include <math.h>
#include<stdio.h>
#define PI 3.14159265
#define ANGMAX 12.0
#define MAX 600

double plgndr(int l, int m, double x)
//Computes the associated Legendre polynomial Pml(x). Here m and l are integers satisfying 0 <= m <= l, while x lies in the range -1 <= x <= 1.
{
	float fact,pll,pmm,pmmp1,somx2;
	int i,ll;
	if (m < 0 || m > l || fabs(x) > 1.0)
	{
		printf("Bad arguments in routine plgndr");
		exit(1);
		}
		
	pmm=1.0; //Compute Pm m .
	if (m > 0) 
	{
		somx2=sqrt((1.0-x)*(1.0+x));
		fact=1.0;
		for (i=1;i<=m;i++) 
		{
			pmm *= -fact*somx2;
			fact += 2.0;
			}
		}
	if (l == m)
		return pmm;
	else 
	{ 			//Compute Pm m+1 .
		pmmp1=x*(2*m+1)*pmm;
		if (l == (m+1))
			return pmmp1;
		else 
		{ 		//Compute Pm l , l > m + 1.
			for (ll=m+2;ll<=l;ll++) 
			{
				pll=(x*(2*ll-1)*pmmp1-(ll+m-1)*pmm)/(ll-m);
            pmm=pmmp1;
            pmmp1=pll;
            }
			return pll;
			}
		}
	}
	
double sphr(int l,int m,double x)
{

	double fact = 1.0;
	double Plm = plgndr(l,m,x);
	for(int i=l-m+1;i<=l+m;i++)
		fact *=(double)i;
	return sqrt((2.0*l+1.0)/fact/4/PI)*Plm;
	}	
	
int main()
{
	double Plm,Ylm;
	int l,m,lmax;
	double A[MAX][MAX];
	FILE *fp,*fp1;
	
	//
	// Parameters You need to change
	// -------------------------------------------------
	
	fp = fopen("W1.txt","r");					
	fp1 = fopen("phi.d","w");
	m = 4;
	lmax = 1000;
	
	//
	// Read Table 
	// -------------------------------------------------
	
	for(int i=0;i<MAX;i++)
		for(int j=0;j<MAX;j++)
			fscanf(fp,"%lf",&A[i][j]);
	
	//
	// Find maximum
	// -------------------------------------------------

	int Maxx,Maxy;
	double Maxb=-99999.0;
	double theta;
	double distx,disty;
	
	
	for(int i=0;i<MAX;i++)
		for(int j=0;j<MAX;j++)	
			if(Maxb < A[i][j])
			{
				Maxb = A[i][j];
				Maxx = i;
				Maxy = j;
				}

	printf("Max_x %d and Max_y = %d\n",Maxx,Maxy);
	//
	// Integration over blm
	// -------------------------------------------------
	double SumC,SumS,SumNorm;
	double tanphi,phi,phi1[MAX][MAX];
	double YlmC,YlmS;
	
	
	for(l = m;l<=lmax;l+=10)
	{
		SumC = 0.0;
		SumS = 0.0;		
		SumNorm = 0.0; 
		
		for(int j=0;j<MAX;j++)
		{
			for(int i=0;i<MAX;i++)	
			{		
			
	     		distx = (double)(i - Maxx);
	     		disty = (double)(j - Maxy);
   	  		theta = ((1.0*ANGMAX)/MAX)*(PI/180.0)*sqrt(distx*distx + disty*disty);
     		
   	  		if(i == Maxx)
  					phi = PI/2;
	
   	 		else if(j == Maxy)		
   	 			phi = 0;	
   	 		else
   	 		{	
		     		tanphi = fabs(((double)(j - Maxy))/((double)(i - Maxx)));
   		  		phi = atan(tanphi);
   	  			}
   	  				
   	  		if((i - Maxx)<0)
   	  			phi = PI - phi;
   	  		if((j - Maxy)<0)
   	  			phi = -phi;				
				      			
      		Ylm = sphr(l,m,cos(theta));
      		YlmC = Ylm*cos(m*phi);
      		YlmS = Ylm*sin(m*phi);

      		SumC += A[i][j]*YlmC;
      		SumS += A[i][j]*YlmS;
      		SumNorm += A[i][j];
				}			
			}
//		printf("%e \n",SumNorm);
		fprintf(fp1,"%d %e %e\n",l,SumC/SumNorm,SumS/SumNorm);
		}
	printf("Done .. Check Blm.dat");	
	fclose(fp);	
	fclose(fp1);
	}	