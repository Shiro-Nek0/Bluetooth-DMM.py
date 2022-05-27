import DMMdecoder

array_data = [0x1b, 0x84, 0x70, 0xb1, 0x49, 0x6a, 0x9f, 0x3c, 0x66, 0xaa, 0x3b]
string_data = "1b 84 70 b1 49 6a 9f 3c 66 aa 3b"

print(DMMdecoder.decode(array_data))
print(DMMdecoder.decode(string_data))
