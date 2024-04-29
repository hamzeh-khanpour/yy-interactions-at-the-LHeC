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

    TH1 *histMassdilepton =  new TH1F("M_{inv}", "", 500, 0.0, 500.0);
    TH1 *histPtdilepton   =  new TH1F("Pt", "",      50, 0.0, 100.0);
    TH1 *histq2           =  new TH1F("q2", "",      50, 0.0, 100.0);
    TH1 *histq2prime      =  new TH1F("q2prime", "", 50, 0.0, 100.0);

    TH1 *histetall         =  new TH1F("etall", "",     40, -20.0, 20.0);
    TH1 *histYll           =  new TH1F("Yll", "",       20, -10.0, 10.0);
    TH1 *histThetall       =  new TH1F("Thetall", "",   30, -5.0, 5.0);


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



    Float_t Mll = 0.0;
    Float_t Ptll = 0.0;
    Float_t Q2 = 0.0;
    Float_t q2 = 0.0;

    Float_t Q2prime = 0.0;
    Float_t q2prime = 0.0;

    Float_t Etall   = 0.0;
    Float_t Yll     = 0.0;
    Float_t Thetall = 0.0;

    Float_t Mtau     = 1.77686;


   Float_t  integrated_luminosity = 0.0;
   Float_t  integrated_cross_section_value_BH = 0.0;

   Float_t  event_weight_BH  = 0.0;



