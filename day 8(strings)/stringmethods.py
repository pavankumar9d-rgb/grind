# 1. upper()
# The upper() method converts a string to upper case.

str = "abdef"
print(str.upper())

# 2. lower()
# The lower() method converts a string to lower case.

q = 'ABEcdg'
print(q.lower())

# 3.strip()
# The strip() method removes any while spaces before and after the string.

w = "pavan kumar"
print(w.strip())

# 4.rstrip()
# The rstrip() removes any trailing characters.

r = "pavan !!!"
print(r.rstrip("!"))

# 5.replace()
# This method replaces all occurrences of a string with another string.

t = "pavan kumar"
print(t.replace("pa","ku"))

# 6. spilt()
# This method spilts the given string at the specified instance and returns the seprated string as list items.

y = "silver surfer"
print(y.split(" "))

# 7.capitalize()
# This method only changes the first letter only to the uppercase remaining will be same.

u = "hello"
print(u.capitalize())

# 8.center()
# This method aligns the string to the center as per the parameters given by the user.

i = "welcome pavan kumar"
print(i.center(30," "))

# 9.count()
# This method returns the number of items the given value has occurred within the given string.

o = "qwertyuidfghjkcvbnmabnnajoa"
countstr = o.count("a")
print(countstr)

# 10.endswitch()
# The endswitch() method checks if the string ends with a given value. if yes then return true else return false.

p = "asdfghjklqwertyui !!!"
print(p.endswith("!!!"))


# 11. find()
# this method searches for the first occurance of the given value and gives thr value and returns the index.

a = "qwertysdfghjkrtyuiop"
print(a.find("t"))

# 12.isalnum()
# This method returns True only if the entire sting only consists of a-z, A-Z, 0-9.
# If any other character or puncuations are present then it returns false.

s = "wertyuiojhgfdsxcvbn@"
print(s.isalnum())

# 13.isalpha()
# this method returns true only if the entrie string is only a-z, A-Z.
# If any other charcater or punctuations or numbers then it will be false.

d = "wertyuifdsxcbnm0"
print(d.isalpha())

# 14.isprintable()
# This method returns True if all the value within the given string are printable, if not, then return false.

f = "sdfghjk654ews"
print(f.isprintable())

# 15.islower()
# This returns true if the string is lower else false

g = "dsdfghjkluytres"
print(g.islower())

# 16.isupper()
# This returns true if the full string is upper else false

h = "SDFOIUYTRDVBN"
print(h.isupper())

# 17.isspace()
# This method return true if any space between the string else false

j = "fghjchj"
print(j.isspace())

# 18.istitle()
# This returns true only id the first letter of rach word of the string is in caps, else false.

k = "SDFGHJK Ddfgh"
print(k.istitle())

# 19.startswith()
# This method checks if the string starts with a given value. if yes then return True, else returns False.

l = "Pavan is a donkey"
print(l.startswith("Pavan"))

# 20.swapcase()
# This method changes the characters casing of the string. Upper to lower and lower to upper.

z = "WERT SDF ERTY"
print(z.swapcase())

# 21.title()
# This converts the string to the title.

x =" sdfgh dfghj ertyu bnm"
print(x.title())