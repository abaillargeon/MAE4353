import numpy as np
from bolt_group_class import *
from bolt_class import *
from failure_class import *
from scipy.optimize import newton

A = .5
B = 3
C = 6
L = 8
t = .5
d = .5
F = 2500 #lbf
Sy = 65e3 #psi
pitch = 1.0/13
A_d = np.pi/4*d**2
A_t = 0.1419
E_bolt = 30e6
t_nut = 7.0/16

#check bolts for shear
a = bolt_group()
a.add_bolt([0,C],  A_d)
a.add_force([0,F],[0,0])
T = a.torque()
f = a.total_shear_forces(T)
f_max = f[0]
tau = f_max/A_t

#tension
b = bolt()
grip_l = A + t 
bolt_l = A + t + t_nut 
bolt_l = np.ceil(bolt_l*4.0)/4
L_t = 2*d + .25
l_d = bolt_l - L_t
l_t = grip_l - l_d
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)
D = 1.5 * d

def E_member(x):#define the E function
    return 30e6 
b._E = E_member #redefine object function
k_m = b.member_stiffness(grip_l,D,d,0,grip_l)
C_joint = b.joint_constant(k_b,k_m)
F_tensile = F*B/(L-(L-C)/2)
F_preload = Sy*.75*A_t
sigma = (F_tensile*C_joint+F_preload)/A_t

f = failure()
f.sigma_x = sigma
f.tau_yz = tau
sigma_vm = f.von_mises()
print 'Bolt failure von Mises factor of safety: ' + str(Sy/sigma_vm)