void lpair_tau_tau::Loop()
{
//   In a ROOT session, you can do:
//      root> .L lpair_tau_tau.C
//      root> lpair_tau_tau t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch




	Tsignal_LHeC->Branch("Mll",&Mll);
	Tsignal_LHeC->Branch("Ptll",&Ptll);
	Tsignal_LHeC->Branch("q2",&q2);
	Tsignal_LHeC->Branch("q2prime",&q2prime);

    Tsignal_LHeC->Branch("Etall",&Etall);
    Tsignal_LHeC->Branch("Yll",&Yll);
    Tsignal_LHeC->Branch("Thetall",&Thetall);


//    gStyle->SetOptStat(0);



   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries; jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;





      Float_t  integrated_luminosity = 1.0; // fb^{-1}

      Float_t  integrated_cross_section_value_BH  = 48.8223395;   //   pb

      Float_t  event_weight_BH  = integrated_cross_section_value_BH  * integrated_luminosity / nentries;



// ============================================================================================

//      cout << "kMaxparticles =" << kMaxparticles << endl;
//      cout << "particles_momentum_m_v1 =" << particles_momentum_m_v1[1] << endl;
//      cout << "particles_pid =" << particles_pid[6] << endl;

// ============================================================================================



  Protonin.SetPxPyPzE( particles_momentum_m_v1[0], particles_momentum_m_v2[0], particles_momentum_m_v3[0], particles_momentum_m_v4[0] );
  Protonout.SetPxPyPzE( particles_momentum_m_v1[2], particles_momentum_m_v2[2], particles_momentum_m_v3[2], particles_momentum_m_v4[2] );



  Electronin.SetPxPyPzE( particles_momentum_m_v1[3], particles_momentum_m_v2[3], particles_momentum_m_v3[3], particles_momentum_m_v4[3] );
  Electronout.SetPxPyPzE( particles_momentum_m_v1[5], particles_momentum_m_v2[5], particles_momentum_m_v3[5], particles_momentum_m_v4[5] );

//        cout << "Electronin Pz = "   <<  Electronin.Pz()  << endl;
//        cout << "Electronin E = "   <<  Electronin.E()  << endl;




  QPrim.SetPxPyPzE( particles_momentum_m_v1[1], particles_momentum_m_v2[1], particles_momentum_m_v3[1], particles_momentum_m_v4[1] );

  q.SetPxPyPzE( particles_momentum_m_v1[4], particles_momentum_m_v2[4], particles_momentum_m_v3[4], particles_momentum_m_v4[4] );


//  cout << "QPrim Px = "   <<  QPrim.Px()  << endl;




    for (Int_t i = 1; i <= kMaxparticles; i++) {

        if ( particles_pid[i] == -15 ) {  // && particles_status[i] == 5


 TVector3 Muonplus;

//        cout << "particles_status= "          <<  particles_status[i]  << endl;
//        cout << "particles_momentum_m_v1= "   <<  particles_momentum_m_v1[i]  << endl;
//        cout << "particles_momentum_m_v2= "   <<  particles_momentum_m_v2[i]  << endl;
//        cout << "particles_momentum_m_v3= "   <<  particles_momentum_m_v3[i]  << endl;
//        cout << "particles_momentum_m_v4= "   <<  particles_momentum_m_v4[i]  << endl;

  Muonplus.SetXYZ( particles_momentum_m_v1[i], particles_momentum_m_v2[i], particles_momentum_m_v3[i] );

//        cout << "Muonplus Px = "   <<  Muonplus.Px()  << endl;



//        cout << "MyGoodLeptonplus Px = "   <<  MyGoodLeptonplus.Px()  << endl;

        }


        else if ( particles_pid[i] == 15 ) {  // && particles_status[i] == 5


 TVector3 Muonminus;

//        cout << "particles_momentum_m_v1= "   <<  particles_momentum_m_v1[i]  << endl;
//        cout << "particles_momentum_m_v2= "   <<  parti	Tsig_Afb_ee_kt_ES_REC->Fill();cles_momentum_m_v2[i]  << endl;
//        cout << "particles_momentum_m_v3= "   <<  particles_momentum_m_v3[i]  << endl;
//        cout << "particles_momentum_m_v4= "   <<  particles_momentum_m_v4[i]  << endl;

  Muonminus.SetXYZ( particles_momentum_m_v1[i], particles_momentum_m_v2[i], particles_momentum_m_v3[i] );

//        cout << "Muonminus Px = "   <<  Muonminus.Px()  << endl;



//        cout << "MyGoodLeptonminus Px = "   <<  MyGoodLeptonminus.Px()  << endl;
//        cout << "MyGoodLeptonminus Pt = "   <<  MyGoodLeptonminus.Pt()  << endl;
//        cout << "MyGoodLeptonminus M = "    <<  MyGoodLeptonminus.M()   << endl;
//        cout << "MyGoodLeptonminus P = "    <<  MyGoodLeptonminus.P()   << endl;
//        cout << "MyGoodLeptonminus Pt = "   <<  MyGoodLeptonminus.Pt()  << endl;

        }


    }  // End do loop on kMaxparticles


  MyGoodLeptonplus.SetPxPyPzE( particles_momentum_m_v1[7], particles_momentum_m_v2[7], particles_momentum_m_v3[7], particles_momentum_m_v4[7] );
  MyGoodLeptonminus.SetPxPyPzE( particles_momentum_m_v1[6], particles_momentum_m_v2[6], particles_momentum_m_v3[6], particles_momentum_m_v4[6] );


      MydiLepton = MyGoodLeptonplus + MyGoodLeptonminus;

      Mydiphoton = QPrim + q;


      Mll  = MydiLepton.M();
      Ptll = MydiLepton.Pt();

      Etall   =  MydiLepton.Eta();
      Thetall =  MydiLepton.Theta();

//      cout << "Mll = "  << Mll  << endl;


      Q2 = fabs(q.Mag2());
      Q2prime = fabs(QPrim.Mag2());


      q2 = Q2;
      q2prime = Q2prime;


//    Etall = -TMath::Log(TMath::Tan(Thetall / 2.0));

    // Calculate rapidity using: y = 1/2 ln ( (E+Pz)/(E-Pz) )
    Yll = 1.0/2.0 * TMath::Log( (MydiLepton.E() + MydiLepton.Pz()) / (MydiLepton.E() - MydiLepton.Pz()) );

    // Calculate rapidity using: y = Eta - cos(Theta)/2 (m/p_T)^2
//      Yll = Etall -  TMath::Cos(Thetall)/2.0 * (Mtau/Ptll)* (Mtau/Ptll);




      histMassdilepton->Fill(Mll,event_weight_BH);
      histPtdilepton->Fill(Ptll,event_weight_BH);
      histq2->Fill(q2);
      histq2prime->Fill(q2prime);

      histetall->Fill(Etall);
      histYll->Fill(Yll,event_weight_BH);
      histThetall->Fill(Thetall);


      Tsignal_LHeC->Fill();


   }  // end events loop


     target = new TFile ("LHeC_E.root","recreate");
     target->cd();

     Tsignal_LHeC->Write();

     target->Close();


