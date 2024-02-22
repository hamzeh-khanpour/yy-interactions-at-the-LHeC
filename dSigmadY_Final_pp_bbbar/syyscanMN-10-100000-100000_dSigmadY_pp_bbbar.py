
# Final Version -- Febraury 2024 -- Hamzeh Khanpour

import Syy
import ALLM
import numpy as np

# last two arguments: mNmax (not squared), Q2max (squared)

mNmax  = 10.0
q2pmax2 = 100000.0
q2pmax1 = 100000.0

# wlist = [10., 20., 50., 100., 200., 500.]
# wlist = [200.]
# wln = np.linspace(1., 3., 41)
wln = np.linspace(-3.5, 3.5, 202)
# wln = np.linspace(1., 2.5, 76)
# wln = np.linspace(3., 3.25, 13)
wlist = [1.0*x for x in wln]


res_param = (mNmax, q2pmax2, q2pmax1, wlist)
res_inel = (mNmax, q2pmax2, q2pmax1, [])
res_el = (mNmax, q2pmax2, q2pmax1, [])


inelastic = True


for Y in wlist:
    print('Y, nMmax, q2pmax2, q2pmax1:', Y, mNmax, q2pmax2, q2pmax1)
    if inelastic:
        flux_inel_w = Syy.flux_inel_yy_atW(Y, 7000.0, 7000.0, q2pmax2, mNmax, q2pmax1)

        # print(flux_inel_w)

        s_cms = 4.0 * 7000.0 * 7000.0

        syy = 2.0 * flux_inel_w[0] / s_cms

        res_inel[3].append(syy)
        print('inel: {:2f} {:5e}     {:5e} {:5e}'
              .format(Y, syy, flux_inel_w[0], flux_inel_w[1]))


    flux_el = Syy.flux_el_yy_atW(Y, 7000.0, 7000.0, q2pmax2, q2pmax1)

    # print(flux_el)

    s_cms = 4.0 * 7000.0 * 7000.0

    syy = 2.0 * flux_el[0] / s_cms

    res_el[3].append(syy)
    print('el: {:2f} {:5e}     {:5e} {:5e}'
          .format(Y, syy, flux_el[0], flux_el[1]))



with open('10_100000_100000_dSigmadY_pp_bbbar.dat', 'w') as f:
    print(res_param, file = f)     
    print(res_inel, file = f)
    print(res_el, file = f)
