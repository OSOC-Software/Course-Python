my_string = "My String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_other_string + my_string)
print(my_other_string + "\n"+  my_string)
print("\t" + my_other_string + "\t"+  my_string)

# Formateo
name , surname, age = "Juan Diego", "Osorio Castrillon", 29
print("Mi nombre es {} {} {} ".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y edad {age}")
print("Mi nombre es %s %s y edad %d" %(name, surname, age))

# Desempaquetado caracteres
language = "Juan"
a, b, c, d  = language

print(a)
print(b)
print(c)
print(d)

# Division
slice_language = language[0:2]
print(slice_language)

slice_language = language[0:]
print(slice_language)

slice_language = language[-2]
print(slice_language)

slice_language = language[0:6:2]
print(slice_language)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.lower())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("a"))
