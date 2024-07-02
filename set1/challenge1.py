"""
HEX to BASE64 convert

String=[49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d]
output=[SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t]

@input hex string from the user

@returned by hex2base64: Byte encode of base64

@decode: converts byte to string
"""

from base64 import b64encode

def hex2base64(hex_string):
    return b64encode(bytes.fromhex(hex_string))


hex_string = str(input("Enter hex: "))
print(hex2base64(hex_string).decode())

