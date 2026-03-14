numbers = [1,2,3,4]
print(numbers)

words = ["word1", "word2", "word3"]
print(words[1])    

# 1. append method
fruits = ["grapes", "apple"]
fruits.append("mango") #add it at the end of the list
print(fruits)

# 2. insert method
fruits.insert(1, "papaya") #used to insert fruits at a particular position
print(fruits)

#3. Concatenation
fruits1=["kiwi", "banana"]
print(fruits + fruits1)

#4. extend
fruits2 = ["pomogranate", "avacado"]
# fruits.append(fruits1) # this will add list inside a list
fruits.extend(fruits2) # this will add
print(fruits)

#5. pop
fruits.pop() # it will delete last element in the list
fruits.pop(1) # it will delete the element in the position 1


# 6. remove method
fruits.remove("apple") #if you don't know the position you can use remove method

# 7. count
print(fruits.count("grapes"))

# 8. sort
print(fruits.sort())
print(sorted(fruits))

# 9. clear --> clears the entire list
print(fruits.clear())


fruits = ['orange', 'apple', 'pear']
fruits3 = fruits
print(fruits3)

print(fruits == fruits3) # values are same
print(fruits1 is fruits3) # same memory

# 10. split --> convert string to list
userinfo = "John Wesley".split()
print(userinfo)

name, age = 'John,24'.split(',')
print(name)
print(age)

# 11. Join --> convert list to string
userinfo2 = ['john', '28']
print(','.join(userinfo2))

# 12 --> Range to list
numbers = list(range(1,11))
print(numbers)

# 13. index --> To find the position of a element in list
print(numbers.index(5))