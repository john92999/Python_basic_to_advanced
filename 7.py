def add_two(a,b):
    print(a+b)

number1, number2 = input("enter numbers comma seperated").split(",")
add_two(int(number1), int(number2))