Double_t xl1=0.70, yl1=0.70, xl2=xl1+0.0, yl2=yl1+0.0;

TLegend *leg = new TLegend(xl1,yl1,xl2,yl2);
leg->SetBorderSize(0);

leg->AddEntry(histMassdilepton,"Elastic (#tau^{+}#tau^{-}) cepgen","L")->SetTextColor(kBlue+1);

leg->SetTextSize(0.04);
leg->SetTextFont(12);
leg->SetFillStyle(0);

//    (#sqrt{s} = 365 GeV, L_{int} = 1.5 ab^{-1})    1.5 ab^{-1} (365 GeV)

TLatex *t2a = new TLatex(0.5,0.9,"#bf{LHeC}");
                t2a->SetNDC();
                t2a->SetTextFont(42);
                t2a->SetTextSize(0.04);
                t2a->SetTextAlign(20);


TLatex *t3a = new TLatex(0.40,0.80,"Q^{2}_{e,max}<10^{2} GeV^{2};  Q^{2}_{p,max}<10^{2} GeV^{2}");
                t3a->SetNDC();
                t3a->SetTextFont(42);
                t3a->SetTextSize(0.04);
                t3a->SetTextAlign(20);
                t3a->SetTextColor(2);

// =======================================================================



TCanvas* c1 = new TCanvas("c1","Massdilepton", 10, 10, 900, 700);

//histMassdilepton->SetTitle("Jet Algorithem = ee_genkt_cambridge");
histMassdilepton->GetXaxis()->SetTitle("M_{#tau^{+}#tau^{-}} [GeV]");
//histMassdilepton->GetXaxis()->SetTitleOffset(1.25);
histMassdilepton->GetXaxis()->SetLabelFont(22);
histMassdilepton->GetXaxis()->SetTitleFont(22);
histMassdilepton->GetYaxis()->SetTitle("d#sigma/dM_{#tau^{+}#tau^{-}} [pb/GeV]");  //   # of Events
histMassdilepton->GetYaxis()->SetTitleOffset(1.40);
histMassdilepton->GetYaxis()->SetLabelFont(22);
histMassdilepton->GetYaxis()->SetTitleFont(22);

histMassdilepton->GetYaxis()->SetRangeUser(0.0001,1000);
histMassdilepton->GetXaxis()->SetRangeUser(10,500);


   // histMassdilepton->SetFillStyle(3001);
//    histMassdilepton->SetFillColor(kGreen+1);
    histMassdilepton->SetLineWidth(3);
    histMassdilepton->SetLineColor(kBlue+1);

    histMassdilepton->Scale(1.0/ 1.0);
    histMassdilepton->Draw("hist");

    cout<<"Integral(Massdilepton) =" << histMassdilepton->Integral()<<endl;


     c1->SetLogy(1);
     c1->SetLogx(1);

 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

//c1->SaveAs("Massdilepton_LHeC.pdf");
//c1->SaveAs("Massdilepton_LHeC.C");
//c1->SaveAs("Massdilepton_LHeC.eps");
//c1->SaveAs("Massdilepton_LHeC.root");
//c1->SaveAs("Massdilepton_LHeC.jpg");



// =======================================================================



TCanvas* c2 = new TCanvas("c2","Ptdilepton", 10, 10, 900, 700);

//histPtdilepton->SetTitle("Jet Algorithem = ee_genkt_cambridge");
histPtdilepton->GetXaxis()->SetTitle("P_{T}^{#tau^{+}#tau^{-}} [GeV]");
//histPtdilepton->GetXaxis()->SetTitleOffset(1.25);
histPtdilepton->GetXaxis()->SetLabelFont(22);
histPtdilepton->GetXaxis()->SetTitleFont(22);
histPtdilepton->GetYaxis()->SetTitle("d#sigma/dP_{T}^{#tau^{+}#tau^{-}} [pb/GeV]");   //    # of Events
histPtdilepton->GetYaxis()->SetTitleOffset(1.40);
histPtdilepton->GetYaxis()->SetLabelFont(22);
histPtdilepton->GetYaxis()->SetTitleFont(22);

//histPtdilepton->GetYaxis()->SetRangeUser(0,100);

