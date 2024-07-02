"""
Fixed XOR
    1c0111001f010100061a024b53535009181c
  ^ 686974207468652062756c6c277320657965
-------------------------------------------
    746865206b696420646f6e277420706c6179
"""

hex1 = str(input("enter hex: "))
hex2 = str(input())

result = hex(int(hex1,16)^int(hex2,16))[2:]

print(result)
