#JSON-Powered Expense Tracker
import json
from datetime import date
from dateutil import parser
import os

#function go get date
def get_date():

    own_custome = input("\n1.default today date\n 2.Enter custome date\n Enter you choice:")
    if own_custome == '1':
        expense_date = date.today()
    elif own_custome == '2':
        expense_date = parser.parse(input("Enter date: "))
    else :
        print("Invalid input try again!")
        return get_date()
    return expense_date.isoformat()

def add_expense(storage):    
    category = input("In which category you want to add your expense: ")

    if category not in storage:
        print(f"{category} doesn't exist in our category")
        crete_category = input("\n Do you want to create new category (y/n): ")
        if crete_category == 'y':
            storage[category] = []
        else:
            return

    product_name = input("Add name for storing: ")
    amount = int(input("How much Money do you used:"))
    description = input("Add description(press Enter for blank)")
    expense_date_val = get_date()

    storage[category]= [product_name,amount, description, expense_date_val]

    with open('data.json', 'w') as fp:  
        json.dump(storage, fp)
    print("Sucessfully added")

def view_monthly_expenses(storage):
    total = 0
    for category in storage:
        for items in storage[category]:
            total +=items[1]

    return total

def view_all(storage):
    print(json.dumps(storage, indent=4))

def main():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as fp:
            storage = json.load(fp)
    else:
        storage = {}

    while True: 
        print("\n1.Add Expense\n2.View Total\n3.View All\n4.Exit")
        choice = input("choose one : ")
        
        if choice == '1':
            add_expense(storage)
        elif choice == '2':
            print("Total spent:", view_monthly_expenses(storage))
        elif choice == '3':
            view_all(storage)
        elif choice == '4':
            break
        else:
            print("invalid input")

if __name__ == "__main__":
    main()