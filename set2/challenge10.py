"""
Implement CBC mode

It is a cipher mode allowing us to encrypt irregularly-sized messages,despite the fact that a block cipher natively only transforms individual blocks. 

Basic steps for CBC
- Divide plaintext into fixed size blocks
- XOR the first plaintext block 
- Encrypt result
- xor result with next plaintext
"""

from codecs import encode, decode
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

with open('10.txt','r') as f:
    cipher_text = f.read().replace('\n','')
cipher_text = decode(bytes(cipher_text,'utf-8'), 'base64')
assert(len(cipher_text) % 16 == 0)

IV = b'\x00' * 16
key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)


plain_text = b''
for i in range(0,len(cipher_text), 16):
    blocks = cipher_text[i:i+16]
    decrypted_block = cipher.decrypt(blocks)
    plain_text += strxor(decrypted_block, IV)
    IV = blocks
print(plain_text.decode('utf-8'))