
    // Variables to hold Mll values
    Float_t Mll=0;



void CompareMllDistributions() {
    // Open the ROOT file
    TFile* file = TFile::Open("/home/hamzeh-khanpour/Desktop/lpair_tau_tau_E/LHeC_Compare.root");
    if (!file || file->IsZombie()) {
        std::cerr << "Error: Could not open file" << std::endl;
        return;
    }

   gStyle->SetPalette(kBird);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(1);


    // Create histograms
    TH1F* hist_E = new TH1F("hist_E", "Mll Distribution (LHeC_E)", 100, 0, 200);
    TH1F* hist_QE = new TH1F("hist_QE", "Mll Distribution (LHeC_QE)", 100, 0, 200);


    // Get the TTree objects
    TTree* tree_E = (TTree*)file->Get("LHeC_E");
    TTree* tree_QE = (TTree*)file->Get("LHeC_QE");
    if (!tree_E || !tree_QE) {
        std::cerr << "Error: Could not retrieve TTrees from the file" << std::endl;
        file->Close();
        return;
    }



    // Set branch addresses
    tree_E->SetBranchAddress("Mll", &Mll);
    tree_QE->SetBranchAddress("Mll", &Mll);





//     cout << "tree_E->GetEntries() =" << tree_E->GetEntries() << endl;


    // Fill histograms
    for (Long64_t i = 0; i < tree_E->GetEntries(); i++) {
        tree_E->GetEntry(i);
        hist_E->Fill(Mll);
    }


    for (Long64_t i = 0; i < tree_QE->GetEntries(); i++) {
        tree_QE->GetEntry(i);
        hist_QE->Fill(Mll);
    }

    // Plot histograms
    TCanvas* canvas = new TCanvas("canvas", "Mll Comparison", 800, 600);
    hist_E->SetLineColor(kBlue);
    hist_E->Draw();
    hist_QE->SetLineColor(kRed);
    hist_QE->Draw("SAME");

    // Add legend
    TLegend* legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    legend->AddEntry(hist_E, "LHeC_E", "l");
    legend->AddEntry(hist_QE, "LHeC_QE", "l");
    legend->Draw();

    // Cleanup
    file->Close();
}
