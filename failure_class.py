import numpy as np
class failure:
    """Failure theory class - MSS and von Mises"""
    sigma_x = 0
    sigma_y = 0
    sigma_z = 0
    tau_xy = 0
    tau_yz = 0
    tau_zx = 0
    
    def mohrs_circle(self):
        a = np.array([[self.sigma_x, self.tau_xy, self.tau_zx],[self.tau_xy, self.sigma_y, self.tau_yz],[self.tau_zx, self.tau_yz, self.sigma_z]])
        eig = np.linalg.eigvals(a)
        return sorted(eig, reverse=True)
    def max_shear(self):
        a = self.mohrs_circle()
        return (a[0] - a[2])/2
    def von_mises(self):
        a = self.mohrs_circle()
        return np.sqrt((a[1]-a[0])**2+(a[2]-a[0])**2+(a[2]-a[1])**2)/np.sqrt(2)
        