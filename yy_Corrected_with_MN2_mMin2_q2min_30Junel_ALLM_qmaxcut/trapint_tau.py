import matplotlib.pyplot as plt
import numpy as np
import sys

def cs_tautau_w(wvalue):
    re = 2.8179403262e-15 * 137. / 128.
    me = 0.510998950e-3
    mtau = 1.77686

    cs = 4. * np.pi * re * re * me * me / wvalue / wvalue \
         * (np.log(wvalue * wvalue / mtau / mtau) - 1)

    return cs
    

def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_tautau_w(wv[i])
        cs_1 = cs_tautau_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ * nanobarn


sys.path.append('./values')

from wgrid_15_3_3_1018 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9., 8.))
ax.set_xlim(10., 1000.)
ax.set_ylim(1.e-3, 1.e2)

inel_label = 'M_N < ' + str(inel[0]) + 'GeV'
title_label = 'Q2e/p < ' + str(inel[1]) + '/' + str(inel[2]) + 'GeV^2'
plt.loglog(wv2[:101], int_el[:101], 'b-', label = 'elastic')
plt.loglog(wv1[:101], int_inel[:101], '-', label = inel_label)
plt.legend(title = title_label)
plt.grid()

"""
from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv1[:101], int_inel[:101], '-', label = inel_label)
plt.legend(title = title_label)

from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv2[:101], int_inel[:101], '-', label = inel_label)
plt.legend(title = title_label)
"""

plt.show()