cout<<"Integral(Ptdilepton) ="<<histPtdilepton->Integral()<<endl;

   // histPtdilepton->SetFillStyle(3001);
//    histPtdilepton->SetFillColor(kGreen+1);
    histPtdilepton->SetLineWidth(3);
    histPtdilepton->SetLineColor(kBlue+1);

    histPtdilepton->Draw("hist");


     c2->SetLogy(1);
//   c2->SetLogx(1);

 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

//c2->SaveAs("Ptdilepton_LHeC.pdf");
//c2->SaveAs("Ptdilepton_LHeC.C");
//c2->SaveAs("Ptdilepton_LHeC.eps");
//c2->SaveAs("Ptdilepton_LHeC.root");
//c2->SaveAs("Ptdilepton_LHeC.jpg");




// =======================================================================



TCanvas* c3 = new TCanvas("c3","etall", 10, 10, 900, 700);

//histetall->SetTitle("Jet Algorithem = ee_genkt_cambridge"); t5a->Draw("same");
histetall->GetXaxis()->SetTitle("#eta^{#tau^{+}#tau^{-}}");
//histetall->GetXaxis()->SetTitleOffset(1.25);
histetall->GetXaxis()->SetLabelFont(22);
histetall->GetXaxis()->SetTitleFont(22);
histetall->GetYaxis()->SetTitle("# Events");
histetall->GetYaxis()->SetTitleOffset(1.40);
histetall->GetYaxis()->SetLabelFont(22);
histetall->GetYaxis()->SetTitleFont(22);

//histetall->GetYaxis()->SetRangeUser(1,100);


 cout<<"Integral(etal) ="<<histetall->Integral()<<endl;

   // histetall->SetFillStyle(3001);
//    histetall->SetFillColor(kGreen+1);
    histetall->SetLineWidth(3);
    histetall->SetLineColor(kBlue+1);

//    histetall->Draw("hist");
    histetall->Draw("hist");


 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

// c3->SetLogy(1);


//c3->SaveAs("etall_LHeC.pdf");
//c3->SaveAs("etall_LHeC.C");
//c3->SaveAs("etall_LHeC.eps");
//c3->SaveAs("etall_LHeC.root");
//c3->SaveAs("etall_LHeC.jpg");




// =======================================================================



TCanvas* c4 = new TCanvas("c4","Yll", 10, 10, 900, 700);

//histYll->SetTitle("Jet Algorithem = ee_genkt_cambridge"); t5a->Draw("same");
histYll->GetXaxis()->SetTitle("Y^{#tau^{+}#tau^{-}}");
//histYll->GetXaxis()->SetTitleOffset(1.25);
histYll->GetXaxis()->SetLabelFont(22);
histYll->GetXaxis()->SetTitleFont(22);
histYll->GetYaxis()->SetTitle("d#sigma/dY^{#tau^{+}#tau^{-}} [pb/GeV]");
histYll->GetYaxis()->SetTitleOffset(1.40);
histYll->GetYaxis()->SetLabelFont(22);
histYll->GetYaxis()->SetTitleFont(22);

//histYll->GetYaxis()->SetRangeUser(1,100);


 cout<<"Integral(Yl) ="<<histYll->Integral()<<endl;

   // histYll->SetFillStyle(3001);
//    histYll->SetFillColor(kGreen+1);
    histYll->SetLineWidth(3);
    histYll->SetLineColor(kBlue+1);

//    histYll->Draw("hist");
    histYll->Draw("hist");


 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

// c4->SetLogy(1);
// c4->SetLogx(1);


//c4->SaveAs("Yll_LHeC.pdf");
//c4->SaveAs("Yll_LHeC.C");
//c4->SaveAs("Yll_LHeC.eps");
//c4->SaveAs("Yll_LHeC.root");
//c4->SaveAs("Yll_LHeC.jpg");




// =======================================================================



TCanvas* c5 = new TCanvas("c5","Thetall", 10, 10, 900, 700);

