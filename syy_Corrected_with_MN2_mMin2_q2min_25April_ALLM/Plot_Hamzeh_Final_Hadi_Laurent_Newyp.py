
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
from wgrid_10_100000_10_elastic_tagged_Newyp import *

fig, ax = plt.subplots(figsize = (8, 9))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.e-7, 1.0)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.loglog(wvalues[3][:303], elas1[3][:303], linestyle = 'solid',  linewidth=3, label = 'tagged elastic (LHeC@1.2TeV)')
plt.loglog(wvalues[3][:303], elas2[3][:303], linestyle = 'dashdot',  linewidth=3, label = 'tagged elastic (LHeC@0.75TeV)')
plt.loglog(wvalues[3][:303], elas3[3][:303],
           linestyle=(0, (5, 2, 1, 2, 1, 2)),  # Custom dash-dot-dot pattern
           linewidth=3,  # Line thickness
           label='untagged elastic (LHeC@1.2TeV)')
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dotted', linewidth=3, label = inel_label)
#plt.grid()



# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from wgrid_100_100000_100000_elastic_tagged_Newyp import *

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$)').format(10,np.log10(inel[2]))
plt.loglog(wvalues[3][:303], inel[3][:303], linestyle = 'dashed', linewidth=3, label = inel_label)
plt.legend(title = title_label)




# Save the output values in a text file
output_data = np.column_stack((wvalues[3][:303], elas1[3][:303], inel[3][:303]))
header = 'W_Value Elastic Inelastic'
np.savetxt('output_values_Syy.txt', output_data, header=header, fmt='%0.8e', delimiter='\t')




#font1 = {'family':'serif','color':'black','size':24}
#font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("W (GeV)")
plt.ylabel("S$_{\gamma \gamma}$ (GeV$^{-1}$)")




plt.savefig("syy_with_MN2_mMin2_q2min_Final_25April_Modified_Newyp.pdf")
plt.savefig("syy_with_MN2_mMin2_q2min_Final_25April_Modified_Newyp.jpg")

plt.show()



# ================================================================================


