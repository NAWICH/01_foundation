contact = {}

n = input("How many number you want to add:")
for i in range(int(n)):
    name = input(f"\n--- Contact {i+1} ---\nEnter name: ")
    phone = input("Enter number: ")
    email = input("Enter email: ")
    contact[name] = {
        "phone" : phone,
        "email" : email
    }
getter = input("\nwhose information do you need: ")
result = contact.get(getter)

if result:
    print(f"Found! phone: {result['phone']} | Email: {result['email']}")
else :
    print("Contact not found")