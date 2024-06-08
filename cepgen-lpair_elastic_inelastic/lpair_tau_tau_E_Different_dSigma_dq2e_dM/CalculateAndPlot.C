#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <TH1.h>
#include <TH2.h>
#include <TCanvas.h>
#include <TStyle.h>

void CalculateAndPlot() {
    gStyle->SetOptStat(0);

    // Set the bin width correction
    double binWidthCorrection = 1.0;


      Float_t  integrated_luminosity = 1.0; // fb^{-1}

//      Float_t  integrated_cross_section_value_BH  = 4.55272144e+01;   //   pb  q2 = 10 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 4.88223395e+01;   //   pb  q2 = 100 GeV^2
      Float_t  integrated_cross_section_value_BH  = 4.96239207e+01;   //   pb  q2 = 1000 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 4.95740596e+01;   //   pb  q2 = 10000 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 4.96574771e+01;   //   pb  q2 = 100000 GeV^2




    // Open the input file
    TFile *inputFile = new TFile("LHeC_E_1000_1000.root", "READ");
    if (!inputFile) {
        std::cerr << "Error: Unable to open input file!" << std::endl;
        return;
    }

    // Load the TTree containing the data
    TTree *tree = (TTree*)inputFile->Get("LHeC_E");
    if (!tree) {
        std::cerr << "Error: Unable to retrieve TTree from input file!" << std::endl;
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

    // Loop over the entries in the TTree
    Long64_t nEntries = tree->GetEntries();
    for (Long64_t i = 0; i < nEntries; ++i) {
        tree->GetEntry(i);


      Float_t  event_weight_BH  = integrated_cross_section_value_BH  * integrated_luminosity / nEntries;



        // Fill the histograms with the calculated double differential cross-section
        histMll->Fill(Mll, binWidthCorrection*event_weight_BH);
        histq2->Fill(q2, binWidthCorrection*event_weight_BH);
        hist2D->Fill(q2, Mll, binWidthCorrection);
    }

    // Save the histograms to a file
    TFile *outputFile = new TFile("double_differential_cross_section.root", "RECREATE");
    if (!outputFile) {
        std::cerr << "Error: Unable to create output file!" << std::endl;
        return;
    }
    histMll->Write();
    histq2->Write();
    hist2D->Write();
    outputFile->Close();

    // Plot the double differential cross-section vs. Mll
    TCanvas *canvasMll = new TCanvas("canvasMll", "Double Differential Cross-Section vs M_{#tau^{+}#tau^{-}}", 800, 600);
    histMll->GetXaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
    histMll->GetYaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV]");
    histMll->GetYaxis()->SetMoreLogLabels(); // Set logarithmic scale for y-axis
    histMll->Draw("hist");
    canvasMll->SaveAs("double_differential_cross_section_vs_Mll.png");

    // Calculate area under the Mll histogram
    double areaMll = histMll->Integral();

    cout << " areaMll = "  <<  areaMll  << endl;


    // Plot the double differential cross-section vs. q2
    TCanvas *canvasq2 = new TCanvas("canvasq2", "Double Differential Cross-Section vs q^{2}_{e}", 800, 600);
    histq2->GetXaxis()->SetTitle("q^{2}_{e} [GeV^{2}]");
    histq2->GetYaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV^{2}]");
    histq2->GetYaxis()->SetMoreLogLabels(); // Set logarithmic scale for y-axis
    histq2->Draw("hist");
    canvasq2->SaveAs("double_differential_cross_section_vs_q2.png");


    // Calculate area under the q2 histogram
    double areaq2 = histq2->Integral();

    cout << " areaq2 = "  <<  areaq2  << endl;


    // Plot the 2D histogram
    TCanvas *canvas2D = new TCanvas("canvas2D", "Double Differential Cross-Section 2D", 800, 600);
    hist2D->GetXaxis()->SetTitle("q^{2}_{e} [GeV^{2}]");
    hist2D->GetYaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
    hist2D->GetZaxis()->SetTitle("d^{2}#sigma/ dq^{2}_{e} dM_{#tau^{+}#tau^{-}} [pb/GeV^{2}]");
    hist2D->Draw("colz");
    canvas2D->SaveAs("double_differential_cross_section_2D.png");

    // Calculate area under the 2D histogram
    double area2D = hist2D->Integral();

    cout << " area2D = "  <<  area2D  << endl;


    // Clean up
    delete histMll;
    delete histq2;
    delete hist2D;
    delete inputFile;
    delete outputFile;
    delete canvasMll;
    delete canvasq2;
    delete canvas2D;
}

int main() {
    // Set the global style
    gStyle->SetOptStat(1);

    // Calculate and plot the double differential cross-section
    CalculateAndPlot();

    return 0;
}
