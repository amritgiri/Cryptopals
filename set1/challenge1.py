"""
HEX to BASE64 convert

@input hex string from the user

@returned by hex2base64: Byte encode of base64

@decode: converts byte to string
"""

from base64 import b64encode

def hex2base64(hex_string):
    return b64encode(bytes.fromhex(hex_string))


hex_string = str(input("Enter hex: "))
print(hex2base64(hex_string).decode())



"""To check the answer is correct"""

res = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if hex2base64(hex_string).decode() == res:
    print("Correct")