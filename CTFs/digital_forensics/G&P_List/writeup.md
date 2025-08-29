# CyberTalents  - G&P List - Digital Forensics 

# Challenge Description
The challenge provides a `docx` file and you should search for the flag.

## Steps to solve
1. In kali linux, change the file extension to .zip file.
```
cp file.docx file.zip
```
2. Then, unzip it to an external directory.
```
unzip file.zip -d content
```
3. Open the directory and observe the flag

## Explanation
1. Modern word documents `.docx` are not a single binary file like the old `.doc` format.
2. Internally, `.docx` is a ZIP archive containing multiple XML files and folders.
3. So by changing the file extension to `.zip`, we can use tools like `unzip` to unzip the .docx file into folders and files.

## Solution
```
877c1fa0445adaedc5365d9c139c5219
```
## Screenshot
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/digital_forensics/G&P_List/writeup_images/flag.png)
