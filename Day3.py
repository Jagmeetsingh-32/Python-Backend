import re
a=str(input("Enter the username: "))
b=str(input("Enter your password: "))
l=[]
if (len(b)<8):
    l.append("Too short ")
if not (re.search('[A-Z]',b)):
    l.append("NO uppercase letter")
if not (re.search('[0-9]',b)):
    l.append("No numbers")
valid=["password123","12345678","admin@123"]
if  (re.search('|'.join(valid),b)):
    print("Warning: Don't use such type of password")
elif l:
    for i in l:
        print(i)
file1=open("C:\\Users\\acer\\OneDrive\\Grok daily_pr\\output.txt","a")
file1.write("\nUsername: "+a+"\nPassword: "+b)
file1.close()



def data_leak():
    try:
        with open("C:\\Users\\acer\\OneDrive\\Grok daily_pr\\output.txt","r") as files:
            for i in files:
                if "Username" in i:
                    username=i.split("Username")[1].strip()
                    print("Leaked username",username)
    except FileNotFoundError:
        print("File not found")
data_leak()                   
