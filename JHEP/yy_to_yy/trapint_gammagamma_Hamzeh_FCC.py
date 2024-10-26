
#   ep -> e (\gamma\gamma) p [pb]   FCC-eh
#   Hamzeh Khanpour --- October 2024
#   Light by light scattering at the LHeC using the matrix element by Laurent


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

# Constants
alpha  = 1 / 137  # Fine-structure constant
hbarc2 = 0.389  # Conversion factor to pb

# Mandelstam variables
def t_min(W):
    return -W**2

def t_max(W):
    return 0


# Differential cross-section for gamma-gamma -> gamma-gamma using ggMatrixElements
def diff_cs_gg_to_gg(s, t):
    # Calculate the squared matrix element using ggMatrixElements
    sqme = ggMatrixElements.sqme_sm(s, t, False)  # s, t, exclude loops = False
    return sqme / (16. * np.pi * s**2.)  # The prefactor for 2-to-2 scattering



# Total cross-section for gamma-gamma -> gamma-gamma as a function of W
def cs_gg_to_gg_w(W):
    s = W**2.                # s = W^2
    t_min_value = t_min(W)
    t_max_value = t_max(W)



# Numerical integration over t
    def integrand(t, s):
        return diff_cs_gg_to_gg(s, t)

    result, _ = quad(integrand, t_min_value, t_max_value, args=(s,))
    return result * hbarc2 * 1e9  # Convert to pb


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


from wgrid_10_100000_10_FCC import *  # Importing W grid and photon flux values

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-6, 1.e0)



# Set formatters to ensure no scientific notation for ticks
ax.get_yaxis().set_major_formatter(plt.ScalarFormatter())
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())


# Enable minor ticks
ax.minorticks_on()
ax.tick_params(which='both', direction='in', right=True, top=True)




inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wv2[:303], int_el[:303], linestyle = 'solid',  linewidth=2,  label = 'elastic')
plt.loglog(wv1[:303], int_inel[:303], linestyle = 'dotted',  linewidth=2, label = inel_label)







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


#plt.grid()

plt.legend(title = title_label)








# Add additional information
info_text = "FCC-he"
plt.text(0.67, 0.61, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=16, color='blue', fontweight='bold')

info_text_2 = r"$E_e$=60 GeV; $E_p$=50000 GeV"
plt.text(0.67, 0.55, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=16, color='blue', fontweight='bold')






# Save the output values in a text file
output_data = np.column_stack((wv2[:303], int_el[:303], int_inel[:303]))
header = 'W_Value_Elastic_Inelastic'
np.savetxt('output_values_ep_epgg_FCC.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}

plt.xlabel("W$_0$ [GeV]", fontdict=font2)
plt.ylabel(r"$\sigma_{{\rm ep}\to {\rm e}(\gamma\gamma\to\gamma\gamma){\rm p}^{(\ast)}}$ (W > W$_0$) [pb]", fontdict = font2)


plt.savefig("cs_ep_yy_yy_FCC.pdf")     # Light by light scattering at the LHeC

plt.show()


##################################################################

