# While 
condition = 0 
while condition<10:
    print("Dentro de While")
    condition += 1
else:
    print("Fin else While")
print("Fin while")

# For

my_list = [12,23,34,6,78,4,5,56,6,2,1,1]
for element in my_list:
    print(element)

my_tuple = (12,3,54,6,7,23)
for element in my_tuple:
    print(element)

my_set = {212,3,45,6,7,8}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Juan", "Edad": 29, "Apellido": "OsorioC"}
for element in my_dict:
    print(element)


my_list_2 = [13,12,45,231,123,3]
for element in my_list_2:
    print(element)
else:
    print("Fin For")