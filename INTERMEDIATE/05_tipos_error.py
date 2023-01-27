#SyntaxError
    # print "Hola Error" # Error
    # print("Hola Correcto") # OK

#NameError
    # print(name) # Error
    # name = "Juan" # OK
    # print(name) # OK

#IndexError
    # list_ = [1,2,3,4,5]
    # print(list_[5]) # Error
    # print(list_[1]) # OK

#ModuleNotFoundError
    # import Maths # Error
    # import math # OK

#AttributeError
    # print(math.PI) # Error
    # print(math.pi) # OK

#KeyError
    # dict = {nombre:"Juan", 1: 1.80}
    # print(dict.apellido) # Error
    # print(dict.nombre) # OK

#TypeError
    # dict = {nombre:"Juan"}
    # print(dict["1"]) # Error
    # print(dict[1]) # OK

#ImportError
    # from math import PI # Error
    # from math import pi # OK

#ValueError
    # name = int("10 años") # Error
    # name = int("10") # OK

#ZeroDivisionError
    # print(10 / 0) # Error
    # print(10 / 1) # OK