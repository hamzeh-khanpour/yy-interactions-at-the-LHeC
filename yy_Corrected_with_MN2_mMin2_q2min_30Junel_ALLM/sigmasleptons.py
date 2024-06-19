import numpy as np
import matplotlib.pyplot as plt
import math

# Generate x values from 0 to 2*pi
wvalue = np.linspace(10, 1000, 300)

def cs_DM_w(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mDM = 100.0
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise comparison
    condition = (1.0 - 4.0 * mDM * mDM / wvalue**2.0) >= 0.0
    beta = np.sqrt(np.where(condition, 1.0 - 4.0 * mDM * mDM / wvalue**2.0, np.nan))

    # Element-wise calculation of cs
    cs = np.where(wvalue > mDM, (4.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             (2.0 - beta**2.0 - (1.0-beta**4.0)/(2.0 * beta)*np.log((1.0+beta)/(1.0-beta))), 0.0)  * 1e9

    return cs

# Calculate y values using cs_DM_w function
y = cs_DM_w(wvalue)

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(wvalue, y)

ax.set_yscale("log")

# Customize the plot
ax.set_xlabel('W [GeV]')
ax.set_ylabel('$\sigma_{\gamma \gamma -> S^+ S^-}$ (pb)')
ax.set_title('$\sigma_{\gamma \gamma ->  S^+ S^-}$')

# Save the plot as a PDF file
# plt.savefig('cs_DM_w_plot.pdf')

# Show the plot
plt.show()
