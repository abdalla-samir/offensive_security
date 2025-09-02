import argparse
import base64

parser = argparse.ArgumentParser(description="A command-line tool to encode or decode a file's content using hex, base64, or binary formats.")
parser.add_argument("-i","--input",required=True,help="input file")
parser.add_argument("-o","--output",required=True,help="output file")
parser.add_argument("-t","--type",choices=["hex","base64","binary",],required=True,help="Choose the format for encoding/decoding: hex, base64, or binary")
parser.add_argument("-m","--mode",choices=["encode","decode"],required=True,help="Select operation mode: 'encode' will convert plain text to the chosen format, 'decode' will convert from that format back to plain text")
args = parser.parse_args()

input_file = ""
with open(args.input,"r") as f:
    input_file += f.read()
    
if args.type == "hex":
    if args.mode == "encode":
        plain_text = input_file
        hex_encoded = plain_text.encode("utf-8").hex()
        with open(args.output,"w") as f:
            f.write(hex_encoded)
    else:
        plain_text = input_file
        hex_clean_code = plain_text.replace("\n","").replace(" ","")
        decoded_bytes = bytes.fromhex(hex_clean_code)
        hex_decoded = decoded_bytes.decode("utf-8",errors="ignore")
        with open(args.output,"w") as f:
            f.write(hex_decoded)
elif args.type == "base64":
    if args.mode == "encode":
        plain_text = input_file
        base64_encoded = base64.b64encode(plain_text.encode("utf-8")).decode("utf-8")
        with open(args.output,"w") as f:
            f.write(base64_encoded)
    else:
        base64_code = input_file
        base64_clean_code = base64_code.replace("\n","").replace(" ","")
        base64_byte = base64.b64decode(base64_clean_code)
        base64_decoded = base64_byte.decode("utf-8",errors="ignore")
        with open(args.output,"w") as f:
            f.write(base64_decoded)
elif args.type == "binary":
    if args.mode == "encode":
        plain_text = input_file
        binary = ""
        for character in plain_text:
            binary += format(ord(character), "08b")
        with open(args.output,"w") as f:
            f.write(binary)
    else:
        binary_code = input_file
        binary_array = []
        binary_decoded = ""
        for index in range(0, len(binary_code), 8):
            if binary_code[index:index+8] == "\n":
                continue
            binary_array.append(binary_code[index:index+8])
        for chunk in binary_array:
            binary_decoded += chr(int(chunk,2))
        with open(args.output,"w") as f:
            f.write(binary_decoded)
