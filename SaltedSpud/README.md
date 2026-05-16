# SaltedSpud
## What is it?
SaltedSpud is a hash cracker that allows users to input a hash (MD5, SHA1, SHA256, SHA512) and check it against either a standard wordlist, or their own file.
  - This is **ONLY** intended for educational use and fun. Do NOT use for malicious purposes

The default list can be found [here](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt)

## How to run
  1. First, run the code from your command line or from your favorite IDE (Neovim is the GOAT)
  2. Enter if you will be using the default list from SecLists, or your own.
     2a. If your own, enter the path/filename
  3. Enter the type of hash you will be using
  4. Enter the hash
  5. Your hash will be checked against the chosen wordlist
  6. An output will be given based upon if your hash was cracked!
     6a. If it was cracked, the plaintext password will be printed as well as how long it took.
     6b. If it wasn't, the program will tell you it wasn't found in the list, as well as runtime.

## Future
- Will support all hash algorithms from hashlib
- Will have some quality of life improvements

## Modules and default list
- [time](https://docs.python.org/3/library/time.html)
- [hashlib](https://docs.python.org/3/library/hashlib.html)
- [Default 100,000 common passwords from SecLists](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt)
