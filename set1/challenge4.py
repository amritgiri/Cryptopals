"""
Find the single character XOR from 
4.txt
"""

from challenge3 import decrypt_hex

with open('4.txt', 'r') as f:
    raw_text = f.readlines()
    possible = {}
    for cipher in raw_text:
        cipher_text = bytes.fromhex(cipher)
        decrypt = decrypt_hex(cipher=cipher_text)
        if decrypt:
            possible[cipher] = decrypt
    print(possible)
