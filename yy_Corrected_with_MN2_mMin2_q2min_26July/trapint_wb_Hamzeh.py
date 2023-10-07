import matplotlib.pyplot as plt
import numpy as np
import sys



plt.rcParams["axes.linewidth"] = 1.8
plt.rcParams["xtick.major.width"] = 1.8
plt.rcParams["xtick.minor.width"] = 1.8
plt.rcParams["ytick.major.width"] = 1.8
plt.rcParams["ytick.minor.width"] = 1.8

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15

plt.rcParams["legend.fontsize"] = 15

plt.rcParams['legend.title_fontsize'] = 'x-large'




def cs_tautau_w(wvalue):
    re = 2.8179403262e-15 * 137. / 128.
    me = 0.510998950e-3
    mtau = 1.77686

    cs = 4. * np.pi * re * re * me * me / wvalue / wvalue \
         * (np.log(wvalue * wvalue / mtau / mtau) - 1)

    return cs


def cs_ww_w(wvalue):
    re = 2.8179403262e-15 * 137. / 128.
    me = 0.510998950e-3
    mw = 80.379

    if wvalue > 2. * mw:
        cs = 9. * np.pi * re * re * me * me / mw / mw \
             * np.sqrt(wvalue * wvalue - 4. * mw * mw) / wvalue
    elif wvalue > 300.:
        cs = 8. * np.pi * re * re * me * me / mw / mw
    else:
        cs = 0.

    return cs
    

def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    wmid = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
#        cs_0 = cs_tautau_w(wv[i])
#        cs_1 = cs_tautau_w(wv[i + 1])
        cs_0 = cs_ww_w(wv[i])
        cs_1 = cs_ww_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        wmid[i] = wv[i] + wvwid * 0.5
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmid, integ * nanobarn


sys.path.append('./values')

from wgrid_1_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9., 8.))
# ax.set_xlim(10., 1000.)
ax.set_xlim(161., 1000.)
ax.set_ylim(2.e-4, 1.e1)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:101], int_el[:101], linestyle = 'solid',  linewidth=2,  label = 'elastic')
plt.loglog(wv1[:101], int_inel[:101], linestyle = 'dotted',  linewidth=2, label = inel_label)


plt.legend(title = title_label)

#plt.grid()





from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:101], int_inel[:101], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)




font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]",  fontdict = font2)
plt.ylabel("$\sigma_{WW}$ (W > W$_0$) [pb]", fontdict = font2)


plt.savefig("cs_WW_MN2_mMin2_q2min_Final.pdf")
plt.savefig("cs_WW_MN2_mMin2_q2min_Final.jpg")


plt.show()





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



