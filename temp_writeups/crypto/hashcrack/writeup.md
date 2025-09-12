# picoCTF - hashcrack - Cryptography

## Challenge Description
The challenge required breaking three layers of password hashes in order: MD5, SHA-1, SHA-256. By finding the original passwords for all three hashes, you could obtain the flag.

## Solution
To solve the challenge, I wrote a python script to:

   - Read a wordlist containing common passwords `rockyou.txt`.
 
   - Compute the hash of each password using `MD5`, `SHA-1` or `SHA-256`.
 
   - Compare the computed hash with the target hash.
 
   - Finally, print the password when a match is found.

## Python Script
```
import hashlib

wordlist = "rockyou.txt"
hashes = {
    "md5":"482c811da5d5b4bc6d497ffa98491e38",
    "sha1":"b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3",
    "sha256":"916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745"
}


for hash_type, target_hash in hashes.items():
    with open(wordlist,"r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password_hashed = getattr(hashlib, hash_type)(password.strip().encode()).hexdigest()
            if password_hashed == target_hash:
                print(f"Password found: {password}")
                break
            else:
                continue
```


## Screenshots
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/hashcrack/writeup_images/hash_cracking.png)
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/hashcrack/writeup_images/challenge.png)
