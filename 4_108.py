import numpy as np
from buckling_class import *
from scipy.optimize import brentq
#givens
bore = 2 #in
p = 1500 #psi
l = 50 #in
C = 1.0 #rounded-rounded end conditions

def f(d,l,C):#define difference function to use root finder later
    col = buckling()
    col.E = 30e6 #psi
    col.Sy = 37.5e3 #psi
    nd = 2.5 #safety factor
    k = col.radiusOfGyrationCirc(d)
    stress = (p * np.pi/4 * bore**2 * nd)/(np.pi/4* d**2)
    diff = col.criticalStress(l,k,C) - stress
    return diff

#solution
#uses [http://en.wikipedia.org/wiki/Brent's_method] to find root
partA = brentq(f, -1.0, 10.0, args=(l,C))
print 'a. ' + str(partA) + ' inches'

l = 16 #in
partB = brentq(f, .5, 10.0, args=(l,C))
print 'b. ' + str(partB) + ' inches'

#now we set d to 1.25 and .75 and find safety factors
def safetyFactor(d,l,C):
    col = buckling()
    col.E = 30e6 #psi
    col.Sy = 37.5e3 #psi
    k = col.radiusOfGyrationCirc(d)
    stress = (p * np.pi/4 * bore**2)/(np.pi/4 * d**2)
    sf = col.criticalStress(l,k,C) / stress
    return sf

print 'c. ' + str(safetyFactor(1.25,50,C)) + ', ' + str(safetyFactor(0.75,16,C))#find safety factors for l=50,l=16