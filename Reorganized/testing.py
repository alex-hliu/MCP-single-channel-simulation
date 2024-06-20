mylist = [1,2,3,4,5,6,7,8,9,10]

newlist = []

mylist[:] = [element for element in mylist if element > 5]

print(mylist)
