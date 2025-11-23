from auth import register, login
from vault import add_entry, list_entries, delete_entry
from db import init_db

def main():
    init_db()

    print("\n🔐 Voice-Protected Password Manager")
    print("----------------------------------")

    while True:
        print("\n1. Register")
        print("2. Login to Vault")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()

        elif choice == "2":
            if login():
                vault_menu()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


def vault_menu():
    while True:
        print("\n--- Vault Menu ---")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Logout")

        c = input("Choose: ")

        if c == "1":
            add_entry()
        elif c == "2":
            list_entries()
        elif c == "3":
            delete_entry()
        elif c == "4":
            return
        else:
            print("Invalid selection!")


if __name__ == "__main__":
    main()
