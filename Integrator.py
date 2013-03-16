import numpy as np


class Integrator(object):

    def __init__(self, dt, f):
        self.dt = dt
        self.f = f
        self.f.c.a = f.a(0.)
        #self.c.springMatrix = self.c.d()*self.c.sledMatrix

    def integrate(self, t):    # TODO: force will need time parameter
        self.f.c.p = self.f.c.p + self.f.c.v * self.dt + self.f.c.a * 0.5 * self.dt ** 2
        a_n = self.f.c.a.copy()
        self.f.c.a = self.f.a(t)
        self.f.c.v += (a_n + self.f.c.a) * self.dt * 0.5

    def cheat_i(self):
        pass

