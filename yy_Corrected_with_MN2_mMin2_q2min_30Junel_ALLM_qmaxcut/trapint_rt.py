from ROOT import TCanvas, TGraph, TLegend
from ROOT import gROOT, gPad

import numpy as np
import sys

def trap_integ(wv, fluxv):
    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)
    for i in range(len(wv) - 2, -1, -1):
        wvwid = wv[i + 1] - wv[i]
        traparea = wvwid * 0.5 * (fluxv[i] + fluxv[i + 1])
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = integ[i + 1] + traparea

    return wmin, integ


sys.path.append('./values')

from wgrid_1_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

wv1, int_inel = trap_integ(wv, ie)
wv2, int_el = trap_integ(wv, el)

# fig, ax = plt.subplots(figsize = (9., 8.))
# ax.set_xlim(10., 1000.)
# ax.set_ylim(1.e-5, 1.e-1)

c1 = TCanvas('c1', 'Integrated S_{#gamma#gamma} (W > W_{0}) at the LHeC', 700, 700)
c1.SetLogy()
c1.SetLogx()

gPad.SetLeftMargin(0.15)
gPad.SetBottomMargin(0.12)

inel_label1 = 'M_{N} < ' + str(inel[0]) + 'GeV'
title_label = 'Q^{2}_{e/p} < ' + str(inel[1]) + '/' + str(inel[2]) + ' GeV^{2}'

# plt.loglog(wv2[:101], int_el[:101], 'b-', label = 'elastic')
# plt.loglog(wv1[:101], int_inel[:101], '-', label = inel_label)
# plt.grid()

gr1 = TGraph(len(wv2[:101]), wv2[:101], int_el[:101])
gr1.SetLineColor(1)
gr1.SetLineWidth(2)
gr1.GetXaxis().SetTitle('W_{0} [GeV]')
gr1.GetXaxis().SetTitleOffset(1.3)
gr1.GetXaxis().SetLimits(10., 1000.)
gr1.GetXaxis().SetMoreLogLabels()
gr1.GetYaxis().SetTitle('Integrated S_{#gamma#gamma} (W > W_{0})')
gr1.SetMinimum(1.e-5)
gr1.SetMaximum(2.e-1)
gr1.SetTitle('')
gr1.Draw('AC')

gri1 = TGraph(len(wv1[:101]), wv1[:101], int_inel[:101])
gri1.SetLineStyle(2)
gri1.SetLineWidth(2)
gri1.Draw('C')


from wgrid_2_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label2 = 'M_{N}< ' + str(inel[0]) + 'GeV'
# plt.loglog(wv1[:101], int_inel[:101], '-', label = inel_label)
# plt.legend(title = title_label)

gri2 = TGraph(len(wv1[:101]), wv1[:101], int_inel[:101])
gri2.SetLineStyle(3)
gri2.SetLineWidth(3)
gri2.Draw('C')

from wgrid_3_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
wv1, int_inel = trap_integ(wv, ie)

inel_label3 = 'M_{N}< ' + str(inel[0]) + 'GeV'
# plt.loglog(wv2[:101], int_inel[:101], '-', label = inel_label)
# plt.legend(title = title_label)

gri3 = TGraph(len(wv1[:101]), wv1[:101], int_inel[:101])
gri3.SetLineStyle(4)
gri3.SetLineWidth(4)
gri3.Draw('C')

leg = TLegend(0.5, 0.7, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetHeader(title_label, '')
leg.AddEntry(gr1, 'Elastic', 'l')
leg.AddEntry(gri1, 'Inelastic ' + inel_label1, 'l')
leg.AddEntry(gri2, 'Inelastic ' + inel_label2, 'l')
leg.AddEntry(gri3, 'Inelastic ' + inel_label3, 'l')
leg.Draw()

# plt.show()
