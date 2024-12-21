import json
import getpass

def load_passwords(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords, filename):
    with open(filename, 'w') as file:
        json.dump(passwords, file)

def main():
    filename = 'passwords.json'
    passwords = load_passwords(filename)

    while True:
        action = input("Do you want to (add/view/exit)? ").strip().lower()
        if action == "add":
            site = input("Enter the site name: ")
            password = getpass.getpass("Enter the password: ")
            passwords[site] = password
            save_passwords(passwords, filename)
            print(f"Password for {site} added.")
        elif action == "view":
            site = input("Enter the site name: ")
            if site in passwords:
                print(f"Password for {site}: {passwords[site]}")
            else:
                print("No password found for that site.")
        elif action == "exit":
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()