import numpy as np
import matplotlib.pyplot as plt
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

sys.path.append('./values')

from dSigmadY_10_100000_10_higgsinos_MN10_tagged_elastic_m100GeV import *

fig, ax = plt.subplots(figsize=(11.0, 9.0))
ax.set_xlim(0.0, 5.0)
ax.set_ylim(0.0001, 0.001)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10, np.log10(inel[1]))

# Plot elastic and inelastic cross-sections
elastic_plot, = plt.plot(wvalues[3][:202], elas[3][:202], linestyle='dashed', linewidth=2, color='blue', label='tagged elastic')
inelastic_plot, = plt.plot(wvalues[3][:202], inel[3][:202], linestyle='dashdot', linewidth=2, color='red', label=inel_label)

# Calculate the area under the plots
area_elastic = np.trapz(elas[3][:202], wvalues[3][:202])
area_inelastic = np.trapz(inel[3][:202], wvalues[3][:202])

print("Area under elastic plot:", area_elastic)
print("Area under inelastic plot:", area_inelastic)

# Add legend with specified colors
legend = plt.legend(handles=[elastic_plot, inelastic_plot], title=title_label)

# Add additional information
info_text = "LHeC"
plt.text(0.2, 0.90, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=20, color='black')

info_text_2 = "$M_{higgsinos}$ = 100 GeV"
plt.text(0.2, 0.85, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=20, color='black')

# Set label colors
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')

# Set axis labels
plt.xlabel("$Y_{higgsinos}$", fontdict={'family': 'serif', 'color': 'black', 'size': 24})
plt.ylabel("$d\sigma/dY_{higgsinos}$ [pb]", fontdict={'family': 'serif', 'color': 'black', 'size': 24})

# Save the plot
plt.savefig("dSigmadY_higgsinos100GeV_25April_m100GeV.pdf")
plt.savefig("dSigmadY_higgsinos100GeV_25April_m100GeV.jpg")

# Show the plot
plt.show()
