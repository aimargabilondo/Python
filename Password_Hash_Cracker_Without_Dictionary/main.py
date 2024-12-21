import hashlib
import random
import string

target_hash = "9834876dcfb05cb167a5c24953eba58c4ac89b1adf57f28f2f9d09af107ee8f0"  

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

collision_found = False

while not collision_found:
    input_str = random_string(3)  # Generate a random string of length 3, if you want try with a longer password change de number 3
    hash_value = hashlib.sha256(input_str.encode()).hexdigest()  # Change 'sha256' to change hashing algorim

    if hash_value == target_hash:
        print(f"Match found! Input: {input_str} produces the target hash: {hash_value}")
        collision_found = True
