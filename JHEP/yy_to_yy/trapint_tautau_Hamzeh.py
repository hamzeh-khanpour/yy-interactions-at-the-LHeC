#      Hamzeh & Laurent  --- 1 October 2024

import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.integrate import quad  # Import quad for numerical integration
import ggMatrixElements  # Import your photon-photon matrix element module

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
# Photon-photon cross-section σ(γγ→γγ) using the matrix element
def cs_gg_to_gg_w(wvalue):
    alpha = 1 / 137  # Fine-structure constant
    t_min = -wvalue**2  # Define integration limits for t (Mandelstam variable)
    t_max = 0

    # Photon-photon cross-section integrand (using squared matrix element)
    def integrand(t, s):
        return ggMatrixElements.sqme_sm(s, t, False)  # Call SM matrix element

    # Perform numerical integration over t to get the total cross-section
    s = wvalue**2  # Mandelstam variable s = W^2
    result, _ = quad(lambda t: integrand(t, s), t_min, t_max)  # Pass s as a fixed argument using lambda
    return result / (16 * np.pi * s**2) * 1e9  # Convert to picobarns (pb)


##################################################################

def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_gg_to_gg_w(wv[i])  # Use the photon-photon cross section here
        cs_1 = cs_gg_to_gg_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40
    return wmin, integ  # Return the integrated cross section


##################################################################

sys.path.append('./values')

from wgrid_10_100000_10 import *  # Importing W grid and photon flux values

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
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_gg.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')




font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]", fontdict=font2)
plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma\to\gamma\gamma){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]", fontdict = font2)




plt.savefig("cs_yy_yy.pdf")
plt.show()
