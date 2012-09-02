import numpy as np
from buckling_class import *
from scipy.optimize import newton
#givens
mass = 300 #kg
theta = 15 #deg
l = 350e-3 #m
w = 30e-3 #m
C = 1.4 #end conditions

#FBD shows maximum loading at theta=15 degrees spread over 4 bars
load = mass * 9.81 / np.sin(np.radians(theta)) / 4

def f(t,l,C,w,load):#define difference function to use root finder later
    col = buckling()
    col.E = 207e9 #Pa
    col.Sy = 180e6 #Pa
    nd = 3.5 #safety factor
    k = col.radiusOfGyrationRect(w,t)
    stress = (load * nd)/(t * w)
    diff = col.criticalStress(l,k,C) - stress
    return diff

    
f(10e-3,l,C,w,load)  
#solution
#uses newton-raphson to find root
partA = newton(f, 10e-3, fprime=None, args=(l,C,w,load))

print 'size: ' + str(partA*1000) + 'mm'

def safetyFactor(t,l,C,w,load):#define difference function to use root finder later
    col = buckling()
    col.E = 207e9 #Pa
    col.Sy = 180e6 #Pa
    nd = 3.5 #safety factor
    k = col.radiusOfGyrationRect(w,t)
    stress = (load)/(t * w)
    sf = col.criticalStress(l,k,C) / stress
    return sf

print 'safety factor: ' + str(safetyFactor(6e-3,l,C,w,load))