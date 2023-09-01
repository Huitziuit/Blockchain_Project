from hashlib import sha256
import imp
from os import system
import time

transactions_1=["User <Erick Huitziuit> init $10 HuitziCoins",
                "User <Adan Giovani> init $10 HuitziCoins",
                "User <Alarcón Ramos> init $10 HuitziCoins"]

transactions_2=["User <Erick Huitziuit> send $5 HuitziCoins to <Adan Giovani>",
                "User <Erick Huitziuit> send $2 HuitziCoins to <Alarcón Ramos>"]



class Block:
    def __init__(self, previous_hash_block, data) -> None:
        self.previous_hash_block = previous_hash_block
        self.data = data
        self.pW=0

    def hash(self):
        content_block="DATA: " + "_".join(self.data) + " & PREVIOUS HASH: "+ self.previous_hash_block + " & PW: "+str(self.pW) 
        return sha256(content_block.encode()).hexdigest()
    

class Blockchain:
    difficulty = 4

    def __init__(self) -> None:
        self.chain = []
        self.hashesd = []
        self.count = 0
    
    def add(self, block):
        self.chain.append(block)

    def mine(self, block):
        while True: 
            if block.hash()[:self.difficulty] == "7" * self.difficulty:
                self.add(block)
                break
            else:        
                self.hashesd.append(str(block.hash()))
                self.count+=1
                if self.count>10:
                    print("\n\nMinando la transaccion:\n"+ " ".join(block.data)+"\n\n")
                    for i in range (10):
                        print("HASH: "+ self.hashesd[i])
                        
                    self.hashesd.clear()
                    self.count=0
                    time.sleep(00.1)
                    system("cls")
                block.pW += 1


print("hello")

blockchain = Blockchain()

genesis = Block("0" * 64, transactions_1)
print("Minando bloque genesis...")
blockchain.mine(genesis)
print("Hash bloque genesis: "+blockchain.chain[0].hash())
print("coste del minado: " + str(genesis.pW))

block_2 = Block(str(genesis.hash), transactions_2)
print("\n\nMinando bloque 2...")
blockchain.mine(block_2)
print("Hash bloque 2:       "+blockchain.chain[1].hash())
print("coste del minado: " + str(block_2.pW))



