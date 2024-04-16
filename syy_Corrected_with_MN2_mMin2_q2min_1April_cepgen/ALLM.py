
# Final Version -- 1 March 2024 -- Hamzeh Khanpour


import math
import scipy.integrate as integ

import pycepgen



# 202 ALLM97 (continuum, FT/HERA photoprod. tot.x-s 1356 points fit)
sf_ALLM97 = pycepgen.StructureFunctionsFactory.build(202)


# 11 Suri-Yennie
# sf_Suri_Yennie = pycepgen.StructureFunctionsFactory.build(11)


# 301 LUXlike (hybrid)
# sf_luxlike = pycepgen.StructureFunctionsFactory.build(301)


# 303 Kulagin-Barinov (hybrid)
# sf_Kulagin_Barinov = pycepgen.StructureFunctionsFactory.build(303)


# units in GeV

pmass = 0.938272081
pi0mass = 0.1349768


# ALLM parameters -- arXiv:hep-ph/9712415

Mass2_0 = 0.31985
Mass2_P = 49.457
Mass2_R = 0.15052
Q2_0    = 0.52544
Lambda2 = 0.06527

Ccp = (0.28067, 0.22291,  2.1979)
Cap = (-0.0808, -0.44812, 1.1709)
Cbp = (0.36292, 1.8917,   1.8439)

Ccr = (0.80107, 0.97307, 3.4942)
Car = (0.58400, 0.37888, 2.6063)
Cbr = (0.01147, 3.7582,  0.49338)



# --------------------------------------------------------------


def tvalue(Q2):
    return math.log \
           ((math.log((Q2 + Q2_0) / Lambda2) / math.log(Q2_0 / Lambda2)))

def xP(xbj, Q2):
    if xbj == 0:
        print("xbj zero")
        return -1.
    xPinv = 1. + Q2 / (Q2 + Mass2_P) * (1. / xbj - 1.)
    return 1. / xPinv

def xR(xbj, Q2):
    if xbj == 0:
        print("xbj zero")
        return -1.
    xPinv = 1. + Q2 / (Q2 + Mass2_R) * (1. / xbj - 1.)
    return 1. / xPinv

def type1(tval, tuple1):
    return tuple1[0] + tuple1[1] * (tval ** tuple1[2])

def type2(tval, tuple1):
    return tuple1[0] +\
           (tuple1[0] - tuple1[1]) * (1. / (1. + tval ** tuple1[2]) - 1.)

def aP(tval):
    return type2(tval, Cap)

def bP(tval):
    return type1(tval, Cbp)

def cP(tval):
    return type2(tval, Ccp)

def aR(tval):
    return type1(tval, Car)

def bR(tval):
    return type1(tval, Cbr)

def cR(tval):
    return type1(tval, Ccr)

def allm_f2P(xbj, Q2):
    tval = tvalue(Q2)
    return cP(tval) * (xP(xbj, Q2) ** aP(tval)) * ((1. - xbj) ** bP(tval))

def allm_f2R(xbj, Q2):
    tval = tvalue(Q2)
    return cR(tval) * (xR(xbj, Q2) ** aR(tval)) * ((1. - xbj) ** bR(tval))

def allm_f2(xbj, Q2):
    return Q2 / (Q2 + Mass2_0) * (allm_f2P(xbj, Q2) + allm_f2R(xbj, Q2))



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
            return sf_ALLM97.F2(xbj, Q2) / Q2**0.0 * 2.0 * mN * mqdiff                  # Hamzeh: It should be Q2**2.0 in Syy200.py
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
            return sf_ALLM97.F2(xbj, Q2) / Q2**0.0  * 2.0 * mN *  (1.0/mqdiff)          # Hamzeh ( 1.0 - qmin2 / math.exp(lnq2) )
        else:
            return 0.

def allm_formE_qmin2(Q2, yp, mMin2, mNmax):
    return integ.quad(allm_xf2_mN, mMin2, mNmax, args=(Q2, yp),
                      epsrel=1.e-2)


# --------------------------------------------------------------


