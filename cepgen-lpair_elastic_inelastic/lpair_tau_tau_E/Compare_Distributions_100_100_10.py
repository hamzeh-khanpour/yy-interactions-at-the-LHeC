

#  Hamzeh Khanpour -- 8 May 2024
#  cepgen-lpair_elastic_inelastic


import ROOT
import array
import matplotlib.pyplot as plt
import numpy as np
import sys
import math


ROOT.gStyle.SetOptStat(0)  # Remove the statistics box from the plots

integrated_cross_section_value_E  = 4.88223395e+01  # pb
integrated_cross_section_value_QE = 2.81581841e+01  # pb


bin_width_correction = 1.0


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

    # Create arrays to hold Mll, Yll, q2prime, and Ptll values
    Mll_E = array.array('f', [0.0])
    Mll_QE = array.array('f', [0.0])
    Yll_E = array.array('f', [0.0])
    Yll_QE = array.array('f', [0.0])
    q2prime_E = array.array('f', [0.0])
    q2prime_QE = array.array('f', [0.0])
    q2_E = array.array('f', [0.0])
    q2_QE = array.array('f', [0.0])
    Ptll_E = array.array('f', [0.0])
    Ptll_QE = array.array('f', [0.0])

    # Set branch addresses
    tree_E.SetBranchAddress("Mll", Mll_E)
    tree_E.SetBranchAddress("Yll", Yll_E)
    tree_E.SetBranchAddress("q2prime", q2prime_E)
    tree_E.SetBranchAddress("q2", q2_E)  # Add q2 branch address
    tree_E.SetBranchAddress("Ptll", Ptll_E)  # Add Ptll branch address
    tree_QE.SetBranchAddress("Mll", Mll_QE)
    tree_QE.SetBranchAddress("Yll", Yll_QE)
    tree_QE.SetBranchAddress("q2prime", q2prime_QE)
    tree_QE.SetBranchAddress("q2", q2_QE)  # Add q2 branch address
    tree_QE.SetBranchAddress("Ptll", Ptll_QE)  # Add Ptll branch address

    # Create histograms for Mll, Yll, q2prime, q2, and Ptll
    hist_Mll_E = ROOT.TH1F("hist_Mll_E", "Mll distribution", 500, 10, 500)
    hist_Mll_QE = ROOT.TH1F("hist_Mll_QE", "Mll distribution", 500, 10, 500)
    hist_Yll_E = ROOT.TH1F("hist_Yll_E", "Yll distribution", 100, -10.0, 10.0)
    hist_Yll_QE = ROOT.TH1F("hist_Yll_QE", "Yll distribution", 100, -10.0, 10.0)
    hist_q2prime_E = ROOT.TH1F("hist_q2prime_E", "q2 proton distribution", 100, 0.0, 100.0)
    hist_q2prime_QE = ROOT.TH1F("hist_q2prime_QE", "q2 proton distribution", 100, 0.0, 100.0)
    hist_q2_E = ROOT.TH1F("hist_q2_E", "q2 electron distribution", 100, 0.0, 100.0)
    hist_q2_QE = ROOT.TH1F("hist_q2_QE", "q2 electron distribution", 100, 0.0, 100.0)
    hist_Ptll_E = ROOT.TH1F("hist_Ptll_E", "Ptll distribution", 50, 0.0, 10.0)
    hist_Ptll_QE = ROOT.TH1F("hist_Ptll_QE", "Ptll distribution", 50, 0.0, 10.0)


    # Fill histograms for Mll, Yll, q2prime, q2, and Ptll
    for i in range(tree_E.GetEntries()):
        tree_E.GetEntry(i)
        weight = integrated_cross_section_value_E / tree_E.GetEntries()
        hist_Mll_E.Fill(Mll_E[0], weight)
        hist_Yll_E.Fill(Yll_E[0], weight)
        hist_q2prime_E.Fill(q2prime_E[0], weight)
        hist_q2_E.Fill(q2_E[0], weight)
        hist_Ptll_E.Fill(Ptll_E[0], weight)

    for i in range(tree_QE.GetEntries()):
        tree_QE.GetEntry(i)
        weight = integrated_cross_section_value_QE / tree_QE.GetEntries()
        hist_Mll_QE.Fill(Mll_QE[0], weight)
        hist_Yll_QE.Fill(Yll_QE[0], weight)
        hist_q2prime_QE.Fill(q2prime_QE[0], weight)
        hist_q2_QE.Fill(q2_QE[0], weight)
        hist_Ptll_QE.Fill(Ptll_QE[0], weight)

    # Calculate area under the curve for each distribution
    area_Mll_E = hist_Mll_E.Integral()
    area_Mll_QE = hist_Mll_QE.Integral()
    area_Yll_E = hist_Yll_E.Integral()
    area_Yll_QE = hist_Yll_QE.Integral()
    area_q2prime_E = hist_q2prime_E.Integral()
    area_q2prime_QE = hist_q2prime_QE.Integral()
    area_q2_E = hist_q2_E.Integral()
    area_q2_QE = hist_q2_QE.Integral()
    area_Ptll_E = hist_Ptll_E.Integral()
    area_Ptll_QE = hist_Ptll_QE.Integral()
    
    

    print("Area under the curve for Mll (elastic):", area_Mll_E)
    print("Area under the curve for Mll (inelastic):", area_Mll_QE)
    print("Area under the curve for Yll (elastic):", area_Yll_E)
    print("Area under the curve for Yll (inelastic):", area_Yll_QE)
    print("Area under the curve for q2 proton (elastic):", area_q2prime_E)
    print("Area under the curve for q2 proton (inelastic):", area_q2prime_QE)
    print("Area under the curve for q2 electron (elastic):", area_q2_E)
    print("Area under the curve for q2 electron (inelastic):", area_q2_QE)
    print("Area under the curve for Ptll (elastic):", area_Ptll_E)
    print("Area under the curve for Ptll (inelastic):", area_Ptll_QE)
    


    # Print histograms as text
    print("\nHistogram contents (Mll):")
    hist_Mll_E.Print()
    hist_Mll_QE.Print()

    print("\nHistogram contents (Yll):")
    hist_Yll_E.Print()
    hist_Yll_QE.Print()

    print("\nHistogram contents (q2prime):")
    hist_q2prime_E.Print()
    hist_q2prime_QE.Print()

    print("\nHistogram contents (q2 - elastic):")
    hist_q2_E.Print()
    print("\nHistogram contents (q2 - inelastic):")
    hist_q2_QE.Print()

    print("\nHistogram contents (Ptll - elastic):")
    hist_Ptll_E.Print()
    print("\nHistogram contents (Ptll - inelastic):")
    hist_Ptll_QE.Print()



