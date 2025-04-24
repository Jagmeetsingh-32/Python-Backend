import re
import time

login_attempt={}
def register():
    while True:
        l=[]
        a=input("Enter the Username: ")
        b=input("Enter Password: ")
        c=input("Enter email: ")
        if len(b)<8:
            l.append("Minimum 8 characters needed in password.")
        if not re.search('[A-Z]',b):
            l.append("No Uppercase in password.")
        if not re.search('[0-9]',b):
            l.append("No Number in password")
        if not re.search('[^@]+@[^@]+.|@',c):
            l.append("No valid email.")
        valid=["admin@123.com","admin@.com"]
        if not re.search('|'.join(valid),c):
            l.append("Warning don't use such emails")
        if True:
            with open("output.txt","r") as file:
                for i in file:
                    if i==c:
                        print("E-mail is already used.")
                        break
        if l:
            for i in l:
                print(i)
        else:
            with open("output.txt","a") as file:
                file.write(f'\n{a}:{b}:{c}')
                print("registration is done")
                break

def login():
    global login_attempt
    a=input("Enter the Username: ")
    b=input("Enter Password: ")
    c=input("Enter email: ")
    if a in login_attempt:
        last_attempt,attempt=login_attempt[a]
        if attempt >=3:
            wait_time=30
            time_elapsed=time.time()-last_attempt
            if time_elapsed < wait_time:
                remain_time=int(wait_time-time_elapsed)
                print(f'Wait for{remain_time}sec to login again.')
                return
    
    success=False
    try:
        with open("output.txt") as file:
            for i in file:
                i=i.strip()
                if i:  # Check if the line is not empty
                    parts = i.split(":")
                    if len(parts) == 3:  # Ensure there are exactly 3 parts
                        username, password, email = parts
                        if username == a and password == b and email == c:
                            print("Successfully logged in.")
                            success = True
                            break
    except FileNotFoundError:
        print("File not found error.")
    
    if not success:
        if a in login_attempt:
            last_attempt,attempt=login_attempt[a]
            login_attempt[a]=(time.time(),attempt+1)
        else:
            login_attempt[a]=(time.time(),1)
        if login_attempt[a][1]>=3:
            print("Your account is locked for 30sec.")
        
                

def page():
    while True:
        print("Enter 1 for registration.\n2 for login.\n3 for exit.")
        choice=input("Enter your choice: ")
        if choice=="1":
            register()
        if choice=="2":
            login()
        if choice=="3":
            print("Ok chlo so jao hun.")
            break
        else:
            print("Wrong choice.")
page()