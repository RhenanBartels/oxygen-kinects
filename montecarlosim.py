# _*_ coding: utf-8 _*_

import numpy as np
from scipy.optimize import leastsq
import time
import sys


def montecarlo(data, curve, x, P, model, itr):
    N = len(data)
    SS = sum(data - curve)**2
    gain = np.sqrt(SS / (N - P))
    curven = curve + gain * np.random.randn(len(curve))
    tau = []
    for Iter in xrange(itr):
        SS = sum(data - curve)**2
        gain = np.sqrt(SS / (N - P))
        curven = curve + gain * np.random.randn(len(curve))
        p0 = [min(curven), max(curven) - min(curven), 10]
        fit = leastsq(model, p0, args=(x, curven))
        tau.append(fit[0][-1])
    tau.sort()
    tRange = [int(0.25 * itr), -int(0.25 * itr)]
    return [tau[tRange[0]], tau[tRange[1]], tau]
