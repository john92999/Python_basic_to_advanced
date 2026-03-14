# tuple 
# similar to list stuple can store any data type but they are immutable, once tuple is created you cannot append, insert, pop or remove

tuple = ("one", "two", "three")
mixed = (1,2,3,4.0)

for i in mixed:
    print(i)

nums = (1) # This is not a tuple
words = ('word 1') # This is not a tuple
print(type(nums), type(words))

nums = (1,) # this is a tuple
words = ('word 1', )
print(type(nums), type(words))

fruits = 'apple', 'banana', 'kiwi'
print( fruits, type(fruits))


#tuple unpacking
fruit1, fruit2, fruit3 = fruits
print(fruit1)

# list inside tuple --> We can do modification to list
favoruites = ('Southren mangolia', ['Tokyo', 'hyderabad'])
popped_item = favoruites[1].pop()
print(popped_item)


# function returning two values --> then the function returns value in tuple
def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(func(2,3))


# tuple to list
tuple_to_list = list((1,2,3))
print(tuple_to_list)

# tuple to string
tuple_to_string = str((1,2,3))
print(tuple_to_string)