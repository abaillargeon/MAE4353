import numpy as np
from bolt_group_class import *
from bolt_class import *
from failure_class import *
from scipy.optimize import newton

Sy = 1040e6 #Pa
F = 24e3 #N
t = 8e-3 #m
f_dist = 200e-3

a = bolt_group()
a.add_force([0,-F],[f_dist,0])

def S(d):
    A_d = np.pi/4*d**2
    #Shear on bolts
    a.add_bolt([0,0],  A_d)
    a.add_bolt([0,32e-3],  A_d)
    a.add_bolt([0,-32e-3],  A_d)
    #print a.bolts
    T = a.torque()
    f = a.total_shear_forces(T)
    f_max = f[1][0] #top bolt
    tau = f_max/A_d

    f = failure() #init failure class
    f.tau_yz = tau
    sigma_vm = f.von_mises()
    n = Sy/sigma_vm #find safety factor
    a.clear_bolts() 
    return n - 2.0

#Solves for d when n = 2.0
d = newton(S, 10e-6, fprime=None, args=(), tol=1.48e-8, maxiter = 500)  
print 'Bolt diameter: ' + str(d*1000) + ' mm'
