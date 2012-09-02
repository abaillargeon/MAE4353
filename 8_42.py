import numpy as np
from bolt_class import *
from scipy.optimize import newton

A = .5
B = 5.0/8
C = 3.5 #pressure vessel D
D = 4.25
E = 6.0 #bolt circle D
F = 8.0
N = 10.0
p_g = 1500.0*1.15 #psi

d = 0.5 #in
pitch = 1.0/13
E_bolt = 30e6 #psi
nut_h = 7.0/16 #in (table A-31)
Sp = 85e3 #Proof / n
print 'Grade: SAE 5'

#Variables
n_bolts = 10

#Bolt lengths/areas
bolt_l = A+B+nut_h
grip_l = A+B
bolt_l = np.ceil(bolt_l*4.0)/4 #closest 1/4in
A_t = 0.1419 #table 8-2
A_d = np.pi / 4 * .5 ** 2 
L_t = 2 * d + .25
l_d = bolt_l - L_t#unthreaded
l_t = grip_l - l_d#threaded
b = bolt()
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)

D = 1.5 * d
def E_member(x):#define the E function
    if x <= A:#steel
        return 30e6
    else:#cast iron
        return 14.5e6
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D,d,0,grip_l)

C_joint = b.joint_constant(k_b,k_m)

bolt_spacing = np.pi*E/n_bolts/d
print 'Bolt spacing ratio: ' + str(bolt_spacing)
print 'Joint constant: ' + str(C_joint)
F_preload = 0.75 * Sp * A_t
P_ext = p_g*(np.pi/4)*C**2
P_bolt = P_ext / n_bolts

n_load = b.load_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_permanent_set = b.permanent_set_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_joint_separation = b.joint_separation_n(F_preload,C_joint,P_bolt)
print 'Yielding factor of safety: ' + str(n_permanent_set)