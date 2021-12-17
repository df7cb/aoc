#!/usr/bin/python3

with open('16.txt') as f:
    number = int(f.readline().strip(), 16)
    bits = format(number, 'b')
    if len(bits)%4 != 0:
        bits = '000'[:(4 - len(bits)%4)] + bits

print(bits)

def parse(bits):
    if len(bits) < 6:
        if len(bits):
            print("trailing", bits)
        return 0

    version = int(bits[0:3], 2)
    version_sum = version
    type_id = int(bits[3:6], 2)
    #print("version", version, "type_id", type_id)
    if type_id == 4:
        number = 0
        ptr = 6
        while True:
            #print("found", bits[ptr+1:ptr+5])
            number = 16*number + int(bits[ptr+1:ptr+5], 2)
            ptr += 5
            if bits[ptr-5] == '0':
                break
        print("version", version, "type_id", type_id, "number", number)

        version_sum += parse(bits[ptr:])

    else: # other type_id
        length_type = bits[6]
        if length_type == '0':
            #print("length", bits[7:22])
            length = int(bits[7:22], 2)
            print("version", version, "type_id", type_id, "length_type", length_type, "length", length)

            version_sum += parse(bits[22:22+length])
            version_sum += parse(bits[22+length:])
        else:
            #print("length", bits[7:18])
            subpackets = int(bits[7:18], 2)
            print("version", version, "type_id", type_id, "length_type", length_type, "subpackets", subpackets)

            version_sum += parse(bits[18:])

    return version_sum

version_sum = parse(bits)
print("version_sum", version_sum)
