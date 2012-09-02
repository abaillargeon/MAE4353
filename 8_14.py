import numpy as np
from bolt_class import *
from scipy.optimize import newton

l_1 = 2.0 #in
l_2 = 1.0 #in
d = 0.5 #in
pitch = 1.0/13
E = 30e6 #psi

#Part a
nut_h = 7.0/16 #in (table A-31)
bolt_l = l_1+l_2+nut_h
grip_l = l_1+l_2
print str(np.ceil(bolt_l*4.0)/4) + ' in'#closest 1/4in

#Part b
A_t = 0.1419 #table 8-2
A_d = np.pi / 4 * .5 ** 2 
L_t = 2 * d + .25
l_d = bolt_l - L_t#unthreaded
l_t = grip_l - l_d#threaded

b = bolt()
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E)
print str(k_b/1000) + ' ksi'

#Part c
D = 1.5 * d
l = l_1+l_2
def E(x):#define the E function
    if x <= 2:#steel
        return 30e6
    else:#cast iron
        return 14.5e6
b._E = E #redefine object function
print str(b.member_stiffness(l,D,d,0,l)/1000) + ' ksi'
