# Two-photon processes matrix elements

This repository introduces a collection of two-photon processes matrix elements to be used, either in C++ or in Python projects (thanks to the [Boost.Python](https://www.boost.org/doc/libs/1_86_0/libs/python/doc/html/index.html) library)

## Usage

First build the library as for any CMake project:

```bash
cmake /home/hamzeh-khanpour/Documents/GitHub/yy-interactions-at-the-LHeC/JHEP/yy_to_yy/ggMatrixElements-main
make -j 20
```

The requirements are set to be minimal:
- GSL
- Python
- Boost.Python

A `ggMatrixElements.so` shared library should be produced in your build directory. You may either copy it in your working environment, or set Python to search for it when running your script:

```bash
export PYTHONPATH=/home/hamzeh-khanpour/ggMatrixElements-main/:$PYTHONPATH
```

The module can then be imported in your script:

```python
import ggMatrixElements

print(ggMatrixElements.sqme_sm(0.1, -0.1, False))  # s, t, exclude_SM_loops
```




```python
import ggMatrixElements  # Import the photon-photon matrix element module


# Constants
alpha  = 1 / 137  # Fine-structure constant
hbarc2 = 0.389  # Conversion factor to pb

# Mandelstam variables
def t_min(W):
    return -W**2

def t_max(W):
    return 0


# Differential cross-section for gamma-gamma -> gamma-gamma using ggMatrixElements
def diff_cs_gg_to_gg(s, t):
    # Calculate the squared matrix element using ggMatrixElements
    sqme = ggMatrixElements.sqme_sm(s, t, False)  # s, t, exclude loops = False
    return sqme / (16. * np.pi * s**2.)  # The prefactor for 2-to-2 scattering



# Total cross-section for gamma-gamma -> gamma-gamma as a function of W
def cs_gg_to_gg_w(W):
    s = W**2.                # s = W^2
    t_min_value = t_min(W)
    t_max_value = t_max(W)



# Numerical integration over t
    def integrand(t, s):
        return diff_cs_gg_to_gg(s, t)

    result, _ = quad(integrand, t_min_value, t_max_value, args=(s,))
    return result * hbarc2 * 1e9  # Convert to pb


# Generate W values on a logarithmic scale from 10^-4 to 1000 GeV
W_values = np.logspace(-4, 3, 100)  # Photon-photon CM energy in GeV


# Compute the cross-section for each W
cross_sections = [cs_gg_to_gg_w(W) for W in W_values]


```
