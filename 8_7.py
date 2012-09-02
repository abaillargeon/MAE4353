import numpy as np
from failure_class import *
from power_screw_class import *
from buckling_class import *
from scipy.optimize import newton

d_handle = 3.0/8 #in, force float
d_ball = d_handle*2
l_handle = 4.25 #in
d = 3.0/4 #in
l_screw = 8.0 #in
fs = 0.15
alpha = 60.0/2 #UNC standard
pitch = 1.0/10 #in
area_minor = .302 #in^2
d_p = d - (0.649519 * pitch)
#AISI 1006
E = 30e6 #psi
Sy = 41e3 #psi


#a. Bending moment
I_handle = np.pi * d_handle**4/64
l_eff = l_handle - .5*d_ball - d_ball - d #apply force in center of ball, moment just where handle meets screw
F_failure = Sy * I_handle / l_eff / (d_handle/2)
T_failure = F_failure * (l_eff + d/2) #+d_m/2 puts us back on centerline of screw
print 'a. '+str(T_failure)+' in lb'
#b.

def f(F):
    p = power_screw()
    p.type = 'UNC'
    return p.torque_raise(F,fs,d_p,pitch,0,0,alpha) - T_failure #find F where T = T_failure

print 'b. '+str(newton(f, 10e-4, fprime=None))+' lbf'


a = buckling()
a.E = E
a.Sy = Sy
k = a.radiusOfGyrationCirc(d_p)
sigma = a.criticalStress(6,k,1.2)#Assuming C=1.2 for fixed-rounded end conditions
P = sigma*np.pi/4*d_p**2
print 'c. '+str(P)+' lbf'