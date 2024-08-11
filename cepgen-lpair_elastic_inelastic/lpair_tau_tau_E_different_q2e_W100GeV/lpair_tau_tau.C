#define lpair_tau_tau_cxx
#include "lpair_tau_tau.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

TFile *target;
TTree *Tsignal_LHeC = new TTree("LHeC_E","LHeC_E");
TFile *F;

// **********************************************************************
// Book Histograms
// **********************************************************************

TH1 *histMassdilepton = new TH1F("M_{inv}", "", 500, 0.0, 500.0);
TH1 *histq2 = new TH1F("q2", "", 100, 0.0, 100000.0);

TLorentzVector MyGoodLeptonplus;
TLorentzVector MyGoodLeptonminus;
TLorentzVector MydiLepton;

TLorentzVector Electronin;
TLorentzVector Electronout;

TLorentzVector Protonin;
TLorentzVector Protonout;

TLorentzVector QPrim;
TLorentzVector q;

TLorentzVector Mydiphoton;

Float_t bin_width_correction = 100000.0 / 100.0; // bin width = (range / number of bins)

Float_t Mll = 0.0;
Float_t Q2 = 0.0;
Float_t q2 = 0.0;

Float_t integrated_luminosity = 0.0;
Float_t integrated_cross_section_value_BH = 0.0;
Float_t event_weight_BH = 0.0;


//===================================================================


