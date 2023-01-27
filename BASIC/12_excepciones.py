one = 1
two = "2"

try:
    print(one + two)
except: 
    print("Suma de cadena con entero. ERROR !!!!!")
else:
    print("No hubo error")
finally: 
    print("Proceso finalizado")

try:
    print(one + two)
except TypeError as e: 
    print("Suma de cadena con entero. TypeError !!!!!" + e)
except ValueError as e: 
    print("Suma de cadena con entero. ValueError !!!!!" + e)
except Exception as e: 
    print("Suma de cadena con entero. Exception !!!!!" + e)