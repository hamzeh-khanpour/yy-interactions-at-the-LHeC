
# Final Version -- 1 March 2024 -- Hamzeh Khanpour


import math
import scipy.integrate as integ

import pycepgen



# 11 Suri-Yennie
sf_Suri_Yennie = pycepgen.StructureFunctionsFactory.build(11)


# 202 ALLM97 (continuum, FT/HERA photoprod. tot.x-s 1356 points fit)
sf_ALLM97 = pycepgen.StructureFunctionsFactory.build(202)


# 301 LUXlike (hybrid)
# sf_luxlike = pycepgen.StructureFunctionsFactory.build(301)


# units in GeV

pmass = 0.938272081
pi0mass = 0.1349768


# --------------------------------------------------------------



def allm_f2divx_mN(mN, Q2, yp):

    A2 = mN*mN - pmass * pmass                                                            # Hamzeh
    mqdiff = mN*mN - pmass * pmass + Q2                                                   # Hamzeh

    if mqdiff < 0:
        print('mN*mN, Q2:', mN*mN, Q2)
        return 0.

    xbj = Q2 / mqdiff

    qmin2 = (mN*mN / (1.0 - yp) - pmass * pmass) * yp

    if xbj < 0:
        print('xbj: ', xbj)
        return 0.
    else:
        # 27 Jul 2021: adding Qmin2
        if qmin2 < Q2:
            if mN < 2.0:
                return sf_Suri_Yennie.F2(xbj, Q2) / Q2**0.0 * 2.0 * mN * mqdiff  # Hamzeh: It should be Q2**2.0 in Syy200.py
            else:
                return sf_ALLM97.F2(xbj, Q2) / Q2**0.0 * 2.0 * mN * mqdiff  # Hamzeh: It should be Q2**2.0 in Syy200.py
        else:
            return 0.

def allm_formM_mN2(Q2, yp, mMin2, mNmax):
    return integ.quad(allm_f2divx_mN, mMin2, mNmax, args=(Q2, yp),
                      epsrel=1.e-2)



# --------------------------------------------------------------



def allm_xf2_mN(mN, Q2, yp):

    A2 = mN*mN - pmass * pmass                                                           # Hamzeh
    mqdiff = mN*mN - pmass * pmass + Q2

    if mqdiff < 0:
        print('mN*mN, Q2:', mN*mN, Q2)
        return 0.

    xbj = Q2 / mqdiff

    qmin2 = (mN*mN / (1.0 - yp) - pmass * pmass) * yp

    if xbj < 0:
        print('xbj: ', xbj)
        return 0.
    else:

        if qmin2 < Q2:
            if mN < 2.0:
                return sf_Suri_Yennie.F2(xbj, Q2) / Q2**0.0  * 2.0 * mN *  (1.0 / mqdiff)  # Hamzeh ( 1.0 - qmin2 / math.exp(lnq2) )
            else:
                return sf_ALLM97.F2(xbj, Q2) / Q2**0.0  * 2.0 * mN *  (1.0 / mqdiff)  # Hamzeh ( 1.0 - qmin2 / math.exp(lnq2) )
        else:
            return 0.0

def allm_formE_qmin2(Q2, yp, mMin2, mNmax):
    return integ.quad(allm_xf2_mN, mMin2, mNmax, args=(Q2, yp),
                      epsrel=1.e-2)


# --------------------------------------------------------------


