# list comprehension
'''

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1,11)]
print(squares2)

'''

'''
negative  = []
for i in range(1,11):
    negative.append(-i)
print(negative)

negative2 = [-i for i in range(1,11)]

'''

'''
names = ['John', 'Wesley', 'William']
new_list = []
 
for name in names:
    new_list.append(name[0])

print(new_list)

new_list_2 = [n[0] for n in names]
print(new_list_2)


'''

'''

numbers = list(range(1,11))
even_nums = [i for i in numbers if i%2 ==0]
print(even_nums)
odd_nums = [i for i in numbers if i%2 !=0]
print(odd_nums)

'''
'''

nums = list(range(1,20))
new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]

'''

'''
example = [[1,2,3], [1,2,3], [1,2,3]]

nested_comp = [[i for i in range(1,4)] for j in range(3)]

'''


# Dictionary comprehension

#square = {1:1, 2:4, 3:9}
square2 = {num: num**2 for num in range(1,11)}
print(square2)

string = 'John Wesley'
word_count = {char:string.count(char) for char in string}
print(word_count)

# d = {1: 'odd', 2: 'even'}
odd_even = {i: ('even' if i%2 == 0 else 'odd') for i in range(1,11)}
print(odd_even)

 