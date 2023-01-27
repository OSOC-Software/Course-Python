my_tuple = tuple()
my_tuple_2 = ()


my_tuple = (12,3,5,"Juan")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[2])
print(my_tuple[0:1])

print(my_tuple.count(12))
print(my_tuple.index("Juan"))


# my_tuple[1] = 12 #Error
my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple[1] = 12 
print(my_tuple)


del my_tuple
# print(my_tuple) No exist for DEL