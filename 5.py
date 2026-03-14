'''
i=1
while i<10:
    print("hello world")
    i +=1

'''
'''

number = int(input("Enter a number: "))
i=total=0
while i <= number:
    total +=i
    i +=1
print(total)

'''

name = input("enter your name: ")
temp_var=""
i = 0
while i < len(name):
    name = name.replace(" ","")
    if name[i] not in temp_var:
        print(f'{name[i]} : {name.count(name[i])}')
    temp_var += name[i]
    i +=1
