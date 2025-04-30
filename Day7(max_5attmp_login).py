import bcrypt
import time
from datetime import datetime

# Global variables
login_attempts = {}
LOCKOUT_TIME = 30  # seconds
MAX_ATTEMPTS = 5

def register():
    username = input("Enter Username for registration: ").strip()
    password = input("Enter Password for registration: ").encode()
    
    # Input validation
    if not username or not password:
        print("Username and password cannot be empty!")
        return
        
    hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt())
    
    try:
        # Check if username already exists
        with open("user7.txt", "r") as f:
            for line in f:
                if line.split(":")[0] == username:
                    print("Username already exists!")
                    return
                    
        # Save new user
        with open("user7.txt", "a") as f:
            f.write(f'{username}:{hashed_pass.decode()}\n')
            print("Registration successful!")
            
    except FileNotFoundError:
        # Create file if it doesn't exist
        with open("user7.txt", "w") as f:
            f.write(f'{username}:{hashed_pass.decode()}\n')
            print("Registration successful!")

def login():
    global login_attempts
    
    username = input("Enter Username for Login: ").strip()
    password = input("Enter Password for Login: ").encode()
    
    # Check rate limiting
    if username in login_attempts:
        last_attempt, attempts = login_attempts[username]
        
        if attempts >= MAX_ATTEMPTS:
            time_elapsed = time.time() - last_attempt
            if time_elapsed < LOCKOUT_TIME:
                remaining = int(LOCKOUT_TIME - time_elapsed)
                print(f'Account locked! Try again in {remaining} seconds.')
                return
            else:
                # Reset after lockout period
                login_attempts[username] = (time.time(), 0)
    
    try:
        with open("user7.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                    
                stored_user, stored_hash = line.split(":", 1)
                
                if stored_user == username:
                    if bcrypt.checkpw(password, stored_hash.encode()):
                        print("Login successful!")
                        # Reset attempts on successful login
                        if username in login_attempts:
                            del login_attempts[username]
                        return
                    else:
                        print("Invalid password!")
                        # Update failed attempts
                        if username in login_attempts:
                            login_attempts[username] = (time.time(), login_attempts[username][1] + 1)
                        else:
                            login_attempts[username] = (time.time(), 1)
                            
                        if login_attempts[username][1] >= MAX_ATTEMPTS:
                            print("Too many failed attempts! Account locked for 30 seconds.")
                        return
                            
            print("Username not found!")
            
    except FileNotFoundError:
        print("No users registered yet!")
        return

def page():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

if __name__ == "__main__":
    page()
