"""
Single-byte XOR cipher

    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
"""

import string

def find_random(text):
    valid_list = string.ascii_letters+"'\" \\x!?.\n-:#$_+,0123456789"
    for check_valid in text:
        if check_valid not in valid_list:
            return True
    return False

def decrypt_xor(cipher):
    probable_text = {}
    for key in range(256):
        decrypt_cipher = ''.join(chr(c ^ key) for c in cipher)
        check_random = find_random(decrypt_cipher)
        if not check_random:
            probable_text[key] = decrypt_cipher
    return probable_text

if __name__ == "__main__":
    raw = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipher_text = bytes.fromhex(raw)
    print(decrypt_xor(cipher=cipher_text))