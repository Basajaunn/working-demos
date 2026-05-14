import hashlib
import time
from logo import art

print(art)
print("Welcome to SaltedSpud! This is an EDUCATIONAL USE ONLY hash cracker that checks a hash against the 100,000 most common passwords list from SecLists by default. You can also choose your own file!")
print("Have fun with it, and do not use this for malicious purposes!!!\n")

## Import file for hashlib and declare it
def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            raw_list = f.read()

        pass_list = raw_list.splitlines()
        return pass_list
    except FileNotFoundError:
        print("That file wasn't found.")
        return None

## Ask for hash type
def hash_alg():
    while True:
        hash_type = input("What type of hash are you entering? MD5, SHA256, SHA512 or SHA1? \n").upper()
        if hash_type == "MD5":
            algorithm= hashlib.md5
            break
        elif hash_type == "SHA256":
            algorithm = hashlib.sha256
            break
        elif hash_type == "SHA512":
            algorithm = hashlib.sha512
            break
        elif hash_type == "SHA1":
            algorithm = hashlib.sha1
            break
        else:
            print("Invalid input, please try again!")
        
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
    while True:
        choice = input("Will you be using the default list? Type yes or no: ").lower()
        if choice == "yes":
            file_name = "100kpass.txt"
            break
        elif choice == "no":
            file_name = input("Please enter the path and file name of your chosen wordlist: \n")
            break
        else:
            print("Invalid input, please try again!")

    pass_list = read_file(file_name)
    
    if pass_list:
        algorithm = hash_alg()
        entered_hash = user_hash()
        start = time.perf_counter()
        user_password = hashing_logic(pass_list, algorithm, entered_hash)
        end = time.perf_counter()
        crack_time = end - start
        if user_password:
            print(f"Your hash was cracked! The password was {user_password}")
            print(f"It took {crack_time:.4f} seconds to crack")
        else:
            print("Your hash was not found in the chosen list!")
            print(f"It took {crack_time:.4f} seconds to look for your password!")
    else:
        print("Invalid filename. Please restart the program.")


if __name__ == "__main__":
    main()
