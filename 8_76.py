import numpy as np
from bolt_group_class import *
from bolt_class import *
from failure_class import *
from scipy.optimize import newton

d = 12e-3 #m
pitch = 1.75e-3 #m/turn
Sy = 420e6 #Pa
F = 12e3 #N
t = 8e-3 #m
f_dist = 200e-3

t_nut = 10.8e-3 #m
A_d = np.pi/4*d**2
A_t = 84.3 / 1000**2 #m^2

St_bracket = 380e6 #Pa
Sy_bracket = 210e6 #Pa

#Shear on bolts
a = bolt_group()
a.add_bolt([0,0],  A_d)
a.add_bolt([0,32e-3],  A_d)
a.add_bolt([0,-32e-3],  A_d)
a.add_force([0,-F],[f_dist,0])
T = a.torque()
f = a.total_shear_forces(T)
f_max = f[1][0]
tau = f_max/A_d

f = failure()
f.tau_yz = tau
sigma_vm = f.von_mises()
print 'Bolt shear factor of safety: ' + str(Sy/sigma_vm)

#Bearing on bolts/bracket
A_proj_bolt = d*t
sigma_bolt = f_max / A_proj_bolt
print 'Bolt bearing factor of safety: ' + str(Sy/sigma_bolt)

A_proj_bracket = d*t
sigma_bracket = f_max / A_proj_bracket
print 'Bracket bearing factor of safety: ' + str(Sy_bracket/sigma_bracket)

#Bending in bracket
M = F*f_dist
c = 68e-3 #m
I = 1.0/12*t*(c*2)**3 - 1.0/12*t*d**3 - 2*(1.0/12*t*d**3 + (t*d)*(32e-3)**2)
sigma_bending = M*c/I
print 'Bracket bending factor of safety: '+ str(Sy_bracket/sigma_bending)