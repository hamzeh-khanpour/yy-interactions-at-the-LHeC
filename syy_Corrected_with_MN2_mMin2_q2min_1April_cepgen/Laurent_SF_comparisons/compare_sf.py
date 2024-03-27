import allm as hk_allm
import pycepgen
import numpy as np
import matplotlib.pyplot as plt
import math

cg_allm97 = pycepgen.StructureFunctionsFactory.build(202)

q2vals = [0.001, 0.01, 0.1, 1.0, 10.0, 50.0, 100.0, 1000.0]

fig, plts = plt.subplots(len(q2vals), 2, figsize=(10, 10))
fig.suptitle('$F_2$ comparison, ALLM97')

for i in range(len(q2vals)):
    q2 = q2vals[i]
    axis = np.linspace(1.e-5, 1., 500, endpoint=False)
    hk_f2 = [hk_allm.allm_f2(xbj, q2) for xbj in axis]
    cg_f2 = [cg_allm97.F2(xbj, q2) for xbj in axis]
    diff_f2 = [100.*(hk_f2[i]-cg_f2[i])/hk_f2[i] for i in range(len(axis))]
    plts[i, 0].plot(axis, hk_f2, 'k', label='Hamzeh')
    plts[i, 0].plot(axis, cg_f2, 'r--', label='CepGen')
    plts[i, 0].legend(title='$Q^2$ = {:g} GeV$^2$'.format(q2))
    plts[i, 0].grid()
    plts[i, 0].set_yscale('log')
    plts[i, 0].set_xlabel('$x_{Bj}$')
    plts[i, 0].set_ylabel('$F_{2}(x_{Bj}, Q^2)$')
    plts[i, 1].plot(axis, diff_f2, 'k')
    plts[i, 1].grid()
    plts[i, 1].set_xlabel('$x_{Bj}$')
    plts[i, 1].set_ylabel('(HK-CG)/HK (%)')

plt.tight_layout()
plt.savefig('allm_test.png')
plt.show()
