import numpy as np
from fatigue_class import *
from scipy.optimize import newton
import matplotlib.pyplot as plt

#givens
l = 140e-3 #m
w = 20e-3 #m
t = 4e-3 #m
r_bend = 4e-3 #m - Refers to the inside edge of the bend (not r_c!)
min_delta = 2e-3 #m
max_delta = 6e-3 #m
hardness = 490 #Bhn
E = 207e9 #Pa

#intermediate calculations
I = 1.0/12*w*t**3
A = w*t
Sut = hardness * .5 #kpsi, 2-21
Sy = 0.9 * Sut
fa = fatigue()
Se = fa.enduranceLimitKpsi(Sut)

#tbl A-9
f_min = min_delta*3*E*I/l**3
f_max = max_delta*3*E*I/l**3
M_min = f_min * (l+r_bend/2)
M_max = f_max * (l+r_bend/2)

print 'Min latching force: ' + str(f_min) + ' N'
print 'Max latching force: ' + str(f_max) + ' N'

#curved beams in bending
r_c = r_bend+(t/2)
r_o = r_c+(t/2)
r_i = r_c-(t/2)
r_n = t/np.log(r_o/r_i)
e = r_c - r_n

#find stresses 
sigma_inner_min = f_min/A + (M_min*(r_n-r_i))/(A*e*r_i)
sigma_inner_max = f_max/A + (M_max*(r_n-r_i))/(A*e*r_i)
sigma_outer_min = f_min/A + (M_min*(r_n-r_o))/(A*e*r_o)
sigma_outer_max = f_max/A + (M_max*(r_n-r_o))/(A*e*r_o)

sigma_inner_mid = (sigma_inner_min + sigma_inner_max)/2
sigma_outer_mid = (sigma_outer_min + sigma_outer_max)/2

sigma_inner_amplitude = (sigma_inner_min - sigma_inner_max)/2
sigma_outer_amplitude = (sigma_outer_min - sigma_outer_max)/2

#convert to IP
sigma_inner_mid_ksi = sigma_inner_mid * 0.000145037738 / 1000
sigma_outer_mid_ksi = sigma_outer_mid * 0.000145037738 / 1000
sigma_inner_amplitude_ksi = sigma_inner_amplitude * 0.000145037738 / 1000
sigma_outer_amplitude_ksi = sigma_outer_amplitude * 0.000145037738 / 1000 


#plot
Sm = np.arange(-20, 300, 1)
a = fatigue()

plt.plot(
    Sm, a.gerber(Sm,Se,Sut), 'b-', 
    np.abs(sigma_outer_mid_ksi), np.abs(sigma_outer_amplitude_ksi), 'g^', 
    np.abs(sigma_inner_mid_ksi), np.abs(sigma_inner_amplitude_ksi), 'b^')
plt.title('Designer\'s Diagram')
plt.axis([0, 250, 0, 150])
plt.xlabel(r'$\sigma_m$',fontsize=20)
plt.ylabel(r'$\sigma_a$',fontsize=20)
plt.text(140, 80, 'Gerber Fatigue Curve', fontsize=15)
plt.annotate('Outer Edge, does not fail', xy=(np.abs(sigma_outer_mid_ksi), np.abs(sigma_outer_amplitude_ksi)))
plt.annotate('Inner Edge, does not fail', xy=(np.abs(sigma_inner_mid_ksi), np.abs(sigma_inner_amplitude_ksi)))
plt.show()