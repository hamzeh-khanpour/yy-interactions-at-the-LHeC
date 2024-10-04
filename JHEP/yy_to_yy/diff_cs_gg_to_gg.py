import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import ggMatrixElements  # Import the photon-photon matrix element module

# Constants
alpha = 1 / 137  # Fine-structure constant
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
    return sqme / (16 * np.pi * s**2)  # The prefactor for 2-to-2 scattering

# Total cross-section for gamma-gamma -> gamma-gamma as a function of W
def cs_gg_to_gg_w(W):
    s = W**2  # s = W^2
    t_min_value = t_min(W)
    t_max_value = t_max(W)

    # Numerical integration over t
    def integrand(t, s):
        return diff_cs_gg_to_gg(s, t)

    result, _ = quad(integrand, t_min_value, t_max_value, args=(s,))
    return result * hbarc2  # Convert to pb

# Generate W values on a logarithmic scale from 10^-4 to 1000 GeV
W_values = np.logspace(-4, 3, 100)  # Photon-photon CM energy in GeV

# Compute the cross-section for each W
cross_sections = [cs_gg_to_gg_w(W) for W in W_values]

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(W_values, cross_sections, 'b-', label=r'$\sigma(\gamma\gamma \to \gamma\gamma)$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\sqrt{s}$ (GeV)')
plt.ylabel(r'$\sigma_{\gamma\gamma \to \gamma\gamma}$ (pb)')
plt.title(r'$\gamma\gamma \to \gamma\gamma$ Cross Section as a function of $\sqrt{s}$')
plt.grid(True)
plt.legend()
plt.show()
