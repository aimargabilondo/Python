import hashlib

def hash_password(password, algorithm='sha256'):
    """Hash a password using the specified algorithm."""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm: {}".format(algorithm))

def crack_password(hash_to_crack, dictionary_file, algorithm='sha256'):
    """Attempt to crack the password hash using a dictionary attack."""
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            if hash_password(password, algorithm) == hash_to_crack:
                return password
    return None

if __name__ == "__main__":
    hash_to_crack = '5f4dcc3b5aa765d61d8327deb882cf99'
    dictionary_file = 'dictionary.txt'  #this txt have some common passwords, if you change can you use other dictionarys
    algorithm = 'md5'  #change 'sha256' to other shash algorithm

    cracked_password = crack_password(hash_to_crack, dictionary_file, algorithm)
    
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in dictionary.")