import json
import getpass
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def main():
    key = generate_key()
    save_key(key)

    passwords = {}
    while True:
        action = input("Do you want to (add/view/exit)? ").strip().lower()
        if action == "add":
            site = input("Enter the site name: ")
            password = getpass.getpass("Enter the password: ")
            encrypted_password = encrypt_password(password, key)
            passwords[site] = encrypted_password.decode()
            print(f"Password for {site} added.")
        elif action == "view":
            site = input("Enter the site name: ")
            if site in passwords:
                encrypted_password = passwords[site].encode()
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Password for {site}: {decrypted_password}")
            else:
                print("No password found for that site.")
        elif action == "exit":
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()