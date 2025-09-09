# picoCTF - Based - General-skills

# Challenge Description
To get the flag, you should go through three steps:
1. The program gives you **binary data** and you convert it to word.
2. The program gives you **octal data** and you convert it to word.
3. The program gives you **hexadecimal data** and you convert it to word.

If you enter all values correctly, you will get the flag.

## Solution
I wrote a simple Python script with three functions to decode Binary, Octal, and Hexadecimal strings into plain text.

```
def binary_to_word(binary):
    binaries = binary.split(" ")
    word = ""
    for binary in binaries:
        decimal = int(binary,2)
        character = chr(decimal)
        word += character
    print(word)
    
def octal_to_word(nums):
    octals = nums.split(" ")
    word = ""
    for octal in octals:
        word += chr(int(octal,8))
    print(word)

def hex_to_word(hexa):
    word = bytes.fromhex(hexa).decode()
    print(word)

binary_to_word("Binary_input")
octal_to_word("octal_input")
hex_to_word("hexadecimal_input")
```
### Input
```
binary_to_word("01101100 01101001 01101101 01100101")
octal_to_word("141 156 151 155 141 164 151 157 156")
hex_to_word("70656172")
```

### Output
```
lime
animation
pear
```

After decoding the given values, and entering them in the program in the right order,  
the challenge reveals the **flag**:
```
picoCTF{learning_about_converting_values_02167de8}
```
## Screenshots

![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/based/writeup_images/image_one.png)
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/based/writeup_images/image_two.png)
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/based/writeup_images/image_three.png)
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/crypto/based/writeup_images/image_four.png)
