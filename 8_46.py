import numpy as np
from bolt_class import *
from scipy.optimize import newton

t_block = 20e-3 #m
t_joist = 20e-3 #m
P = 18e3 #N
E_block = 135e9 #GPa
E_bolt = 207e9 #Gpa

t_washer = 4.6e-3 #m
t_nut = 21.5e-3
d = 24e-3 #m
Sp = 600e6 #Pa

pitch = 3e-3 # mm/turn
A_t = 353.0 / 1000**2 #m^2
A_d = np.pi/4*d**2
K = 0.18
n_bolts = 4

F_preload = 0.9 * A_t * Sp

b = bolt()
T = b.torque_approx(K,d,F_preload)
print 'a. '+ str(T) + 'N m'

grip_l = t_washer + t_block + t_joist + t_washer
bolt_l = t_washer + t_block + t_joist + t_washer + t_nut + 2*pitch
bolt_l = (np.ceil((bolt_l*1000)/5.0)*5)/1000
L_t = 2*d + 6e-3
l_d = bolt_l - L_t
l_t = grip_l - l_d
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)

D = 1.5 * d
def E_member(x):#define the E function
    if x <= t_washer:
        return 207e9
    elif x<=t_washer+t_block:
        return 135e9
    elif x<=t_washer+t_block+t_joist:
        return 207e9
    else:
        return 207e9
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D,d,0,grip_l)

C_joint = b.joint_constant(k_b,k_m)

P_bolt = P / n_bolts
n_load = b.load_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_permanent_set = b.permanent_set_n(Sp,A_t,F_preload,C_joint,P_bolt)
n_joint_separation = b.joint_separation_n(F_preload,C_joint,P_bolt)

print 'b. Overload factor of safety: ' + str(n_load)
print 'Yielding factor of safety: ' + str(n_permanent_set)
print 'Joint separation factor of safety: ' + str(n_joint_separation)