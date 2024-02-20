import matplotlib.pyplot as plt
import numpy as np
import sys
import math


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



##################################################################

def cs_sleptons_w_condition(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    msleptons = 100.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * msleptons * msleptons / wvalue**2.0 >= 0.0, 1.0 - 4.0 * msleptons * msleptons / wvalue**2.0, np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > msleptons, (2.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             (2.0 - beta**2.0 - (1.0 - beta**4.0)/(2.0 * beta) * np.log( (1.0 + beta)/(1.0 - beta)) ), 0.0) * 1e9

    return cs


##################################################################

def cs_sleptons_w(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    msleptons = 100.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise comparison
    beta = np.sqrt( 1.0 - 4.0 * msleptons * msleptons / wvalue**2.0 )

    # Element-wise calculation of cs
    cs = (2.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0* (beta) * \
             ( 2.0 - beta**2.0 - (1.0 - beta**4.0)/(2.0 * beta)*np.log((1.0 + beta)/(1.0 - beta)) ) * 1e9

    return cs

##################################################################

def cs_sleptons_w_old(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    msleptons = 100.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)
    # alpha2 = alpha * alpha

    if (1.0 - 4.0 * msleptons * msleptons / wvalue**2.0) >= 0.0:
        beta = np.sqrt(1.0 - 4.0 * msleptons * msleptons / wvalue**2.0)
    else:
        # Handle the case where the expression is negative (e.g., set beta to NaN)
        beta = np.nan

    if wvalue > msleptons:
        cs = (2.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             (2.0 - beta**2.0 - (1.0 - beta**4.0)/(2.0 * beta)*math.log((1.0 + beta)/(1.0 - beta))) * 1e9
    else:
        cs = 0.0

    return cs

##################################################################


"""
def cs_sleptons_w(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    msleptons = 10.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise comparison
    condition = (1.0 - 4.0 * msleptons * msleptons / wvalue) >= 0
    beta = np.sqrt(np.where(condition, 1.0 - 4.0 * msleptons * msleptons / wvalue, np.nan))

    # Element-wise calculation of cs
    cs = np.where(wvalue > msleptons, (4.0 * np.pi * alpha2 * hbarc2 ) / wvalue* (beta) * \
             (2.0 - beta**2.0 - (1-beta**4.0)/(2.0 * beta)*np.log((1.0+beta)/(1.0-beta))), 0.)

    return cs
"""


def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_sleptons_w_condition(wv[i])
        cs_1 = cs_sleptons_w_condition(wv[i + 1])
#        cs_0 = cs_sleptons_w(wv[i])
#        cs_1 = cs_sleptons_w(wv[i + 1])
#        cs_0 = cs_sleptons_w_old(wv[i])
#        cs_1 = cs_sleptons_w_old(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ   # * 1000000000.0



sys.path.append('./values')

from wgrid_1_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(100.0, 1000.0)
ax.set_ylim(1.0e-9, 1.0e3)



inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'tagged elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

#plt.grid()

plt.legend(title = title_label)

#plt.grid()





from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)







from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)







# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_sleptons.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')







font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]",  fontdict = font2)
plt.ylabel("$\sigma_{\widetilde{\ell}^+\widetilde{\ell}^-}$ (W > W$_0$) [pb]", fontdict = font2)



plt.savefig("cs_sleptons_MN2_mMin2_q2min_Final.pdf")
plt.savefig("cs_sleptons_MN2_mMin2_q2min_Final.jpg")



plt.show()





"""
from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv1[:202], int_inel[:202], '-', label = inel_label)
plt.legend(title = title_label)

from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv2[:202], int_inel[:202], '-', label = inel_label)
plt.legend(title = title_label)
"""


