
# Final Version -- December 2024 -- Hamzeh Khanpour

# ================================================================================


import mplhep as hep
import numpy as np
import matplotlib.pyplot as plt
import sys

hep.style.use("CMS")
#plt.style.use(hep.style.ROOT)


'''plt.rcParams["axes.linewidth"] = 1.8
plt.rcParams["xtick.major.width"] = 1.8
plt.rcParams["xtick.minor.width"] = 1.8
plt.rcParams["ytick.major.width"] = 1.8
plt.rcParams["ytick.minor.width"] = 1.8

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15

plt.rcParams["legend.fontsize"] = 15

plt.rcParams['legend.title_fontsize'] = 'x-large' '''


def cs_ww_w(wvalue):

    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mw = 80.379
    hbarc2 =  0.389
    alpha2 = (1.0/128.0)*(1.0/128.0)

    #if wvalue > 2.0 * mw:
        #cs = (19.0/2.0) * np.pi * re * re * me * me / mw / mw \
             #* np.sqrt(wvalue * wvalue - 4.0 * mw * mw) / wvalue
    #elif wvalue > 300.0:
        #cs = 8.0 * np.pi * re * re * me * me / mw / mw
    #else:
        #cs = 0.0

    if wvalue > 2.0 * mw:
        cs = (19.0/2.0) * np.pi * hbarc2 * alpha2  / mw / mw \
             * np.sqrt(wvalue * wvalue - 4.0 * mw * mw) / wvalue         * 1e9
    elif wvalue > 300.0:
        cs = 8.0 * np.pi * hbarc2 * alpha2  / mw / mw                    * 1e9
    else:
        cs = 0.0

    return cs




def cs_ww_w_PR364(wvalue):

    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mw = 80.379
    hbarc2 =  0.389
    alpha2 = (1.0/128.0)*(1.0/128.0)

    beta = np.sqrt(np.where(1.0 - 4.0 * mw * mw / wvalue**2.0 >= 0, 1.0 - 4.0 * mw * mw / wvalue**2.0, np.nan))

    cs = np.pi * hbarc2 * alpha2 / wvalue**2.0 * beta * \
         ( -3.0 * (1.0 - beta**4.0)/beta * np.log((1.0 + beta)/(1.0 - beta)) + \
           2.0* (22.0 - 9.0 * beta**2.0 + 3.0*beta**4.0)/(1.0 - beta**2.0) )*1e9

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

    return wmid, integ  # * nanobarn


sys.path.append('./values')





from wgrid_10_100000_10_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (8, 8))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)
# ax.set_xlim(10., 1000.)
ax.set_xlim(161.0, 1000.0)
ax.set_ylim(1.0e-4, 1.0e1)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=3,  label = 'tagged elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=3, label = inel_label)


plt.legend(title = title_label)

#plt.grid()





from wgrid_50_100000_1000_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=3, label = inel_label)
plt.legend(title = title_label)








from wgrid_300_100000_100000_elastic_tagged import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=3, label = inel_label)
plt.legend(title = title_label)





# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_WW.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')





font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]")
plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma \to W^+W^-){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]")

# plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma\to\tau^+\tau^-){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]", fontdict = font2)



plt.savefig("cs_WW_MN2_mMin2_q2min_Final_25April.pdf")
plt.savefig("cs_WW_MN2_mMin2_q2min_Final_25April.jpg")


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