void lpair_tau_tau::Loop()
{


    Tsignal_LHeC->Branch("Mll", &Mll);
    Tsignal_LHeC->Branch("q2", &q2);

    gStyle->SetOptStat(0);

    if (fChain == 0) return;

    Long64_t nentries = fChain->GetEntriesFast();
    Long64_t nbytes = 0, nb = 0;
    for (Long64_t jentry = 0; jentry < nentries; jentry++) {
        Long64_t ientry = LoadTree(jentry);
        if (ientry < 0) break;
        nb = fChain->GetEntry(jentry); nbytes += nb;
        // if (Cut(ientry) < 0) continue;

        Float_t integrated_luminosity = 1.0; // fb^{-1}

//      Float_t  integrated_cross_section_value_BH  = 1.09699502e-01;   //   pb  q2 = 10 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 1.23163613e-01;   //   pb  q2 = 100 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 1.35747061e-01;   //   pb  q2 = 1000 GeV^2
//      Float_t  integrated_cross_section_value_BH  = 1.42254623e-01;   //   pb  q2 = 10000 GeV^2
      Float_t  integrated_cross_section_value_BH  = 1.42553272e-01;   //   pb  q2 = 100000 GeV^2

        Float_t event_weight_BH = integrated_cross_section_value_BH * integrated_luminosity / nentries;


//===================================================================


        Protonin.SetPxPyPzE(particles_momentum_m_v1[0], particles_momentum_m_v2[0], particles_momentum_m_v3[0], particles_momentum_m_v4[0]);
        Protonout.SetPxPyPzE(particles_momentum_m_v1[2], particles_momentum_m_v2[2], particles_momentum_m_v3[2], particles_momentum_m_v4[2]);

        Electronin.SetPxPyPzE(particles_momentum_m_v1[3], particles_momentum_m_v2[3], particles_momentum_m_v3[3], particles_momentum_m_v4[3]);
        Electronout.SetPxPyPzE(particles_momentum_m_v1[5], particles_momentum_m_v2[5], particles_momentum_m_v3[5], particles_momentum_m_v4[5]);

        QPrim.SetPxPyPzE(particles_momentum_m_v1[1], particles_momentum_m_v2[1], particles_momentum_m_v3[1], particles_momentum_m_v4[1]);
        q.SetPxPyPzE(particles_momentum_m_v1[4], particles_momentum_m_v2[4], particles_momentum_m_v3[4], particles_momentum_m_v4[4]);


        for (Int_t i = 1; i <= kMaxparticles; i++) {
            if (particles_pid[i] == -15) {  // && particles_status[i] == 5
                TVector3 Muonplus;
                Muonplus.SetXYZ(particles_momentum_m_v1[i], particles_momentum_m_v2[i], particles_momentum_m_v3[i]);
            }
            else if (particles_pid[i] == 15) {  // && particles_status[i] == 5
                TVector3 Muonminus;
                Muonminus.SetXYZ(particles_momentum_m_v1[i], particles_momentum_m_v2[i], particles_momentum_m_v3[i]);
            }
        }  // End do loop on kMaxparticles

        MyGoodLeptonplus.SetPxPyPzE(particles_momentum_m_v1[7], particles_momentum_m_v2[7], particles_momentum_m_v3[7], particles_momentum_m_v4[7]);
        MyGoodLeptonminus.SetPxPyPzE(particles_momentum_m_v1[6], particles_momentum_m_v2[6], particles_momentum_m_v3[6], particles_momentum_m_v4[6]);

        MydiLepton = MyGoodLeptonplus + MyGoodLeptonminus;
        Mydiphoton = QPrim + q;

        Mll = MydiLepton.M();
        Q2 = fabs(q.Mag2());
        q2 = Q2;

        histMassdilepton->Fill(Mll, event_weight_BH);
        histq2->Fill(q2, event_weight_BH * bin_width_correction);

        Tsignal_LHeC->Fill();
    }  // end events loop



    target = new TFile("LHeC_E_100000_100000.root", "recreate");
    target->cd();
    Tsignal_LHeC->Write();

    target->Close();



//===================================================================



    Double_t xl1 = 0.70, yl1 = 0.70, xl2 = xl1 + 0.0, yl2 = yl1 + 0.0;

    TLegend *leg = new TLegend(xl1, yl1, xl2, yl2);
    leg->SetBorderSize(0);
    leg->AddEntry(histMassdilepton, "Elastic (#tau^{+}#tau^{-}) cepgen", "L")->SetTextColor(kBlue + 1);
    leg->SetTextSize(0.04);
    leg->SetTextFont(12);
    leg->SetFillStyle(0);

    TLatex *t2a = new TLatex(0.5, 0.9, "#bf{LHeC}");
    t2a->SetNDC();
    t2a->SetTextFont(42);
    t2a->SetTextSize(0.04);
    t2a->SetTextAlign(20);

    TLatex *t3a = new TLatex(0.40, 0.80, "Q^{2}_{e,max}<10^{5} GeV^{2};  Q^{2}_{p,max}<10^{5} GeV^{2}; #color[4]{W > 100 GeV}");
    t3a->SetNDC();
    t3a->SetTextFont(42);
    t3a->SetTextSize(0.04);
    t3a->SetTextAlign(20);
    t3a->SetTextColor(2);



//===================================================================



    TCanvas *c1 = new TCanvas("c1", "Massdilepton", 10, 10, 900, 700);

    histMassdilepton->GetXaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
    histMassdilepton->GetXaxis()->SetLabelFont(22);
    histMassdilepton->GetXaxis()->SetTitleFont(22);
    histMassdilepton->GetYaxis()->SetTitle("d#sigma/dM_{#tau^{+}#tau^{-}} [pb/GeV]");
    histMassdilepton->GetYaxis()->SetLabelFont(22);
    histMassdilepton->GetYaxis()->SetTitleFont(22);
    histMassdilepton->SetLineWidth(3.0);
    histMassdilepton->SetLineColor(kBlue + 1);

    histMassdilepton->Draw("HIST E");

    c1->SetLogy(1);
    c1->SetLogx(0);

    leg->Draw("same");
    t2a->Draw("same");
    t3a->Draw("same");

//    c1->SaveAs("LHeC_Massdilepton_100GeV_W100GeV.pdf");




//===================================================================



    TCanvas *c2 = new TCanvas("c2", "Q2", 10, 10, 900, 700);

    histq2->GetXaxis()->SetTitle("q^{2} [GeV^{2}]");
    histq2->GetXaxis()->SetLabelFont(22);
    histq2->GetXaxis()->SetTitleFont(22);
    histq2->GetYaxis()->SetTitle("d#sigma/dq^{2} [pb/GeV^{2}]");
    histq2->GetYaxis()->SetLabelFont(22);
    histq2->GetYaxis()->SetTitleFont(22);
    histq2->SetLineWidth(3.0);
    histq2->SetLineColor(kBlue + 1);

    histq2->Draw("HIST E");

    c2->SetLogy(1);
    c2->SetLogx(0);


    leg->Draw("same");
    t2a->Draw("same");
    t3a->Draw("same");


 cout<<"Integral(q2e) ="<<histq2->Integral() / bin_width_correction <<endl;


// Get the bin numbers for the range 100 to 1000
    int bin_start = histq2->FindBin(10000);
    int bin_end   = histq2->FindBin(100000);

// Perform the integration over the specified bin range
    double integral = histq2->Integral(bin_start, bin_end);

// Apply the bin width correction if necessary
    integral /= bin_width_correction;

// Output the result
std::cout << "Integral(10000 GeV^2 < q2 < 100000 GeV^2) = " << integral << std::endl;


    c2->SaveAs("LHeC_q2_100000GeV_W100GeV.pdf");
}


