import re
import time

login_attempts = {}

def new_user():
    a = input("Enter Username: ")
    b = input("Enter Password: ")
    l = []
    
    if len(b) < 8:
        l.append("Minimum 8 character required.")
    if not re.search('[A-Z]', b):
        l.append("No Uppercase.")
    if not re.search('[1-9]', b):
        l.append("One number required.")
    
    if l:
        for i in l:
            print(i)
    else:
        with open("output.txt", "a") as file:
            file.write(f"{a}:{b}\n")  # Added newline
        print("Registration is done.")

def login():
    global login_attempts
    a = input("Enter Username: ")
    b = input("Enter Password: ")
    
    # Check if the user is locked out
    if a in login_attempts:
        last_attempt_time, attempts = login_attempts[a]
        if attempts >= 3:
            lockout_time = 30
            time_elapsed = time.time() - last_attempt_time
            if time_elapsed < lockout_time:
                remaining = int(lockout_time - time_elapsed)
                print(f"Account locked! Wait for {remaining} more seconds.")
                return
            else:
                # Reset attempts after lockout period
                login_attempts[a] = (time.time(), 0)

    success = False
    try:
        with open("output.txt") as files:
            for line in files:
                if ':' in line:  # Check if line contains a colon
                    username, password = line.strip().split(":")
                    if username == a and password == b:
                        print("\nLogin Successful")
                        success = True
                        break
    except FileNotFoundError:
        print("No users registered yet.")
        return

    if not success:
        print("Invalid Username or Password.")
        
        # Update login attempts
        if a in login_attempts:
            last_attempt_time, attempts = login_attempts[a]
            login_attempts[a] = (time.time(), attempts + 1)
        else:
            login_attempts[a] = (time.time(), 1)
        
        if login_attempts[a][1] >= 3:
            print("Account locked for 30 seconds!")

def page():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Program ended...")
            break
        else:
            print("Invalid choice!")

page()
