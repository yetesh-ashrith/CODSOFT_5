import json

FILENAME = 'contacts.json'

def load_contacts():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    contact = {
        "name": input("Enter name: "),
        "phone": input("Enter phone number: "),
        "email": input("Enter email: "),
        "address": input("Enter address: ")
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']}")
        print("")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = [c for c in contacts if search_term in c['name'] or search_term in c['phone']]
    if found:
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']} - {c['address']}")
    else:
        print("No contacts found matching your search.\n")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'] == name:
            c['phone'] = input("Enter new phone number: ")
            c['email'] = input("Enter new email: ")
            c['address'] = input("Enter new address: ")
            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c['name'] == name:
            contacts.remove(c)
            save_contacts(contacts)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    contacts = load_contacts()
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1': add_contact(contacts)
        elif choice == '2': view_contacts(contacts)
        elif choice == '3': search_contact(contacts)
        elif choice == '4': update_contact(contacts)
        elif choice == '5': delete_contact(contacts)
        elif choice == '6': break
        else: print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()