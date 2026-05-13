import hashlib

## Import file for hashlib and declare it
def read_file():
    with open('100kpass.txt', 'r') as f:
        raw_list = f.read()

    pass_list = raw_list.splitlines()
    return pass_list

## Ask for hash type
def hash_alg():
    hash_type = input("What type of hash are you entering? MD5, SHA256, SHA512 or SHA1? \n")
    if hash_type == "MD5":
        algorithim = hashlib.md5()
    elif hash_type == "SHA256":
        algorithim = hashlib.sha256()
    elif hash_type == "SHA512":
        algorithim = hashlib.sha512()
    elif hash_type == "SHA1":
        algorithim = hashlib.sha1() 
    
    return algorithim
## Ask user for hash input
def user_hash():
    entered_hash = input("Please enter your hash to be checked: \n")
    
    return entered_hash


def hashing_logic(pass_list, algorithim, entered_hash):
    x = algorithim
        for s in pass_list:
            encoded_data = s.encode()
            x.update(encoded_data)
            x.hexdigest()
            if x.hexdigest() == entered_hash:
                match = True
                print("Your hash has been cracked!")
            else:
                match = False

## Begin main function of program 
def main():
    pass_list = read_file()
    algorithim = hash_alg()
    entered_hash = user_hash()
    hashing_logic(pass_list, algorithim, entered_hash)

    
if __name__ == "__main__":
    main()

## Alert user of match
