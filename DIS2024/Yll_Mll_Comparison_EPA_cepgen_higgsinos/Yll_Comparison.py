import ROOT
import array
import numpy as np
import sys

##################################################################
ROOT.gStyle.SetOptStat(0)  # Remove the statistics box from the plots

integrated_cross_section_value_E  = 1.01516903e-03  # pb
integrated_cross_section_value_QE = 9.35686193e-04  # pb

bin_width_correction = 10.0

##################################################################

def compare_distributions(filename):
    # Open the ROOT file
    file = ROOT.TFile(filename)
    if file.IsZombie():
        print("Error: Could not open file", filename)
        return

    # Get the TTree objects
    tree_E = file.Get("LHeC_E")
    tree_QE = file.Get("LHeC_QE")
    if not tree_E or not tree_QE:
        print("Error: Could not retrieve TTrees from the file")
        file.Close()
        return

    # Create arrays to hold Yll values
    Yll_E = []
    Yll_QE = []

    # Fill arrays with Yll values
    for event in tree_E:
        Yll_E.append(event.Yll)
    for event in tree_QE:
        Yll_QE.append(event.Yll)

    # Create ROOT histograms for Yll
    hist_Yll_E = ROOT.TH1F("hist_Yll_E", "", 100, 0.0, 10.0)
    hist_Yll_QE = ROOT.TH1F("hist_Yll_QE", "", 100, 0.0, 10.0)

    # Fill histograms with Yll values with weights
    for y in Yll_E:
        hist_Yll_E.Fill(y, bin_width_correction*integrated_cross_section_value_E / len(Yll_E))
    for y in Yll_QE:
        hist_Yll_QE.Fill(y, bin_width_correction*integrated_cross_section_value_QE / len(Yll_QE))

    # Load Yll data from Matplotlib
    from dSigmadY_10_100_100_higgsinos_MN100 import wvalues, elas, inel
    Yll_MPL = wvalues[3][:303]

    # Create ROOT graphs for Yll from Matplotlib data
    graph_Yll_MPL_elastic = ROOT.TGraph(len(Yll_MPL), array.array('d', Yll_MPL), array.array('d', elas[3][:303]))
    graph_Yll_MPL_inelastic = ROOT.TGraph(len(Yll_MPL), array.array('d', Yll_MPL), array.array('d', inel[3][:303]))

# Plot histograms and graphs for Yll
    canvas_Yll = ROOT.TCanvas("canvas_Yll", "Yll Comparison", 900, 800)
    hist_Yll_E.SetLineColor(ROOT.kMagenta)
    hist_Yll_E.GetYaxis().SetTitle("d#sigma/dY_{higgsinos} [pb/GeV]")  # Y-axis title
    hist_Yll_E.GetXaxis().SetTitle("Y_{higgsinos}")  # X-axis title
    hist_Yll_E.SetMinimum(0)  # Set y-axis minimum to 0
    hist_Yll_E.SetMaximum(0.001)  # Set y-axis maximum to 0.001
    hist_Yll_E.SetLineWidth(1)

## Set scientific notation for y-axis labels
    #hist_Yll_E.GetYaxis().SetLabelOffset(0.03)  # Adjust label offset
    #hist_Yll_E.GetYaxis().SetLabelSize(0.03)  # Adjust label size
## Format the y-axis labels as scientific notation manually
    #hist_Yll_E.GetYaxis().SetMoreLogLabels(False)  # Enable more space for labels
    #hist_Yll_E.GetYaxis().SetNoExponent(True)  # Disable automatic exponent format
    hist_Yll_E.Draw()


    hist_Yll_QE.SetLineColor(ROOT.kGreen)
    hist_Yll_QE.SetLineWidth(1)
    hist_Yll_QE.Draw("SAME")



    # Set the line color and style for the elastic (EPA) and inelastic (EPA) graphs
    graph_Yll_MPL_elastic.SetLineColor(ROOT.kBlue)
    graph_Yll_MPL_elastic.SetLineStyle(1)  # Solid line
    graph_Yll_MPL_elastic.SetLineWidth(2)  # Solid line
    graph_Yll_MPL_elastic.Draw("SAME")

    graph_Yll_MPL_inelastic.SetLineColor(ROOT.kRed)
    graph_Yll_MPL_inelastic.SetLineStyle(2)  # Dashed line
    graph_Yll_MPL_inelastic.SetLineWidth(2)  # Dashed line
    graph_Yll_MPL_inelastic.Draw("SAME")



    # Add legend for Yll with a larger box
    legend_Yll = ROOT.TLegend(0.6, 0.6, 0.85, 0.85)
    legend_Yll.AddEntry(graph_Yll_MPL_elastic, "elastic (EPA)", "l")
    legend_Yll.AddEntry(graph_Yll_MPL_inelastic, "inelastic (EPA)", "l")
    legend_Yll.AddEntry(hist_Yll_E, "elastic (cepgen)", "l")
    legend_Yll.AddEntry(hist_Yll_QE, "inelastic (cepgen)", "l")
    legend_Yll.SetBorderSize(1)  # Set the border size of the legend
    legend_Yll.SetLineColor(ROOT.kGray)  # Set the border color of the legend
    legend_Yll.Draw()




    # Add information for Yll
    latex_Yll = ROOT.TLatex()
    latex_Yll.SetNDC()
    latex_Yll.SetTextFont(42)
    latex_Yll.SetTextSize(0.03)
    latex_Yll.DrawLatex(0.15, 0.85,
                        "LHeC (E_{e}=50 GeV; E_{p}=7000 GeV)")
    latex_Yll.DrawLatex(0.15, 0.78,
                        "Q^{2}_{e}<10^{2} GeV^{2}; Q^{2}_{p}<10^{2} GeV^{2}; M_{N}<10 GeV")
    latex_Yll.DrawLatex(0.24, 0.72,
                        "M_{higgsinos} = 100 GeV")

    # Save the plot for Yll as a PDF file
    canvas_Yll.SaveAs("Yll_Comparison_higgsinos_DIS2024.pdf")

    # Draw the canvas
    canvas_Yll.Draw()

##################################################################

    # Calculate area under the curve for each distribution
    area_Yll_E = hist_Yll_E.Integral() / bin_width_correction
    area_Yll_QE = hist_Yll_QE.Integral() / bin_width_correction

    print("Area under the curve for Yll (elastic (cepgen)):", area_Yll_E)
    print("Area under the curve for Yll (inelastic (cepgen)):", area_Yll_QE)

    # Calculate area under the curve for Matplotlib data
    area_Yll_MPL_elastic = 0
    area_Yll_MPL_inelastic = 0
    for i in range(len(Yll_MPL) - 1):
        area_Yll_MPL_elastic += (Yll_MPL[i + 1] - Yll_MPL[i]) * (elas[3][i + 1] + elas[3][i]) / 2
        area_Yll_MPL_inelastic += (Yll_MPL[i + 1] - Yll_MPL[i]) * (inel[3][i + 1] + inel[3][i]) / 2

    print("Area under the curve for Yll (elastic (EPA)):", area_Yll_MPL_elastic)
    print("Area under the curve for Yll (inelastic (EPA)):", area_Yll_MPL_inelastic)

    # Cleanup
    file.Close()

# Call the function with the filename of the ROOT file
compare_distributions("LHeC_higgsino_Compare.root")



