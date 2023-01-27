my_dict = dict()
my_dict_2 = {}

print(my_dict)
print(my_dict_2)

print(type(my_dict))
print(type(my_dict_2))

my_dict_2 = {
    "Nombre":"Juan", 
    "Edad":29, 
    "Lenguajes": { "Python","Swift","Kotlin" }, # Objeto tipo Set
    1: 1.80,
    2: True
}

print(my_dict_2)
print(len(my_dict_2))

print(my_dict_2["Nombre"])
print(my_dict_2[1])
print(my_dict_2[2])

my_dict_2["Esposa"] = "Ximena Serna"
print(my_dict_2)


print(my_dict_2)
del my_dict_2[2]
print(my_dict_2)

print("Esposa" in my_dict_2)

print(my_dict_2.items())
print(my_dict_2.keys())
print(my_dict_2.values())

list1 = ["Nombre", "1", "Piso"]
new_dict = dict.fromkeys(list1)
print(new_dict)

new_dict = dict.fromkeys(["Nombre", "1", "Piso"])
print(new_dict)

new_dict = dict.fromkeys(my_dict_2)
print(new_dict)