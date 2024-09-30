# Two-photon processes matrix elements

This repository introduces a collection of two-photon processes matrix elements to be used, either in C++ or in Python projects (thanks to the [Boost.Python](https://www.boost.org/doc/libs/1_86_0/libs/python/doc/html/index.html) library)

## Usage

First build the library as for any CMake project:

```bash
cmake /path/to/sources
make [-jN]
```

The requirements are set to be minimal:
- GSL
- Python
- Boost.Python

A `ggMatrixElements.so` shared library should be produced in your build directory. You may either copy it in your working environment, or set Python to search for it when running your script:

```bash
export PYTHONPATH=/path/to/build/directory:$PYTHONPATH
```

The module can then be imported in your script:

```python
import ggMatrixElements

print(ggMatrixElements.sqme_sm(0.1, -0.1, False))  # s, t, exclude_SM_loops
```