//histThetall->SetTitle("Jet Algorithem = ee_genkt_cambridge"); t5a->Draw("same");
histThetall->GetXaxis()->SetTitle("#theta^{#tau^{+}#tau^{-}}");
//histThetall->GetXaxis()->SetTitleOffset(1.25);
histThetall->GetXaxis()->SetLabelFont(22);
histThetall->GetXaxis()->SetTitleFont(22);
histThetall->GetYaxis()->SetTitle("# Events");
histThetall->GetYaxis()->SetTitleOffset(1.40);
histThetall->GetYaxis()->SetLabelFont(22);
histThetall->GetYaxis()->SetTitleFont(22);

//histThetall->GetYaxis()->SetRangeUser(1,100);


 cout<<"Integral(Yl) ="<<histThetall->Integral()<<endl;

   // histThetall->SetFillStyle(3001);
//    histThetall->SetFillColor(kGreen+1);
    histThetall->SetLineWidth(3);
    histThetall->SetLineColor(kBlue+1);

//    histThetall->Draw("hist");
    histThetall->Draw("hist");


 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

// c5->SetLogy(1);


//c5->SaveAs("Thetall_LHeC.pdf");
//c5->SaveAs("Thetall_LHeC.C");
//c5->SaveAs("Thetall_LHeC.eps");
//c5->SaveAs("Thetall_LHeC.root");
//c5->SaveAs("Thetall_LHeC.jpg");

// =======================================================================



TCanvas* c8 = new TCanvas("c8","q2e", 10, 10, 900, 700);

//histq2->SetTitle("Jet Algorithem = ee_genkt_cambridge"); t5a->Draw("same");
histq2->GetXaxis()->SetTitle("q^{2}_{e, max}");
//histq2->GetXaxis()->SetTitleOffset(1.25);
histq2->GetXaxis()->SetLabelFont(22);
histq2->GetXaxis()->SetTitleFont(22);
histq2->GetYaxis()->SetTitle("# Events");
histq2->GetYaxis()->SetTitleOffset(1.40);
histq2->GetYaxis()->SetLabelFont(22);
histq2->GetYaxis()->SetTitleFont(22);

//histq2->GetYaxis()->SetRangeUser(1,100);


 cout<<"Integral(q2e) ="<<histq2->Integral()<<endl;

   // histq2->SetFillStyle(3001);
//    histq2->SetFillColor(kGreen+1);
    histq2->SetLineWidth(3);
    histq2->SetLineColor(kBlue+1);

//    histq2->Draw("hist");
    histq2->Draw("hist");


 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

 c8->SetLogy(1);


//c8->SaveAs("q2e_LHeC.pdf");
//c8->SaveAs("q2e_LHeC.C");
//c8->SaveAs("q2e_LHeC.eps");
//c8->SaveAs("q2e_LHeC.root");
//c8->SaveAs("q2e_LHeC.jpg");




// =======================================================================



TCanvas* c9 = new TCanvas("c9","q2p", 10, 10, 900, 700);

//histq2prime->SetTitle("Jet Algorithem = ee_genkt_cambridge"); t5a->Draw("same");
histq2prime->GetXaxis()->SetTitle("q^{2}_{p, max}");
//histq2prime->GetXaxis()->SetTitleOffset(1.25);
histq2prime->GetXaxis()->SetLabelFont(22);
histq2prime->GetXaxis()->SetTitleFont(22);
histq2prime->GetYaxis()->SetTitle("# Events");
histq2prime->GetYaxis()->SetTitleOffset(1.40);
histq2prime->GetYaxis()->SetLabelFont(22);
histq2prime->GetYaxis()->SetTitleFont(22);

//histq2prime->GetYaxis()->SetRangeUser(1,100);


 cout<<"Integral(q2p) ="<<histq2prime->Integral()<<endl;

   // histq2prime->SetFillStyle(3001);
//    histq2prime->SetFillColor(kGreen+1);
    histq2prime->SetLineWidth(3);
    histq2prime->SetLineColor(kBlue+1);

//    histq2prime->Draw("hist");
    histq2prime->Draw("hist");


 leg->Draw("same");
 t2a->Draw("same");
 t3a->Draw("same");

 c9->SetLogy(1);


//c9->SaveAs("q2p_LHeC.pdf");
//c9->SaveAs("q2p_LHeC.C");
//c9->SaveAs("q2p_LHeC.eps");
//c9->SaveAs("q2p_LHeC.root");
//c9->SaveAs("q2p_LHeC.jpg");



// =======================================================================



}   // The end of main program lpair_tau_tau

