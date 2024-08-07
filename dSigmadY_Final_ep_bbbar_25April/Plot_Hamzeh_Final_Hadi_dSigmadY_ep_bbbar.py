
# Final Version -- Febraury 2024 -- Hamzeh Khanpour

# ================================================================================

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
# from syy_1_3_3_0804 import *
# from syy_1_3_4_0805 import *
# from syy_1_4_4_0907 import *

from dSigmadY_ep_bbbar_10_100000_10_tagged_elastic import *


fig, ax = plt.subplots(figsize = (11.0, 9.0))
ax.set_xlim(0.0, 5.0)
ax.set_ylim(0.0001, 0.002)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.plot(wvalues[3][:303], elas[3][:303], linestyle = 'dashed',  linewidth=2, color='blue', label = 'tagged elastic')
plt.plot(wvalues[3][:303], inel[3][:303], linestyle = 'dashdot', linewidth=2, color='red', label = inel_label)
#plt.grid()
plt.legend(title = title_label)



# Add additional information
info_text = "$ep \\rightarrow e (\gamma\gamma \\to b \\bar{b}) p^*$"
plt.text(0.2, 0.90, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=25, color='black')

#info_text_2 = "$M_{higgsinos}$ = 100 GeV"
#plt.text(0.2, 0.85, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=20, color='black')


# Setting y-axis to log scale
#plt.yscale('log')

# Set label colors
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')

# Add legend with specified colors
legend = plt.legend(title = title_label)
legend.get_texts()[0].set_color("blue")  # Color for 'elastic'
legend.get_texts()[1].set_color("red")   # Color for inel_label



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("$Y_{b \\bar{b}}$",  fontdict = font2)
plt.ylabel("$d\sigma/dY_{b \\bar{b}}$ [pb]", fontdict = font2)


plt.savefig("dSigmadY_ep_bbbar_25April.pdf")
plt.savefig("dSigmadY_ep_bbbar_25April.jpg")

plt.show()



# ================================================================================


