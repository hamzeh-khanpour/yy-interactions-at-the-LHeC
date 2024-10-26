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




##################################################################

def cs_ttbar_w_condition_Hamzeh(wvalue):  # Eq.62 of Physics Reports 364 (2002) 359-450
    mtop = 172.50
    Qf = 2.0/3.0
    Nc = 3.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * mtop * mtop / wvalue**2.0 >= 0.0, 1.0 - 4.0 * mtop * mtop / wvalue**2.0, np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > mtop, ( 4.0 * np.pi * alpha2 * Qf**4.0 * Nc * hbarc2 ) / wvalue**2.0 * (beta) * \
             ( (3.0 - (beta**4.0))/(2.0 * beta) * np.log((1.0 + beta)/(1.0 - beta)) - 2.0 + beta**2.0 ), 0.0) * 1e9

    return cs

##################################################################




def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_ttbar_w_condition_Hamzeh(wv[i])
        cs_1 = cs_ttbar_w_condition_Hamzeh(wv[i + 1])
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

from wgrid_10_100000_10_FCC import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(350.0, 1000.0)
ax.set_ylim(1.e-6, 1.e-1)


inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'tagged elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

#plt.grid()

plt.legend(title = title_label)

#plt.grid()







from wgrid_50_100000_1000_FCC import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)










from wgrid_300_100000_100000_FCC import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)






# Add additional information
info_text = "FCC-he"
plt.text(0.67, 0.61, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=16, color='blue', fontweight='bold')

info_text_2 = r"$E_e$=60 GeV; $E_p$=50000 GeV"
plt.text(0.67, 0.55, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=16, color='blue', fontweight='bold')





# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value_Elastic_Inelastic'
np.savetxt('output_values_ttbar_FCC.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')







font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]", fontdict=font2)
plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma\to t \bar{t}){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]", fontdict = font2)




plt.savefig("cs_ttbar_FCC.pdf")
plt.savefig("cs_ttbar_FCC.jpg")



plt.show()




