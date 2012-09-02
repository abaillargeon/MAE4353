import numpy as np
import scipy as sp
from scipy.optimize import newton

class spring:
    G = 1
    A = 1
    m = 1
    Ndmin = 1.2
    def _init_material(self, A, m):
        self.A = A
        self.m = m
    def spring_index(self, d, D):
        return D/d
    def _shear_stress(self, F, d, D):
        return 8*F*D/np.pi/d**3 + 4*F/np.pi/d**2
    def _bergstrasser_correction_factor(self, C):#Equivalent to Kc
        return 2*C*(4*C + 2)/((4*C-3)*(2*C + 1))
    def corrected_shear_stress(self, F, d, D):
        return self._bergstrasser_correction_factor(self.spring_index(d,D))*self._shear_stress(F, d, D)
    def deflection(self, F, d, D, Na):
        return 8*F*D**3*Na/(d**4*self.G)
    def scale(self, d, D, Na):#aka spring rate
        return d**4*self.G/(8*(D**3)*Na)
    def natural_frequency(self, d, D, Na):
        return .5*np.sqrt(self.scale(d, D, Na)*386/(np.pi**2*d**2*D*Na*0.284/4))
    def material_volume(self, d, D, Nt):
        return np.pi**2*d**2*Nt*D/4
    def stress_ultimate(self, d):
        return self.A/d**self.m
    def free_length_compression(self, Ls, eps, ymax):
        return Ls + (1+eps)*ymax
    def n_turns(self, Na, Ne):
        return Na+Ne
    def n_solid(self, Nt):
        return Nt
    def find_D(self, d, F):#solve for D
        return newton(self.find_D_minimizer, 10e-6, fprime=None, args=(d,F))        
    def find_D_minimizer(self, D, d, F):
        Ssy = 0.45*self.stress_ultimate(d)*1000
        tau_max = Ssy/self.Ndmin
        return self.corrected_shear_stress(F, d, D)-tau_max
    def find_F(self, d, D):#solve for F
        return newton(self.find_F_minimizer, 10e-6, fprime=None, args=(d,D))        
    def find_F_minimizer(self, F, d, D):
        Ssy = 0.45*self.stress_ultimate(d)*1000
        tau_max = Ssy/self.Ndmin
        return self.corrected_shear_stress(F, d, D)-tau_max
    def find_active_turns(self, d, D, k):#solve for Na
        return newton(self.find_active_turns_minimizer, 10e-6, fprime=None, args=(d, D, k))        
    def find_active_turns_minimizer(self, Na, d, D, k):
        return self.scale(d, D, Na) - k