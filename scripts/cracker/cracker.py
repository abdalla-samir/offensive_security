import argparse
import hashlib

parser = argparse.ArgumentParser(description="this tool used for cracking passwords")
parser.add_argument("-i","--input",required=True,help="the input hashed password")
parser.add_argument("-w","--wordlist",required=False,help="List of passwords")
parser.add_argument("-o", "--output",required=False,help="The output file to save the results")
parser.add_argument("-a","--attack",choices=["dictionary","rainbow","hybrid","bruteforce"],required=True,help="the type of cracking")
parser.add_argument("-t","---type",choices=["md5","sha256","sha512","sha3_224","sha3_256","sha3_384","sha3_512","shake_128","shake_256"],required=True,help="the type of hash to crack")
args = parser.parse_args()

hashed_password = open(args.input).read().split()
hash_func = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
    "sha3_224": hashlib.sha3_224,
    "sha3_256":hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_512": hashlib.sha3_512,
    "shake_128": hashlib.shake_128,
    "shake_256": hashlib.shake_256
}
hash_type = hash_func[args.type]

if args.attack == "dictionary":
    with open(args.wordlist,"r") as pass_file:
            for password in pass_file:
                hashed_dictionary_password = hash_type(password.strip().encode("utf-8")).hexdigest()
                if hashed_dictionary_password == hashed_password:
                    print(f"The Password is {password}")
                else:
                    continue
