import numpy as np
from bolt_class import *
from fatigue_class import *
from scipy.optimize import newton

#Givens
d = 3.0/8 #in
E_bolt = 30e6 #psi
t_nut = 21.0/64 #in
n_bolts = 6
t_bracket = 3.0/4

E_cyl = 30e6
t_cyl = 3.0/8 #in
d_cyl = 4.0 #in
l_cyl = 12.0 #in
p_cyl = 2000.0 #psi

Sp = 85e3 #psi
Se = 18.6e3 #psi
Sut = 120e3 #psi

pitch = 1.0/16 # 
A_t = 0.0775
A_d = np.pi/4*d**2
K = 0.18

F_preload = 0.75 * A_t * Sp #lbs

#Find T
b = bolt()
T = b.torque_approx(K,d,F_preload)

grip_l = t_bracket + l_cyl + t_bracket 
bolt_l = t_bracket + l_cyl + t_bracket + t_nut + 2*pitch
bolt_l = np.ceil(bolt_l*4.0)/4
L_t = 2*d + .5
l_d = bolt_l - L_t
l_t = grip_l - l_d
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)
print 'a. Bolt stiffness: ' + str(k_b/1000) + ' ksi'

#Assuming k_m comes only from the cylinder
A_cyl = np.pi/4*((d_cyl+2*t_cyl)**2-d_cyl**2)
k_m = A_cyl*E_cyl/l_cyl/n_bolts
print 'Member stiffness: '+ str(k_m/1000) + ' ksi'

P_bolt = np.pi/4*d_cyl**2*p_cyl/n_bolts
C_joint = b.joint_constant(k_b,k_m)

#Find gerber factor of safety
f = fatigue()
sigma_preload = F_preload / A_t
sigma_a = C_joint * (P_bolt - 0) / A_t / 2
sigma_m = C_joint * (P_bolt + 0) / A_t / 2 + sigma_preload
n_gerber = f.gerber_n(sigma_preload,sigma_a,Se,Sut)
print 'b. Gerber factor of safety: ' + str(n_gerber)

def f(p_cyl):#Find when n_joint_separation = 1
    P_bolt = np.pi/4*d_cyl**2*p_cyl/n_bolts
    n_joint_separation = b.joint_separation_n(F_preload,C_joint,P_bolt)
    return n_joint_separation - 1.0
    
print 'c. Joint separation pressure: ' + str(newton(f, 10e-3, fprime=None)) + ' psi'