import numpy as np
import scipy as sp
from scipy.integrate import quad
class bolt:
    """Bolt class - adapted from Delahoussaye mathcad files"""
    def thread_length(self,l,d):
        if l < 6:
            return 2*d + .25
        else:
            return 2*d + .5            
    def _frustum_area(self,x,D,d,l):
        if x > l/2.0:
            x = l-x
        return np.pi*((x*np.tan(np.radians(30)) + D/2)**2 - (d/2)**2)    
    def _E(self,x):#this function needs to be redefined upon instantiation
        return 1
    def bolt_stiffness(self,lt,ld,At,Ad,E):
        if ld == 0:
            return At*E/lt
        if lt == 0:
            return Ad*E/ld
        return (Ad*At*E)/(Ad*lt + At*ld)    
    def member_stiffness(self,l,D,d,l_1,l_2):
        s = sp.integrate.quad(lambda x: 1.0/(self._E(x)*self._frustum_area(x,D,d,l)),l_1,l_2)
        return np.reciprocal(s[0])   
    def joint_constant(self,kb,km):
        return kb/(kb+km)   
    def torque_approx(self,K,d,F_preload):
        return K*d*F_preload  
    def force_preload(self,K,d,T):
        return T/(K*d)   
    def load_n(self,Sp,At,F_preload,C,P):
        return (Sp*At - F_preload) / (C * P)       
    def joint_separation_n(self,F_preload,C,P):
        return F_preload/((1.0 - C)*P)  
    def permanent_set_n(self,Sp,At,F_preload,C,P):
        return Sp*At / (C*P + F_preload)  