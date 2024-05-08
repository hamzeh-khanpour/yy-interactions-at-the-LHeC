//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Apr 23 22:15:29 2024 by ROOT version 6.28/06
// from TTree hepmc3_tree/hepmc3_tree
// found on file: lpair_tau_tau.root
//////////////////////////////////////////////////////////

#ifndef lpair_tau_tau_h
#define lpair_tau_tau_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class lpair_tau_tau {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.
   static constexpr Int_t kMaxparticles = 8;
   static constexpr Int_t kMaxvertices = 3;

   // Declaration of leaf types
 //HepMC3::GenEventData *hepmc3_event;
   Int_t           event_number;
   Int_t           momentum_unit;
   Int_t           length_unit;
   Int_t           particles_;
   Int_t           particles_pid[kMaxparticles];   //[particles_]
   Int_t           particles_status[kMaxparticles];   //[particles_]
   Bool_t          particles_is_mass_set[kMaxparticles];   //[particles_]
   Double_t        particles_mass[kMaxparticles];   //[particles_]
   Double_t        particles_momentum_m_v1[kMaxparticles];   //[particles_]
   Double_t        particles_momentum_m_v2[kMaxparticles];   //[particles_]
   Double_t        particles_momentum_m_v3[kMaxparticles];   //[particles_]
   Double_t        particles_momentum_m_v4[kMaxparticles];   //[particles_]
   Int_t           vertices_;
   Int_t           vertices_status[kMaxvertices];   //[vertices_]
   Double_t        vertices_position_m_v1[kMaxvertices];   //[vertices_]
   Double_t        vertices_position_m_v2[kMaxvertices];   //[vertices_]
   Double_t        vertices_position_m_v3[kMaxvertices];   //[vertices_]
   Double_t        vertices_position_m_v4[kMaxvertices];   //[vertices_]
   vector<double>  weights;
   Double_t        event_pos_m_v1;
   Double_t        event_pos_m_v2;
   Double_t        event_pos_m_v3;
   Double_t        event_pos_m_v4;
   vector<int>     links1;
   vector<int>     links2;
   vector<int>     attribute_id;
   vector<string>  attribute_name;
   vector<string>  attribute_string;
 //HepMC3::GenRunInfoData *GenRunInfo;
   vector<string>  weight_names;
   vector<string>  tool_name;
   vector<string>  tool_version;
   vector<string>  tool_description;
//   vector<string>  attribute_name;
//   vector<string>  attribute_string;

   // List of branches
   TBranch        *b_hepmc3_event_event_number;   //!
   TBranch        *b_hepmc3_event_momentum_unit;   //!
   TBranch        *b_hepmc3_event_length_unit;   //!
   TBranch        *b_hepmc3_event_particles_;   //!
   TBranch        *b_particles_pid;   //!
   TBranch        *b_particles_status;   //!
   TBranch        *b_particles_is_mass_set;   //!
   TBranch        *b_particles_mass;   //!
   TBranch        *b_particles_momentum_m_v1;   //!
   TBranch        *b_particles_momentum_m_v2;   //!
   TBranch        *b_particles_momentum_m_v3;   //!
   TBranch        *b_particles_momentum_m_v4;   //!
   TBranch        *b_hepmc3_event_vertices_;   //!
   TBranch        *b_vertices_status;   //!
   TBranch        *b_vertices_position_m_v1;   //!
   TBranch        *b_vertices_position_m_v2;   //!
   TBranch        *b_vertices_position_m_v3;   //!
   TBranch        *b_vertices_position_m_v4;   //!
   TBranch        *b_hepmc3_event_weights;   //!
   TBranch        *b_hepmc3_event_event_pos_m_v1;   //!
   TBranch        *b_hepmc3_event_event_pos_m_v2;   //!
   TBranch        *b_hepmc3_event_event_pos_m_v3;   //!
   TBranch        *b_hepmc3_event_event_pos_m_v4;   //!
   TBranch        *b_hepmc3_event_links1;   //!
   TBranch        *b_hepmc3_event_links2;   //!
   TBranch        *b_hepmc3_event_attribute_id;   //!
   TBranch        *b_hepmc3_event_attribute_name;   //!
   TBranch        *b_hepmc3_event_attribute_string;   //!
   TBranch        *b_GenRunInfo_weight_names;   //!
   TBranch        *b_GenRunInfo_tool_name;   //!
   TBranch        *b_GenRunInfo_tool_version;   //!
   TBranch        *b_GenRunInfo_tool_description;   //!
   TBranch        *b_GenRunInfo_attribute_name;   //!
   TBranch        *b_GenRunInfo_attribute_string;   //!

   lpair_tau_tau(TTree *tree=0);
   virtual ~lpair_tau_tau();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef lpair_tau_tau_cxx
