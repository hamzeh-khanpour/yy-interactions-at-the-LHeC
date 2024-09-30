#include <cassert>
#include <cmath>
#include <stdexcept>

#include "ggMatrixElements/HelicityAmplitudes.h"
#include "ggMatrixElements/MatrixElements.h"

namespace eft_aaaa {
  // Computes the  squared matrix element and the SM interference from free zeta_1, zeta_2
  double sqme(double s, double t, bool exclude_loops_SM, double zeta1, double zeta2) {
    //NOTE: zeta1/zeta2 expressed in GeV^-4
    if (s < 0 || t > 0 || t < -s)
      throw std::runtime_error("Invalid domain. Valid range is s>=0 and -s<=t<=0");

    double re_ex;
    double im_ex;
    double re_SM;
    double im_SM;

    double value = 0;

    // Mpppp:
    Mpppp_eft(zeta1, zeta2, s, t, &re_ex, &im_ex);  // exotic matrix element
    re_ex *= 8;  // factor 8 is needed because of the conventions in Costantini, DeTollis, Pistoni
    im_ex *= 8;
    sm_aaaa::me_SM(Mpppp_fermion, s, t, &re_SM, &im_SM, exclude_loops_SM);  //  SM matrix element:

    value += re_ex * (re_ex + 2 * re_SM) + im_ex * (im_ex + 2 * im_SM);

    // repeat for the other helicities

    // Mppmm:
    Mppmm_eft(zeta1, zeta2, s, t, &re_ex, &im_ex);
    re_ex *= 8;
    im_ex *= 8;
    sm_aaaa::me_SM(Mppmm_fermion, s, t, &re_SM, &im_SM, exclude_loops_SM);

    value += re_ex * (re_ex + 2 * re_SM) + im_ex * (im_ex + 2 * im_SM);

    // Mpmmp:
    Mpmmp_eft(zeta1, zeta2, s, t, &re_ex, &im_ex);
    re_ex *= 8;
    im_ex *= 8;
    sm_aaaa::me_SM(Mpmmp_fermion, s, t, &re_SM, &im_SM, exclude_loops_SM);

    value += re_ex * (re_ex + 2 * re_SM) + im_ex * (im_ex + 2 * im_SM);

    // Mpmpm:
    Mpmpm_eft(zeta1, zeta2, s, t, &re_ex, &im_ex);
    re_ex *= 8;
    im_ex *= 8;
    sm_aaaa::me_SM(Mpmpm_fermion, s, t, &re_SM, &im_SM, exclude_loops_SM);

    value += re_ex * (re_ex + 2 * re_SM) + im_ex * (im_ex + 2 * im_SM);

    // Mpppm
    Mpppm_eft(zeta1, zeta2, s, t, &re_ex, &im_ex);
    re_ex *= 8;
    im_ex *= 8;
    sm_aaaa::me_SM(Mpppm_fermion, s, t, &re_SM, &im_SM, exclude_loops_SM);

    value += 4 * (re_ex * (re_ex + 2 * re_SM) + im_ex * (im_ex + 2 * im_SM));

    return 0.5 * value;
  }
}  //namespace eft_aaaa
