import numpy as np
from bolt_class import *
from scipy.optimize import newton

d = 10e-3 #m M10x1.5
pitch = 1.5 #
A_t = 58.0 / (1000**2) #m^2
E_bolt = 207e9 #Pa

#section 1&3
l_1 = 10e-3 #m
l_2 = 30e-3 #m
l_3 = 10e-3 #m

grip_l = l_1+l_2+(d/2)
bolt_l = l_1+l_2+1.5*d
print str(np.ceil((bolt_l*1000)/5.0)*5) + ' mm' #closest 5mm up

#Part b
A_d = np.pi / 4 * d ** 2 
L_t = (2 * (d*1000) + 6)/1000 
l_d = bolt_l - L_t#unthreaded
l_t = grip_l - l_d#threaded

b = bolt()
k_b = b.bolt_stiffness(l_t,l_d,A_t,A_d,E_bolt)
print str(k_b/1e6) + ' MPa'

#Part c
D = 1.5 * d
l = grip_l
def E(x):#define the E function
    if x <= 10e-3:#Al
        return 71.7e9
    elif x <= 40e-3:#Steel
        return 207e9
    else:#cast iron
        return 71.7e9
b._E = E #redefine object function
print str(b.member_stiffness(l,D,d,0,l)/1e6) + ' MPa'
