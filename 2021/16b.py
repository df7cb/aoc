#!/usr/bin/python3

with open('16.txt') as f:
    number = int(f.readline().strip(), 16)
    bits = format(number, 'b')
    if len(bits)%4 != 0:
        bits = '000'[:(4 - len(bits)%4)] + bits

print(bits)
print(len(bits))

def parse(bits):
    if len(bits) < 6:
        if len(bits):
            print("trailing", bits)
        return 0, 0

    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    #print("version", version, "type_id", type_id)
    if type_id == 4:
        number = 0
        ptr = 6
        while True:
            #print("found", bits[ptr+1:ptr+5])
            number = 16*number + int(bits[ptr+1:ptr+5], 2)
            if bits[ptr] == '0':
                print("version", version, "type_id", type_id, "number", number)
                return number, ptr+5
            ptr += 5

    else: # other type_id
        length_type = bits[6]
        if length_type == '0':
            #print("length", bits[7:22])
            length = int(bits[7:22], 2)
            print("version", version, "type_id", type_id, "length_type", length_type, "length", length)

            sub_values = []
            ptr = 22
            while ptr < 22 + length:
                v, p = parse(bits[ptr:])
                sub_values.append(v)
                ptr += p

        else:
            #print("length", bits[7:18])
            subpackets = int(bits[7:18], 2)
            print("version", version, "type_id", type_id, "length_type", length_type, "subpackets", subpackets)

            sub_values = []
            ptr = 18
            for i in range(subpackets):
                v, p = parse(bits[ptr:])
                sub_values.append(v)
                ptr += p

    if type_id == 0:
        return sum(sub_values), ptr
    elif type_id == 1:
        prod = 1
        for v in sub_values:
            prod *= v
        return prod, ptr
    elif type_id == 2:
        return min(sub_values), ptr
    elif type_id == 3:
        return max(sub_values), ptr
    elif type_id == 5:
        return sub_values[0] > sub_values[1], ptr
    elif type_id == 6:
        return sub_values[0] < sub_values[1], ptr
    elif type_id == 7:
        return sub_values[0] == sub_values[1], ptr
    else:
        assert(0)

version_sum = parse(bits)
print("version_sum", version_sum)
