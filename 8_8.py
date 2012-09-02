import numpy as np
from failure_class import *
from power_screw_class import *
from buckling_class import *
from scipy.optimize import newton

d_handle = 3.0/8 #in, force float
d_ball = d_handle*2
l_handle = 3.5 #in
d = 3.0/4 #in
fs = 0.15
fc = 0.15
dc = 1.0
pitch = 1.0/6 #in
force = 8 #lbf

d_r = d - pitch/2 #ACME thread, Fig 8.3
T = force * l_handle

def f(F):
    p = power_screw()
    p.type = 'ACME'
    return p.torque_raise(F,fs,d_r,pitch,dc,fc) - T #find F where T_raise = T

print 'a. '+str(newton(f, 10e-4, fprime=None))+' lbf'



