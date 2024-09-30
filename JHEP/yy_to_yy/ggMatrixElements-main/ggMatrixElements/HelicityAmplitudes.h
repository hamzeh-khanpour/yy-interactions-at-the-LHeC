// Computes different helicity amplitudes as defined in
// Costantini, DeTollis, Pistoni; Nuovo Cim. A2 (1971) 733-787

#ifndef ggMatrixElements_HelicityAmplitudes_h
#define ggMatrixElements_HelicityAmplitudes_h

int limits(double sred, double tred);

void Mxxxx_fermion(double x, double y, double *re, double *im);
void Mpppp_fermion(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpmmp_fermion(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpmpm_fermion(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpppm_fermion(double sred, double tred, double *re, double *im, int exclude_loops);
void Mppmm_fermion(double sred, double tred, double *re, double *im, int exclude_loops);

void Mxxxx_vector(double x, double y, double *re, double *im);
void Mpppp_vector(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpmmp_vector(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpmpm_vector(double sred, double tred, double *re, double *im, int exclude_loops);
void Mpppm_vector(double sred, double tred, double *re, double *im, int exclude_loops);
void Mppmm_vector(double sred, double tred, double *re, double *im, int exclude_loops);

void Mxxxx_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);
void Mpppp_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);
void Mpmmp_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);
void Mpmpm_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);
void Mppmm_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);
void Mpppm_spin0even(double x, double y, double m, double f0, double w_const, double a2, double *re, double *im);

void Mpppp_eft(double zeta1, double zeta2, double s, double t, double *re, double *im);
void Mpmmp_eft(double zeta1, double zeta2, double s, double t, double *re, double *im);
void Mpmpm_eft(double zeta1, double zeta2, double s, double t, double *re, double *im);
void Mppmm_eft(double zeta1, double zeta2, double s, double t, double *re, double *im);
void Mpppm_eft(double zeta1, double zeta2, double s, double t, double *re, double *im);

#endif
