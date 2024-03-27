import pycepgen
import numpy as np
import matplotlib.pyplot as plt
import math

cg_budnev_e = pycepgen.PartonFluxFactory.build('BudnevEPALepton', {'pdgId': 11})
cg_budnev_p = pycepgen.PartonFluxFactory.build('BudnevEPAProton')

fig, plts = plt.subplots(1, 2, figsize=(10, 10))
#fig.suptitle('$F_2$ comparison, ALLM97')

def flux_el(param, w):
    return 0.

def hk_flux():
    pass
def cg_flux():
    pass

w_axis = np.linspace(10., 2000., 500, endpoint=False)
hk_flux_el = [flux_el(hk_flux, w) for w in w_axis]
cg_flux_el = [flux_el(cg_flux, w) for w in w_axis]
diff_fluxes_el = [100.*(hk_flux_el[i]-cg_flux_el[i])/hk_flux_el[i] for i in range(len(w_axis))]
plts[0].plot(axis, hk_f2, 'k', label='Hamzeh')
plts[0].plot(axis, cg_f2, 'r--', label='CepGen')
plts[0].legend(title='$Q^2$ = {:g} GeV$^2$'.format(q2))
plts[0].grid()
plts[0].set_yscale('log')
plts[0].set_xlabel('$w_{\gamma\gamma}$')
plts[0].set_ylabel('d$L_{\gamma\gamma}$/d$w_{\gamma\gamma}$')
plts[1].plot(diff_fluxes_el)
plts[1].grid()

plt.tight_layout()
plt.savefig('fluxes_test.png')
