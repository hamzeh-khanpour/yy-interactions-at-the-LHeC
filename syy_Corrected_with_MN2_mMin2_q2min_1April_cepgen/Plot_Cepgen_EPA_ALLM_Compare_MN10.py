
# Final Version -- 1 March 2024 -- Hamzeh Khanpour

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
from Compare_ALLM_MN10 import *

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(2.e-7, 1.e-1)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wvalues[3][:303], elas[3][:303], linestyle = 'solid',  color = 'blue', linewidth=2, label = 'ALLM (EPA)')
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashed', color = 'red', linewidth=2, label = 'ALLM (cepgen)')
#plt.grid()
plt.legend(title = title_label)



# Save the output values in a text file
output_data = np.column_stack((wvalues[3][:303], elas[3][:303], inel[3][:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_Syy.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')



# Add additional information
info_text = "$M_N < 10 \,GeV$, $Q^2_p < 10  \, GeV^2$"
plt.text(0.3, 0.90, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=15, color='black')



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("W [GeV]",  fontdict = font2)
plt.ylabel("S$_{\gamma \gamma}$ [GeV$^{-1}$]", fontdict = font2)




plt.savefig("Compare_ALLM_MN10.pdf")
plt.savefig("Compare_ALLM_MN10.jpg")

plt.show()



# ================================================================================


