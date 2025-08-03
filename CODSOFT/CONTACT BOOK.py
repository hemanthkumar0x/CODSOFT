contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"{name} - {info['phone']} - {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {name} - {contacts[name]['phone']} - {contacts[name]['email']}")
    else:
        print("Contact not found.")

while True:
    print("\n--- CONTACK BOOK ---")
    print("1. ADD CONTACTS")
    print("2. VIEW CONTACTS")
    print("3. SEARCH CONTACT")
    print("4. EXIT")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting Contact Book... Goodbye!")
        break
    else:
        print("Invalid choice.")
