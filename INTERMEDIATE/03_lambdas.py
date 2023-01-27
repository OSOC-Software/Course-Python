suma_lambda = lambda first_value, second_value: first_value + second_value
print(suma_lambda(4,4))

multiply_values = lambda one, two, three, four: one*two-three/four
print(multiply_values(1,2,3,4))

def suma_fun(a,b):
    return suma_lambda(a,b)
print(suma_fun(1,2))

def suma_fun_2(val):
    return lambda first_value, second_value: first_value + second_value + val

suma_fun_2(1)(122,)