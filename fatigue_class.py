import numpy as np
class fatigue:
    """Class implementing fatigue equations, adapted from Mathcad provided by Dr. Delahoussaye"""
    """Beware, these equations are only valid for IP units. Conversions must be made script-side"""
    Se = 1
    Sut = 1
    def sigmaFKpsi(self,Sut):
        return Sut + 50
    def enduranceLimitKpsi(self,Sut):
        if Sut < 212:
            return .504 * Sut
        else:
            return 107
    #fully reversed
    def sfKpsi(self,Sut,Se,N):
        if Se == 0:
            Se = enduranceLimitKpsi(Sut)
        b = -1*np.log10(sigmaFKpsi(Sut)/Se)/np.log10(2e6)
        f = (sigmaFKpsi(Sut)*2e3**b)/Sut
        a = (f**2*Sut**2)/Se
        return a*N**2
    def nKpsi(self,Sut,Se,sigma):
        if Se == 0:
            Se = enduranceLimitKpsi(Sut)
        b = -1*log10(sigmaFKpsi(Sut)/Se)/log10(2e6)
        f = (sigmaFKpsi(Sut)*2e3**b)/Sut
        a = (f**2*Sut**2)/Se
        return (sigma/a)**(1/b)    
    def soderberg(self,Se,Sy,Sm):
        return (-1*Sm + Sy)*Se/Sy
    def goodman(self,Se,Sut,Sm):
        return -1*(Sm - Sut)*Se/Sut
    def gerber(self,Sm,Se,Sut):
        return (-1*Sm**2+Sut**2)*Se/Sut**2
    def deElliptic(self,Se,Sy,Sm):
        return sqrt(-1*Sm**2 + Sy**2)*Se/Sy
    def gerber_n(self,sigma_i,sigma_a,Se,Sut):
        return ((Sut/2/Se*(-Sut+np.sqrt(Sut**2 + 4*Se*sigma_i+4*Se**2)))-sigma_i)/sigma_a
    def goodman_n(self,sigma_i,sigma_m,sigma_a,Se,Sut):
        return (Se*(Sut-sigma_i))/((sigma_a*Sut)+Se*(sigma_m-sigma_i))