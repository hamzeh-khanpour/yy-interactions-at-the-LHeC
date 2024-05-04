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

# Sigma_{gamma_gamma} for higgsinos


def cs_higgsinos_w_condition_Hamzeh(wvalue):  # Eq.62 of Physics Reports 364 (2002) 359-450
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mhiggsinos = 100.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * mhiggsinos * mhiggsinos / wvalue**2.0 >= 0.0, 1.0 - 4.0 * mhiggsinos * mhiggsinos / wvalue**2.0, np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > mhiggsinos, ( 4.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             ( (3.0 - (beta**4.0))/(2.0 * beta) * np.log((1.0 + beta)/(1.0 - beta)) - 2.0 + beta**2.0 ), 0.0) * 1e9 * 1.0

    return cs


##################################################################

def trap_integ(wv, fluxv):

    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        traparea = fluxv[i] * cs_higgsinos_w_condition_Hamzeh(wv[i])
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = traparea

    return wmin, integ







sys.path.append('./values')




from wgrid_10_100000_10 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(200.0, 500.0)
ax.set_ylim(1.0e-6, 1.0e-4)


inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)

#plt.grid()

plt.legend(title = title_label)

#plt.grid()


##################################################################


from wgrid_50_100000_1000 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wv2[:303], int_inel[:303], linestyle = 'dashdot',  linewidth=2, label = inel_label)
plt.legend(title = title_label)



##################################################################


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
np.savetxt('dSigmadW_ep_higgsinos.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')



##################################################################


# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('dSigmadW_ep_higgsinos_elastic_inelastic.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')




font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W [GeV]",  fontdict = font2)
plt.ylabel("$d\sigma/dW  (ep \\rightarrow e p higgsinos)$ [pb]", fontdict = font2)



plt.savefig("dSigmadW_ep_higgsinos_elastic_inelastic.pdf")
plt.savefig("dSigmadW_ep_higgsinos_elastic_inelastic.jpg")



##################################################################


# Call the function to debug
wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

# Print values for debugging
print("wv2[:303]:", wv2[:303])
print("int_el[:303]:", int_el[:303])
print("wv1[:303]:", wv1[:303])
print("int_inel[:303]:", int_inel[:303])


##################################################################



# Calculate and display the area under the curves
area_elastic = np.trapz(int_el[:303], wv2[:303])  # Trapezoidal rule for area under elastic curve
area_inelastic = np.trapz(int_inel[:303], wv1[:303])  # Trapezoidal rule for area under inelastic curve

print("Area under elastic curve:", area_elastic, "pb*GeV")
print("Area under inelastic curve:", area_inelastic, "pb*GeV")






plt.show()

