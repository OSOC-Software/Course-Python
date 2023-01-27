import re

my_string = "Esta es la lección número 7 expresiones regulares"
my_string_2 = "Esta no es la lección número 6"

match = re.match("Esta es la lección", my_string, re.I)
start,end = match.span()
print(match)
print(start,end)
print(my_string[start:end])
print(re.match("Esta es la lección", my_string_2))

# Search
search = re.search("lección",my_string,re.I)
print(search)

# Find All

findall = re.findall("a", "Hola desde una funcion lenguaje python")
print(findall)
print(len(findall))

# Split

split = re.split("7", my_string)
print(split)

# Sub

sub = re.sub("Esta|esta", "estaaa", my_string)
print(sub)

# Patterns

pattern = r'[L|l]ección'
print(re.findall(pattern, my_string))

pattern = r'[L|l]ección|expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a|z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))