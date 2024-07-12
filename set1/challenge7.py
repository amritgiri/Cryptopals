"""
The base64 content of 7.txt has been encrypted via AES-128 in ECB mode under the key 
"YELLOW SUBMARINE".
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too). 
Decrypt it.
"""

import base64
from Crypto.Cipher import AES

def decrypt_aes_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB) # AES.MODE_ECB determines the ECB mode
    return cipher.decrypt(data)

if __name__=="__main__":
    with open("7.txt", "r") as f:
        data = base64.b64decode(f.read())
        key = b"YELLOW SUBMARINE"
        print(decrypt_aes_ecb(data, key).decode("utf-8"))