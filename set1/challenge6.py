"""
Break repeating-key XOR
    the provided 6.txt is base64 after being encrypted with repeating key xored
"""

import base64
from challenge5 import repeating_key_XOR
import challenge3

KEYSIZE_MIN = 2
KEYSIZE_MAX = 40

def hm_dist(byte1, byte2):
    return sum(bin(a^b).count('1') for a, b in zip(byte1,byte2))

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
    print(f"key: {key_length} ==> Distance: {min_hm_dist}")
    return key_length

if __name__ == "__main__":
    assert hm_dist(b'this is a test', b'wokka wokka!!!')

    with open("6.txt", "r") as f:
        encrypted_content = base64.b64decode(f.read())
        key_size = determine_key_size(encrypted_content)
        dec_key = ""

        for i in range(key_size):
            block = bytes(encrypted_content[i::key_size])
            decrypted = challenge3.decrypt_xor(block)
            if decrypted:
                dec_key += chr(list(decrypted.keys())[0])
            else:
                print(f"failed for block {i}")
                dec_key += "?"
        print("decrypted_key: ", dec_key)

        print(repeating_key_XOR(encrypted_content,dec_key.encode()).decode())