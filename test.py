import DMMdecoder

#test data for 11 Byte protcol but as array on hex values
array_data11 = [0x1b, 0x84, 0x70, 0xb1, 0x49, 0x6a, 0x9f, 0x3c, 0x66, 0xaa, 0x3b]
#test data for 11 Byte protcol
string_data11 = "1b 84 70 b1 49 6a 9f 3c 66 aa 3b"

#test data for 10 Byte protcol but as array on hex values
array_data10 = [0x1b, 0x84, 0x71, 0x45, 0x38, 0x0e, 0xf5, 0xfe, 0x60, 0xaa]
#test data for 10 Byte protcol
string_data10 = "1b 84 71 45 38 0e f5 fe 60 aa"

#DMMdecoder.decode(value) returns a dictionary with the following keys:
#typeID: the type of device (11 or 01)
#display: the value of the display (ex: -1.23)
#icons: a list of the icons that are on screen (ex: ["HOLD", "ºC"])

print(DMMdecoder.decode(array_data11))
print(DMMdecoder.decode(string_data11))
print(DMMdecoder.decode(array_data10))
print(DMMdecoder.decode(string_data10))