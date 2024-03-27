import pycepgen

sf_luxlike = pycepgen.StructureFunctionsFactory.build(202)

print(sf_luxlike.F2(0.5, 100.0))
