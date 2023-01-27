# pip / cli

import numpy

print(numpy.version.version)

numpy_array = numpy.array([1,2,3,4,5,6,8,98,3,23,42,1,3,5,11234,1,123,123])
print(numpy_array * 2)
print(type(numpy_array))

import pandas

# pip list
# pip uninstall pandas
# pip show numpy 

import requests

# get_ = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# print(get_)
# print(get_.status_code)
# print(get_.json())


from  packages import aritmetics
from  packages import otheraritmetics

suma = aritmetics.suma(1,2)
print(suma)

suma2 = otheraritmetics.suma(1,2)
print(suma2)