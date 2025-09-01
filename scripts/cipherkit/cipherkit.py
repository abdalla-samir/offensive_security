import argparse
import base64

parser = argparse.ArgumentParser(description="this tool used for decoding")
parser.add_argument("-i","--input",required=True,help="input file") #=> args.input
parser.add_argument("-o","--output",required=True,help="output file") #=> args.output
parser.add_argument("-t","--type",choices=["hex","base64","binary",],required=True,help="decoding type")
parser.add_argument("-m","--mode",choices=["encode","decode"],required=True,help="encode or decode the file")
args = parser.parse_args()

input_file = ""
with open(args.input,"r") as f:
    input_file += f.read()

####### decoding hex format to plain text #######
if args.type == "hex":
    if args.mode == "encode":
        plain_text = input_file
        hex_encoded = plain_text.encode("utf-8").hex()
        print(hex_encoded)
    else:
        hex_code = input_file
        hex_clean_code = hex_code.replace("\n","").replace(" ","")
        decoded_bytes = bytes.fromhex(hex_clean_code)
        hex_decoded = decoded_bytes.decode("utf-8",errors="ignore")
        print(hex_decoded)

if args.type == "base64":
    if args.mode == "encode":
        plain_text = input_file
        base64_encoded = base64.b64encode(plain_text.encode("utf-8")).decode("utf-8")
        print(base64_encoded)
    else:
        base64_code = input_file
        base64_clean_code = base64_code.replace("\n","").replace(" ","")
        base64_decoded = base64.b64decode(base64_clean_code)
        plain_text = base64_decoded.decode("utf-8",errors="ignore")

