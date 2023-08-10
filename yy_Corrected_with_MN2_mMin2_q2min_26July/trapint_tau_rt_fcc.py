# import matplotlib.pyplot as plt

from ROOT import TCanvas, TGraph, TLegend
from ROOT import gROOT, gPad

import numpy as np
import sys

def cs_tautau_w(wvalue):
    re = 2.8179403262e-15 * 137. / 128.
    me = 0.510998950e-3
    mtau = 1.77686

    cs = 4. * np.pi * re * re * me * me / wvalue / wvalue \
         * (np.log(wvalue * wvalue / mtau / mtau) - 1)

    return cs
    

def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        cs_0 = cs_tautau_w(wv[i])
        cs_1 = cs_tautau_w(wv[i + 1])
        traparea = wvwid * 0.5 * (fluxv[i] * cs_0 + fluxv[i + 1] * cs_1)
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    nanobarn = 1.e+40

    return wmin, integ * nanobarn


sys.path.append('./values')

# from wgrid_15_3_3_1018 import *
from syy_fcc_15_3_3_0430 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

# section pyplot
# fig, ax = plt.subplots(figsize = (9., 8.))
c1 = TCanvas('c1', '#gamma#gamma #rightarrow #tau#tau at the LHeC', 700, 700)
c1.SetLogy()
c1.SetLogx()
# ax.set_xlim(10., 1000.)
# ax.set_ylim(1.e-3, 1.e2)
## c1.DrawFrame(10., 1.e-3, 1000., 1.e2)

gPad.SetLeftMargin(0.15)
gPad.SetBottomMargin(0.12)

inel_label = 'M_{N} < ' + str(inel[0]) + 'GeV'
title_label = 'Q^{2}_{e/p} < ' + str(inel[1]) + '/' + str(inel[2]) + ' GeV^{2}'

gr1 = TGraph(len(wv2[:126]), wv2[:126], int_el[:126])
gr1.SetLineColor(1)
gr1.SetLineWidth(2)
gr1.GetXaxis().SetTitle('W [GeV]')
gr1.GetXaxis().SetTitleOffset(1.3)
gr1.GetXaxis().SetLimits(10., 3000.)
gr1.GetYaxis().SetTitle('#sigma_{#tau#tau} (W > W_{0}) [pb]')
gr1.SetMinimum(1.e-3)
gr1.SetMaximum(1.e2)
gr1.SetTitle('')
# gr1.SetTitle('#gamma#gamma #rightarrow #tau#tau at the LHeC')
gr1.Draw('AC')

gr2 = TGraph(len(wv1[:126]), wv1[:126], int_inel[:126])
gr2.SetLineStyle(2)
gr2.SetLineWidth(2)
gr2.Draw('C')

leg = TLegend(0.5, 0.7, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetHeader(title_label, '')
leg.AddEntry(gr1, 'Elastic', 'l')
leg.AddEntry(gr2, 'Inelastic ' + inel_label, 'l')
leg.Draw()


# plt.loglog(wv2[:126], int_el[:126], 'b-', label = 'elastic')
# plt.loglog(wv1[:126], int_inel[:126], '-', label = inel_label)
# plt.legend(title = title_label)
# plt.grid()


"""
from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv1[:126], int_inel[:126], '-', label = inel_label)
plt.legend(title = title_label)

from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label = 'M_N < ' + str(inel[0])
plt.loglog(wv2[:126], int_inel[:126], '-', label = inel_label)
plt.legend(title = title_label)
"""

# plt.show()
