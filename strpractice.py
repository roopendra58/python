###creating a string
s = 'this is a string'
s1 = "this is a string s1"
s2 = '''this is a string s3'''
print(s)
print(s1)
print(s2)

###string slicing
print(s[0:10])
print(s1[:5])
print(len(s2))
###string methods usage

r = "roopendra prathap kanam"
print(r)
print(len(r))
print(r[9:17])
print(r[-23])
print(r.upper())
print(r.lower())
print(r[::-1])
print(r.count())

##Print each character of a string using a loop.

s = "roopendra prathap"
for i in s:
    print(i)
### slicing using the for loop
s1 = "roopendra prathap"
for i in s1:
    if s1[0:8]:
        continue
    else:
        print(i)
 
###string using while loop
r1 = "roopendra prathap"
while r1[6] == 'd':
    print(r1)
    break  ###while is used to checking based on the condition 

## Check whether a string is empty or not.
r ="roopendra prathap"
if len(r)==0:
    print("this is empty string")
else:
    print("the string is not empty string is:",r)

###Reverse a string.
r = "roopendra prathap"
print(r[::-1])
print(r)

###Check whether a string is a palindrome.  and also taking user string input
r = input("enter a string:")
if r == r[::-1]:
    print("the string is palindrome:",r)
else:
    print("the string is not palindrome")
 
##Remove spaces from a string. 
r = "r o o p e n d r a p r a t h a p"
print(r.lstrip())
print(r.replace(" ",""))
print(r.rstrip())

##Print characters at even index positions.
s = input("Enter a string: ")

for i in range(0, len(s), 2):
    print(s[i], end="")

##Remove duplicate characters from string
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)

###Find largest word in a sentence 
r = "roopendra prathap kanam"
