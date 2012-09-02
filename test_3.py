
Kf = 2
tau_max = 3920 #psi
tau_fatigue = tau_max * Kf


# #60 electrode
tau_a = tau_fatigue #psi
tau_m = tau_fatigue / 2

Sut = 62e3 #psi Table 9.3
Sse = 18e3 #psi Table 9.6

def n(Sut,Sse,tau_a,tau_m):#pg 497 example
    a = .5*(0.67*Sut/tau_m)**2*tau_a/Sse
    b = -1 + (1+(2*tau_m*Sse/0.67/Sut/tau_a)**2)**.5
    return a*b
    
#gerber
print 'N - gerber fatigue'
print str(n(Sut,Sse,tau_a,tau_m))

print 'N - static failure'
print Sse/(tau_max)
