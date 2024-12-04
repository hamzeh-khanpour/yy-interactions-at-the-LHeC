
# Final Version -- Febraury 2024 -- Hamzeh Khanpour

# ================================================================================

import mplhep as hep
import numpy as np
import matplotlib.pyplot as plt
import sys

hep.style.use("CMS")
#plt.style.use(hep.style.ROOT)

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
from dSigmadY_pp_bbbar import *


fig, ax = plt.subplots(figsize = (8.0, 8.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)


ax.set_xlim(-3.50, 3.50)
ax.set_ylim(0.00001, 0.0008)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.plot(wvalues[3][:202], elas[3][:202], linestyle = 'dashed',  linewidth=3, color='blue', label = 'elastic')
plt.plot(wvalues[3][:202], inel[3][:202], linestyle = 'dashdot', linewidth=3, color='red', label = inel_label)
#plt.grid()
plt.legend(title = title_label)



# Add additional information
info_text = "$pp \\rightarrow p p b \\bar{b}$"
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



plt.xlabel("$Y$")
plt.ylabel("$d\sigma/dY " " (pp \\rightarrow p p b \\bar{b})$ [pb]")


plt.savefig("dSigmadY_pp_bbbar_Modified.pdf")
plt.savefig("dSigmadY_pp_bbbar_Modified.jpg")

plt.show()



# ================================================================================


