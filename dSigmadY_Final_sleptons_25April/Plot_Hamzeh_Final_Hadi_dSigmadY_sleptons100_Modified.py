
# Final Version -- Febraury 2024 -- Hamzeh Khanpour

# ================================================================================

import mplhep as hep
import numpy as np
import matplotlib.pyplot as plt
import sys

hep.style.use("CMS")
#plt.style.use(hep.style.ROOT)


import matplotlib.ticker as mticker



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



sys.path.append('./values')
# from syy_1_3_3_0804 import *
# from syy_1_3_4_0805 import *
# from syy_1_4_4_0907 import *

from dSigmadY_sleptons_10_100000_10_tagged_elastic_m100GeV import *


fig, ax = plt.subplots(figsize = (8.0, 8.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)


ax.set_xlim(0.0, 5.0)
ax.set_ylim(0.02, 0.2)





# Set y-axis to scientific format
formatter = mticker.ScalarFormatter(useMathText=True)
formatter.set_powerlimits((-2, 2))
ax.yaxis.set_major_formatter(formatter)




inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.plot(wvalues[3][:202], [value * 1000 for value in elas[3][:202]], linestyle = 'dashed',  linewidth=3, color='blue', label = 'tagged elastic')
plt.plot(wvalues[3][:202], [value * 1000 for value in inel[3][:202]], linestyle = 'dashdot', linewidth=3, color='red', label = inel_label)
#plt.grid()
plt.legend(title = title_label)



# Add additional information
info_text = "$ep \\rightarrow e (\gamma\gamma \\to \widetilde{\ell}^+ \widetilde{\ell}^-) p^*$"
plt.text(0.650, 0.650, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=25, color='black')

info_text_2 = "$M_{\widetilde{\ell}}$ = 100 GeV"
plt.text(0.650, 0.550, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=25, color='black')



# Setting y-axis to log scale
# plt.yscale('log')




# Set label colors
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')

# Add legend with specified colors
legend = plt.legend(title = title_label)
legend.get_texts()[0].set_color("blue")  # Color for 'elastic'
legend.get_texts()[1].set_color("red")   # Color for inel_label



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("$Y_{\widetilde{\ell}^+ \widetilde{\ell}^-}$")
plt.ylabel("$d\sigma/dY_{\widetilde{\ell}^+ \widetilde{\ell}^-}$ [fb]")


plt.savefig("dSigmadY_sleptons100GeV_MN100_25April_m100GeV_Modified.pdf")
plt.savefig("dSigmadY_sleptons100GeV_MN100_25April_m100GeV_Modified.jpg")

plt.show()



# ================================================================================


