'''CLI tool taht manages a hidden .env file. and automatically generate a safe version of that file for github'''
#1.look for .gitignore if not found crate one
#2.check if .env is inside .gitignore. if not append it
#3.take key and value from the user and appends it to end of the .env
#4.opens the .env file and look for key and repalce the value with ***
#5.saves to .env.example
#6.create a fundtion which find .env aand read every linad and temporarily store those values in the system's memory
#7.once the secret is in memory simple use os.getenv('Key') to use it

import os
import json
from dotenv import load_dotenv

def look_for_gitignore():
    #step 1
    if not os.path.exists('.gitignore'):
        with open(".gitignore", "w") as f:
            f.write(".env\n")
        print(".gitignore crated and .env added")
    else:
        #2 check if .env is inside .gitignore
        with open(".gitignore", "r") as f:
            content = f.read()
        if '.env' not in content:
            with open(".gitignore", 'a') as f:
                f.write("\n.env")
                print(".env is added to existing .gitignore")

def add_into_dotenv():
    #3.take key and value and append to .env
    key = input("Enter key to write in .env(for eg:API_key): ").upper()
    value = input("Enter value: ")

    with open(".env", 'w') as f:
        f.write(f"{key} = {value}\n")
    print(f"key saved to .env")

def make_example():
    #4 & 5 open the .env file and look for key and save into .example
    if not os.path.exists(".env"):
        print(".env doesn't exist")
        return
    with open('.env', 'r') as f_real:
        lines = f_real.readlines()
    
    with open('.env.example', 'w') as f_ex:
        for line in lines:
            if '=' in line:
                key = line.split('=')[0]
                f_ex.write(f"{key} = Enter your key here\n")
    print(".env.example updated")

def load_into_memory_and_test():
    #6.read variable form a .env file and sets them in os.environment
    load_dotenv()

    #7.use os.getenv('Key') to get them from memory
    target = input("Enter th ekey name you want to test: ").upper()
    secret = os.getenv(target)

    if secret:
        print(f"found {target} = {secret[:2]}*******")
    else:
        print(f"ERROR! {target} not found")

def main():
    look_for_gitignore()
    while True:
        print("1.Add key and value to .env\n2.make .env.example\n3.load and test \n4.exit")
        choice = input("Choice: ")

        if choice == '1': 
            add_into_dotenv()
        elif choice == '2':
            make_example()
        elif choice == '3':
            load_into_memory_and_test()
        elif choice == '4':
            break
        else: 
            print("Invalid input")

if __name__ =="__main__":
    main()
