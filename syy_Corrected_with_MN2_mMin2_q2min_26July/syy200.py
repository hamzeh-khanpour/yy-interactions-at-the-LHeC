
# Final Version -- October 2023 -- Hamzeh

import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integ
import allm


# units in GeV

# v3->newest: integration in dQ^2/Q^2 -> dlnQ^2

ALPHA2PI = 7.2973525693e-3 / math.pi  #  * 0.5                                # Hamzeh

emass = 5.1099895e-4
pmass = 0.938272081
pi0mass = 0.1349768

def qmin2(mass, y):
    return mass * mass * y * y / (1 - y)

# flux at given y with q2max point-like form factor
# Q2 integration was done analytically
def flux_y_pl(y, mass, qmax2):
    if (y <= 0 or y >= 1):
        print('invalid y value: ', y)
        return -1.0
    else:
        qmin2v = qmin2(mass, y)
        # print('qmin2v', qmin2v)
        y1 = (1./2.) * (1. + (1. - y) * (1. - y)) / y                         # Hamzeh  1 -> 1/2
        y2 = 1. * (1. - y) / y                                                # Hamzeh  2 -> 1                                                         
        flux1 = y1 * math.log(qmax2 / qmin2v)
        flux2 = y2 * (1. - qmin2v / qmax2)
        # print(flux1, flux2)
        return ALPHA2PI * (flux1 - flux2)

# flux at given y with q2max with dipole form factor
def flux_y_dipole(y, mass, qmax2): 
    if (y <= 0 or y >= 1):
        print('invalid y value: ', y)
        return -1.0
    else:
        qmin2v = qmin2(mass, y)
	# integration from qmin2 to qmax2
        flux_y_tmp = integ.quad(flux_y_q2_dipole,
                                math.log(qmin2v), math.log(qmax2),
                                args=(y, mass, qmin2v))
        # print(flux_y_tmp)
        return flux_y_tmp[0]



def flux_y_inel(y, mMin2, qmax2, mNmax, pout=False): 
    if (y <= 0 or y >= 1):
        print('invalid y value: ', y)
        return -1.0
    else:
        qmin2v = (mMin2*mMin2 / (1 - y) - pmass * pmass) * y                   # Hamzeh mMin2-> mMin2*mMin2
        if pout:
            print('qmin2, qmax2:', qmin2v, qmax2)
	# integration from qmin2 to qmax2
#        flux_y_tmp = integ.quad(flux_y_q2_inel,
#                                math.log(qmin2v), math.log(qmax2),
#                                args=(y, mMin2, mNmax, qmin2v),
#  				epsrel=1.e-3)
        flux_y_tmp = integ.quad(flux_y_q2_inel_mN2,
                                math.log(qmin2v), math.log(qmax2),
                                args=(y, mMin2, mNmax, qmin2v),
				epsrel=1.e-2)
#				epsabs=1.e-5, epsrel=1.e-5)
        if pout:
            print('y, flux: {:8.5e} {:8.5e}'.format(y, flux_y_tmp[0]))
        return flux_y_tmp[0]



# returning flux factor at given (q2, y)
# with dipole form factor with effective mass parameter
def flux_y_q2_dipole(lnq2, y, mass, qmin2v):
        gE2 = (1 + math.exp(lnq2)/0.71) ** (-4)
        gM2 = 7.78 * gE2
        formE = (4 * mass * mass * gE2 + math.exp(lnq2) * gM2) \
                / (4 * mass * mass + math.exp(lnq2))
        formM = gM2
        flux_tmp = (1 - y) * (1 - qmin2v / math.exp(lnq2)) * formE \
                               + y * y * 0.5 * formM
        flux_tmp *= ALPHA2PI / y
        # print(lnq2, flux_tmp)
        return flux_tmp



def flux_y_q2_inel(lnq2, yp, mMin2, nMmax, qmin2v, pout=False):
        # integration variable: q2
	#
        # print('minmax: ', mMin2, nMmax)
        formE = allm.allm_formE2(math.exp(lnq2), yp, mMin2, nMmax)[0]
	# 27 Jun: M2->M3, divide by xQ2 and integrate over mN^2
	# 27 Jun: put back to M3 -> M2 but try with /x^2 instead of /x^3
	# 1 Jul: trying M4: x**(-3) = z
        formM = allm.allm_formM4(math.exp(lnq2), yp, mMin2, nMmax)[0]
#        formM = allm.allm_formM2(q2, yp, mMin2, nMmax)[0]
        flux_tmp = (1 - yp) * (1 - qmin2v / math.exp(lnq2)) * formE \
                               + yp * yp * 0.5 * formM
        flux_tmp *= ALPHA2PI / yp
        if pout:
            print('inel q2, y, E M flux: {:.4e} {:.4e} {:.4e} {:.4e} {:.4e}'
                  .format(q2, yp, formE, formM, flux_tmp))
        return flux_tmp












