import re


a=str(input("Enter your password: "))
if(len(a)<8):
    print("Password too short")
elif not(re.search('[A-Z]',a)):
    print("No uppercase letters")
elif not(re.search('[0-9]',a)):
    print("no numbers")
elif re.search(r'password123|admin|1234568', a):
    print("Warning")
else:
    print("password selected")
