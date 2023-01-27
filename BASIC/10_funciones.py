def my_function():
    print("First function")

my_function()

def sum_two_values(a,b):
    print(a+b)

sum_two_values(1,2)
sum_two_values("1","2")


def sum_two_values_return(a,b):
    return a+b

result = sum_two_values_return(23,124)
print(result)

def print_name(name, surname):
    print(f"Usuario {name} {surname}")

print_name("Juan Diego", "Osorio C")


def print_name_2(name, surname):
    print(f"Usuario {name} {surname}")

print_name_2(name="Juan Diego",surname= "Osorio C")

def print_name_default(name, surname, alias="Default"):
    print(f"Usuario {name} {surname}, Alias: {alias}")

print_name_default("Juan", "Osorio")


def infinity_params(*params):
    print(params)

infinity_params("Hola", 23,4,345,234, "Juan")