from datetime import datetime
import json
from Crypto.Hash import SHA256

class User:
    def __init__(self, username):
        self.username = username
        self.balance = 0
        self.private_key = self.compute_private_key()

    def compute_private_key(self):
        return "key"


class Block:
    def __init__(self, index, data, previous_block_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.prev_hash = previous_block_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = {
            "index":self.index,
            "timestamp":self.timestamp,
            "data":self.data,
            "previous_hash":self.prev_hash,
            "nonce":self.nonce
        }

        block_string = json.dumps(block_data, sort_keys=True).encode("utf-8")

        h = SHA256.new()
        h.update(block_string)
        return h.hexdigest()
    
    def mine(self):
        while not self.hash.startswith("67"):
            self.nonce += 1
            self.hash = self.calculate_hash()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        block = Block(0, "Genesis Block Created", "0")
        block.mine()
        return block
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index+1, data, previous_block.hash)
        new_block.mine()
        if new_block.hash.startswith("67"):
            self.chain.append(new_block)
            print("Valid block added.")
        else:
            print("Invalid block not added")

    def validate_block(self, block):
        if block.hash != block.calculate_hash():
            return False
    
        if not block.hash.startswith("67"):
            return False
        
        return True
    
    def validate_chain(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]

            if not self.validate_block(current_block):
                return False
            
            if i == 0:
                continue

            previous_block = self.chain[i-1]

            if current_block.prev_hash != previous_block.hash:
                return False
        
        print("Blockchain validated.")
        return True

    def print_chain(self):
        for block in self.chain:
            print("Block Index: " + str(block.index))
            print("Data: " + str(block.data))
            print("Hash: " + str(block.hash))
            print("Timestamp: " + str(block.timestamp))
            print("--------")

chain = Blockchain()
chain.add_block("huds0n mined 30 chunguscoin")
chain.add_block("huds0n transfered 30 chunguscoin to 4d1t")
chain.add_block("4d1t transfered 10 chunguscoin to j34n_s4l4c")

chain.print_chain()
chain.validate_chain()
