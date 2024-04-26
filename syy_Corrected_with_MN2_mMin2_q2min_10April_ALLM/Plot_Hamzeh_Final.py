import numpy as np
import matplotlib.pyplot as plt
import sys

plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams["xtick.major.width"] = 1.5
plt.rcParams["xtick.minor.width"] = 1.5
plt.rcParams["ytick.major.width"] = 1.5
plt.rcParams["ytick.minor.width"] = 1.5

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

plt.rcParams["legend.fontsize"] = 12

plt.rcParams['legend.title_fontsize'] = 'x-large'



sys.path.append('./values')
# from syy_1_3_3_0804 import *
# from syy_1_3_4_0805 import *
# from syy_1_4_4_0907 import *
from wgrid_1_4_4_0908 import *

fig, ax = plt.subplots(figsize = (9., 8.))
ax.set_xlim(10., 1000.)
ax.set_ylim(2.e-7, 1.e-2)

inel_label = 'M$_N$ < ' + str(inel[0]) + '' ' GeV'
title_label = 'Q$^2$ (e/p) < ' + str(inel[1]) + '/' + str(inel[2]) + ' GeV$^2$'
plt.loglog(wvalues[3][:101], elas[3][:101], linestyle = 'solid',  linewidth=2, label = 'elastic')
plt.loglog(wvalues[3][:101], inel[3][:101], linestyle = 'dotted', linewidth=2, label = inel_label)
#plt.grid()



# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from wgrid_2_4_4_0908 import *

inel_label = 'M$_N$ < ' + str(inel[0])  + '' ' GeV'
#plt.loglog(wvalues[3][:101], inel[3][:101], linestyle = 'dashed', linewidth=2, label = inel_label)
plt.legend(title = title_label)



# from syy_3_3_3_0804 import *
# from syy_3_3_4_0805 import *
# from syy_3_4_4_0907 import *
from wgrid_3_4_4_0908 import *

inel_label = 'M$_N$ < ' + str(inel[0])  + '' ' GeV'
plt.loglog(wvalues[3][:101], inel[3][:101], linestyle = 'dashdot', linewidth=2, label = inel_label)
plt.legend(title = title_label)

font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'black','size':20}

plt.xlabel("W [GeV]",  fontdict = font2)
plt.ylabel("S$_{\gamma \gamma}$", fontdict = font2)

plt.savefig("syy_with_MN2_mMin2.pdf")

plt.show()
