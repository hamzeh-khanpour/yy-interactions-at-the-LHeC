
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
from wgrid_1_4_4_0908 import *

fig, ax = plt.subplots(figsize = (9.0, 8.0))
ax.set_xlim(0.0, 5.0)
ax.set_ylim(0.0, 0.01)

inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10,np.log10(inel[1]))
plt.plot(wvalues[3][:101], elas[3][:101], linestyle = 'solid',  linewidth=2, label = 'elastic')
plt.plot(wvalues[3][:101], inel[3][:101], linestyle = 'dotted', linewidth=2, label = inel_label)
#plt.grid()



font1 = {'family':'serif','color':'black','size':24}
font2 = {'family':'serif','color':'black','size':24}



plt.xlabel("Y",  fontdict = font2)
plt.ylabel("dS/dY", fontdict = font2)


plt.savefig("dSigmadY.pdf")
plt.savefig("dSigmadY.jpg")

plt.show()



# ================================================================================


