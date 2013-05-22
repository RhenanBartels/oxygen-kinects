# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from _excel_python_slice_2 import open_by_range
import xlwt

plt.switch_backend('qt4Agg')
plt.ion()
data = open_by_range('Pplatratado.xls', 'Ppla', 'R1:R536')
time = np.arange(0, len(data))
#plt.plot(time, data)


def model1(par, time, data):
    err = data - (par[0] + par[1] * np.exp(-time / par[2]))
    return err


def model2(par, time, data):
    err = data - (par[0] + par[1] * np.exp(-(time - par[2]) / par[3]) +
                  par[4] * np.exp(-(time - par[5]) / par[6]))
    return err


def model3(par, time, data):
    err = data - (par[0] + par[1] * np.exp(-time / par[2]) * np.sinh(par[3] * time))
    return err

def curveeval(par, time, fn_type='mono'):
    if fn_type == 'mono':
        return par[0] + par[1] * np.exp(-time / par[2])
    elif fn_type == 'bi':
        return par[0] + par[1] * np.exp(-(time - par[2]) / par[3]) + par[4] *\
                                        np.exp(-(time - par[5]) / par[6])
    else:
        return par[0] + par[1] * np.exp(-time / par[2]) * np.sinh(par[3] * time)

OW = xlwt.Workbook()
S = OW.add_sheet('Plan1')

p0Mono = [min(data), max(data) - min(data), 0.36 * (max(data) - min(data))]
p0bi = [min(data), 0.2 * (max(data) - min(data)), 10, 0.36 * (max(data) - min(data)),
        0.8 * (max(data) - min(data)), 20,0.36 * (max(data) - min(data))]
p0Sinh  = [min(data), max(data) - min(data), 1, 1]

P = int((time[-1] - 30) / 30) + 1

start = 0;
stop = 30;
tau = []
ind1 = np.where(time >= start)[0][0]

for iterator in xrange(P):
    ind2 = np.where(time >= stop)[0][0]
    data_temp = data[ind1:ind2]
    time_temp = time[ind1:ind2]
    p0 = [min(data_temp), max(data_temp) - min(data_temp), 0.36 * max(data_temp)]
    reg = leastsq(model1,p0, args=(time_temp, data_temp))
    S.write(iterator, 0, reg[0][-1])
    tau.append(reg[0][-1])
    stop += 30
OW.save('R9.xls')
index = np.arange(len(tau)) * 30 + 30
plt.plot(index, tau, 'k.-')
plt.xlabel('Tempo (s)')
plt.ylabel('Tau (s)')
plt.ylim([0, 60])
