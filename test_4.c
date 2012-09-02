#include <stdio.h>
#include <math.h>

float catalog_load(float xd, float load_axial, float load_radial, float V, float C0, float R, float a);
float interpolate(float x1, float x2, float y1, float y2, float x);
void xy_ball(float *xy_arr, float load_axial, float load_radial, float V, float C0);

void main(){
	float hours = 25000;
	float speed = 600;//rpm
	float L10 = 1e6;
	float ba_load_radial = 215.034*4.4482;//N
	float ba_load_axial = 555*4.4482;//N
	float bb_load_radial = 76.059*4.4482;//N
	float bb_load_axial = 0;
	float V = 1.0;//1.2 if outside rotates
	float R = 0.99;//reliability
	
	float Ld, xd, C0, xy[2];
	
	Ld = hours * speed * 60.0;
	xd = Ld/L10;
	//Bearing A
	C0 = 85000; //N
	printf("Bearing A (C0: %2.2f) Catalog Load: %2.2f\n",C0,catalog_load(xd,ba_load_axial,ba_load_radial,V,C0,R,3.0));
	//Bearing B
	C0 = 8800;
	printf("Bearing B (C0: %2.2f) Catalog Load: %2.2f\n",C0,catalog_load(xd,bb_load_axial,bb_load_radial,V,C0,R,10.0/3));
}

float catalog_load(float xd, float load_axial, float load_radial, float V, float C0, float R, float a){
	float xy_ball_bearing[2], corrected_load, C10;
	xy_ball(xy_ball_bearing,load_axial,load_radial,V,C0);	
	if(load_axial < 0.01){ corrected_load = load_radial; } 
	else{ corrected_load = xy_ball_bearing[0]*V*load_radial + xy_ball_bearing[1]*load_axial; }
	C10 = 1.3*corrected_load*pow(xd/(0.02+4.439*pow(log(1.0/R),1.0/1.483)),1.0/a);
	return C10;
}

float interpolate(float x1, float x2, float y1, float y2, float x){
	return (x-x1)/(x2-x1)*(y2-y1) + y1;
}

void xy_ball(float *xy_arr, float load_axial, float load_radial, float V, float C0){
	//Assume Fa/(VFr) > e
	int i = 0;
	/* Table 11-1 in array */
	float FaC0[] = {0.014,0.021,0.028,0.042,0.056,0.070,0.084,0.11,0.17,0.28,0.42,0.56};
	float Y2[] = {2.30,2.15,1.99,1.85,1.71,1.63,1.55,1.45,1.31,1.15,1.04,1.00};
	while(i<11){ 
		if(load_axial/C0 < FaC0[i]){break;}
		i++;
	}
	xy_arr[0] = 0.56;
	if(i == 0){ xy_arr[1] = FaC0[0]; }
	else{ xy_arr[1] = interpolate(FaC0[i-1],FaC0[i],Y2[i-1],Y2[i],load_axial/C0);}
}






