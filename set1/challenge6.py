"""
Break repeating-key XOR
    the provided 6.txt is base64 after being encrypted with repeating key xored
"""

from challenge5 import repeating_key_XOR
from challenge3 import find_random, decrypt_xor

KEYSIZE_MIN = 2
KEYSIZE_MAX = 40

def hm_dist(a: bytes, b: bytes):
    return sum(bin(a^b).count('1') for a, b in zip(a,b))

def determine_key_size(ciphertext):
    min_hm_dist = float('inf')
    key_length = None
    for keysize in range(KEYSIZE_MIN, KEYSIZE_MAX+1):
        blocks = []
        for i in range(0, keysize * 4, keysize):
            block = ciphertext[i:i+keysize]
            blocks.append(block)
        distances = []
        for i in range(4):
            for j in range(i+1, 4):
                distances.append(hm_dist(blocks[i], blocks[j])/keysize)
        #Average of the each keysize
        average_dist = sum(distances)/len(distances)
        if average_dist < min_hm_dist:
            min_hm_dist = average_dist
            key_length = keysize
    return key_length

if __name__ == "__main__":
    assert hm_dist(b'this is a test', b'wokka wokka!!!')
