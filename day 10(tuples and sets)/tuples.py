# tuples are immutable lists, meaning they cannot be changed after they are created. They are defined using parentheses () instead of square brackets [].
# these are ordered collections of elements, and they can contain duplicate values. Tuples are useful for grouping related data together and can be used as keys in dictionaries.
# these are unchangeable, so they are often used to represent fixed collections of items.
# functions that can be used with tuples include count(), index(), len(), max(), min(), sum(), sorted(), and reversed().

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("pavan", 19, False, 5.3, 19)
print(tuple1)
print(tuple2)

details = ("kumar", 19, "pavan", 5.3, False)
print(details[0])

country = ("India", "USA", "UK", "Canada", "Australia")
if "USA" in country:
    print("USA is present in the tuple")
else: 
    print("USA is not present in the tuple")
    
animals = ("dog", "cat", "rabbit", "hamster", "parrot")
print(animals[3:7])
print(animals[-3:-1])

