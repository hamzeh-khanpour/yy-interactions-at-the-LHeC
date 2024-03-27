import matplotlib.pyplot as plt
import numpy as np
import sys

# Function for Monte Carlo integration
def monte_carlo_integ(func, x_min, x_max, num_samples=10000):
    x_samples = np.random.uniform(x_min, x_max, num_samples)
    y_samples = func(x_samples)
    integral = np.mean(y_samples) * (x_max - x_min)
    return integral

# Cross-section function
def cs_electron_w_condition_Hamzeh(wvalue):  # Eq.62 of Physics Reports 364 (2002) 359-450
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

# Trap integration function (updated to use Monte Carlo integration)
def trap_integ(wv, fluxv):
    # Function to integrate
    def integrand(w):
        cs = cs_electron_w_condition_Hamzeh(w)
        return np.interp(w, wv, fluxv) * cs

    # Perform Monte Carlo integration
    integral = monte_carlo_integ(integrand, np.min(wv), np.max(wv))
    return integral

# Plotting code (unchanged)
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

# Define cross-section data and perform integration
sys.path.append('./values')
from EPA_ALLM_sf import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

int_inel = trap_integ(wv, ie)
int_el = trap_integ(wv, el)

# Plotting
fig, ax = plt.subplots(figsize=(9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-3, 10.e2)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10, np.log10(inel[1]))
plt.loglog(wv[:101], int_el[:101], linestyle='solid', linewidth=2, label='tagged elastic')
plt.loglog(wv[:101], int_inel[:101], linestyle='dotted', linewidth=2, label=inel_label)
plt.legend(title=title_label)
plt.xlabel("W$_0$ [GeV]")
plt.ylabel("$\sigma_{\\tau^+\\tau^-}$ (W > W$_0$) [pb]")
plt.savefig("cs_tautau_MN2_mMin2_q2min_Final.pdf")
plt.savefig("cs_tautau_MN2_mMin2_q2min_Final.jpg")
plt.show()
