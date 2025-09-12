# CyberTalents  - T-Jungle - Web Security

# Challenge Description
The challenge provides php code with a condition that takes the value from the `passwd` URL query string, hashes it, and compares it with a predefined hash value, if the condition is true, access is granted.

## Steps to solve
1. In the URL, add the following query: 
```
/?passwd=QNKCDZO
```
2. Observe that you granted access and the flag appears.


## Explanation
1. The php code takes the value of the query parameter `passwd` and passes it to `hash()` function.
2. Notice that PHP uses the `==` operator and the hashed value on the right-hand side begins with `0e` followed by digits like that `0e123465789....`.
3. When you use `==`, PHP tries to convert both sides to numbers if they look numeric.
4. PHP interprets this value as scientific notation: `0 x 10^(....)`.
5. Since anything multiplied by zero is zero, the hash value is effectively treated as 0.
6. By entering a value that, when hashed, produces a string in the pattern `0e......`, PHP treats it as zero
7. Thus `0 == 0` is true, the condition passes, and access is granted, printing the flag.

## Solution
```
/?passwd=QNKCDZO
```

## Sceenshot
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/T-jungle/writeup_images/t_jungle_challenge.png)
