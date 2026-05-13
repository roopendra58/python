## the identity operators
a =50 
b =70
c = 50
print(a is b)
print(a is c)
print(b is not c)

##membershipe operators

list = [10,20,30,40,50,60,70,80]
list1 = ['apple','bananna','orange','watermelon']
list3 = ['c',"roopendra",40,56.09,64564]
for i in list,list1,list3:
    print(i)
print("roopendra" in list3)
print("lemon" not in list1)
print("this is for practice")
a = ["roopendr","prathap","kanam",'r',51,5262422]
for i in a:
    print(i)

##strings
s ="roopendra prathap"
for i in s:
    print(i)

##list methods
a = ["roopendr","prathap","kanam",'r',51,5262422,10,20,30,40,50,60,70,80,'apple','bananna','orange','watermelon']
a.append(500)
a.remove("roopendr")
print(a)
a.clear()
print(a)
a.extend(0)
print(a)

n =5
for i in range(1,n+1):
    for j in range(i):
        print("*",end ="")
    print()
n = 5

for i in range(1, n+1):
    for j in range(i):
        print("*",end = "  " )
    print()
        
##functions
def addition(x,y):
    if x<y:
        print("x is less than y:")
    else:
        print("x is grater than y")
addition(10,10)

##sum of the numbers from the 1 to 100
total = 0
for i in range(1,100):
    total = total + i
    print(total)
##sum of the numbers from the 1 to n
a =int(input("enter a number:"))
total = 0
for i in range(1,a):
    total = total + i
    print(total)

##multiplication table
a = int(input("enter a number:"))
for i in range(1,11):
 print(a,"*",i,"=",a*i)

##Factorial of a Number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

##count Digits in a Number
a = "4525552251255255252452"
print(len(a))