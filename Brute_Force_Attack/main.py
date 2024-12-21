import itertools
import time

def brute_force_crack(target_password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>,.-;:_¨{[}]+*"!|@#~$%€&/()=ªº\\¬^¿¡?'
    attempts = 0
    start_time = time.time()

    for length in range(1, len(target_password) + 1):  
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target_password:
                end_time = time.time()
                print(f"Password '{target_password}' cracked in {attempts} attempts and {end_time - start_time:.2f} seconds.")
                return
    print("Password not found.")

# Set the target password here
target_password = "!a_"

brute_force_crack(target_password)