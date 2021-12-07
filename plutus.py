# Plutus Ethereum Brute Forcer
# Made by Isaac Delly
# https://github.com/Isaacdelly/Plutus
# Added fastecdsa - June 2019 - Ian McMurray
# Modified for Ethereum - December 2021 - LongWayHomie 

from eth_account import Account
import multiprocessing
import time

def generate_key():
        public_key = Account.create('12345678')
        private_key = public_key.privateKey;
        return {
        "private_key":private_key,
        "public_key":public_key
        }

def process(private_key, public_key, address, database):
        if address.address in database:
                with open('results.txt','a') as file:
                        file.write('Hex private key: ' + str(private_key.hex()) + '\n' + 
                                'Public address: ' + str(address.address) + '\n' + 
                                'Address: ' + str(address.address) + '\n\n')
        if address.address not in database:
                print("Ethereum Wallet: " + address.address)

def main(database):
        while True:
                t = generate_key();
                private_key = t["private_key"];
                #print("[PRIV] DEBUG: " + str(private_key.hex()))
                public_key = t["public_key"];
                address = public_key
                #print("[PUB] DEBUG: " + str(address.address))
                if address != -1:
                        process(private_key, public_key, address, database)

if __name__ == '__main__':
        database = [set(line.strip() for line in open('database/top100.txt'))]
        print('Starting Ethereum Brute-Forcer...')
        print('Ethereum list of wallets loaded')
        time.sleep(1)
        print('Executing...')

        for cpu in range(multiprocessing.cpu_count()):
                multiprocessing.Process(target = main, args = (database, )).start()
