# Notes on CepGen interfacing

## CepGen installation

The easiest way is to follow [the online manual](https://cepgen.hepforge.org/install.html) instructions, with the `master` branch as baseline:

```bash
git clone https://github.com/cepgen/cepgen.git
cd cepgen
mkdir build && cd build
```

To enable the Python 3 bindings, both `python3` and `python3-devel` (`python3-dev` on Ubuntu/Debian) must be installed on your system. The next step is then to generate the Makefile and build, either using GNU Make:
```bash
cmake .. && make -j
```
or using the faster [Ninja builder](https://ninja-build.org/):
```bash
cmake -GNinja .. && ninja
```

Finally, once everything is built, export the `CEPGEN_PATH` environment variable and add it to your `PYTHONPATH`:
```bash
export CEPGEN_PATH=/path/to/your/cepgen/directory
export PYTHONPATH=$CEPGEN_PATH/build:$PYTHONPATH
```

## Usage of Python bindings
After installation, you will be all set to import the CepGen Python bindings in all your scripts:
```python
import pycepgen as cg
import numpy as np

q2 = 10.  # units: GeV^2

# collinear fluxes
cg_epa_el = cg.CollinearFluxFactory.build('EPAFlux')
cg_epa_in = cg.CollinearFluxFactory.build('EPAFlux', {'formFactors': {'mod_name': 'InelasticNucleon'}})
for x in np.linspace(0., 1., 11):
    print(x, cg_epa_el.fluxQ2(x, q2), cg_epa_in.fluxQ2(x, q2))

# structure functions
cg_sf_allm = cg.StructureFunctionsFactory.build(202)
for xbj in np.linspace(0., 1., 11):
    print(xbj, cg_sf_allm.F2(xbj, q2), cg_sf_allm.FL(xbj, q2))
```
## Description of CepGen modules/parameterisations
Some useful tools for the listing of all parameterisation modules handled are:
- the `bin/cepgen` main executable with the `-l` flag, providing a brief list of all modules loaded in the runtime database ;
- the `bin/cepgenDescribeModules` utility, listing all (`-a`) or specific modules (`-m module_name`) parameters and their default values ;
- the [raw HTML list](https://cepgen.hepforge.org/raw-modules.html) of modules shown in the project website ; this latter only contains the barebone CepGen modules (excluding all [CepGenAddOns](https://github.com/cepgen/cepgen/tree/master/CepGenAddOns) wrappers).