# 1. list.sort()
# This method is used to sort the list in ascending order by default. It modifies the original list.

l = [1,2,3,4,5,90,45,12,67]
print(l)
l.sort()
print(l)

# 2. reverse()
#This reverse reverses the order of the list

color = [1,2,4,5]
color.reverse()
print(color)

# 3. index()
# This method returnes the index of the first occurance of the list item.

f = [1,2,3,4,8,2,6,2,4]
print(f.index(4))

# 4. Count()
# Returns the count of the number of items with the given value.

print(f.count(2))

# 5. copy()
# Returns copy of the list.
# This can be done to perform opreations on the list without modifying the original list.

p = ["pop","trunk","max","joke"]
newlist = p.copy()
print(p)
print(newlist) 

# 6.append()
# This appends(add) the value to the list.

p.append("green")
print(p) 

# 7. inser()
# This method inserts an item at the given index. Users has to specify index and the item to be inserted within the insert() method.

g = ["volley","indigo","car"]
g.insert(1,"box")
print(g)

# 8. extend()
# This method adds a entire list or any other collection data type(set,tuple,dictionary) to the exisiting list.

h = ["green","umbrella","blue"]
h.extend(g)
print(h)

# 9. Concatenation
# simply add two lists by using "+" in print
print(g+p)

