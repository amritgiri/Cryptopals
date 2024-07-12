"""
Detect AES in ECB mode
One of the 8.txt is encrypted in ECB mode 
detect it
Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext. 
"""

def detect_ecb(data):
    probable_ecb = {}
    for i in data:
        raw = bytes.fromhex(i)
        # as in description there state 16 byte plaintext and ciphertext
        blocks = [raw[i:i+16] for i in range(0,len(raw),16)]

        repeating_block = {}
        for b in blocks:
            count = blocks.count(b)
            if count > 1:
                repeating_block[b] = blocks.count(b)
        if len(repeating_block)>0:
            probable_ecb[i] = len(repeating_block)
    return probable_ecb


with open("a8.txt", "r") as f:
    data = f.readlines()
    print(detect_ecb(data))