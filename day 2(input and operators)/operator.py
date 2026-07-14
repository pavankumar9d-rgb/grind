#operator

# 1.Aithmetic operator
a = 4
b = 3
print(a + b) #add  #output = 7
print(a - b) #sub  #output = 1
print(a * b) #mul  #output = 12
print(a % b) #mod  #output = 1

# 2.Comparision operators - output is Boolean value(T/F)
a = 4
b = 3
print(b > a) #greater than #output = False
print(b < a) #lesser than  #output = True 
print(a == b) #equal operator #output = False
print(a != b) #not equal operator #output = True

# 3.Assignment operator
a = 5 #assignment operator

# 4.Logical operator
#Rules 
# 1. T + T = T
# 2. F + T = F
# 3. F + F = F

a = 10
b = 20
print(a > 10 and b < 10)    #and operator #output = False
print(a == 10 and b == 20)  #and operator #output = True

#Rules for or operator
#T + F = T
print(a == 10 or b < 10)    #or operator #output = False

print(not(a == 10 and b == 20)) #not operator #output = False

# 5.Identity operator - is, is not(T/F)
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y) #is #output = True
print(x is z) #is #output = False
#Reason = It is based on locations not on the values are same or not.

print(x is not z) #is not #output = True

# 6.Membership operator - in, not in
my_list = ['apple','banana','orange']
print('apple' in my_list)   #in #output = True
print('apple' not in my_list) #not in #output = False


# 7. Bitwise operators - AND(&), OR( | ), XOR( ^ ), NOT( ~ ) etc
a = 5 #5 in binary - 0101
b = 3 #3 in binary - 0010
print(a & b) #AND #output = 1
print(a | b) #OR #output = 7
print(a ^ b) #XOR #output = 6