##################################################################


    # Plot histograms for Mll
    canvas_Mll = ROOT.TCanvas("canvas_Mll", "Mll Comparison", 800, 600)
    hist_Mll_E.SetLineColor(ROOT.kBlue)
    hist_Mll_E.SetMinimum(1e-4)  # Set minimum y-axis value
    hist_Mll_E.SetMaximum(100)  # Set maximum y-axis value
    hist_Mll_E.GetYaxis().SetTitle("d#sigma/dM_{#tau^{+}#tau^{-}} [pb/GeV]")  # Y-axis title
    hist_Mll_E.GetXaxis().SetTitle("M_{#tau^{+}#tau^{-}} [GeV] = W_{#gamma#gamma} [GeV]")  # X-axis title
    hist_Mll_E.Draw()
    hist_Mll_QE.SetLineColor(ROOT.kRed)
    hist_Mll_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
    canvas_Mll.SetLogy()
    canvas_Mll.SetLogx()

    # Add legend for Mll
    legend_Mll = ROOT.TLegend(0.65, 0.65, 0.80, 0.80)
    legend_Mll.AddEntry(hist_Mll_E, "elastic (cepgen)", "l")
    legend_Mll.AddEntry(hist_Mll_QE, "inelastic (cepgen)", "l")
    legend_Mll.SetTextFont(42)
    legend_Mll.SetTextSize(0.035)    
    legend_Mll.SetBorderSize(0)  # Remove the border around the legend
    legend_Mll.Draw()

    # Add information for Mll
    latex_Mll = ROOT.TLatex()
    latex_Mll.SetNDC()
    latex_Mll.SetTextFont(42)
    latex_Mll.SetTextSize(0.035)
    latex_Mll.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2},  Q^{2}_{p,max}<10^{2} GeV^{2}, M_{N} < 10 GeV")

    latex_Mll.DrawLatex(0.15, 0.2,
                        "#color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for Mll as a PDF file
    canvas_Mll.SaveAs("Mll_Comparison_100.pdf")
    
    # Draw the canvas
    canvas_Mll.Draw()  


##################################################################



    # Plot histograms for Yll
    canvas_Yll = ROOT.TCanvas("canvas_Yll", "Yll Comparison", 800, 600)
    hist_Yll_E.SetLineColor(ROOT.kBlue)
#    hist_Yll_E.SetMinimum(1e-4)  # Set minimum y-axis value
#    hist_Yll_E.SetMaximum(100)  # Set maximum y-axis value
    hist_Yll_E.GetYaxis().SetTitle("d#sigma/dY_{#tau^{+}#tau^{-}} [pb/GeV]")  # Y-axis title
    hist_Yll_E.GetXaxis().SetTitle("Y_{#tau^{+}#tau^{-}}")  # X-axis title
    hist_Yll_E.Draw()
    hist_Yll_QE.SetLineColor(ROOT.kRed)
    hist_Yll_QE.Draw("SAME")

    # Add legend for Yll
    legend_Yll = ROOT.TLegend(0.7, 0.7, 0.80, 0.80)
    legend_Yll.AddEntry(hist_Yll_E, "elastic (cepgen)", "l")
    legend_Yll.AddEntry(hist_Yll_QE, "inelastic (cepgen)", "l")
    legend_Yll.SetTextFont(42)
    legend_Yll.SetTextSize(0.035)  
    legend_Yll.SetBorderSize(0)  # Remove the border around the legend
    legend_Yll.Draw()

    # Add information for Yll
    latex_Yll = ROOT.TLatex()
    latex_Yll.SetNDC()
    latex_Yll.SetTextFont(42)
    latex_Yll.SetTextSize(0.035)
    latex_Yll.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2},  Q^{2}_{p,max}<10^{2} GeV^{2}, M_{N} < 10 GeV")

    latex_Yll.DrawLatex(0.15, 0.2,
                        "#color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for Yll as a PDF file
    canvas_Yll.SaveAs("Yll_Comparison_100.pdf")
    
    # Draw the canvas
    canvas_Yll.Draw()  
    
    

##################################################################

    

    # Plot histograms for q2prime
    canvas_q2prime = ROOT.TCanvas("canvas_q2prime", "q2prime Comparison", 800, 600)
    hist_q2prime_E.SetLineColor(ROOT.kBlue)
    hist_q2prime_E.SetMinimum(1e-4)  # Set minimum y-axis value
    hist_q2prime_E.SetMaximum(100)  # Set maximum y-axis value
    hist_q2prime_E.GetYaxis().SetTitle("d#sigma/dq^{2}_{p} [pb/GeV]")  # Y-axis title
    hist_q2prime_E.GetXaxis().SetTitle("q^{2}_{p} [GeV^{2}]")  # X-axis title
    hist_q2prime_E.Draw()
    hist_q2prime_QE.SetLineColor(ROOT.kRed)
    hist_q2prime_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
#    canvas_q2prime.SetLogx()    
    canvas_q2prime.SetLogy()

    # Add legend for q2prime
    legend_q2prime = ROOT.TLegend(0.7, 0.7, 0.80, 0.80)
    legend_q2prime.AddEntry(hist_q2prime_E, "elastic (cepgen)", "l")
    legend_q2prime.AddEntry(hist_q2prime_QE, "inelastic (cepgen)", "l")
    legend_q2prime.SetTextFont(42)
    legend_q2prime.SetTextSize(0.035)  
    legend_q2prime.SetBorderSize(0)  # Remove the border around the legend
    legend_q2prime.Draw()

    # Add information for q2prime
    latex_q2prime = ROOT.TLatex()
    latex_q2prime.SetNDC()
    latex_q2prime.SetTextFont(42)
    latex_q2prime.SetTextSize(0.035)
    latex_q2prime.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2},  Q^{2}_{p,max}<10^{2} GeV^{2}, M_{N} < 10 GeV")

    latex_q2prime.DrawLatex(0.15, 0.2,
                        "#color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for q2prime as a PDF file
    canvas_q2prime.SaveAs("q2proton_Comparison_100.pdf")

    # Draw the canvas
    canvas_q2prime.Draw()  


##################################################################



    # Plot histograms for q2
    canvas_q2 = ROOT.TCanvas("canvas_q2", "q2 Comparison", 800, 600)
    hist_q2_E.SetLineColor(ROOT.kBlue)
    hist_q2_E.SetMinimum(1e-3)  # Set minimum y-axis value
    hist_q2_E.SetMaximum(100)  # Set maximum y-axis value
    hist_q2_E.GetYaxis().SetTitle("d#sigma/dq^{2}_{e} [pb/GeV^{2}]")
    hist_q2_E.GetXaxis().SetTitle("q^{2}_{e} [GeV^{2}]")
    hist_q2_E.Draw()
    hist_q2_QE.SetLineColor(ROOT.kRed)
    hist_q2_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
#    canvas_q2.SetLogx()
    canvas_q2.SetLogy()

    # Add legend for q2
    legend_q2 = ROOT.TLegend(0.7, 0.7, 0.80, 0.80)
    legend_q2.AddEntry(hist_q2_E, "elastic (cepgen)", "l")
    legend_q2.AddEntry(hist_q2_QE, "inelastic (cepgen)", "l")
    legend_q2.SetTextFont(42)
    legend_q2.SetTextSize(0.035)  
    legend_q2.SetBorderSize(0)
    legend_q2.Draw()

    # Add information for q2
    latex_q2 = ROOT.TLatex()
    latex_q2.SetNDC()
    latex_q2.SetTextFont(42)
    latex_q2.SetTextSize(0.035)
    latex_q2.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2},  Q^{2}_{p,max}<10^{2} GeV^{2}, M_{N} < 10 GeV")

    latex_q2.DrawLatex(0.15, 0.2,
                        "#color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for q2 as a PDF file
    canvas_q2.SaveAs("q2_electron_Comparison_100.pdf")
    
    # Draw the canvas
    canvas_q2.Draw()    
    
    
##################################################################




    # Plot histograms for Ptll
    canvas_Ptll = ROOT.TCanvas("canvas_Ptll", "Ptll Comparison", 800, 600)
    hist_Ptll_E.SetLineColor(ROOT.kBlue)
    hist_Ptll_E.SetMinimum(1e-3)  # Set minimum y-axis value
    hist_Ptll_E.SetMaximum(100)  # Set maximum y-axis value
    hist_Ptll_E.GetYaxis().SetTitle("d#sigma/dP^{T}_{#tau^{+}#tau^{-}} [pb/GeV^{2}]")
    hist_Ptll_E.GetXaxis().SetTitle("P_{T}^{#tau^{+}#tau^{-}} [GeV]")
    hist_Ptll_E.Draw()
    hist_Ptll_QE.SetLineColor(ROOT.kRed)
    hist_Ptll_QE.Draw("SAME")

    # Set y-axis to logarithmic scale
    canvas_Ptll.SetLogy()

    # Add legend for Ptll
    legend_Ptll = ROOT.TLegend(0.7, 0.7, 0.80, 0.80)
    legend_Ptll.AddEntry(hist_Ptll_E, "elastic", "l")
    legend_Ptll.AddEntry(hist_Ptll_QE, "inelastic", "l")
    legend_Ptll.SetTextFont(42)
    legend_Ptll.SetTextSize(0.035)  
    legend_Ptll.SetBorderSize(0)
    legend_Ptll.Draw()

    # Add information for Ptll
    latex_Ptll = ROOT.TLatex()
    latex_Ptll.SetNDC()
    latex_Ptll.SetTextFont(42)
    latex_Ptll.SetTextSize(0.035)
    latex_Ptll.DrawLatex(0.15, 0.8,
                        "Q^{2}_{e,max}<10^{2} GeV^{2},  Q^{2}_{p,max}<10^{2} GeV^{2}, M_{N} < 10 GeV")

    latex_Ptll.DrawLatex(0.15, 0.2,
                        "#color[2]{(#tau^{+}#tau^{-}) cepgen}")

    # Save the plot for Ptll as a PDF file
    canvas_Ptll.SaveAs("Ptll_Comparison_100.pdf")

    # Draw the canvas
    canvas_Ptll.Draw()


    # Cleanup
    file.Close()

# Call the function with the filename of the ROOT file
compare_distributions("LHeC_Compare_100_100_10.root")


##################################################################
