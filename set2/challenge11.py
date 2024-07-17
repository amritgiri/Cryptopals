from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

def generate_random_aes_key():
    return get_random_bytes(16)

def encryption_oracle(data):
    key = generate_random_aes_key()

    p_bytes = get_random_bytes(random.randint(5,10))
    append_bytes = get_random_bytes(random.randint(5,10))

    pt = p_bytes + data + append_bytes
    pt = pad(pt, AES.block_size)

    if random.randint(0,1) == 0:
        cipher = AES.new(key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)
        mode = 'ECB'
    else:
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pt)
        mode = 'CBC'

    return ct, mode

def detect_mode(ct):
    blocks = [ct[i:i+AES.block_size] for i in range(0, len(ct), AES.block_size)]

    if len(blocks) != len(set(blocks)):
        return 'ECB'
    else:
        return 'CBC'


data = b'this is just a test to detect mode of aes' * 64

ct, am = encryption_oracle(data)
detected_mode = detect_mode(ct)

print(f'Actual mode: {am}')
print(f'Detected mode: {detected_mode}')
