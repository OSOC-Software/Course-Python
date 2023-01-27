my_list = list()
other_list = [] 

print(len(my_list))

my_list = [123,4,6,23,2,21,5,567,78,345,2,2]

print(len(my_list))

other_list = [213, 2.4, 12, "Juan", "OsoCas", True]

print(len(other_list))
print(type(other_list))
print(type(my_list))

print(my_list[0])
print(my_list[-1])

print(my_list.count(2))

age, height, address, surname, abc, defgh = other_list

print(age, height, address, surname, abc, defgh)

print(my_list + other_list)

# my_list = "Hola Juan Tu puedes con todo ! ! !"
my_list.append("Hola Juan Tu puedes con todo ! ! !")
print(my_list)

my_list.insert(1, "Hola Juan Tu puedes con todo ! ! !")
print(my_list)

my_list[2] = "Sigue adelante, lo estás logrando"
print(my_list)

my_list.remove(123)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

del my_list[4]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list.clear()
print(my_list)





 