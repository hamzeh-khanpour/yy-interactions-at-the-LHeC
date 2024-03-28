
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
from cepgen_ALLM_sf_MN50 import *

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-6, 1.e-1)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
#plt.loglog(wvalues[3][:303], elas[3][:303], linestyle = 'solid',  linewidth=2, label = 'elastic')
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'solid', linewidth=2, label = 'cepgen_ALLM_sf')
#plt.grid()



# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from cepgen_luxlike_sf_MN50 import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashed', linewidth=2, label = 'cepgen_luxlike_sf')
plt.legend(title = title_label)






from cepgen_Kulagin_Barinov_sf_MN50 import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashdot', linewidth=2, label = 'cepgen_Kulagin_Barinov_sf')
plt.legend(title = title_label)






from cepgen_GRAPE_like_sf_MN50 import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dotted', linewidth=2, label = 'cepgen_GRAPE_like_sf')
plt.legend(title = title_label)








# Save the output values in a text file
output_data = np.column_stack((wvalues[3][:303], elas[3][:303], inel[3][:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_Syy.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')



# Add additional information
info_text = "$M_N < 50 \,GeV$, $Q^2_p < 10^3  \, GeV^2$"
plt.text(0.25, 0.90, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=15, color='black')



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("W [GeV]",  fontdict = font2)
plt.ylabel("S$_{\gamma \gamma}$ [GeV$^{-1}$]", fontdict = font2)




plt.savefig("Plot_Compare_SF_MN50.pdf")
plt.savefig("Plot_Compare_SF_MN50.jpg")

plt.show()



# ================================================================================


