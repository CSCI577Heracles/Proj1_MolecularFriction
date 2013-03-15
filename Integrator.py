import numpy as np


class Integrator(object):

    def __init__(self, dt, f):
        self.dt = dt
        self.f = f
        self.f.c.a = f.a()

    def integrate(self):
        self.f.c.p = self.f.c.p + self.f.c.v * self.dt + self.f.c.a * 0.5 * self.dt ** 2
        a_n = self.f.c.a.copy()
        self.f.c.a = self.f.a()
        self.f.c.v += (a_n + self.f.c.a) * self.dt * 0.5

