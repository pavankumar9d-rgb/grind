#Lists are ordered collection of data items
#they store multiple items in a single variables
#List items are separated by commas and enclosed within square brackets[]
#Lists are changeable meaning we can alter them after creation.



l = [3,5,600]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

# 1.
lst1 = [1,2,3,4,5,6,7,8]
lst2 = ["RED","GREEN","BLUE"]
print(lst1)
print(lst2)

# 2.
color = ["red","blue","green","yellow","grey"]
print(color[len([-1])])
print(color[-2])
print(color[-3])
print(color[-4])
print(color[-5])

#3 
if "3" in color:
    print("yes")
else:
    print("no")
    
    
#4 concatenation types
print(color[2:4])
print(color[1:-1])
print(color[1:5:1])

#5.
#lists comprehension are used for creating new lists from other iterables like lists,
#tuples,dictionaries, sets and even in arrays and string

#syntax : list[expression(item) for item in iterable if Condition]

lst = [i*i for i in range(4)]
print(lst)

lst = [i*i for i in range(12) if i%2==0]
print(lst)