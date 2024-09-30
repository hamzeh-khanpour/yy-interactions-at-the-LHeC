#include <boost/python.hpp>

#include "ggMatrixElements/MatrixElements.h"

BOOST_PYTHON_FUNCTION_OVERLOADS(sqme_sm, sm_aaaa::sqme, 2, 3)
BOOST_PYTHON_FUNCTION_OVERLOADS(sqme_eft, eft_aaaa::sqme, 2, 5)

BOOST_PYTHON_MODULE(ggMatrixElements) {
  namespace py = boost::python;

  py::def("sqme_sm", sm_aaaa::sqme, sqme_sm((py::arg("s"), py::arg("t"), py::arg("exclude_loops") = false)));
  py::def(
      "sqme_eft",
      eft_aaaa::sqme,
      sqme_eft((
          py::arg("s"), py::arg("t"), py::arg("exclude_loops") = false, py::arg("zeta1") = 0., py::arg("zeta2") = 0.)));
}
