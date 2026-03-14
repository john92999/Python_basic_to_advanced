'''
def add_two(a,b):
    print(a+b)

number1, number2 = input("enter numbers comma seperated: ").split(",")
add_two(int(number1), int(number2))
'''

'''

def last_char(name):
    return name[-1]

print(last_char('John'))

'''

'''

def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

print(greatest(1,2,3))

'''

name = input("Enter a name: ")
def is_palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False
print(is_palindrome(name))