###taking the multiple inputs from the user 
first_name,last_name = input("enter the first and last name:").split()
print("first_name:",first_name)
print("last_name:",last_name)

##taking integer input from the user
a = int(input("enter a number a:"))
b = int(input("enter number b:"))
c = a+b
print("the sum of the two numbers:",c)

###taking the multiple number inputs
a, b = map(int, input("Enter two numbers: ").split())
print("The value of a:", a)
print("The value of b:", b)
c = a+b
print("the sum of the two numbers:",c)

###taking the flot input
price = float(input("enter the price:"))
if price >= 1000:
    print("you get 100 cash price:100")
else:
    print("buy next time to get price thank you for shopping:")
print("the total price :",price)

###