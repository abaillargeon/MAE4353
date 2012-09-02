import numpy as np
from bolt_class import *
from fatigue_class import *
from scipy.optimize import newton

#Givens
t_block = 1.5 #in
P_min = 4e3 #lbs
P_max = 6e3 #lbs
E_bolt = 30e6 #psi
t_nut = 41.0/64 #in

d = 3.0/4 #in
Sp = 85e3 #psi
Se = 18.6e3 #psi
Sut = 120e3 #psi

pitch = 1.0/16 # 
A_t = 0.373
A_d = np.pi/4*d**2
K = 0.18

F_preload = 25e3 #lbs

#Find T
b = bolt()
T = b.torque_approx(K,d,F_preload)

grip_l = t_block 
bolt_l = t_block + t_nut + 2*pitch
bolt_l = np.ceil(bolt_l*4.0)/4
L_t = 2*d + .25
l_d = bolt_l - L_t
l_t = grip_l - l_d
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)

D = 1.5 * d
def E_member(x):#define the E function
    return 16e6 
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D,d,0,grip_l)

C_joint = b.joint_constant(k_b,k_m)

P_bolt = P_max
n_load = b.load_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_permanent_set = b.permanent_set_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_joint_separation = b.joint_separation_n(F_preload,C_joint,P_bolt)

print 'a. Yielding factor of safety: ' + str(n_permanent_set)
print 'b. Overload factor of safety: ' + str(n_load)
print 'c. Joint separation factor of safety: ' + str(n_joint_separation)

#Find goodman factor of safety
f = fatigue()
sigma_preload = F_preload / A_t
sigma_a = C_joint * (P_max - P_min) / A_t / 2
sigma_m = C_joint * (P_max + P_min) / A_t / 2 + sigma_preload
n_goodman = f.goodman_n(sigma_preload,sigma_m,sigma_a,Se,Sut)
print 'd. Goodman fatigue factor of safety: ' + str(n_goodman)