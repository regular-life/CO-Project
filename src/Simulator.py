
# inports
from data.Dic import *
from utils.Functions import *
import sys

doc = []
line_list = sys.stdin.readlines()
for line in line_list:
    current_sentence = line.strip()
    doc.append(current_sentence)

# line = input()
# if line:
#     doc.append(line)
# while (line[:5] != "11010"):
#     line = input()
#     doc.append(line)
# line_list = sys.stdin.readlines()

# store values

registor = [0, 0, 0, 0, 0, 0, 0]
address_loc = {}

def flagtobin(flag):
    a = [str(i) for i in flag]
    return "0" * 12 + "".join(a)


cur_line = doc[0]

flag = [0, 0, 0, 0]

line_no = 0
x = -1
while (cur_line[:5] != "11010"):
    test = False
    # Checking the Type of OPcode
    x = line_no
    OP_code = cur_line[:5]
    type = OP[cur_line[:5]]

    if (type == 'A'):

        reg1 = bintodec(cur_line[7:10])
        reg2 = bintodec(cur_line[10:13])
        reg3 = bintodec(cur_line[13:16])

        if (OP2[OP_code] == "add"):
            registor[reg1] = registor[reg2] + registor[reg3]
        if (OP2[OP_code] == "sub"):
            registor[reg1] = registor[reg2] - registor[reg3]
        if (OP2[OP_code] == "mul"):
            registor[reg1] = registor[reg2] * registor[reg3]
        if (OP2[OP_code] == "xor"):
            registor[reg1] = xor(decToBinary(registor[reg2], 16), decToBinary(registor[reg3], 16))
        if (OP2[OP_code] == "or"):
            registor[reg1] = orf(decToBinary(registor[reg2], 16), decToBinary(registor[reg3], 16))
        if (OP2[OP_code] == "and"):
            registor[reg1] = andf(decToBinary(registor[reg2], 16), decToBinary(registor[reg3], 16))
        if (OP2[OP_code] == "addf"):
            reg1 = (cur_line[7:10])
            reg2 = (cur_line[10:13])
            reg3 = (cur_line[13:16])
            val_2 = BinaryToFloatFormat(reg2)
            val_3 = BinaryToFloatFormat(reg3)
            if (val_2 + val_3 > 31.5 or val_2 + val_3 < 0.125):
                registor[bintodec(reg1)] = 0
                flag[0] = 1
            else:
                registor[bintodec(reg1)] = floatFormatToBinary(val_2 + val_3)
        if (OP2[OP_code] == "subf"):
            reg1 = (cur_line[7:10])
            reg2 = (cur_line[10:13])
            reg3 = (cur_line[13:16])
            val_2 = BinaryToFloatFormat(reg2)
            val_3 = BinaryToFloatFormat(reg3)
            if (val_2 - val_3 > 31.5 or val_2 - val_3 < 0.125):
                registor[bintodec(reg1)] = 0
                flag[0] = 1
            else:
                registor[bintodec(reg1)] = floatFormatToBinary(val_2 - val_3)


        if (0 >= registor[reg1] or registor[reg1] <= 65,535):
            flag = [0,0,0,0]
        else:
            registor[reg1] = 0
            flag[0] = 1 

        line_no = line_no + 1
        cur_line = doc[line_no]
    if (type == 'B'):

        reg1 = (cur_line[6:9])

        Imm = bintodec(cur_line[9:])
        reg2 = reg1

        if (OP2[OP_code] == "movi"):
            registor[bintodec(reg1)] = Imm

        if (OP2[OP_code] == "rs"):
            for i in range(Imm):
                reg2 = reg2[0:2]
                reg2 = "0" + reg2
            registor[bintodec(reg1)] = bintodec(reg2)
        if (OP2[OP_code] == "ls"):
            for i in range(Imm):
                reg2 = reg2[1:3]
                reg2 = reg2 + "0"
            registor[bintodec(reg1)] = bintodec(reg2)
        if (OP2[OP_code] == "movf"):
            registor[bintodec(reg1)] = float(Imm)
        flag = [0,0,0,0]

        line_no = line_no + 1
        cur_line = doc[line_no]
        
    if (type == 'C'):

        reg1 = bintodec(cur_line[10:13])
        reg2 = bintodec(cur_line[13:])

        if (OP2[OP_code] == "div"):

            if (reg2 == 0):

                flag[0] = 1
                registor[0] = 0
                registor[1] = 0

            else:

                registor[0] = registor[reg1] // registor[reg2]
                registor[1] = registor[reg1] % registor[reg2]

                flag = [0,0,0,0]

        elif (OP2[OP_code] == "movr"):
            if (reg2 >= 7):
                registor[reg1] = bintodec(flagtobin(flag))
            else:
                registor[reg1] = registor[reg2]
            flag = [0,0,0,0]

        elif (OP2[OP_code] == "not"):

            registor[reg1] = bintodec(notf(decToBinary(registor[reg2], 16)))
            flag = [0,0,0,0]
        elif (OP2[OP_code] == "cmp"):

            if (registor[reg1] == registor[reg2]):

                flag[3] = 1

            if (registor[reg1] > registor[reg2]):

                flag[2] = 1

            if (registor[reg1] < registor[reg2]):
                flag[1] = 1

        line_no = line_no + 1
        cur_line = doc[line_no]

    if (type == 'D'):

        reg1 = bintodec(cur_line[6:9])
        address = cur_line[9:]

        if (OP2[OP_code] == "ld"):

            if (address in address_loc):
                registor[reg1] = address_loc[address]
            else:
                registor[reg1] = 0

        if (OP2[OP_code] == "st"):
            address_loc[address] = registor[reg1]

        line_no = line_no + 1
        cur_line = doc[line_no]

        flag = [0,0,0,0]
    if (type == 'E'):

        address = bintodec(cur_line[-7:]) 
        x = line_no
        if (OP2[OP_code] == "jmp"):

            line_no = address
            cur_line = doc[address]

        if (OP2[OP_code] == "jlt"):

            if (flag[1]):
                line_no = address
                test = True
                cur_line = doc[address]

                flag = [0,0,0,0]
            else:
                line_no = line_no + 1
                cur_line = doc[line_no]
                flag = [0,0,0,0]

        if (OP2[OP_code] == "jgt"):

            if (flag[2]):
                test = True

                line_no = address
                cur_line = doc[address]
                flag = [0,0,0,0]

            else:
                line_no = line_no + 1
                cur_line = doc[line_no]
                flag = [0,0,0,0]

        if (OP2[OP_code] == "je"):

            if (flag[3]):
                test = True

                line_no = address
                cur_line = doc[address]
                flag = [0,0,0,0]

            else:
                line_no = line_no + 1
                cur_line = doc[line_no]
                flag = [0,0,0,0]
    print(decToBinary(x, 7) + "        " + decToBinary(registor[0], 16), decToBinary(registor[1], 16),decToBinary(registor[2], 16), decToBinary(registor[3], 16), decToBinary(registor[4], 16),decToBinary(registor[5], 16), decToBinary(registor[6], 16), flagtobin(flag))
    flag = [0,0,0,0]

    print(decToBinary(line_no, 7) + "        " + decToBinary(registor[0], 16), decToBinary(registor[1], 16),decToBinary(registor[2], 16), decToBinary(registor[3], 16), decToBinary(registor[4], 16),decToBinary(registor[5], 16), decToBinary(registor[6], 16), flagtobin(flag))

    for i in doc:
        print(i.strip())
        
    x = len(doc)

    while (x <= 127):
        if (decToBinary(x, 7) in address_loc):
            print(decToBinary(address_loc[decToBinary(x, 7)], 16).strip())
        else:
            print(decToBinary(0, 16).strip())
        x = x + 1

    # with open(r"/home/sanyam/Desktop/hlo",'r') as f:
    #     a = f.readlines()
    #     for lines in a:
    #         print(lines,end="")