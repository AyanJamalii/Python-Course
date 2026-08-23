import json
import os

while True:
  print("\n--- 📞 CONTACT BOOK MANAGER ---")
  print("1. View all Contacts")
  print("2. Add new Contact")
  print("3. Search Contact")
  print("4. Close Contacts")

  choice = input("Enter your choice (1-4): ").strip()

  if choice == "1":
    if os.path.exists("contacts.json"):
      with open("contacts.json", "r") as f:
        try:
          contacts = json.load(f)
        except json.JSONDecodeError:
          contacts = {}

      if contacts:
        print("\n--- Contact List ----")
        for name, number in contacts.items():
          print(f"👤 {name} : {number}")
      else:
        print("\nContact book is empty.")
    else:
      print("\nNo contact is in list.")

  elif choice == "2":
    name = input("Enter Contacts Name: ").strip()
    number = input("Enter Contacts Number: ").strip()

    contacts = {}

    if os.path.exists("contacts.json"):
      with open("contacts.json", "r") as f:
        try:
          contacts = json.load(f)
        except json.JSONDecodeError:
          contacts = {}

    if name in contacts:
      print(f"⚠️ {name} already exists in Contacts.")
    else:
      contacts[name] = number
      with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
      print(f"✅ {name} added to Contacts successfully!")

  elif choice == "3":
    search_contact = input("Search Contact Name: ").strip()

    if os.path.exists("contacts.json"):
      with open("contacts.json", "r") as f:
        try:
          contacts = json.load(f)
        except json.JSONDecodeError:
          contacts = {}

      if search_contact in contacts:
        print(f"\n🔍 Found: {search_contact} ➔ {contacts[search_contact]}")
      else:
        print(f"\n❌ '{search_contact}' not found in list.")
    else:
      print("\nNo contacts saved yet.")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid choice! Please choose 1-4.")
    