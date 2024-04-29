
# Hamzeh Khanpour -- 30 April

import ROOT
import array


ROOT.gStyle.SetOptStat(0)  # Remove the statistics box from the plots


integrated_cross_section_value_E = 48.8223395  # pb
integrated_cross_section_value_QE = 24.703  # pb

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

    # Create arrays to hold Mll, Yll, and q2prime values
    Mll_E = array.array('f', [0.0])
    Mll_QE = array.array('f', [0.0])
    Yll_E = array.array('f', [0.0])
    Yll_QE = array.array('f', [0.0])
    q2prime_E = array.array('f', [0.0])
    q2prime_QE = array.array('f', [0.0])

    # Set branch addresses
    tree_E.SetBranchAddress("Mll", Mll_E)
    tree_E.SetBranchAddress("Yll", Yll_E)
    tree_E.SetBranchAddress("q2prime", q2prime_E)
    tree_QE.SetBranchAddress("Mll", Mll_QE)
    tree_QE.SetBranchAddress("Yll", Yll_QE)
    tree_QE.SetBranchAddress("q2prime", q2prime_QE)

    # Create histograms for Mll, Yll, and q2prime
    hist_Mll_E = ROOT.TH1F("hist_Mll_E", "Mll distribution", 500, 10, 500)
    hist_Mll_QE = ROOT.TH1F("hist_Mll_QE", "Mll distribution", 500, 10, 500)
    hist_Yll_E = ROOT.TH1F("hist_Yll_E", "Yll distribution", 100, -10.0, 10.0)
    hist_Yll_QE = ROOT.TH1F("hist_Yll_QE", "Yll distribution", 100, -10.0, 10.0)
    hist_q2prime_E = ROOT.TH1F("hist_q2prime_E", "q2prime distribution", 50, 0.0, 100.0)
    hist_q2prime_QE = ROOT.TH1F("hist_q2prime_QE", "q2prime distribution", 50, 0.0, 100.0)

    # Fill histograms and apply weighting for Mll
    for i in range(tree_E.GetEntries()):
        tree_E.GetEntry(i)
        weight = integrated_cross_section_value_E / tree_E.GetEntries()
        hist_Mll_E.Fill(Mll_E[0], weight)
        hist_Yll_E.Fill(Yll_E[0], weight*5)
        hist_q2prime_E.Fill(q2prime_E[0])

    for i in range(tree_QE.GetEntries()):
        tree_QE.GetEntry(i)
        weight = integrated_cross_section_value_QE / tree_QE.GetEntries()
        hist_Mll_QE.Fill(Mll_QE[0], weight)
        hist_Yll_QE.Fill(Yll_QE[0], weight*5)
        hist_q2prime_QE.Fill(q2prime_QE[0])


    # Calculate area under the curve for each distribution
    area_Mll_E = hist_Mll_E.Integral()
    area_Mll_QE = hist_Mll_QE.Integral()
    area_Yll_E = hist_Yll_E.Integral()/5.0
    area_Yll_QE = hist_Yll_QE.Integral()/5.0
    area_q2prime_E = hist_q2prime_E.Integral()
    area_q2prime_QE = hist_q2prime_QE.Integral()

    print("Area under the curve for Mll (elastic):", area_Mll_E)
    print("Area under the curve for Mll (quasi-elastic):", area_Mll_QE)
    print("Area under the curve for Yll (elastic):", area_Yll_E)
    print("Area under the curve for Yll (quasi-elastic):", area_Yll_QE)
    print("Area under the curve for q2prime (elastic):", area_q2prime_E)
    print("Area under the curve for q2prime (quasi-elastic):", area_q2prime_QE)


    # Plot histograms for Mll
    canvas_Mll = ROOT.TCanvas("canvas_Mll", "Mll Comparison", 800, 600)
    hist_Mll_E.SetLineColor(ROOT.kBlue)
    hist_Mll_E.SetMinimum(1e-4)  # Set minimum y-axis value
    hist_Mll_E.SetMaximum(100)   # Set maximum y-axis value
    hist_Mll_E.GetYaxis().SetTitle("d#sigma/dM_{#tau^{+}#tau^{-}} [pb/GeV]")  # Y-axis title
    hist_Mll_E.GetXaxis().SetTitle("M_{#tau^{+}#tau^{-}} [GeV] = W_{#gamma#gamma} [GeV]")  # X-axis title
    hist_Mll_E.Draw()
    hist_Mll_QE.SetLineColor(ROOT.kRed)
    hist_Mll_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
    canvas_Mll.SetLogy()
    canvas_Mll.SetLogx()


    # Add legend for Mll
    legend_Mll = ROOT.TLegend(0.7, 0.7, 0.85, 0.85)
    legend_Mll.AddEntry(hist_Mll_E, "elastic", "l")
    legend_Mll.AddEntry(hist_Mll_QE, "quasi-elastic", "l")
    legend_Mll.SetBorderSize(0)  # Remove the border around the legend
    legend_Mll.Draw()


    # Add information for Mll
    latex_Mll = ROOT.TLatex()
    latex_Mll.SetNDC()
    latex_Mll.SetTextFont(42)
    latex_Mll.SetTextSize(0.035)
    latex_Mll.DrawLatex(0.15, 0.8, "Q^{2}_{e,max}<10^{2} GeV^{2};  Q^{2}_{p,max}<10^{2} GeV^{2}; #color[2]{(#tau^{+}#tau^{-}) cepgen}")


    # Save the plot for Mll as a PDF file
    canvas_Mll.SaveAs("Mll_Comparison.pdf")

    # Plot histograms for Yll
    canvas_Yll = ROOT.TCanvas("canvas_Yll", "Yll Comparison", 800, 600)
    hist_Yll_E.SetLineColor(ROOT.kBlue)
    hist_Yll_E.GetYaxis().SetTitle("d#sigma/dY_{#tau^{+}#tau^{-}} [pb/GeV]")  # Y-axis title
    hist_Yll_E.GetXaxis().SetTitle("Y_{#tau^{+}#tau^{-}}")  # X-axis title
    hist_Yll_E.Draw()
    hist_Yll_QE.SetLineColor(ROOT.kRed)
    hist_Yll_QE.Draw("SAME")

    # Add legend for Yll
    legend_Yll = ROOT.TLegend(0.7, 0.7, 0.85, 0.85)
    legend_Yll.AddEntry(hist_Yll_E, "elastic", "l")
    legend_Yll.AddEntry(hist_Yll_QE, "quasi-elastic", "l")
    legend_Yll.SetBorderSize(0)  # Remove the border around the legend
    legend_Yll.Draw()

    # Add information for Yll
    latex_Yll = ROOT.TLatex()
    latex_Yll.SetNDC()
    latex_Mll.SetTextFont(42)
    latex_Mll.SetTextSize(0.035)
    latex_Mll.DrawLatex(0.15, 0.8, "Q^{2}_{e,max}<10^{2} GeV^{2};  Q^{2}_{p,max}<10^{2} GeV^{2}; #color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for Yll as a PDF file
    canvas_Yll.SaveAs("Yll_Comparison.pdf")

    # Plot histograms for q2prime
    canvas_q2prime = ROOT.TCanvas("canvas_q2prime", "q2prime Comparison", 800, 600)
    hist_q2prime_E.SetLineColor(ROOT.kBlue)
    hist_q2prime_E.GetYaxis().SetTitle("# Event")  # Y-axis title
    hist_q2prime_E.GetXaxis().SetTitle("q^{2}_{p, max} [GeV^{2}]")  # X-axis title
    hist_q2prime_E.Draw()
    hist_q2prime_QE.SetLineColor(ROOT.kRed)
    hist_q2prime_QE.Draw("SAME")


    # Set y-axis to logarithmic scale
    canvas_q2prime.SetLogy()


    # Add legend for q2prime
    legend_q2prime = ROOT.TLegend(0.7, 0.7, 0.85, 0.85)
    legend_q2prime.AddEntry(hist_q2prime_E, "elastic", "l")
    legend_q2prime.AddEntry(hist_q2prime_QE, "quasi-elastic", "l")
    legend_q2prime.SetBorderSize(0)  # Remove the border around the legend
    legend_q2prime.Draw()

    # Add information for q2prime
    latex_q2prime = ROOT.TLatex()
    latex_q2prime.SetNDC()
    latex_Mll.SetTextFont(42)
    latex_Mll.SetTextSize(0.035)
    latex_Mll.DrawLatex(0.15, 0.8, "Q^{2}_{e,max}<10^{2} GeV^{2};  Q^{2}_{p,max}<10^{2} GeV^{2}; #color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for q2prime as a PDF file
    canvas_q2prime.SaveAs("q2prime_Comparison.pdf")

    # Cleanup
    file.Close()

# Call the function with the filename of the ROOT file
compare_distributions("/home/hamzeh-khanpour/Desktop/lpair_tau_tau_E/LHeC_Compare.root")