def flux_y_q2_inel_mN2(lnq2, yp, mMin2, nMmax, qmin2v, pout=False):
        # integration variable: q2
	#

        qmin2 = (mMin2*mMin2 / (1 - yp) - pmass * pmass) * yp                   # Hamzeh
        
        formE = allm.allm_formE_qmin2(math.exp(lnq2), yp, mMin2, nMmax)[0]
        formMq2 = allm.allm_formM_mN2(math.exp(lnq2), yp, mMin2, nMmax)[0]
        
        # YY 30.07.2021: formM was divided by q2*q2 -> should be q2        
        formMNew = formMq2 / ( math.exp(lnq2) * math.exp(lnq2) )  #        # Hamzeh
        formENew = formE * ( 1.0 - qmin2 / math.exp(lnq2) )       #  / ( math.exp(lnq2) )      # Hamzeh    
        
        flux_tmp = (1 - yp) * formENew \
                    + yp * yp * 0.5 * formMNew
        flux_tmp *= ALPHA2PI / yp
        if pout:
            print('inel q2, y, E M flux: {:.4e} {:.4e} {:.4e} {:.4e} {:.4e}'
#                  .format(q2, yp, formE, formM / math.exp(lnq2), flux_tmp))    
                  .format(q2, yp, formENew, formMNew, flux_tmp))                          # Hamzeh        
        return flux_tmp











# picking up proton and electron mass as external constants
def flux_yy_atye(ye, w, qmax2e, qmax2p, s_cms, pout=False):
    yp = w * w / s_cms / ye
    if pout:
        print(emass, pmass, ye, w, qmax2e, s_cms)
    flux_prod = flux_y_dipole(yp, pmass, qmax2p) \
                * yp * flux_y_pl(ye, emass, qmax2e)
    return flux_prod




# inelastic flux at given ye and W
def flux_yyinel_atye(ye, w, qmax2e, qmax2p, mNmax, s_cms, pout=False):
    yp = w * w / s_cms / ye
    minM2 = (pmass + pi0mass)# * (pmass + pi0mass)                                       # Hamzeh

    # given: ye, w, qmax2e, qmax2p, cms energy
    # calculated inside here: gamma **Monochrome** energy on proton side (yp)
    #   and: minimum mass M_N, to pass
    # point-like on the electron side
    # according to Eq.(A.1)
    flux_prod = flux_y_inel(yp, minM2, qmax2p, mNmax) \
                * yp * flux_y_pl(ye, emass, qmax2e)
    if pout:
        print(emass, pmass, ye, w, qmax2e, s_cms, flux_prod)

    return flux_prod






def flux_el_yy_atW(w, eEbeam, pEbeam, qmax2e, qmax2p):
    # first calculate the ymin for e-side, p-side
    s_cms = 4. * eEbeam * pEbeam
    ymin = w * w / s_cms
    # print(ymin)
    fyyatw = integ.quad(flux_yy_atye, ymin, 1.,
                        args=(w, qmax2e, qmax2p, s_cms))
    return fyyatw



def flux_inel_yy_atW(w, eEbeam, pEbeam, qmax2e, mNmax, qmax2p):
    # first calculate the ymin for e-side, p-side
    s_cms = 4. * eEbeam * pEbeam
    ymin = w * w / s_cms

    # flux for ymin -> 1., at a given w.
    # Qmax2e, Qmax2p are given from experimental constraints (beam holes)
    # integration according to Eq.(A.1) apart from 2/W (external)
    fyyatw = integ.quad(flux_yyinel_atye, ymin, 1.,
                        args=(w, qmax2e, qmax2p, mNmax, s_cms),
			epsrel=1.e-2)
#			epsabs=1.e-5, epsrel=1.e-5)
    return fyyatw



# testing parameter for ZEUS 35m tagger
# ymin = 0.42
# ymax = 0.56
# q2maxv = 0.02

# result_e = integ.quad(flux_y_pl, ymin, ymax, args=(emass, q2maxv))

# print(result_e)

# flux_01_2 = flux_y_dipole(0.1, pmass, 2.)
# print(flux_01_2)
# flux_01_25 = flux_y_dipole(0.1, pmass, 25.)
# print(flux_01_25)
# flux_001_25 = flux_y_dipole(0.01, pmass, 25.)
# print(flux_001_25)


# flux_inel_w200 = flux_inel_yy_atW(200., 50., 7000., 25., 1000., 1000.)
# print(flux_inel_w200)
# syy = 2 * flux_inel_w200[0] / 200.
# print(syy)

# last two arguments: mNmax (not squared), Q2max (squared)
# wvalue = 20.
# flux_inel_w = flux_inel_yy_atW(wvalue, 50., 7000., 25., 1000., 1000.)
# print(flux_inel_w)
# syy = 2 * flux_inel_w[0] / wvalue
# print(syy)

# flux_w200 = flux_el_yy_atW(wvalue, 50., 7000., 25., 1000.)
# print(flux_w200)
# syy = 2 * flux_w200[0] / wvalue
# print(syy)


