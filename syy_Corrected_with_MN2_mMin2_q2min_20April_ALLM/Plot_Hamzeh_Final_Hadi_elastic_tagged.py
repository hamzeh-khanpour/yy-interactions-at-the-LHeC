
# Final Version -- October 2023 -- Hamzeh Khanpour

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
from wgrid_1_4_4_0908_elastic_tagged import *

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(2.e-7, 1.e-1)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e/Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wvalues[3][:303], elas[3][:303], linestyle = 'dashed',  linewidth=2, color='blue', label = 'elastic')
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashdot', linewidth=2, color='red', label = 'tagged elastic ($0.01 < y_p < 0.2$)')
#plt.grid()


plt.legend(title = title_label)


# Set label colors
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')

# Add legend with specified colors
legend = plt.legend(title = title_label)
legend.get_texts()[0].set_color("blue")  # Color for 'elastic'
legend.get_texts()[1].set_color("red")   # Color for inel_label





font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("W [GeV]",  fontdict = font2)
plt.ylabel("S$_{\gamma \gamma}$ [GeV$^{-1}$]", fontdict = font2)




plt.savefig("syy_elastic_tagged.pdf")
plt.savefig("syy_elastic_tagged.jpg")

plt.show()



# ================================================================================


