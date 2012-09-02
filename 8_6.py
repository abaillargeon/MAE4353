import numpy as np
from failure_class import *
from power_screw_class import *

#givens
load = 5000 #lbf
d = 2 #in
pitch = .25 #in
fs = 0.05
fc = 0.08
dc = 3.5 #in
speed_ratio = 60
eta = 0.95
omega_motor = 1720 * np.pi * 2 #rad/min

#calculations
#a. (rev/s * in/rev)
press_speed = omega_motor/speed_ratio/2/np.pi*pitch
print 'a. '+str(press_speed)+'in/min'

#b. assume max power needed to raise screws
p = power_screw()
p.type = 'ACME'
power = 2 * p.torque_raise(load,fs,d,pitch,dc,fc) * omega_motor / (speed_ratio*eta) / 60
hp = power/12/550
print 'b. '+str(hp)+' HP'