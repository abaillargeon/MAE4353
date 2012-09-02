import numpy as np
from bolt_group_class import *
from failure_class import *
from scipy.optimize import newton

d = 0.5 #m
A_b = np.pi/4*d**2 #m^2
F = 2000 #lbf
E_bolt = 30e6
Sy = 92e3 #psi SAE grade 5

#check bolts for shear
#centroid is left side of channel, on centerline
a = bolt_group()
a.add_bolt([1.0,0],  A_b)
a.add_bolt([5.0,-2.0], A_b)
a.add_bolt([5.0,2], A_b)
a.add_force([0,-F],[12,0])

T = a.torque()
f = a.total_shear_forces(T)
f_max = f[2]
tau = f_max/A_b

f = failure()
f.tau_xy = tau
sigma = f.von_mises()
print 'Von Mises bolt shear factor of safety: ' + str(Sy/sigma) 
