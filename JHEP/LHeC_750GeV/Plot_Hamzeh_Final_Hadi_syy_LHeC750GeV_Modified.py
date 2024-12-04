
# Final Version -- December 2024 -- Hamzeh Khanpour

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
from wgrid_10_100000_10_LHeC750 import *

fig, ax = plt.subplots(figsize = (8.0, 8.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)
ax.set_xlim(10.0, 750.0)
ax.set_ylim(1.e-7, 1.e0)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wvalues[3][:303], elas[3][:303], linestyle = 'solid',  linewidth=3, label = 'elastic')
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dotted', linewidth=3, label = inel_label)
#plt.grid()



# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from wgrid_50_100000_1000_LHeC750 import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashdot', linewidth=3, label = inel_label)
plt.legend(title = title_label)



# from syy_3_3_3_0804 import *
# from syy_3_3_4_0805 import *
# from syy_3_4_4_0907 import *
from wgrid_300_100000_100000_LHeC750 import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashdot', linewidth=3, label = inel_label)
plt.legend(title = title_label)

plt.grid()


# Add additional information
info_text = "LHeC@750 GeV"
plt.text(0.32, 0.18, info_text, transform=ax.transAxes, ha='center', va='center', fontsize=22, color='blue', fontweight='bold')

info_text_2 = r"$E_e$=20 GeV; $E_p$=7000 GeV"
plt.text(0.32, 0.12, info_text_2, transform=ax.transAxes, ha='center', va='center', fontsize=22, color='blue', fontweight='bold')




# Save the output values in a text file
output_data = np.column_stack((wvalues[3][:303], elas[3][:303], inel[3][:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_Syy.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')




font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("W [GeV]")
plt.ylabel("S$_{\gamma \gamma}$ [GeV$^{-1}$]")




plt.savefig("syy_LHeC_750GeV_Modified.pdf")
plt.savefig("syy_LHeC_750GeV_Modified.jpg")

plt.show()



# ================================================================================


