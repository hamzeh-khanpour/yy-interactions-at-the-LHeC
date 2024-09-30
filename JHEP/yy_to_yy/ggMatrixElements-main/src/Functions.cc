#include <gsl/gsl_sf.h>

#include <cmath>

#include "ggMatrixElements/Utils.h"

double ReB(double z) {
  if (z == 0)  // b is infinite
    return 0;
  if (z < 0) {  // b > 1
    const auto b = sqrt(1 - 1 / z);
    //     return 0.5 * b * log( (1+b) / (b-1) ) - 1;
    return b * atanh(1 / b) - 1;
  }
  if (z >= 1) {  // 0 <= b < 1
    const auto b = sqrt(1 - 1 / z);
    //      return 0.5 * b * log( (1+b) / (1-b) ) - 1;
    return b * atanh(b) - 1;
  }
  // b is imaginary
  const auto b = sqrt(1 / z - 1);
  return b * atan(1 / b) - 1;
}

double ImB(double z) {
  if (z > 1) {
    return -M_PI / 2 * sqrt(1 - 1 / z);
  } else {
    return 0;
  }
}

double ReT(double z) {
  if (z == 0)  // b is infinite
    return 0;
  if (z < 0) {  // b>1 is real
    const auto b = sqrt(1 - 1 / z);
    const auto temp = 0.5 * log((1 + b) / (b - 1));
    return temp * temp;
  }
  if (z > 1) {  // 0<b<1 is real
    const auto b = sqrt(1 - 1 / z);
    const auto temp = 0.5 * log((1 + b) / (1 - b));
    return temp * temp - 0.25 * M_PI * M_PI;
  }
  if (z == 1)  // b=0
    return -0.25 * M_PI * M_PI;
  // b is imaginary
  const auto b = sqrt(1 / z - 1);
  const auto temp = atan(1 / b);
  return -temp * temp;
}

double ImT(double z) {
  if (z > 1)
    return -M_PI * acosh(sqrt(z));
  return 0;
}

double ReF(double q, double a) {  // some auxiliary function used in ReI(z,w)
                                  // (sum of the 4 dilogs)
  gsl_sf_result result_re;
  gsl_sf_result result_im;

  double r;
  double theta;

  double result;

  if (q > 0 && q < 1) {  // b(q) is imaginary, arguments of dilogs are complex
    const auto b = sqrt(1 / q - 1);

    r = (a + 1) / sqrt(a * a + b * b);
    theta = -atan(b / a);  // r e^itheta = (a+1)/(a+b)

    gsl_sf_complex_dilog_e(r, theta, &result_re, &result_im);

    result = -2 * result_re.val;  // -Re[ Li2( a+1/a+b) + Li2( a+1/a-b)]

    r = (a - 1) / sqrt(a * a + b * b);  // r e^itheta = (a-1)/(a+b)

    gsl_sf_complex_dilog_e(r, theta, &result_re, &result_im);

    result += 2 * result_re.val;  // Re[ Li2( a-1/a+b) + Li2( a-1/a-b)]
  } else {                        // b(q) real and so are all the arguments of the dilogs
    const auto b = sqrt(1 - 1 / q);

    result = gsl_sf_dilog((a - 1) / (a + b));
    result += gsl_sf_dilog((a - 1) / (a - b));
    result -= gsl_sf_dilog((a + 1) / (a + b));
    result -= gsl_sf_dilog((a + 1) / (a - b));
  }

  return result;
}

double ReI(double z, double w) {  // allowed regions z,w<=0 || z>=0,-z<=w<=0
  if (z == 0 || w == 0)
    return 0;

  const auto lim = 1.e-4;

  // because of exact cancellations Taylor-expand
  // the function near the origin to maintain double precision
  if (z < lim && z > -lim && w < lim && w > -lim)
    //      return 2./3.*z*z;
    return 2. / 3. * z * w + 4. / 15. * z * w * (z + w) + 16. / 105. * z * w * (z * z + w * w + z * w / 2);

  const auto a = sqrt(1 - 1 / w - 1 / z);

  return (ReF(z, a) + ReF(w, a)) / (2 * a);
}

double ImI(double z, double w) {  // allowed regions z,w<=0 || z>=0,-z<=w<=0
  if (z == 0 || w == 0)
    return 0;

  const auto a = std::sqrt(1 - 1 / z - 1 / w);

  double b;
  if (z > 1 && w < 0)
    b = std::sqrt(1 - 1 / z);
  else if (w > 1 && z < 0)
    b = std::sqrt(1 - 1 / w);
  else
    return 0;

  return M_PI / (2 * a) * std::log((a - b) / (a + b));
}
