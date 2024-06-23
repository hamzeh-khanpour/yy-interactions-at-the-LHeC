import matplotlib.pyplot as plt
import numpy as np
import sys


plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams["xtick.major.width"] = 1.5
plt.rcParams["xtick.minor.width"] = 1.5
plt.rcParams["ytick.major.width"] = 1.5
plt.rcParams["ytick.minor.width"] = 1.5

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

plt.rcParams["legend.fontsize"] = 12

plt.rcParams['legend.title_fontsize'] = 'x-large'


def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)
    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        traparea = wvwid * 0.5 * (fluxv[i] + fluxv[i + 1])
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    return wmin, integ


sys.path.append('./values')

from wgrid_1_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9., 8.))
ax.set_xlim(10., 1000.)
ax.set_ylim(1.e-5, 1.5e-1)

inel_label = 'M$_N$ < ' + str(inel[0]) + ' GeV'
title_label = 'Q$^2$ (e/p) < ' + str(inel[1]) + '/' + str(inel[2]) + ' GeV$^2$'
plt.loglog(wv2[:101], int_el[:101], linestyle = 'solid',  linewidth=2,  label = 'elastic')
plt.loglog(wv1[:101], int_inel[:101], linestyle = 'dotted',  linewidth=2, label = inel_label)
#plt.grid()

from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M$_N$ < ' + str(inel[0])  + ' GeV'
plt.loglog(wv1[:101], int_inel[:101], linestyle = 'dashed',  linewidth=2, label = inel_label)
plt.legend(title = title_label)

from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M$_N$ < ' + str(inel[0])  + ' GeV'
plt.loglog(wv2[:101], int_inel[:101], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)


font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'black','size':20}

plt.xlabel("W$_0$ [GeV]",  fontdict = font2)
plt.ylabel("Integrated S$_{\gamma \gamma}$ (W > W$_0$) [GeV]", fontdict = font2)

plt.savefig("syy_int_with_MN2_mMin2_Final.pdf")


plt.show()
