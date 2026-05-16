import re
import getpass
from logo import banner
print(banner)

print("Welcome to the password strength test!\n")
print("After entering your password, you will be given a score from 0-10. 10 being very secure and 0 being not secure at all. If the score is negative, you should change your password immediately.")
print("This is purely for fun and educational purposes, this is not advice nor does it hold me liable for any passwords cracked after testing. NO password is 100% secure, please stay up to date on security trends and take your own precautions!!!\n")

with open('passlist.txt', 'r') as f:
    raw_text = f.read()

password_list = raw_text.splitlines()

usr_pwd = getpass.getpass("Enter your password to be checked! It will not show anything for security purposes. ")

score = 0

def length_test(usr_pwd):
    length = len(usr_pwd)
    safe = 16
    if length >= safe:
        print("This password meets the length requirements.")
        return 3
    elif length < 16 and length > 10:
        print("This password is good, but should be 16 characters.")
        return 1
    else:
        print("This password is too short, it could be guessed or cracked more easily.")
        return 0

def common_pwd_check(usr_pwd):
    if usr_pwd in password_list:
        print("Your password was found in a list of the 10000 most common passwords.")
        return -3
    else:
        print("Your password wasn't found in the 10,000 most common passwords.")
        return 1

def repeating_characters(usr_pwd):
    s = ""
    repeating = 0
    for letter in usr_pwd:
        if s == letter:
            repeating += 1
            s = letter
        else:
            s = letter

    if repeating >= 10:
        print("You have ten or more repeating characters. This isn't bad, but it isn't good either. Try using a combination of different ones for length requirements, not just a spamming of the same one\n")
        return 1
    elif repeating >= 3 and repeating < 10:
        print("You have multiple repeating characters next to one another. This is bad security practice.")
        return -1
    elif repeating >= 1 and repeating < 3:
        print("You have repeating characters next to one another. This is bad security practice.")
        return 0
    elif repeating < 1:
        print("Your password doesn't have any repeating characters, that is great!")
        return 2

def variation(usr_pwd):
    unique_characters = 0
    if re.search(r"[a-z]", usr_pwd):
        unique_characters += 1

    if re.search(r"[A-Z]", usr_pwd):
        unique_characters += 1
    
    if re.search(r"[0-9]", usr_pwd):
        unique_characters += 1
    
    if re.search(r"[!@#$%^&*()]", usr_pwd):
        unique_characters += 1
    
    if unique_characters == 1:
        return 0
    elif unique_characters == 2:
        return 1
    elif unique_characters == 3:
        return 2
    elif unique_characters == 4:
        return 3

score += length_test(usr_pwd)
score += common_pwd_check(usr_pwd)
score += repeating_characters(usr_pwd)
score += variation(usr_pwd)

print("The scoring system is as follows:")
print("Any negative number is bad!\n 0-2 is a weak password\n 3-5 is an okay password\n 6-8 is a good password\n 9-10 is a great password!")
print(f"Your password score is {score}")
