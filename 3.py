
language = "python"

# positions(index number)

# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

print(language[0:3]) #[StartArgument : StopArgument]
print(language[3:-3])
print(language[-3:6])
print(language[1:])

#Syntax [StartArgument: StopArgument -1 : StepArgument]
print("John"[3::-1]) # Reversing a string
print("John"[::-1]) # Reversing a string
print("John"[-1::-1]) # Reversing a string


#String Methods

name = "JoHn WeSleY"

# 1. len() function
lenght = len(name)
print(lenght)

# 2. lower() method
print(name.lower())

# 3. upper() method
print(name.upper())

# 4. title() method
print(name.title())

# 5. count() method
print(name.lower().count("h"))

# 6. lstrip() method
name = "    john wesley      "
dots = "..............." 

print((name + dots).lstrip())

# 7. rstrip method
print(name.rstrip())

# 8. strip method --> It will remove the left and right spaces but not the middle space in the name like "john wesley"
print(name.strip() + dots)

# 9. replace syntax (character to be replaced, replacing character, number of times to rplace)
string = "she is beautiful and she is a good dancer"
print(string.replace("is", "was"))
print(string.replace("is", "was", 1))

# 10. find() method, find the position of character or string, syntax (str/char to find, starting position)
print(string.find("is"))
print(string.find("is", 5))

is_pos1 = string.find("is")
print(string.find("is", is_pos1 + 1))

# 11. center() method, add extra character to both left and right sides, syntax (what should be center position, character to be added on left and right) if we don't give any character to be added then it will add spaces
name = "John"
print(name.center(7, "*"))

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
