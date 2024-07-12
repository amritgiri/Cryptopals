"""
Implementing repeating key XOR
Challenge:
        Burning 'em, if you ain't quick and nimble
        I go crazy when I hear a cymbal
    Encrypt it, under the key "ICE", using repeating-key XOR.
"""

def repeating_key_XOR(txt, key):
    ans_xor = []
    for i in range(len(txt)):
        # ord function in python returns the unicode from the given character
        # which in this case basically means the provided character is converted to integer using ord() 
        ans_xor.append((txt[i])^(key[i%len(key)]))
    return bytes(ans_xor)



if __name__=="__main__":
    txt = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = b"ICE"

    print(repeating_key_XOR(txt,key).hex())
