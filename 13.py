'''

def total(a,b):
    return (a+b)

print(total(2,3))

'''

'''
def all_total(*args):
    total = 0
    print(args) #here arguments will become as tuple
    print(type(args))
    for num in args:
        total = total + num
    return total
print(all_total(1,2,3,4,5,6))

'''
'''

def multiply_nums(num, *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(1,2,3,4,4,6)) 

'''

'''

def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [2,3,4]
print(multiply_nums(*nums)) #here the list will unpack, if we don't unpack it will go as a single list variablw

'''

'''

def func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'{k}:{v}')

func(first_name = 'John', last_name = 'Wesley')

d = {'name': 'william', 'age': 30}
func(**d) # unpacking dictionary

'''

def func(name = 'unknown', age=28):
    print(name)
    print(age)

func('John')

# order of parameters, *args, default_parameters, **kwargs
def func(name, *args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('John', 1, 2, 3, a=1, b=2)