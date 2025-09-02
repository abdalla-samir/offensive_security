# CipherKit

## Command
```
./cipherkit -i <input_file> -t <type:[hex,base64,binary]> -m<mode:[encode,decode]> -o <output_file>
```

## Description
- A command-line tool to encode or decode a file's content using hex, base64, or binary formats.
- It takes a given file and conver it's content into a given format, it simply can:
	- Convert binary to plain text and vice versa
	- Convert hex to plain text and vice versa
	- Convert base64 to plain text and vice versa
- By one script you can convert anything you want


## Usage Example
```
./cipherkit -i file.txt -t hex -m encode -o output.txt
```

## Screenshot
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/scripts/cipherkit/tool_image/cipherkit_tool.png)
