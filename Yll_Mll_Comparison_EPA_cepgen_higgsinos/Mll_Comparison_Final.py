import ROOT
import array
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

# Import data for cross-section calculation
from wgrid_10_100_100 import *

# ROOT settings
ROOT.gStyle.SetOptStat(0)  # Remove the statistics box from the plots

# Integrated cross-section values
integrated_cross_section_value_E  = 1.01516903e-03  # pb
integrated_cross_section_value_QE = 9.35686193e-04  # pb

bin_width_correction = 1.0


##################################################################


# Function to compare Mll distributions
def compare_Mll_distributions(filename_root):
    # Open the ROOT file
    file_root = ROOT.TFile(filename_root)
    if file_root.IsZombie():
        print("Error: Could not open ROOT file", filename_root)
        return

    # Get the TTree objects from ROOT file
    tree_E = file_root.Get("LHeC_E")
    tree_QE = file_root.Get("LHeC_QE")
    if not tree_E or not tree_QE:
        print("Error: Could not retrieve TTrees from the ROOT file")
        file_root.Close()
        return

    # Create arrays to hold Mll values from ROOT
    Mll_E = array.array('f', [0.0])
    Mll_QE = array.array('f', [0.0])

    # Set branch addresses for Mll in ROOT
    tree_E.SetBranchAddress("Mll", Mll_E)
    tree_QE.SetBranchAddress("Mll", Mll_QE)

    # Create histograms for Mll from ROOT
    hist_Mll_E = ROOT.TH1F("hist_Mll_E", "Mll distribution", 300, 200, 500)
    hist_Mll_QE = ROOT.TH1F("hist_Mll_QE", "Mll distribution", 300, 200, 500)

    # Fill histograms for Mll from ROOT
    for i in range(tree_E.GetEntries()):
        tree_E.GetEntry(i)
        weight = integrated_cross_section_value_E / tree_E.GetEntries()
        hist_Mll_E.Fill(Mll_E[0], bin_width_correction * weight)

    for i in range(tree_QE.GetEntries()):
        tree_QE.GetEntry(i)
        weight = integrated_cross_section_value_QE / tree_QE.GetEntries()
        hist_Mll_QE.Fill(Mll_QE[0], bin_width_correction * weight)

    # Plot histograms for Mll using ROOT
    canvas_Mll = ROOT.TCanvas("canvas_Mll", "Mll Comparison", 800, 600)
    hist_Mll_E.SetLineColor(ROOT.kBlue)
    hist_Mll_E.SetMinimum(1e-6)  # Set minimum y-axis value
    hist_Mll_E.SetMaximum(1e-4)  # Set maximum y-axis value
    hist_Mll_E.GetYaxis().SetTitle("d#sigma/dM_{higgsino} [pb/GeV]")  # Y-axis title
    hist_Mll_E.GetXaxis().SetTitle("M_{higgsino} [GeV] = W_{#gamma#gamma} [GeV]")  # X-axis title
    hist_Mll_E.Draw()
    hist_Mll_QE.SetLineColor(ROOT.kRed)
    hist_Mll_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
    canvas_Mll.SetLogy()
    canvas_Mll.SetLogx()

    # Add legend for Mll
    legend_Mll = ROOT.TLegend(0.7, 0.7, 0.85, 0.85)
    legend_Mll.AddEntry(hist_Mll_E, "elastic (cepgen)", "l")
    legend_Mll.AddEntry(hist_Mll_QE, "quasi-elastic (cepgen)", "l")
    legend_Mll.SetBorderSize(0)  # Remove the border around the legend
    legend_Mll.Draw()

    # Add information for Mll
    latex_Mll = ROOT.TLatex()
    latex_Mll.SetNDC()
    latex_Mll.SetTextFont(42)
    latex_Mll.SetTextSize(0.035)
    latex_Mll.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2};  Q^{2}_{p,max}<10^{2} GeV^{2}; #color[2]{(higgsino) cepgen}")

    # Save the plot for Mll as a PDF file
    canvas_Mll.SaveAs("Mll_Comparison_root_mathplotlib_Final.pdf")

    # Draw the canvas
    canvas_Mll.Draw()


    # Calculate the area under the histograms
    area_hist_E = hist_Mll_E.Integral() * bin_width_correction
    area_hist_QE = hist_Mll_QE.Integral() * bin_width_correction

    print("Area under elastic histogram (lpair):", area_hist_E, "pb*GeV")
    print("Area under quasi-elastic histogram (lpair):", area_hist_QE, "pb*GeV")


