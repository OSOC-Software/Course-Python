my_conditions = True

if my_conditions:
    print("Dentro de la condicion IF 1")

my_conditions = 5*2

if my_conditions == 11:
    print("Dentro de la condicion IF 2")

if my_conditions >= 10:
    print("Dentro de la condicion IF 3")
else: 
    print("Dentro de la condicion else 1")

my_conditions = 12 * 3
if my_conditions > 10 and my_conditions < 20:
    print("Doble condicion 1")
elif my_conditions > 20: 
    print("Else If 1 ")

print("Fuera de las condiciones IF")


my_string = ""

if my_string:
    print("En my string")
if not my_string:
    print("En NOT my string")