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
length = len(usr_pwd)

score = 0

def length_test(usr_pwd):
    global score
    safe = 16
    if length >= safe:
        print("This password meets the length requirements.")
        score += 3
    elif length < 16 and length > 10:
        print("This password is good, but should be 16 characters.")
        score +=1
    else:
        print("This password is too short, it could be guessed or cracked more easily.")

length_test(usr_pwd)

def common_pwd_check(usr_pwd):
    global score
    if usr_pwd in password_list:
        print("Your password was found a the list of the 10000 most common passwords.")
        score -= 3
    else:
        print("Your password wasn't found in the 10,000 most common passwords.")
        score += 1

common_pwd_check(usr_pwd)

def repeating_characters(usr_pwd):
    global score
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
        score += 1
    if repeating >= 3 and repeating < 10:
        print("You have multiple repeating characters next to one another. This is bad security practice.")
        score -= 1
    elif repeating >= 1 and repeating < 3:
        print("You have repeating characters next to one another. This is bad security practice.")
    elif repeating < 1:
        print("Your password doesn't have any repeating characters, that is great!")
        score += 2

repeating_characters(usr_pwd)

def variation(usr_pwd):
    global score
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
        score += 1
    elif unique_characters == 2:
        score += 2
    elif unique_characters == 3:
        score += 3
    elif unique_characters == 4:
        score += 4
    
variation(usr_pwd)

print(f"Your password score is {score}")
