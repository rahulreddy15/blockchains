###### Blockchains

Every block on the blockchain contains within itself the hash of the previous block. This goes all the way back to the first block.

A block can contain any data: files, images, transactions, records, etc.
Ethereum is called a "world computer" because ethereum blocks contain executable code as part of their data, instructing participants on the network to perform operations on the network itself.

Chain -> Each block contains hash of the previous block forming a chain
Linking of Hashes -> Fraud Prevention & Immutability

If an attacker somehow corrupted an earlier block in the chain, then all subsequent blocks will have to change because their hashes will be incorrect. If a single bit in any earlier block were to be tampered with the entire blockchain thereafter woulld be invalid. This is the chain in blockchain - They are secured by a chain of hashes.

If somebody were to defraud a block, by changing the amount of a transaction somewhere in the chain, the previous_hash field of the next block would be different, leading to all the consequent hashes being different. And everyone in the Bitcoin network would immediately notice the discrepancy and ignore the change.

