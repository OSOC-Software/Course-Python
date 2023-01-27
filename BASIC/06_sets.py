my_set = set() # set 
my_set_2 = {} # dict o set

my_set_2 = {"Juan", 3,123,True}

print(my_set)
print(my_set_2)

print(type(my_set))
print(type(my_set_2))

print(len(my_set_2))

my_set_2.add("Continua creciendo") # Estructura NO ORDENADA
print(my_set_2)

my_set_2.add("Continua creciendo") # No admite repetidos
print(my_set_2)


print("Juan" in my_set_2)
print("Juan" in my_set)

print(my_set_2)
my_set_2.remove(3)
print(my_set_2)

my_set_2.clear()
print(my_set_2)
print(len(my_set_2))

#del my_set_2
#print(my_set_2) #Error


my_set = {12,3.2,54,5}
my_list= list(my_set)
print(my_set)
print(my_list)

my_new_set = my_set.union(my_set_2)
print(my_new_set.union(my_new_set)) #No permite duplicados repetidos 
print(my_new_set)


print(my_new_set.difference(my_set))