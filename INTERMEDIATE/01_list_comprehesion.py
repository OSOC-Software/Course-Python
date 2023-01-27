my_list_original = [12,4,5,6,1213,123,467,4e6,78,0]
my_list = [i for i in my_list_original]
print(my_list)

 
my_list = [i for i in range(7)]
print(my_list)

my_range = range(0,8)
print(my_range)

new_list = list(my_range)
print(new_list)


new_list = list([i * i for i in range(10)])
print(new_list)

def sum_five(a):
    return a + 5

new_list = list([sum_five(i) for i in range(10)])
print(new_list)
