"""
Fixed XOR
    1c0111001f010100061a024b53535009181c
  ^ 686974207468652062756c6c277320657965
-------------------------------------------
    746865206b696420646f6e277420706c6179

assert is use to validate the condition if false provides assertion error
"""

def fixedXOR(x, y):
    assert len(x) == len(y)
    return hex(int(x,16)^int(y,16))[2:]

hex1 = str(input("enter hex: "))
hex2 = str(input())

result = fixedXOR(hex1,hex2)

print(result)
