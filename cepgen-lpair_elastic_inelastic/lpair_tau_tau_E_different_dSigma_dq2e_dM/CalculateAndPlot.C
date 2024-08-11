#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <TH1.h>
#include <TH2.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TLegend.h>
#include <TLatex.h>

void CalculateAndPlot() {
    gStyle->SetOptStat(0);

    // Set the bin width correction
    double binWidthCorrection = 1.0;

    // Integrated luminosity in fb^{-1}
    Float_t integrated_luminosity = 1.0; // fb^{-1}

    // Integrated cross-section value in pb
    Float_t integrated_cross_section_value_BH = 4.96239207e+01; // pb

    // Open the input file
    TFile *inputFile = new TFile("LHeC_E_1000_1000.root", "READ");
    if (!inputFile || !inputFile->IsOpen()) {
        std::cerr << "Error: Unable to open input file!" << std::endl;
        return;
    }

    // Load the TTree containing the data
    TTree *tree = (TTree*)inputFile->Get("LHeC_E");
    if (!tree) {
        std::cerr << "Error: Unable to retrieve TTree from input file!" << std::endl;
        inputFile->Close();
        return;
    }

    // Define variables to hold the data
    Float_t Mll, q2;

    // Set branch addresses
    tree->SetBranchAddress("Mll", &Mll);
    tree->SetBranchAddress("q2", &q2);

    // Define binning for Mll and q2
    const int nBinsMll = 500; // Number of bins for Mll
    const int nBinsq2 = 1000; // Number of bins for q2
    const double minMll = 0.0; // Minimum value of Mll
    const double maxMll = 500.0; // Maximum value of Mll
    const double minq2 = 0.0; // Minimum value of q2
    const double maxq2 = 1000.0; // Maximum value of q2

    // Create histograms to store the double differential cross-section
    TH1F *histMll = new TH1F("histMll", "", nBinsMll, minMll, maxMll);
    TH1F *histq2 = new TH1F("histq2", "", nBinsq2, minq2, maxq2);
    TH2F *hist2D = new TH2F("hist2D", "", nBinsq2, minq2, maxq2, nBinsMll, minMll, maxMll);

    // Create histograms to store the single differential cross-sections
    TH1F *histSingleMll = new TH1F("histSingleMll", "", nBinsMll, minMll, maxMll);
    TH1F *histSingleq2 = new TH1F("histSingleq2", "", nBinsq2, minq2, maxq2);

    // Loop over the entries in the TTree
    Long64_t nEntries = tree->GetEntries();
    for (Long64_t i = 0; i < nEntries; ++i) {
        tree->GetEntry(i);

        // Calculate the event weight
        Float_t event_weight_BH = integrated_cross_section_value_BH * integrated_luminosity / nEntries;

        // Fill the histograms with the calculated double differential cross-section
        histMll->Fill(Mll, binWidthCorrection * event_weight_BH);
        histq2->Fill(q2, binWidthCorrection * event_weight_BH);
        hist2D->Fill(q2, Mll, binWidthCorrection * event_weight_BH);

        // Fill the histograms with the calculated single differential cross-sections
        histSingleMll->Fill(Mll, event_weight_BH);
        histSingleq2->Fill(q2, event_weight_BH);
    }

    // Save the histograms to a file
    TFile *outputFile = new TFile("double_differential_cross_section.root", "RECREATE");
    if (!outputFile || !outputFile->IsOpen()) {
        std::cerr << "Error: Unable to create output file!" << std::endl;
        return;
    }
    histMll->Write();
    histq2->Write();
    hist2D->Write();
    histSingleMll->Write();
    histSingleq2->Write();
    outputFile->Close();

    // Define legend and text
    TLegend *leg = new TLegend(0.70, 0.70, 0.90, 0.85);
    leg->SetBorderSize(0);
    leg->SetTextSize(0.04);
    leg->SetTextFont(12);
    leg->SetFillStyle(0);

    TLatex *t2a = new TLatex(0.5, 0.9, "#bf{LHeC}");
    t2a->SetNDC();
    t2a->SetTextFont(42);
    t2a->SetTextSize(0.04);
    t2a->SetTextAlign(20);

    TLatex *t3a = new TLatex(0.40, 0.80, "Q^{2}_{e,max}<10^{3} GeV^{2};  Q^{2}_{p,max}<10^{3} GeV^{2}; #color[4]{W > 10 GeV}");
    t3a->SetNDC();
    t3a->SetTextFont(42);
    t3a->SetTextSize(0.04);
    t3a->SetTextAlign(20);
    t3a->SetTextColor(2);

    // Plot the double differential cross-section vs. Mll
    TCanvas *canvasMll = new TCanvas("canvasMll", "Double Differential Cross-Section vs M_{#tau^{+}#tau^{-}}", 900, 700);
    histMll->GetXaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
    histMll->GetXaxis()->SetLabelFont(22);
    histMll->GetXaxis()->SetTitleFont(22);
    histMll->GetYaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV]");
    histMll->GetYaxis()->SetLabelFont(22);
    histMll->GetYaxis()->SetTitleFont(22);
    histMll->SetLineWidth(3.0);
    histMll->SetLineColor(kBlue + 1);
    histMll->Draw("HIST E");
    canvasMll->SetLogy(1);
    canvasMll->SetLogx(0);
    leg->AddEntry(histMll, "Elastic (#tau^{+}#tau^{-}) cepgen", "L")->SetTextColor(kBlue + 1);
    leg->Draw("same");
    t2a->Draw("same");
    t3a->Draw("same");
    canvasMll->SaveAs("double_differential_cross_section_vs_Mll.png");

    // Calculate area under the Mll histogram
    double areaMll = histMll->Integral();
    std::cout << "areaMll = " << areaMll << " pb" << std::endl;

    // Plot the double differential cross-section vs. q2
    TCanvas *canvasq2 = new TCanvas("canvasq2", "Double Differential Cross-Section vs q^{2}_{e}", 900, 700);
    histq2->GetXaxis()->SetTitle("q^{2}_{e} [GeV^{2}]");
    histq2->GetXaxis()->SetLabelFont(22);
    histq2->GetXaxis()->SetTitleFont(22);
    histq2->GetYaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV^{2}]");
    histq2->GetYaxis()->SetLabelFont(22);
    histq2->GetYaxis()->SetTitleFont(22);
    histq2->SetLineWidth(3.0);
    histq2->SetLineColor(kBlue + 1);
    histq2->Draw("HIST E");
    canvasq2->SetLogy(1);
    canvasq2->SetLogx(0);
    leg->Draw("same");
    t2a->Draw("same");
    t3a->Draw("same");
    canvasq2->SaveAs("double_differential_cross_section_vs_q2.png");

    // Calculate area under the q2 histogram
    double areaq2 = histq2->Integral();
    std::cout << "areaq2 = " << areaq2 << " pb" << std::endl;

    // Plot the 2D histogram
    TCanvas *canvas2D = new TCanvas("canvas2D", "Double Differential Cross-Section vs q^{2}_{e} and M_{#tau^{+}#tau^{-}}", 900, 700);
    hist2D->GetXaxis()->SetTitle("q^{2}_{e} [GeV^{2}]");
    hist2D->GetXaxis()->SetLabelFont(22);
    hist2D->GetXaxis()->SetTitleFont(22);
    hist2D->GetYaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
    hist2D->GetYaxis()->SetLabelFont(22);
    hist2D->GetYaxis()->SetTitleFont(22);
    hist2D->GetZaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV^{2}]");
    hist2D->GetZaxis()->SetLabelFont(22);
    hist2D->GetZaxis()->SetTitleFont(22);
    hist2D->Draw("COLZ");
    canvas2D->SetLogy(1);
    canvas2D->SetLogx(0);
    t2a->Draw("same");
    t3a->Draw("same");
    canvas2D->SaveAs("double_differential_cross_section_2D.png");

    // Calculate area under the 2D histogram
    double area2D = hist2D->Integral();
    std::cout << "area2D = " << area2D << " pb" << std::endl;

    // Cleanup
    delete leg;
    delete t2a;
    delete t3a;
    delete canvasMll;
    delete canvasq2;
    delete canvas2D;
    delete histMll;
    delete histq2;
    delete hist2D;
    delete histSingleMll;
    delete histSingleq2;
    inputFile->Close();
    delete inputFile;
}
