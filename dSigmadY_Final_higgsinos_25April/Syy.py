
# Final Version -- Febraury 2024 -- Hamzeh Khanpour

import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integ
import ALLM


# units in GeV

# v3->newest: integration in dQ^2/Q^2 -> dlnQ^2


ALPHA2PI =  7.2973525693e-3 / math.pi  #  * 0.5                                # Hamzeh

emass    =  5.1099895e-4
pmass    =  0.938272081
pi0mass  =  0.1349768



def qmin2(mass, y):
    return mass * mass * y * y / (1 - y)



# --------------------------------------------------------------


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



# --------------------------------------------------------------



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



# --------------------------------------------------------------



def flux_y_inel(y, mMin2, qmax2, mNmax, pout=False): 
    if (y <= 0 or y >= 1):
        print('invalid y value: ', y)
        return -1.0
    else:
        qmin2v = (mMin2*mMin2 / (1 - y) - pmass * pmass) * y                 # Hamzeh mMin2-> mMin2*mMin2
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



# --------------------------------------------------------------



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



# --------------------------------------------------------------



def flux_y_q2_inel_mN2(lnq2, yp, mMin2, nMmax, qmin2v, pout=False):
        # integration variable: q2
	#

        qmin2v = (mMin2*mMin2 / (1 - yp) - pmass * pmass) * yp                                  # Hamzeh

        formE = ALLM.allm_formE_qmin2(math.exp(lnq2), yp, mMin2, nMmax)[0]
        formMq2 = ALLM.allm_formM_mN2(math.exp(lnq2), yp, mMin2, nMmax)[0]

        # formM was divided by q2*q2 -> should be q2?? Why?
        formMNew = formMq2 / ( math.exp(lnq2) * math.exp(lnq2) )  #                               # Hamzeh
        formENew = formE # * ( 1.0 - qmin2v / math.exp(lnq2) )       #  / ( math.exp(lnq2) )      # Hamzeh

        flux_tmp = (1 - yp) * formENew \
                    + yp * yp * 0.5 * formMNew
        flux_tmp *= ALPHA2PI / yp
        if pout:
            print('inel q2, y, E M flux: {:.4e} {:.4e} {:.4e} {:.4e} {:.4e}'
#                  .format(q2, yp, formE, formM / math.exp(lnq2), flux_tmp))
                  .format(q2, yp, formENew, formMNew, flux_tmp))                               # Hamzeh
        return flux_tmp






##################################################################

# Sigma_{gamma_gamma} for higgsionos

def cs_higgsionos_w_condition_Hamzeh(wvalue):

    mhiggsionos = 200.0

    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * mhiggsionos * mhiggsionos / wvalue**2.0 >= 0, 1.0 - 4.0 * mhiggsionos * mhiggsionos / wvalue**2.0, np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > mhiggsionos, (4.0 * np.pi * alpha2 * hbarc2 ) / wvalue**2.0 * (beta) * \
             ( (3.0 - (beta**4.0))/(2.0 * beta) * np.log((1.0+beta)/(1.0-beta)) - 2.0 + beta**2.0), 0.) * 1e9

    return cs


##################################################################




# picking up proton and electron mass as external constants
def flux_yy_atye(w, Y, qmax2e, qmax2p, s_cms, eEbeam, pEbeam, pout=False):

#    yp = w * w / s_cms / ye

    yp = w * math.exp(Y)  / (2.0*pEbeam)
    ye = w * math.exp(-Y) / (2.0*eEbeam)

    if (yp <= 0.01 or yp >= 0.20 or ye <= 0.0 or ye >= 1.0):                    # Hamzeh take care of tagged elastic    if (yp <= 0.01 or yp >= 0.20):
        print('invalid yp value: ', yp)
        print('invalid ye value: ', ye)
        return 0.0


    if pout:
        print(emass, pmass, w, Y, qmax2e, s_cms)
    flux_prod = cs_higgsionos_w_condition_Hamzeh(w) * flux_y_dipole(yp, pmass, qmax2p) \
                * w * flux_y_pl(ye, emass, qmax2e)


    return flux_prod




# --------------------------------------------------------------



# inelastic flux at given ye and W
def flux_yyinel_atye(w, Y, qmax2e, qmax2p, mNmax, s_cms, eEbeam, pEbeam, pout=False):

#    yp = w * w / s_cms / ye

    yp = w * math.exp(Y)  / (2.0*pEbeam)
    ye = w * math.exp(-Y) / (2.0*eEbeam)

    if (yp <= 0.0 or yp >= 1.0 or ye <= 0.0 or ye >= 1.0):
        print('invalid yp value: ', yp)
        print('invalid ye value: ', ye)
        return 0.0


    minM2 = (pmass + pi0mass)# * (pmass + pi0mass)                                           # Hamzeh

    # given: ye, w, qmax2e, qmax2p, cms energy
    # calculated inside here: gamma **Monochrome** energy on proton side (yp)
    #   and: minimum mass M_N, to pass
    # point-like on the electron side
    # according to Eq.(A.1)
    flux_prod = cs_higgsionos_w_condition_Hamzeh(w) * flux_y_inel(yp, minM2, qmax2p, mNmax) \
                * w * flux_y_pl(ye, emass, qmax2e)
    if pout:
        print(emass, pmass, w, Y, qmax2e, s_cms, flux_prod)

    return flux_prod



# --------------------------------------------------------------



def flux_el_yy_atW(Y, eEbeam, pEbeam, qmax2e, qmax2p):
    # first calculate the ymin for e-side, p-side

    s_cms = 4.0 * eEbeam * pEbeam
    sqrt_cms = math.sqrt(4.0 * eEbeam * pEbeam)

    w0 = 400.000001

#    ymin = w * w / s_cms

#    print(' Y value: ', Y)

    fyyatw = integ.quad(flux_yy_atye, w0, sqrt_cms,
                        args=(Y, qmax2e, qmax2p, s_cms, eEbeam, pEbeam))
    return fyyatw


# --------------------------------------------------------------



def flux_inel_yy_atW(Y, eEbeam, pEbeam, qmax2e, mNmax, qmax2p):
    # first calculate the ymin for e-side, p-side

    s_cms = 4.0 * eEbeam * pEbeam
    sqrt_cms = math.sqrt(4.0 * eEbeam * pEbeam)

    w0 = 400.000001

#    ymin = w * w / s_cms

    # flux for ymin -> 1., at a given w.
    # Qmax2e, Qmax2p are given from experimental constraints (beam holes)
    # integration according to Eq.(A.1) apart from 2/W (external)
    fyyatw = integ.quad(flux_yyinel_atye, w0, sqrt_cms,
                        args=(Y, qmax2e, qmax2p, mNmax, s_cms, eEbeam, pEbeam),
			epsrel=1.e-2)
#			epsabs=1.e-5, epsrel=1.e-5)
    return fyyatw


# --------------------------------------------------------------


