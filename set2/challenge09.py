"""
Implement PKCS#7 padding

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. 
But we almost never want to transform a single block; we encrypt irregularly-sized messages. 

One way we account for irregularly-sized message is by padding, creating a plaintext that is even multiple of the blocksize.
The most popular padding scheme is called PKCS#7

For instance;
"YELLOW SUBMARINE"

..padding to 20 byte would be:
"YELLOW SUBMARINE\x04\x04\x04\x04"
"""

def pkcs_7_padding(data, block_size):
    padding = block_size - (len(data) % block_size)
    return data + bytes([padding] * padding)

if __name__=="__main__":
    data = b"YELLOW SUBMARINE"
    print(pkcs_7_padding(data,20))