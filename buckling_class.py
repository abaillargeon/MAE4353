import numpy as np
class buckling:
    """Class implementing buckling formulas, adapted from Mathcad provided by Dr. Delahoussaye"""
    E = 1
    Sy = 1
    def mode(self,l,k,C):
        if l/k <= np.sqrt(2*np.pi**2*C*self.E/self.Sy):
            return 'Johnson'
        else:
            return 'Euler'
    def johnsonStress(self,l,k,C):
        return self.Sy - (1/(C*self.E))*((self.Sy*l)/(2*np.pi*k))**2
    def eulerStress(self,l,k,C):
        return (C*np.pi**2*self.E)/((l/k)**2)
    def radiusOfGyrationCirc(self, d):
        return d/4
    def radiusOfGyrationRect(self,b,h):
        return np.sqrt(3)/6*h
    def radiusOfGyration(self,I,A):
        return np.sqrt(I/A)
    def criticalStress(self,l,k,C):
        if self.mode(l,k,C) == 'Euler':
            return self.eulerStress(l,k,C)
        else:
            return self.johnsonStress(l,k,C)