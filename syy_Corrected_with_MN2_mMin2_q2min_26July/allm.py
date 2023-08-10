import math
import scipy.integrate as integ

# units in GeV

pmass = 0.938272081
pi0mass = 0.1349768

# ALLM parameters
Mass2_0 = 0.31985
Mass2_P = 49.457
Mass2_R = 0.15052
Q2_0 = 0.52544
Lambda2 = 0.06527

Ccp = (0.28067, 0.22291, 2.1979)
Cap = (-0.0808, -0.44812, 1.1709)
Cbp = (0.36292, 1.8917, 1.8439)

Ccr = (0.80107, 0.97307, 3.4942)
Car = (0.58400, 0.37888, 2.6063)
Cbr = (0.01147, 3.7582, 0.49338)

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


dissocMass2_max = 100.
# dissocMass2_max = 10.
# dissocMass2_min = 3.
dissocMass2_min = pmass + pi0mass

def allm_f2divx(xbj, Q2):
    return allm_f2(xbj, Q2) / xbj

def allm_f2divx3(xbj, Q2):
    return allm_f2(xbj, Q2) / (xbj * xbj * xbj)

def allm_f2divx3_z(z, Q2):
    xbj = z**(-1./3.)
    return allm_f2(xbj, Q2) * xbj / 3.

def allm_f2divx2(xbj, Q2):
    return allm_f2(xbj, Q2) / (xbj * xbj)

def allm_f2divxQ2(mN2, Q2):
    xbj = Q2 / (mN2 - pmass * pmass + Q2)
    return allm_f2(xbj, Q2) / xbj / Q2

def allm_formE(Q2, mMin2):
    xmin = Q2 / (dissocMass2_max - pmass * pmass + Q2)
    xmax = Q2 / (mMin2 - pmass * pmass + Q2)
    return integ.quad(allm_f2divx, xmin, xmax, args=(Q2),
                      epsabs=1.e-5, epsrel=1.e-5)

def allm_formM(Q2, mMin2):
    xmin = Q2 / (dissocMass2_max - pmass * pmass + Q2)
    xmax = Q2 / (mMin2 - pmass * pmass + Q2)
    return integ.quad(allm_f2divx3, xmin, xmax, args=(Q2),
                      epsabs=1.e-5, epsrel=1.e-5)

def allm_formE2(Q2, yp, mMin2, mNmax):
    xmin = Q2 / (mNmax * mNmax - pmass * pmass + Q2)
    # xmin = Q2 / (mNmax * mNmax) / yp
    xmax = Q2 / (mMin2 - pmass * pmass + Q2)
    return integ.quad(allm_f2divx, xmin, xmax, args=(Q2),
                      epsabs=1.e-5, epsrel=1.e-5)

def allm_formM2(Q2, yp, mMin2, mNmax):
    xmin = Q2 / (mNmax * mNmax - pmass * pmass + Q2)
    xmax = Q2 / (mMin2 - pmass * pmass + Q2)
    # print('xmin xmax:', xmin, xmax)
#    return integ.quad(allm_f2divx3, xmin, xmax, args=(Q2),
#                      epsabs=1.e-5, epsrel=1.e-5)
    return integ.quad(allm_f2divx3, xmin, xmax, args=(Q2),
                      epsrel=1.e-3)
#                      epsabs=1.e-5, epsrel=1.e-5)

def allm_formM3(Q2, yp, mMin2, mNmax):
    mlow2 = mMin2
    mhigh2 = mNmax * mNmax
    return integ.quad(allm_f2divxQ2, mlow2, mhigh2, args=(Q2),
                      epsabs=1.e-5, epsrel=1.e-5)

def allm_formM4(Q2, yp, mMin2, mNmax, pout=False):
    """x**(-3) = z i.e. x = z**(-1/3)"""
    xmin = Q2 / (mNmax * mNmax - pmass * pmass + Q2)
    xmax = Q2 / (mMin2 - pmass * pmass + Q2)
    zmin = xmin**(-3)
    zmax = xmax**(-3)
    if pout:
        print('zmin zmax, f(zmin), f(zmax): {:.4e} {:.4e} {:.4e} {:.4e}'
              .format(zmin, zmax,
                      allm_f2divx3_z(zmin, Q2), allm_f2divx3_z(zmax, Q2)))
    return integ.quad(allm_f2divx3_z, zmax, zmin, args=(Q2),
                      epsrel=1.e-3)
#                       epsabs=1.e-5, epsrel=1.e-5)













def allm_f2divx_mN(mN, Q2, yp):

    A2 = mN*mN - pmass * pmass                                                             # Hamzeh
    mqdiff = mN*mN - pmass * pmass + Q2                                                    # Hamzeh 
    
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
            return allm_f2(xbj, Q2) / Q2**0.0 * 2.0 * mN * mqdiff                        # Hamzeh: It should be Q2**2.0 in Syy200.py
        else:
            return 0.

def allm_formM_mN2(Q2, yp, mMin2, mNmax):
    return integ.quad(allm_f2divx_mN, mMin2, mNmax, args=(Q2, yp),
                      epsrel=1.e-2)






def allm_xf2_mN(mN, Q2, yp):
    
    A2 = mN*mN - pmass * pmass                                                             # Hamzeh
    mqdiff = mN*mN - pmass * pmass + Q2

    if mqdiff < 0:
        print('mN*mN, Q2:', mN*mN, Q2)  
        return 0.

    xbj = Q2 / mqdiff
    
    qmin2 = (mN/mN / (1.0 - yp) - pmass * pmass) * yp

    if xbj < 0:
        print('xbj: ', xbj)
        return 0.
    else:
    
        if qmin2 < Q2:
            return allm_f2(xbj, Q2) / Q2**0.0  * 2.0 * mN *  (1.0/mqdiff)   # Hamzeh ( 1.0 - qmin2 / math.exp(lnq2) )   
        else:
            return 0.

def allm_formE_qmin2(Q2, yp, mMin2, mNmax):
    return integ.quad(allm_xf2_mN, mMin2, mNmax, args=(Q2, yp),
                      epsrel=1.e-2)












def elas_formE(Q2):
    gE2 = (1 + Q2/0.71) ** (-4)
    gM2 = 7.78 * gE2
    formE = (4 * pmass * pmass * gE2 + Q2 * gM2) \
                   / (4 * pmass * pmass + Q2)
    return formE

def elas_formM(Q2):
    gE2 = (1 + Q2/0.71) ** (-4)
    gM2 = 7.78 * gE2
    return gM2

testgrid = (0.1, 0.3, 1., 3., 10., 30., 100., 300., 1000.)

def listffQ2():
    ytmp = 0.5
    q2min = (dissocMass2_min / (1 - ytmp) - pmass * pmass) * ytmp
    mMin2 = dissocMass2_min
    print('Q2Min at y = 0.5:', q2min)
    for q2 in testgrid:
        print('ALLM testgrid in Q2:', \
	      q2, allm_formE(q2, mMin2)[0], elas_formE(q2), \
              allm_formM(q2, mMin2)[0], elas_formM(q2))

# listffQ2()
print()

def testf2Q2(xbj, multf = 1.0):
    for q2 in testgrid:
        print(xbj, q2, multf * allm_f2(xbj, q2))

# testf2Q2(0.65, multf = 10.)
# print()
# testf2Q2(0.18, multf = 32.)
# print()
# testf2Q2(0.0025, multf = 9.)
# print()
# testf2Q2(1.5e-4, multf = 7.)

        
