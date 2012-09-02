import numpy as np
from bolt_class import *
from scipy.optimize import newton

#M5x15 grip bolt in tension 
#Use 8.8 or 10.9. 12.9 is also decently cheap at mcmaster


F_rotation = 5500 #N
d = 6e-3 #m
grip_l = 10e-3 + d/2
A_t = 20.1e-6 #m^2
A_d = np.pi / 4 * (d)**2

bolt_l = grip_l + 1.5*d
L_t = 2*d+6e-3
l_d = bolt_l - L_t
l_t = grip_l - l_d 
Sp = 830e6 #Pa class 10.9

b = bolt()
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,207e9)
D = 1.5 * d
def E_member(x):#define the E function
    return 207e9
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D,d,0,grip_l)
C_joint = b.joint_constant(k_b,k_m)
F_preload = 0.75 * Sp * A_t

n_load = b.load_n(Sp,A_t,F_preload,C_joint,F_rotation)
print "Grip bolt in tension: "+ str(n_load)


#M3x6 grip bolts in shear

d = 4e-3
A_t = 8.78e-6
A_d = np.pi / 4 * (d)**2
tau_shear = F_rotation / 4 / A_t
print "Grip bolts in shear: " + str(Sp/tau_shear) 

#M4x?? blade holding bolt in shear

d = 5e-3
A_t = 14.2e-6
A_d = np.pi / 4 * (d)**2
tau_shear = F_rotation / A_d
print "Main grip bolt in shear: " + str(Sp/tau_shear)

#C:\Users\Al\Dropbox\MAE_4353_Code>python project_bolts.py
#Grip bolt in tension: 3.10119442404
#Grip bolts in shear: 3.49364016736
#Main grip bolt in shear: 2.18065808278


