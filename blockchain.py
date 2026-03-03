from user import User
from block import Block
from nft import NFT

class Blockchain:
    def __init__(self):
        self.users = {
            "SYSTEM":User("SYSTEM"),
            "HUDSON":User("HUDSON"),
            "ADIT":User("ADIT")
            }
        
        self.chain = [self.create_genesis_block()]
        self.users["SYSTEM"].balance = 999999999999999999999
        self.nftlist = {
            "67" : NFT("67", "HUDSON", "3toadbanana.github.io/nftdata/hudson1"),
            "124" : NFT("124", "HUDSON", "3toadbanana.github.io/nftdata/hudson2"),
            "27" : NFT("27", "ADIT", "3toadbanana.github.io/nftdata/adit1")
        }
    
    def create_genesis_block(self):
        block = Block(0, "None", "None", 0, "0")
        block.mine()
        return block
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f"Added User {username}!")
            return True
        
        print(f"Error: User {username} already exists.")
        return False

    def print_balances(self):
        for user in self.users:
            print(user + ": " + str(self.users[user].balance))
    
    def add_block(self, sender, receiver, amount, token=None, priv_key=None):
        amount = int(amount)
        
        if sender not in self.users or receiver not in self.users:
            print("Sender or receiver does not exist.")
            return False

        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index+1, sender, receiver, amount, previous_block.hash, token, priv_key)
        new_block.mine()
        if self.validate_block(new_block):
            self.chain.append(new_block)
            print("Valid block added.")
        
        else:
            print("Invalid block not added")
            return False

        self.users[sender].balance -= amount
        self.users[receiver].balance += amount

        if token in self.nftlist and self.nftlist[token].owner == receiver and priv_key == self.users[receiver].private_key:
            self.nftlist[token].owner = sender
            return True
        
        return False

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
            print("Sender: " + str(block.sender))
            print("Receiver: " + str(block.receiver))
            print("Amount Sent: " + str(block.amount))
            print("Hash: " + str(block.hash))
            print("Timestamp: " + str(block.timestamp))
            print("-----------------------------")

    def mint_nft(self, owner, url, token, priv_key):
        if owner not in self.users:
            self.add_user(owner)
            print(f"Added User {owner}!")

        if token in self.nftlist:
            print(f"Error: Token {token} already exists!")
            return False
        
        if priv_key == self.users[owner].private_key:
            newNFT = NFT(token, owner, url)
            self.nftlist[token] = newNFT
            print(f"Minted NFT for User {owner}! Token {token}.")
            return True
        
        return False

    def get_nft(self, id):
        return self.nftlist.get(id)

    def get_user_nfts(self, user):
        if user not in self.users:
            print(f"Error: User {user} is not a valid user!")
            return False
        
        nfts = [{"id": tid, "data": info.url, } for tid, info in self.nftlist.items() if info.owner == user]
        
        if len(nfts) == 0:
            print(f"Error: User {user} has no tokens!") 

        else: 
            print(user + "'s NFTs:")
            for nft in nfts:
                print(nft)

        return nfts

# chain = Blockchain()
# chain.add_user("ADIT")
# chain.add_user("HUDSON")
# chain.add_block("SYSTEM", "ADIT", 200)
# chain.add_block("ADIT", "HUDSON", 100)

# chain.mint_nft("JEAN", "3toadbanana.github.io/nftdata/jean1", "41", "key")

# chain.get_user_nfts("HUDSON")
# chain.get_user_nfts("ADIT")
# chain.add_block("ADIT", "HUDSON", 20, "67", "key")
# chain.get_user_nfts("HUDSON")
# chain.get_user_nfts("ADIT")
# chain.mint_nft("ADIT", "3toadbanana.github.io/nftdata/adit2", "1235", "key")

# chain.print_chain()