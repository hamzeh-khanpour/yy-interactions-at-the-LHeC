
#   \gamma\gamma \to \gamma\gamma (W)  [pb]
#   Hamzeh Khanpour --- October 2024
#   Photon-photon cross-section σ(γγ→γγ) using the matrix element by Laurent

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

import matplotlib.ticker as ticker

import ggMatrixElements  # Import the photon-photon matrix element module


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


# Generate W values on a logarithmic scale from 10^-4 to 1000 GeV
W_values = np.logspace(-4, 3, 100)  # Photon-photon CM energy in GeV


# Compute the cross-section for each W
cross_sections = [cs_gg_to_gg_w(W) for W in W_values]


# Plotting the results
fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(1.0e-4, 1000.0)
#ax.set_ylim(1.0e-3, 1.0e7)


# Set major and minor ticks for the y-axis and x-axis
ax.set_yticks([1.e-3, 1.e-2, 1.e-1, 1.e0, 1.e1, 1.e2, 1.e3, 1.e4, 1.e5, 1.e6, 1.e7])
ax.set_xticks([1.e-4, 1.e-3, 1.e-2, 1.e-1, 1.e0, 1.e1, 1.e2, 1.e3])


# Define minor ticks explicitly
ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=np.arange(1, 10) * 0.1, numticks=10))
ax.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=np.arange(1, 10) * 0.1, numticks=10))


# Set formatters to ensure no scientific notation for ticks
ax.get_yaxis().set_major_formatter(plt.ScalarFormatter())
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())


# Enable minor ticks
ax.minorticks_on()
ax.tick_params(which='both', direction='in', right=True, top=True)



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}


plt.plot(W_values, cross_sections, 'b-', label=r'$\sigma(\gamma\gamma \to \gamma\gamma) [W]$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\sqrt{s}=W_{\gamma\gamma}$ (GeV)', fontdict=font2)
plt.ylabel(r'$\sigma_{\gamma\gamma \to \gamma\gamma} (W)$ (pb)', fontdict=font2)
plt.title(r'$\sigma_{\gamma\gamma \to \gamma\gamma}$ as a function of $\sqrt{s}=W_{\gamma\gamma}$', fontdict=font2)

plt.grid(True)
plt.legend()




plt.savefig("cs_yy_yy.pdf")

plt.show()

######################################################################3
