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



def cs_zz_w(wvalue):

    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mZ = 91.186

    alpha = 1.0/137.0
    hbarc =  197.327
    hbarc2 =  0.389
    convert =  1.0 # hbarc2 * alpha * alpha * 1000000000.0

    if wvalue > 2.0 * mZ:
 #       cs = re * re * me * me * 0.279061 * ( 1.0 - 8315.07/(wvalue*wvalue) )**12.9722
        cs = convert * 0.25786903395035327/ \
            (1.0 + 5.749069613832837e11/wvalue**6.0 + 6.914037195922673e7/wvalue**4.0 +
            23.264122861948383/wvalue**2.0)**44.05927999125431
    else:
        cs = 0.0
    return cs



def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_zz_w(wv[i])
        cs_1 = cs_zz_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ # * nanobarn


sys.path.append('./values')



from wgrid_10_100000_10_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(200.0, 1000.0)
ax.set_ylim(1.e-6, 1.e-3)


inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'tagged elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

#plt.grid()

plt.legend(title = title_label)

#plt.grid()





from wgrid_50_100000_1000_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)










from wgrid_300_100000_100000_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)






# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_ZZ.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')





font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]",  fontdict = font2)
plt.ylabel("$\sigma_{ZZ}$ (W > W$_0$) [pb]", fontdict = font2)



plt.savefig("cs_zz_MN2_mMin2_q2min_Final_20April.pdf")
plt.savefig("cs_zz_MN2_mMin2_q2min_Final_20April.jpg")



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


