import numpy as np
from bolt_group_class import *
from failure_class import *
from scipy.optimize import newton

d = 12e-3 #m
A_b = np.pi/4*d**2 #m^2
F = 3.2e3
Sy = 420e6 #Pa
Sy_beam = 370e6 #Pa
h = 50e-3

#check bolts for shear
a = bolt_group()
a.add_bolt([0.200,0],  A_b)
a.add_bolt([0.250,0], A_b)
a.add_force([0,F/2],[0,0])

T = a.torque()
f = a.total_shear_forces(T)
f_max = f[0]
tau = f_max/A_b

f = failure()
f.tau_xy = tau
sigma = f.von_mises()
print 'Von Mises bolt shear factor of safety: ' + str(Sy/sigma) 

#check right bolt and center of beam
M_right_bolt = F/2*.250
M_center = F/2*.350

I_right_bolt = 1.0/12*20e-3*(h)**3-1.0/12*20e-3*(12e-3)**3
I_center = 1.0/12*20e-3*(h)**3

sigma_right_bolt = M_right_bolt*h/I_right_bolt
sigma_center = M_center*h/I_center
print 'Right bolt hole factor of safety: ' + str(Sy_beam/sigma_right_bolt)
print 'Center of beam factor of safety: ' + str(Sy_beam/sigma_center)