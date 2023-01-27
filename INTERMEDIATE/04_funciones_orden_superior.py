def sum(a):
    return a+1

def sum_2_add_one(a,b, sum_fun):
    return sum_fun(a+b)

print(sum_2_add_one(12,1, sum))

### Clousures

def sum_ten(value1):
    def add(value):
        return value + 10 + value1
    return add

add_ = sum_ten(1)
print(add_(12))


### Built-in Higher Order Functions
numbers = [1,3,5,12]
# Map
def times(n):
    return n*2
times_numbers = list(map(times,numbers))
print(times_numbers)
print(list(map(lambda one: one*2, numbers)))

# Filter

def filter_(number):
    if number > 10: 
        return True
    else:
        return False

print(list(filter(filter_, numbers)))
print(list(filter(lambda number:number>10, numbers)))

# Reduce
from functools import reduce

def sum_2(a,b):
    print(a,b)
    return a+b

print(reduce(sum_2,numbers))