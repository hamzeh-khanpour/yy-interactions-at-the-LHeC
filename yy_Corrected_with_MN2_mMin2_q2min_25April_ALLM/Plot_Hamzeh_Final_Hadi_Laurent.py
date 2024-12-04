
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




from wgrid_10_100000_10 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (8, 8))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-5, 1.0e1)




inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=3,  label = 'elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=3, label = inel_label)
#plt.grid()






from wgrid_50_100000_1000 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashed',  linewidth=3, label = inel_label)
plt.legend(title = title_label)







from wgrid_300_100000_100000 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=3, label = inel_label)
plt.legend(title = title_label)







# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_ntegrated_Syy.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')






#font1 = {'family':'serif','color':'black','size':24}
#font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]")
plt.ylabel("Integrated S$_{\gamma \gamma}$ (W > W$_0$)")




plt.savefig("yy_int_with_MN2_mMin2_q2min_Final_25April_Modified.pdf")
plt.savefig("yy_int_with_MN2_mMin2_q2min_Final_25April_Modified.jpg")




plt.show()



#===========================================================================

