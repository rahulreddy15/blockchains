# This file can be used to verify files downloaded from the internet
# The checksum and hash function will be specified to verify the file
from hashlib import sha256

file_path = "impage.jpeg"
# Read On;y & Read As Bytes
file = open(file_path, "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")