# Hashing is the act of identifying data
# Way to assign a unique/random value for any data
# Input is arbitrary
# Output is always predictable for the same input
# Output of a hash -> digest
# We use crytographic hash functions
# These hashes are practically as good as you can get to unique
import hashlib

# Hash functions expect bytes as input
# encode() method turns strings to bytes
input = [b"backpack", b"Backpack", b"Backpack", b"BACKPACK"]
output = [hashlib.sha256(i) for i in input]

# Hex Digest converts bytes to hex
for out in output:
    print(out.hexdigest())

# Properties of cryptographic hash functions
# Deterministic - Same Input -> Same Hash
# Intractibility - Impossible to guess the input based on the hash (Too many possibilities for brute force)
# Collision Safety - Difficult to find 2 inputs with the same hash
# Avalanche Effect - Smallest input change gives uncorrelated hash
# Speed - Computationally fast to generate a hash

# Bitcoin -> double sha256
# Ethereum -> keccak256

# Bitcoin breakthrough -> Hashes can be used to prove that work for done by a computer
# Bitcoin relies on apparent randomness of crytographic hashes

