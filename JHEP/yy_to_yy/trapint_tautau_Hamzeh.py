
#      Hamzeh & Laurent  --- 1 October 2024

import matplotlib.pyplot as plt
import numpy as np
import sys


import ggMatrixElements
print(ggMatrixElements.sqme_sm(0.1, -0.1, False))  # s, t, exclude_SM_loops



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

def cs_tautau_w_condition_Hamzeh(wvalue):     # Eq.62 of Physics Reports 364 (2002) 359-450     Sigma [yy -> yy]  (W)
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mtau = 1.77686
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * mtau * mtau / wvalue**2.0 >= 0.0, 1.0 - 4.0 * mtau * mtau / wvalue**2.0, np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > mtau, ( 4.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             ( (3.0 - (beta**4.0))/(2.0 * beta) * np.log((1.0 + beta)/(1.0 - beta)) - 2.0 + beta**2.0 ), 0.0) * 1e9

    return cs


##################################################################



def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_tautau_w_condition_Hamzeh(wv[i])
        cs_1 = cs_tautau_w_condition_Hamzeh(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ  # * nanobarn


##################################################################


sys.path.append('./values')

from wgrid_10_100000_10 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-3, 10.e2)


inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'tagged elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

plt.grid()

plt.legend(title = title_label)



# Save the output values in a text file
#output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
#header = 'W_Value Elastic Inelastic'
#np.savetxt('output_values_tau.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')




font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]", fontdict=font2)
#plt.ylabel("$\sigma_{\\tau^+\\tau^-}$ (W > W$_0$) [pb]", fontdict=font2)
plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma\to\tau^+\tau^-){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]", fontdict = font2)




plt.savefig("cs_yy_yy.pdf")
#plt.savefig("cs_yy_yy.jpg")



plt.show()
