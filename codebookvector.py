import numpy as np
import math

class CodeBookVector(object):
    CONST_TMAX = 500.0

    def __init__(self, *args):

        self.x             = args[0]
        self.y             = args[1]
        self.t             = args[2]
        self.neighbourhood = args[3]
        self.learnrate     = args[4]
        self.order         = args[5]
        self.learning      = 1

    def eta(self,t): return 1-1*(t/self.CONST_TMAX)
    def lam(self,t): return self.neighbourhood - self.neighbourhood*(t/self.CONST_TMAX)

    def resetTime(self):
        self.t = 1
        self.learning = 1

    def changeOrder(self, i):
        self.order = i

    def learn(self,x,y):
        ETA = self.eta(self.t)
        self.x         = self.x + ETA*math.exp(-self.order/self.lam(self.t))*(x-self.x)
        self.y         = self.y + ETA*math.exp(-self.order/self.lam(self.t))*(y-self.y)
        self.learning  = self.learning + self.learnrate
        self.t         = self.CONST_TMAX * (1 - math.exp(-0.012*self.learning))
