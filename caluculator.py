a = int(input("enter first number:"))
b = int(input("enter second number:"))
o = input("enter a operator:")
if o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "*":
    print(a*b)
elif o == "/":
    print(a/b)
elif o == "%":
    print(a%b)
elif o == "//":
    print(a//b)
else:
    print("invalid operartor")        