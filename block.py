from datetime import datetime
import json
from Crypto.Hash import SHA256

class Block:
    def __init__(self, index, sender, receiver, amount, previous_block_hash, token=None, priv_key=None):
        self.index = index
        self.timestamp = str(datetime.now())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.prev_hash = previous_block_hash
        self.nonce = 0
        self.token = token
        self.priv_key = priv_key
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = {
            "index":self.index,
            "timestamp":self.timestamp,
            "sender":self.sender,
            "receiver":self.receiver,
            "amount":self.amount,
            "previous_hash":self.prev_hash,
            "nonce":self.nonce,
            "token":self.token,
            "priv_key":self.priv_key
        }

        block_string = json.dumps(block_data, sort_keys=True).encode("utf-8")

        h = SHA256.new()
        h.update(block_string)
        return h.hexdigest()
    
    def mine(self):
        while not self.hash.startswith("67"):
            self.nonce += 1
            self.hash = self.calculate_hash()