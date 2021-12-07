# Plutus Ethereum Brute Forcer

An automated Ethereum wallet collider that brute forces random wallet addresses.
Original Plutus Brute Forcer created by Isaacdelly. 
Ethereum modification done by LongWayHomie with use of eth_account library.

# Like This Project? Donate your findings!

```
DOGE: D6DkzqqLA87bEfERSXjcg1XZEpHrWJopZ8
ETH: 0x01f543F75D163Ce1AABA3fe2bd19f1C405BbE754
```

# Dependencies

<a href="https://www.python.org/downloads/">Python 3.6</a> or higher

Python modules listed in the <a href="/requirements.txt">requirements.txt<a/>
  

# Installation

```
$ git clone https://github.com/LongWayHomie/Plutus-Ethereum.git

$ cd Plutus-Ethereum && pip3 install -r requirements.txt
```

# Quick Start

```
$ python3 plutus.py
```

# Proof Of Concept

Ethereum private keys allow a person to control the wallet that it correlates to. If the wallet has ETH in it, then the private key will allow the person to spend whatever balance the wallet has. 

This program attempts to brute force private keys in an attempt to successfully find a correlating wallet with a positive balance. In the event that a balance is found, the wallet's private key and wallet address are stored in the text file `results.txt` on the user's hard drive.

This program is essentially a brute forcing algorithm. It continuously generates random Ethereum private keys, converts the private keys into their respective wallet addresses, then checks the balance of the addresses. The ultimate goal is to randomly find a wallet with a balance out of the 2<sup>160</sup> possible wallets in existence.

# How It Works

Private keys are generated randomly with use of eth_account library.
By using same library, we create public address (wallet address) from private key.

A pre-calculated database of TOP100 Ethereum addresses with a positive balance is included in this project. The generated address is searched within the database, and if it is found that the address has a balance, then the private key, public key and wallet address are saved to the text file `results.txt` on the user's hard drive.
Feel free to change this database to the list of all Ethereum addresses from <a href="https://gz.blockchair.com/ethereum/addresses/">this repository</a>. Be sure that you have enough RAM to run it.

This program also utilizes multiprocessing through the `multiprocessing.Process()` function in order to make concurrent calculations.

# Efficiency
  
Didn't check it.

# Database FAQ

Database has been created for TOP100 addresses only to check if the program works. 

# Expected Output

Every time this program checks the balance of a generated address, it will print the result to the user. If an empty wallet was generated, then the wallet address will be printed to the terminal. An example is:

>0xDCFCd38b875F0A8615A0D34e353780737Dc64489

However, if a balance is found, then all necessary information about the wallet will be saved to the text file `much_money.txt`. An example is:

>Hex private key: 0x1ae9bae34ffa9375fda3f86777555ca1952d2d99c996dc58a44ca2b676c73b91<br/>
>Public address: 0xE3E99b7C4c094621E05a71305b907039b6b1Be04 <br/>
>Address: 0xE3E99b7C4c094621E05a71305b907039b6b1Be04 <br/>

