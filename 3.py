
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
