import sys
from key_manager import KeyManager

def print_menu():
    print("\nCryptographic Key Management System")
    print("1. Generate new key")
    print("2. List keys")
    print("3. Retrieve key")
    print("4. Rotate key")
    print("5. Delete key")
    print("6. Exit")

def main():
    km = KeyManager()
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        if choice == '1':
            key_id = km.generate_key()
            print(f"Key generated. ID: {key_id}")
        elif choice == '2':
            keys = km.list_keys()
            print("Keys:", keys if keys else "No keys found.")
        elif choice == '3':
            key_id = input("Enter key ID: ").strip()
            key = km.get_key(key_id)
            print(f"Key: {key.decode()}" if key else "Key not found.")
        elif choice == '4':
            key_id = input("Enter key ID to rotate: ").strip()
            if km.rotate_key(key_id):
                print("Key rotated.")
            else:
                print("Key not found.")
        elif choice == '5':
            key_id = input("Enter key ID to delete: ").strip()
            if km.delete_key(key_id):
                print("Key deleted.")
            else:
                print("Key not found.")
        elif choice == '6':
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
