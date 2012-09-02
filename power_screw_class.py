import numpy as np
class power_screw:
    """Power screw class"""
    type = ''#possible Square, ACME, or standard
    
    def torque_raise(self,F,fs,dm,lead,dc,fc,alpha=2):
        if self.type == 'Square':
            return F*dm/2.0*((lead+np.pi*fs*dm)/(np.pi*dm-fs*lead)) + F*fc*dc/2.0
        elif self.type == 'ACME':#beep beep
            return F*dm/2.0*((lead+np.pi*fs*dm*np.reciprocal(np.cos(np.radians(14.5))))/(np.pi*dm-fs*lead*np.reciprocal(np.cos(np.radians(14.5))))) + F*fc*dc/2
        else:
            return F*dm/2.0*((lead+np.pi*fs*dm*np.reciprocal(np.cos(np.radians(alpha))))/(np.pi*dm-fs*lead*np.reciprocal(np.cos(np.radians(alpha))))) + F*fc*dc/2
    def torque_lower(self,l,k,C):
        if self.type == 'Square':
            return F*dm/2.0*((-lead+np.pi*fs*dm)/(np.pi*dm+fs*lead)) + F*fc*dc/2.0
        elif self.type == 'ACME':#beep beep
            return F*dm/2.0*((-lead+np.pi*fs*dm*np.reciprocal(np.cos(np.radians(14.5))))/(np.pi*dm+fs*lead*np.reciprocal(np.cos(np.radians(14.5))))) + F*fc*dc/2
        else:
            return F*dm/2.0*((-lead+np.pi*fs*dm*np.reciprocal(np.cos(np.radians(alpha))))/(np.pi*dm+fs*lead*np.reciprocal(np.cos(np.radians(alpha))))) + F*fc*dc/2
    def nom_shear_stress(self,T,dr):
        return 16*T/np.pi/dr**3
    def efficiency(self,F,lead,T):
        return F*lead/2/np.pi/T
    def axial_stress(self,F,dr):
        return 4*F/np.pi/dr**2
    def bearing_stress(self,F,dm,p):
        return 2*0.38*F/np.pi/dm/p
    def bending_stress(self,F,dr,p):
        return 6*0.38*F/np.pi/dr/p