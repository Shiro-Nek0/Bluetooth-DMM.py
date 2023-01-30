def str2hexarray(string):
    array = string.split(" ")
    for x in range(len(array)):
        array[x] = int("0x"+ array[x],16) #convert hex to int
    return array

def bytewise_XOR(array,xorkey):
    decoded_array = []
    for x in range(len(array)):
        value = array[x] ^ xorkey[x] #Bytewyse XOR operation
        formatted = '0x{0:0{1}X}'.format(value,2) #format to 2 digits hex
        decoded_array.append(formatted)
    return decoded_array

def hex2bin(array):
    bits_from_hex = []
    for x in range(len(array)):
        bits_from_hex.append(bin(int(array[x], base=16)).lstrip('0b').zfill(8)) #convert to binary
    return bits_from_hex

def flip_bits(array):
    inverted_bits = []
    for x in range(len(array)):
        inverted_bits.append(array[x][::-1]) #reverse binary
    return inverted_bits

def array2str(array):
    string = ""
    for x in range(len(array)):
        string += str(array[x])
    return string

def display_decoder(string):
    digits = {
        "1110111":0,
        "0010010":1,
        "1011101":2,
        "1011011":3,
        "0111010":4,
        "1101011":5,
        "1101111":6,
        "1010010":7,
        "1111111":8,
        "1111011":9,
        "0100101":"L",
        "1111110":"A",
        "0000111":"u",
        "0101101":"t",
        "0001111":"o",
        "0000000":" "
    }

    groups = [] #separate string in groups of 8
    for x in range(0,len(string),8):
        groups.append(string[x:x+8])

    reorder = [0,3,2,7,6,1,5,4] #reorder bits to sevseg order
    for x in range(len(groups)):
        temp = ""
        for y in range(len(groups[x])):
            temp += groups[x][reorder[y]]
        groups[x] = temp

    number = ""
    for x in range(len(groups)):
        if x == 0 and groups[0][0] == "1":
            number += "-"

        if x > 0  and groups[x][0] == "1":
            number += "."

        number += str(digits[groups[x][1:]])

    return number

def binary2icons(string, typeID):

    if (typeID == "11"):
        icons = ["?1","Delta", "BT", "BUZ","HOLD","ºF","ºC","DIODE",
                "MAX","MIN","%","AC","F","u(F)","m(F)","n(F)","Hz",
                "ohm","K(ohm)","M(ohm)","V","m(V)","DC","A","AUTO",
                "?7","u(A)","m(A)","?8","?9","?10","?11"]
        
    elif (typeID == "01"):
        icons = ["?1","HOLD","FLASH","BUZ"," ", " ", " ", " ",
                 "NANO", "V", "DC", "AC", "F", "DIODE", "A",
                 "u(F)", "ohm", "K(ohm)","M(ohm)", " ", "Hz" ,"ºF"
                 ,"ºC"]

    icons_array = []
    for x in range(len(string)):
        if string[x] == "1":
            icons_array.append(icons[x])

    return icons_array

def binary2info(string):
    typeID = string[16:18]
    display_number = display_decoder(string[28:60])
    icons = binary2icons(string[24:28]+string[60:87], typeID)

    obj = {
        "typeID": typeID,
        "display": display_number,
        "icons": icons
    }
    return obj


def decode(data):
    xorkey = "41 21 73 55 a2 c1 32 71 66 aa 3b d0 e2 a8 33 14 20 21 aa bb"

    if type(data) == str:
        encoded_array = str2hexarray(data)   
    else:
        encoded_array = data
    xorkey = str2hexarray(xorkey)
    xordecoded = bytewise_XOR(encoded_array,xorkey)
    binary = hex2bin(xordecoded)
    flipped = flip_bits(binary)
    result = array2str(flipped)
    obj = binary2info(result)
    return obj