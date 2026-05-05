c_us = "roop"
c_pass = "1234"
username = input("ener the user name:")
password = input("enter the password:")
if username == c_us:
    print("")
    if c_pass == password:
        print("login sucessful")
else:
    print("enter correct credential")
