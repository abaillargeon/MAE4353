import numpy as np
from bolt_class import *
from scipy.optimize import newton
from fatigue_class import *

A = 0.100 #pressure vessel D
B = 0.200 #bolt circle D
C = 0.300 
D = 20e-3
E = 20e-3
N = 10.0
nut_h = 10.8e-3 #m
d = 12e-3 #m
pitch = 1.75e-3 #m
E_bolt = 207e9 #Pa
Sp = 600e6 #Pa Proof / n
Se = 129e6 #Pa corrected str
Sut = 830e6 #Pa

#Bolt lengths/areas
bolt_l = D+E+nut_h
grip_l = D+E
#bolt_l = np.ceil(bolt_l*4.0)/4 #closest 1/4in
A_t = 84.3/1e6 #m^2 table 8-1
A_d = np.pi / 4 * d ** 2 
L_t = 2 * d + 6e-3
l_d = bolt_l - L_t#unthreaded
l_t = grip_l - l_d#threaded
b = bolt()
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)

D_frustum = 1.5 * d
def E_member(x):#define the E function
    if x <= D:#steel
        return 207e9
    else:#cast iron
        return 100e9
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D_frustum,d,0,grip_l)
C_joint = b.joint_constant(k_b,k_m)
F_preload = 0.75 * Sp * A_t

def F_static(P):
    P_ext = P*(np.pi/4)*(.150)**2
    P_bolt = P_ext / N
    n_load = b.load_n(Sp,A_t,F_preload,C_joint,P_bolt)
    return n_load - 1.0

p_max = newton(F_static, 10e-6, fprime=None, args=(), tol=1.48e-8, maxiter = 500)  
print 'Max static pressure: ' + str(p_max/1e6) + ' MPa'

def F_fatigue(P):
    P_ext = P*(np.pi/4)*(.150)**2
    P_ext = P_ext / N
    sigma_a = C_joint*P_ext/2/A_t
    sigma_m = C_joint*P_ext/2/A_t + F_preload/A_t
    sigma_i = sigma_m - sigma_a  
    n = Se*(Sut-sigma_i)/(Sut*sigma_a + Se*(sigma_m-sigma_i))
    return n - 1.5   

p_max = newton(F_fatigue, 10e-6, fprime=None, args=(), tol=1.48e-8, maxiter = 500)  
print 'Max fatigue pressure: ' + str(p_max/1e6) + ' MPa'












