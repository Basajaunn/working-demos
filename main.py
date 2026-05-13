import hashlib
from logo import art

print(art)

print("Welcome to SaltedSpud! This is an EDUCATIONAL USE ONLY hash cracker that checks a hash against the 100,000 most common passwords list from SecLists")
print("Have fun with it, and do not use this for malicious purposes!!!\n")

## Import file for hashlib and declare it
def read_file():
    with open('100kpass.txt', 'r') as f:
        raw_list = f.read()

    pass_list = raw_list.splitlines()
    return pass_list

## Ask for hash type
def hash_alg():
    hash_type = input("What type of hash are you entering? MD5, SHA256, SHA512 or SHA1? \n").upper()
    if hash_type == "MD5":
         algorithm= hashlib.md5
    elif hash_type == "SHA256":
        algorithm = hashlib.sha256
    elif hash_type == "SHA512":
        algorithm = hashlib.sha512
    elif hash_type == "SHA1":
        algorithm = hashlib.sha1
    
    return algorithm
## Ask user for hash input
def user_hash():
    entered_hash = input("Please enter your hash to be checked: \n")
    
    return entered_hash


def hashing_logic(pass_list, algorithm, entered_hash):
    for s in pass_list:
        s = s.encode()
        t = algorithm(s)
        hashed_word = t.hexdigest()
        if hashed_word == entered_hash:
            user_password = s.decode()
            return user_password
    return False

## Begin main function of program 
def main():
    pass_list = read_file()
    algorithm = hash_alg()
    entered_hash = user_hash()
    user_password = hashing_logic(pass_list, algorithm, entered_hash)
    if user_password:
        print(f"Your hash was cracked! The password was {user_password}")
    else:
        print("Your hash was not found in the 100,000 most common passwords")


if __name__ == "__main__":
    main()
