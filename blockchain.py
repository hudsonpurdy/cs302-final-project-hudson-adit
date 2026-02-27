import time
from datetime import datetime
import json
from Crypto.Hash import SHA256

class Block:
    def __init__(self, index, data, previous_block_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.prev_hash = previous_block_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = {
            "index":self.index,
            "timestamp":self.timestamp,
            "data":self.data,
            "previous_hash":self.prev_hash
        }

        block_string = json.dumps(block_data, sort_keys=True).encode("utf-8")

        h = SHA256.new()
        h.update(block_string)
        return h.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "Genesis Block Created", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index+1, data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print("Block Index: " + str(block.index))
            print("Data: " + str(block.data))
            print("Hash: " + str(block.hash))
            print("Timestamp: " + str(block.timestamp))
            print("--------")

    def validate_block(self):
        pass

chain = Blockchain()
chain.add_block("huds0n mined 30 chunguscoin")
chain.add_block("huds0n transfered 30 chunguscoin to 4d1t")
chain.add_block("4d1t transfered 10 chunguscoin to j34n_s4l4c")

chain.print_chain()
