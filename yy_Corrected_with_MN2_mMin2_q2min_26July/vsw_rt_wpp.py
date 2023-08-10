from ROOT import TCanvas, TGraph, TLegend
from ROOT import gROOT, gPad

import numpy as np
import sys

sys.path.append('./values')
# from syy_1_3_3_0804 import *
# from syy_1_3_4_0805 import *
# from syy_1_4_4_0907 import *
from wgrid_1_4_4_0908 import *

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

# fig, ax = plt.subplots(figsize = (9., 8.))
# ax.set_xlim(10., 1000.)
# ax.set_ylim(2.e-7, 2.e-2)

c1 = TCanvas('c1', 'S_{#gamma#gamma} at the LHeC', 500, 500)
c1.SetLogy()
c1.SetLogx()

gPad.SetLeftMargin(0.15)
gPad.SetBottomMargin(0.12)

inel_label1 = 'M_{N}< ' + str(inel[0]) + 'GeV'
title_label = 'Q^{2}_{e/p} < ' + str(inel[1]) + '/' + str(inel[2]) + 'GeV^{2}'

# plt.loglog(wvalues[3][:101], elas[3][:101], 'b-', label = 'elastic')
# plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
# plt.grid()

gr1 = TGraph(len(wv[:101]), wv[:101], el[:101])
gr1.SetLineColor(1)
gr1.SetLineWidth(2)
gr1.GetXaxis().SetTitle('W [GeV]')
gr1.GetXaxis().SetTitleOffset(1.3)
gr1.GetXaxis().SetLimits(10., 1000.)
gr1.GetXaxis().SetMoreLogLabels()
gr1.GetYaxis().SetTitle('S_{#gamma#gamma} [1/GeV]')
gr1.SetMinimum(2.e-7)
gr1.SetMaximum(2.e-2)
gr1.SetTitle('')
# gr1.SetTitle('S_{#gamma#gamma} at the LHeC')
gr1.Draw('AC')

gri1 = TGraph(len(wv[:101]), wv[:101], ie[:101])
gri1.SetLineStyle(2)
gri1.SetLineWidth(2)
gri1.Draw('C')


# from syy_2_3_3_0804 import *
# from syy_2_3_4_0805 import *
# from syy_2_4_4_0907 import *
from wgrid_2_4_4_0908 import *

inel_label2 = 'M_{N}< ' + str(inel[0]) + 'GeV'

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

gri2 = TGraph(len(wv[:101]), wv[:101], ie[:101])
gri2.SetLineStyle(3)
gri2.SetLineWidth(3)
gri2.Draw('C')

# plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
# plt.legend(title = title_label)

# from syy_3_3_3_0804 import *
# from syy_3_3_4_0805 import *
# from syy_3_4_4_0907 import *
from wgrid_3_4_4_0908 import *

inel_label3 = 'M_{N}< ' + str(inel[0]) + 'GeV'

wv = np.array(wvalues[3])
ie = np.array(inel[3])
el = np.array(elas[3])

gri3 = TGraph(len(wv[:101]), wv[:101], ie[:101])
gri3.SetLineStyle(4)
gri3.SetLineWidth(4)
gri3.Draw('C')

# draw pp values for elastic

wvpp = np.array((50., 100., 150., 200., 250., 500.))
syypp = np.array((7.0e-5, 3.5e-5, 2.2e-5, 1.5e-5, 1.05e-5, 3.0e-6))

gri4 = TGraph(6, wvpp, syypp)
gri4.SetLineStyle(1)
gri4.SetLineWidth(1)
# gri4.SetMarkerStyle(20)
# gri4.SetMarkerSize(0.8)
gri4.Draw('C')

leg = TLegend(0.45, 0.65, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetHeader(title_label, '')
leg.AddEntry(gr1, 'Elastic', 'l')
leg.AddEntry(gri1, 'Inelastic ' + inel_label1, 'l')
leg.AddEntry(gri2, 'Inelastic ' + inel_label2, 'l')
leg.AddEntry(gri3, 'Inelastic ' + inel_label3, 'l')
leg.AddEntry(gri4, 'Elastic LHC pp', 'l')
leg.Draw()

# plt.loglog(wvalues[3][:101], inel[3][:101], '-', label = inel_label)
# plt.legend(title = title_label)

# plt.show()