lpair_tau_tau::lpair_tau_tau(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/home/hamzeh-khanpour/hepmc3-build/QE_10_100_100.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/home/hamzeh-khanpour/hepmc3-build/QE_10_100_100.root");
      }
      f->GetObject("hepmc3_tree",tree);

   }
   Init(tree);
}

lpair_tau_tau::~lpair_tau_tau()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t lpair_tau_tau::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t lpair_tau_tau::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void lpair_tau_tau::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("event_number", &event_number, &b_hepmc3_event_event_number);
   fChain->SetBranchAddress("momentum_unit", &momentum_unit, &b_hepmc3_event_momentum_unit);
   fChain->SetBranchAddress("length_unit", &length_unit, &b_hepmc3_event_length_unit);
   fChain->SetBranchAddress("particles", &particles_, &b_hepmc3_event_particles_);
   fChain->SetBranchAddress("particles.pid", particles_pid, &b_particles_pid);
   fChain->SetBranchAddress("particles.status", particles_status, &b_particles_status);
   fChain->SetBranchAddress("particles.is_mass_set", particles_is_mass_set, &b_particles_is_mass_set);
   fChain->SetBranchAddress("particles.mass", particles_mass, &b_particles_mass);
   fChain->SetBranchAddress("particles.momentum.m_v1", particles_momentum_m_v1, &b_particles_momentum_m_v1);
   fChain->SetBranchAddress("particles.momentum.m_v2", particles_momentum_m_v2, &b_particles_momentum_m_v2);
   fChain->SetBranchAddress("particles.momentum.m_v3", particles_momentum_m_v3, &b_particles_momentum_m_v3);
   fChain->SetBranchAddress("particles.momentum.m_v4", particles_momentum_m_v4, &b_particles_momentum_m_v4);
   fChain->SetBranchAddress("vertices", &vertices_, &b_hepmc3_event_vertices_);
   fChain->SetBranchAddress("vertices.status", vertices_status, &b_vertices_status);
   fChain->SetBranchAddress("vertices.position.m_v1", vertices_position_m_v1, &b_vertices_position_m_v1);
   fChain->SetBranchAddress("vertices.position.m_v2", vertices_position_m_v2, &b_vertices_position_m_v2);
   fChain->SetBranchAddress("vertices.position.m_v3", vertices_position_m_v3, &b_vertices_position_m_v3);
   fChain->SetBranchAddress("vertices.position.m_v4", vertices_position_m_v4, &b_vertices_position_m_v4);
   fChain->SetBranchAddress("weights", &weights, &b_hepmc3_event_weights);
   fChain->SetBranchAddress("event_pos.m_v1", &event_pos_m_v1, &b_hepmc3_event_event_pos_m_v1);
   fChain->SetBranchAddress("event_pos.m_v2", &event_pos_m_v2, &b_hepmc3_event_event_pos_m_v2);
   fChain->SetBranchAddress("event_pos.m_v3", &event_pos_m_v3, &b_hepmc3_event_event_pos_m_v3);
   fChain->SetBranchAddress("event_pos.m_v4", &event_pos_m_v4, &b_hepmc3_event_event_pos_m_v4);
   fChain->SetBranchAddress("links1", &links1, &b_hepmc3_event_links1);
   fChain->SetBranchAddress("links2", &links2, &b_hepmc3_event_links2);
   fChain->SetBranchAddress("attribute_id", &attribute_id, &b_hepmc3_event_attribute_id);
   fChain->SetBranchAddress("attribute_name", &attribute_name, &b_hepmc3_event_attribute_name);
   fChain->SetBranchAddress("attribute_string", &attribute_string, &b_hepmc3_event_attribute_string);
   fChain->SetBranchAddress("weight_names", &weight_names, &b_GenRunInfo_weight_names);
   fChain->SetBranchAddress("tool_name", &tool_name, &b_GenRunInfo_tool_name);
   fChain->SetBranchAddress("tool_version", &tool_version, &b_GenRunInfo_tool_version);
   fChain->SetBranchAddress("tool_description", &tool_description, &b_GenRunInfo_tool_description);
//    fChain->SetBranchAddress("attribute_name", &attribute_name, &b_GenRunInfo_attribute_name);
//    fChain->SetBranchAddress("attribute_string", &attribute_string, &b_GenRunInfo_attribute_string);
   Notify();
}

Bool_t lpair_tau_tau::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void lpair_tau_tau::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t lpair_tau_tau::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef lpair_tau_tau_cxx
