First, install the master version of CepGen. It should:

- contain at least [#24](https://github.com/cepgen/cepgen/pull/24)
- be compiled with the Boost bindings (`boost-devel` should be installed on the system)

A minimal recipe for compilation is:

```bash
git clone https://github.com/cepgen/cepgen.git
cd cepgen
mkdir build && cd build
cmake ..
make -j
```
To speed up things, one can use [Ninja](https://ninja-build.org/), replacing the last two steps with:
```bash
cmake -GNinja ..
ninja
```

Then, once everything is compiled, add the `cepgen/build` path to your Python environment search path:

```bash
export PYTHONPATH=/path/to/your/cepgen/build:$PYTHONPATH
```

This will allow you to import the Python wrapper of CepGen into your runtime environment. You can test it by running the following snippet:

```python
import pycepgen

sf_luxlike = pycepgen.StructureFunctionsFactory.build(301)
print(sf_luxlike.F2(0.5, 100.))
```
