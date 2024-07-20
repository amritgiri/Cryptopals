def validate_padding(text):
    padding_length = text[-1]
    return text.count(padding_length) == padding_length


print(validate_padding(b"YELLOW SUBMARINE\x04\x04\x04\x04")) # True
