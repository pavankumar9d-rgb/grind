#1Print Numbers From 1 to 10


for i in range(1,16):           # output: 1 2 3 4 5 6 7 8 9 10
    print(i)
    
#2 Print Even Numbers up to 20

for j in range(2,21,2):         # output: 2 4 6 8 10 12 14 16 18 20
    print(j)
    
# 3 Calculate the Sum of a Range
total_sum = 0
for k in range(1,11):          #output: 55
    total_sum += k
    
print(total_sum)


#4 Loop Through a List
languages=["p","a","v","a","n"]          #output: p a v a n
for language in languages:
    print(language)
    

#5. Filter List Items using if Conditions
list = [-3,-20,-4,0,1,6,155,190]
for li in list:
    if li > 0:
        print(li)
        
#6. Print Each Character in a String
out = "python"
for l in out:            #output: P y t h o n
    print(l)
    
    
#7. Generate a Multiplication Table
number = 4
for m in range(1,11):
    print(F"{number}x{m}={number * m}")
    
#8. Count the Vowels in a Text
text = "pavan kumar"
vowel_count = 0
for char in text:
    if char in "aeiou":
        vowel_count +=1
        
print(vowel_count)

#9. Reverse a String Using a Loop
p = "python"
reversed_word = ""

for char in p:
    reversed_word = char + reversed_word

print(reversed_word)


#10. Multiply All Numbers in a List
numbers = [1,2,3,4,5]
pro = 1
for o in numbers:
    pro *=o
print(pro)