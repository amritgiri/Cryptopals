"""
Byte at a time ECB decryption (Simple)
"""
from argparse import ArgumentParser
from codecs import encode, decode
from struct import pack
from Crypto.Cipher import AES
from os import urandom
from random import randint
from challenge09 import pkcs_7_padding as pad
from challenge11 import detect_mode

key = urandom(16)

def oracle(pt):
    text = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    pt = pad(pt + decode(text, 'base64'), 16)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pt)

def detect_blocksize(ct):
    sizes = set([len(oracle(b'A' * i)) for i in range(40)])
    sizes = sorted(list(sizes))[:2]
    return(abs(sizes[0] - sizes[1]))
    
def break_AES_ECB(ct, block_size):
    find = lambda val, d : [k for k, v in d.items() if v==val][0]
    pt = b''
    for _ in ct:
        keys = [b'A' * (len(ct)-len(pt)-1) + pt + pack('B', i) for i in range(256)] 
        ref = {key:oracle(key)[:len(ct)] for key in keys}
        val = oracle(b'A' * (len(ct) - len(pt) - 1))[:len(ct)]
        try: pt  = find(val, ref)[-len(pt)-1:]
        except: return pt
    return pt


if __name__ == '__main__':
    block_size = detect_blocksize(oracle)
    assert(detect_mode(oracle(b'A' * 300)) == 'ECB')
    print(break_AES_ECB(oracle(b''), block_size).decode('utf-8'), end='')
