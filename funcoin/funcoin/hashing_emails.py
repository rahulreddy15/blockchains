# 1. Alice and Bob share a secret phrase S
# 2. Alice then creates a hash H of the message M with the secret appended to the end of the message
#    H = Hash(M+s)
# 3. Alice sends H and M to Bob
# 4. Bob checks message integrity by computing H and seeing if the hashes are same

from hashlib import sha256

secret_phrase = 'superragi'

def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()

email_body = "Hey Bob, I think you should learn about Blockchains! I've been investing in Bitcoin and currently have exactly 12.03 BTC in my  account."
print(get_hash_with_secret_phrase(email_body, secret_phrase))

# Where in the body the secret phrase can be inserted can be modified
# The hashing protocol to be used has to be agreed upon beforehand as well
