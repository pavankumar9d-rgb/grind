# STRINGS

# def = In python, anything that you enclose between single or double quotations marks is considered to be a sting.
# A string is essentially a sequence or array of textual data. String are used when working with unicode charcaters.
# These are immutable

# 1.
name = "pavan"
print(name)

n = 'pavan'
print(n)

print("HEllo, "+n +name)

# 2. multiple lines(by using ''' ''' or """ """)
text = """Try Google Flow, the ultimate AI for creatives. 
Transform ideas into reality using Google's advanced 
generative models for cinematic video, images, & tools."""
print(text)

# 3.accesing charcaters of a string
print(name[3])

# 4. looping thorough a string

for character in n:
    print(character)
    