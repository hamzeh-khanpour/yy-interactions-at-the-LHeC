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


####################################################################

def cs_higgs_w_condition(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    MH = 125.0
    G = 4.2e-3
    Gyy = (2.27e-3)*(4.2e-3)
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Use np.greater for element-wise comparison
    condition = np.greater(wvalue, MH)
    cs = np.where(condition, (8.0 * np.pi * np.pi * hbarc2) * (Gyy / MH) * (1.0 / np.pi) *
                  ((MH * G) / ((MH * MH - wvalue * wvalue)*(MH * MH - wvalue * wvalue) + MH * MH * G * G)) * 1e9, 0.0)

    return cs

####################################################################

def cs_higgs_w(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    MH = 125.0
    G = 4.2e-3
    Gyy = (2.27e-3)*(4.2e-3)
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    cs = (8.0 * np.pi * np.pi* hbarc2 ) * (Gyy / MH)* (1.0/ np.pi) * \
         ( (MH *G)/((MH*MH - wvalue*wvalue)*(MH*MH-wvalue*wvalue) + MH*MH*G*G)) * 1e9

    return cs

####################################################################

# Function to calculate cross-section
def higgs_cross_section_final(wvalue):

    # Constants
    M_H = 125.0  # Higgs mass in GeV
    Gamma = 4.07e-3  # Total width
    Gamma_gamma = (2.27e-3)*(Gamma)  # Two-photon width
    hbarc2 =  0.389

    cs = 4.0 * np.pi ** 2.0 * Gamma_gamma * hbarc2 / M_H**2.0  * 1e9

    return cs


####################################################################



    
def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = higgs_cross_section_final(wv[i])
        cs_1 = higgs_cross_section_final(wv[i + 1])
#        cs_0 = cs_higgs_w(wv[i])
#        cs_1 = cs_higgs_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ  # * 1000000000.0


sys.path.append('./values')




from wgrid_10_100000_10 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(100.0, 1000.0)
ax.set_ylim(1.e-8, 1.e1)


inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

#plt.grid()

plt.legend(title = title_label)

#plt.grid()





from wgrid_50_100000_1000 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)






from wgrid_300_100000_100000 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)





# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_Higgs.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')





font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]",  fontdict = font2)
plt.ylabel("$\sigma_{higgs}$ (W > W$_0$) [pb]", fontdict = font2)



plt.savefig("cs_Higgs_MN2_mMin2_q2min_Final_20April.pdf")
plt.savefig("cs_Higgs_MN2_mMin2_q2min_Final_20April.jpg")



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


