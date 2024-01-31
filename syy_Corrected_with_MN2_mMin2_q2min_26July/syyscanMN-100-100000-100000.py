
# Final Version -- October 2023 -- Hamzeh Khanpour

import Syy
import ALLM
import numpy as np

# last two arguments: mNmax (not squared), Q2max (squared)

mNmax = 100.0
q2emax = 100000.0
q2pmax = 100000.0
# wlist = [10., 20., 50., 100., 200., 500.]
# wlist = [200.]
# wln = np.linspace(1., 3., 41)
wln = np.linspace(1.0, 3.0, 303)
# wln = np.linspace(1., 2.5, 76)
# wln = np.linspace(3., 3.25, 13)
wlist = [10.0**x for x in wln]


res_param = (mNmax, q2emax, q2pmax, wlist)
res_inel = (mNmax, q2emax, q2pmax, [])
res_el = (mNmax, q2emax, q2pmax, [])


inelastic = True


for wv in wlist:
    print('w, nMmax, q2emax, q2pmax:', wv, mNmax, q2emax, q2pmax)
    if inelastic:
        flux_inel_w = Syy.flux_inel_yy_atW(wv, 50., 7000., q2emax, mNmax, q2pmax)
        # print(flux_inel_w)
        syy = 2.0 * flux_inel_w[0] / wv
        res_inel[3].append(syy)
        print('inel: {:2f} {:5e}     {:5e} {:5e}'
              .format(wv, syy, flux_inel_w[0], flux_inel_w[1]))


    flux_el = Syy.flux_el_yy_atW(wv, 50., 7000., q2emax, q2pmax)
    # print(flux_el)
    syy = 2.0 * flux_el[0] / wv
    res_el[3].append(syy)
    print('el: {:2f} {:5e}     {:5e} {:5e}'
          .format(wv, syy, flux_el[0], flux_el[1]))



with open('100_100000_100000_ALPHA2PI_MN_Q2_Q2_mMin2_q2min.dat', 'w') as f:
    print(res_param, file = f)     
    print(res_inel, file = f)
    print(res_el, file = f)
