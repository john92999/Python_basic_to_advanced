'''

for i in range(10):
    print("Hello World")

for i in range(1,11):
    print("hi")

'''

'''

number = input("enter a number: ")
total = 0
for i in number:
    total += int(i)
print(total)

'''

'''
for i in range(0,11, 2): # we can give step arguments in for loop
    print(i)

'''


name = input("Enter your name: ").replace(" ", "")
tempvar = ""
for i in name:
    if i not in tempvar:
        print(f'{i}: {name.count(i)}')
        tempvar += i

'''
language = "python3.14"

total = 0

for i in range(len(language)):
    print(type(language[i]))
    if language[i].isdigit():
        total += int(language[i])

print(total)

'''




'''

language = "python3.14"

total = 0

for i in language:
    if i.isdigit():
        total += int(i)

print(total)

'''
