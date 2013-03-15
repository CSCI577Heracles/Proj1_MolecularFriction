import numpy as np
import math


class Force(object):

    def __init__(self, c):
        self.c = c

    def pe(self):
        eps = 1.
        sig = 1.

        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()

        r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)

        rgBuild = (4 * eps) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        rgBuild = np.nan_to_num(rgBuild)
        #print "rgBuild:"
        #print np.sum(rgBuild)
        #print "-------------------"
        return np.sum(rgBuild)

    def ke(self):
        d = 2.
        N = np.size(self.c.x)
        vx = self.c.vx.copy()
        vy = self.c.vy.copy()
        vz = self.c.vz.copy()
        return 1 / ((N - 1) * d) * sum(vx ** 2 + vy ** 2 + vz ** 2)

    def pressure(self):
        ps = 1.
        sig = 1.
        eps = 1.
        d = 2.
        N = np.size(self.c.x)
        
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()
        
        r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        
        px = dx * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        px = np.nan_to_num(px)
        px = np.triu(px)
        py = dy * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        py = np.nan_to_num(py)
        py = np.triu(py)
        pz = dz * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        pz = np.nan_to_num(pz)
        pz = np.triu(pz)
        pt = px + py + pz
        return 1 / (d * N * self.ke()) * np.sum(pt)

    def a(self, eps=1., sig=1.):

        d = self.c.d()
        m = self.c.m.copy()

        dr = self.c.dr()

        r_hat = d / dr

        f = r_hat * (24 * eps) / dr * (2 * (sig / dr) ** 12 - (sig / dr) ** 6)
        f = self.c.vRmNan(-f)
        return np.sum(f, axis=1)


