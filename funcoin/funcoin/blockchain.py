from datetime import datetime
import json
from hashlib import sha256
import random


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Genesis Block
        print("Creating the genesis block")
        self.chain.append(self.new_block())

    def new_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': self.last_block['hash'] if self.last_block else None,
            'nonce': format(random.getrandbits(64), 'x'),
        }

        block_hash = self.hash(block)
        block["hash"] = block_hash

        self.pending_transactions = []

        #print("Created Block: {0}".format(block['index']))
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount
        })

    @staticmethod
    def valid_block(block):
        return block["hash"].startswith("0000")

    def proof_of_work(self):
        count = 0
        while True:
            count += 1
            new_block = self.new_block()
            if (self.valid_block(new_block)):
                print(count)
                break

        self.chain.append(new_block)
        print('Found a new block: ', new_block)


bc = Blockchain()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()
bc.proof_of_work()

