import matplotlib.pyplot as plt
import sys

sys.path.append('./values')
# from syy_1_3_3_0804 import *
# from syy_1_3_4_0805 import *
# from syy_1_4_4_0907 import *
from wgrid_1_4_4_0908 import *

fig, ax = plt.subplots(figsize = (9., 8.))
ax.set_xlim(10., 1000.)
ax.set_ylim(2.e-7, 2.e-2)

inel_label = 'M_N < ' + str(inel[0]) + 'GeV'
title_label = 'Q2e/p < ' + str(inel[1]) + '/' + str(inel[2]) + 'GeV^2'
plt.loglog(wvalues[3][:101], elas[3][:101], 'b-', label = 'elastic')
plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
plt.grid()

# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from wgrid_2_4_4_0908 import *

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
plt.legend(title = title_label)

# from syy_3_3_3_0804 import *
# from syy_3_3_4_0805 import *
# from syy_3_4_4_0907 import *
from wgrid_3_4_4_0908 import *

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
plt.legend(title = title_label)

plt.show()

