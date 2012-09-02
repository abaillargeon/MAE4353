#include <stdio.h>
#include <math.h>

float catalog_load(float xd, float load_axial, float load_radial, float V, float C0, float R);
float interpolate(float x1, float x2, float y1, float y2, float x);
void xy_ball(float *xy_arr, float load_axial, float load_radial, float V, float C0);

void main(){
	float hours = 10000;
	float speed = 400;//rpm
	float L10 = 1e6;
	float load_radial = 8.0;//kN
	float load_axial = 2.0;//kN
	float V = 1.0;//1.2 if outside rotates
	float R = 0.99;//reliability
	
	float Ld, xd, C0, xy[2];
	
	Ld = hours * speed * 60.0;
	xd = Ld/L10;
	
	printf("Enter C0:\n>>>",xd,R);
	scanf("%f",&C0);
	printf("Catalog Load: %f\n",catalog_load(xd,load_axial,load_radial,V,C0,R));
}

float catalog_load(float xd, float load_axial, float load_radial, float V, float C0, float R){
	float xy_ball_bearing[2], corrected_load, C10;
	
	xy_ball(xy_ball_bearing,load_axial,load_radial,V,C0);
	corrected_load = xy_ball_bearing[0]*V*load_radial + xy_ball_bearing[1]*load_axial;
	C10 = 1.0*corrected_load*pow(xd/(0.02+4.439*pow(log(1.0/R),1.0/1.483)),1.0/3);
	return C10;
}

float interpolate(float x1, float x2, float y1, float y2, float x){
	return (x-x1)/(x2-x1)*(y2-y1) + y1;
}

void xy_ball(float *xy_arr, float load_axial, float load_radial, float V, float C0){
	//Assume Fa/(VFr) > e?
	int i = 0;
	/* Table 11-1 in array form */
	float FaC0[] = {0.014,0.021,0.028,0.042,0.056,0.070,0.084,0.11,0.17,0.28,0.42,0.56};
	float Y2[] = {2.30,2.15,1.99,1.85,1.71,1.63,1.55,1.45,1.31,1.15,1.04,1.00};
	while(i<11){ 
		if(load_axial/C0 < FaC0[i]){break;}
		i++;
	}
	xy_arr[0] = 0.56;
	xy_arr[1] = interpolate(FaC0[i-1],FaC0[i],Y2[i-1],Y2[i],load_axial/C0);
}






