import numpy as np
from failure_class import * 

l = 10 * 25.4 #mm
P = 3.0 #HP
omega = 1800 #rpm
d = 18 / 25.4 #in


T = P * 63025 / omega #lbf in
J = np.pi * d**4 / 32
tau = T * d / 2 / J

M = 5 * 27 * 3 #in lbf
I = J / 2
sigma = M * d / 2 / I

f = failure()
f.sigma_x = sigma
f.tau_xy = tau
sigma1 = f.von_mises()

#Q&T 1141
Sy = 1186e3 #psi
print T
print Sy/sigma1

#N = 75.4226284557
