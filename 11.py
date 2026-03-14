# set unorderd collection of unique items

s = {1,2,3,2}
print(s)

l = [1,2,3,4,5,6,2,4,5,6,1,2,3]
print(set(l))

# add
s.add(1)
print(s)

# remove
s.remove(3)
print(s)

# discard
s.discard(5)
print(s) # it doesnot remove throw error if it the item is not there

# clear
s.clear()

# union and intersections
s1 = {1,2,3,4}
s2 = {3,4,5,6}

s3 = s1 | s2
print(s3)

s3 = s1 & s2
print(s3)