##################################################################


    # Calculate elastic and inelastic cross-sections using provided data
    wv = np.array(wvalues[3])
    ie = np.array(inel[3])
    el = np.array(elas[3])

    wv1, int_inel = trap_integ(wv, ie)
    wv2, int_el = trap_integ(wv, el)

    # Matplotlib plot for elastic and inelastic cross-sections
    fig, ax = plt.subplots(figsize=(9.0, 8.0))
    ax.set_xlim(200.0, 500.0)
    ax.set_ylim(1.0e-6, 1.0e-4)

    # Plot elastic and inelastic cross-sections
    ax.loglog(wv2, int_el, linestyle='solid', linewidth=2, label='elastic (EPA)')
    ax.loglog(wv1, int_inel, linestyle='dotted', linewidth=2, label='inelastic (EPA)')

    # Convert ROOT histograms to numpy arrays
    Mll_E_array = np.array([hist_Mll_E.GetBinContent(i) for i in range(1, hist_Mll_E.GetNbinsX() + 1)])
    Mll_QE_array = np.array([hist_Mll_QE.GetBinContent(i) for i in range(1, hist_Mll_QE.GetNbinsX() + 1)])
    bin_edges = np.linspace(200, 500, 301)

    # Plot ROOT histograms on the matplotlib plot
    ax.hist(bin_edges[:-1], bin_edges, weights=Mll_E_array, histtype='step', color='blue', linestyle='-',
            label='elastic (cepgen)')
    ax.hist(bin_edges[:-1], bin_edges, weights=Mll_QE_array, histtype='step', color='red', linestyle='-',
            label='quasi-elastic (cepgen)')

    # Set labels and legend
    ax.set_xlabel("W [GeV]", fontdict={'family': 'serif', 'color': 'black', 'size': 24})
    ax.set_ylabel("$d\sigma/dW (ep \\rightarrow e p higgsinos)$ [pb]",
                  fontdict={'family': 'serif', 'color': 'black', 'size': 24})
    ax.legend(title='Inelastic: $M_N<10$ GeV ($Q^2_p<10^2$ GeV$^2$)', fontsize=15)

    # Save the plot
    plt.savefig("Mll_Comparison_matplotlib_Final.pdf")

    # Show the plot
    plt.show()

    # Cleanup
    file_root.Close()

    # Calculate the area under the plots
    area_int_el = np.trapz(int_el, wv2)
    area_int_inel = np.trapz(int_inel, wv1)

    print("Area under elastic plot:", area_int_el)
    print("Area under inelastic plot:", area_int_inel)


##################################################################

# Sigma_{gamma_gamma} for higgsino


def cs_higgsino_w_condition_Hamzeh(wvalue):  # Eq.62 of Physics Reports 364 (2002) 359-450
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    mhiggsino = 100.0
    hbarc2 = 0.389
    alpha2 = (1.0 / 137.0) * (1.0 / 137.0)

    # Element-wise calculation of beta using np.where
    beta = np.sqrt(np.where(1.0 - 4.0 * mhiggsino * mhiggsino / wvalue ** 2.0 >= 0.0, 1.0 - 4.0 * mhiggsino * mhiggsino / wvalue ** 2.0,
                            np.nan))

    # Element-wise calculation of cs using np.where
    cs = np.where(wvalue > mhiggsino, (4.0 * np.pi * alpha2 * hbarc2) / wvalue ** 2.0 * (beta) * \
                                  ((3.0 - (beta ** 4.0)) / (2.0 * beta) * np.log((1.0 + beta) / (1.0 - beta)) - 2.0 +
                                   beta ** 2.0), 0.0) * 1e9 * 1.0

    return cs


##################################################################

def trap_integ(wv, fluxv):

    wmin = np.zeros(len(wv) - 1)
    integ = np.zeros(len(wv) - 1)

    for i in range(len(wv) - 2, -1, -1):
        traparea = fluxv[i] * cs_higgsino_w_condition_Hamzeh(wv[i])
        wmin[i] = wv[i]
        if i == len(wv) - 2:
            integ[i] = traparea
        else:
            integ[i] = traparea

    return wmin, integ


##################################################################


# Call the function with the filename of the ROOT file
compare_Mll_distributions("LHeC_higgsino_Compare.root")


##################################################################
