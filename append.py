list=[5,2,9]
list.append(100)
print(list)

list=[5,2,9]
list.append(100,101) # TypeError: append() takes exactly one argument (2 given)
print(list)

#adding tupples to the list
list=[1,2,4,2,3]
list.append((1,2))
print(list)