#include "TH1F.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"

// Function to create the histogram of invariant mass
TH1F* CreateInvariantMassHistogram(TTree* tree, const char* variable, int bins, float min, float max) {
    TH1F* h_mass = new TH1F("h_mass", "Invariant Mass of #tau^{+}#tau^{-};M_{#tau^{+}#tau^{-}} [GeV];Events", bins, min, max);
    tree->Draw(Form("%s>>h_mass", variable));
    return h_mass;
}

// Function to convert the histogram to differential cross-section
TH1F* ConvertToDifferentialCrossSection(TH1F* h_mass, double totalCrossSection, double totalEvents) {
    int bins = h_mass->GetNbinsX();
    double binWidth = h_mass->GetBinWidth(1);

    // Create a new histogram for the differential cross-section
    TH1F* h_dsigma = new TH1F("h_dsigma", "Differential Cross-Section;M_{#tau^{+}#tau^{-}} [GeV];d#sigma/dM_{#tau^{+}#tau^{-}} [pb/GeV]", bins, h_mass->GetXaxis()->GetXmin(), h_mass->GetXaxis()->GetXmax());

    // Loop over bins to calculate the differential cross-section
    for (int i = 1; i <= bins; ++i) {
        double content = h_mass->GetBinContent(i);
        double error = h_mass->GetBinError(i);

        // Normalize bin content to get differential cross-section
        double dsigma = (content / totalEvents) * totalCrossSection / binWidth;
        double dsigmaError = (error / totalEvents) * totalCrossSection / binWidth;

        h_dsigma->SetBinContent(i, dsigma);
        h_dsigma->SetBinError(i, dsigmaError);
    }

    return h_dsigma;
}

void plotDifferentialCrossSection() {
    // Load the ROOT file and get the tree
    TFile* file = TFile::Open("LHeC_E_10_10.root");
    TTree* tree = (TTree*)file->Get("LHeC_E");

    // Create the invariant mass histogram
    TH1F* h_mass = CreateInvariantMassHistogram(tree, "M_tau_tau", 50, 0, 200);

    // Total cross-section and number of events (replace with your values)
    double totalCrossSection = 1000; // in pb
    double totalEvents = tree->GetEntries();

    // Convert to differential cross-section
    TH1F* h_dsigma = ConvertToDifferentialCrossSection(h_mass, totalCrossSection, totalEvents);

    // Draw the differential cross-section
    TCanvas* canvas = new TCanvas("canvas", "Differential Cross-Section", 800, 600);
    h_dsigma->Draw();

    // Save the plot
    canvas->SaveAs("differential_cross_section.png");

    // Clean up
    delete h_mass;
    delete h_dsigma;
    delete canvas;
    file->Close();
    delete file;
}
