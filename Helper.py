import string
from OPcode import *
from Functions import *

# Dictionaries

op_code_size = 5

register_size = 3
memory_address_size = 8
immediate_size = 8
registor = [0, 0, 0, 0, 0, 0, 0]
ls_instructions1 = ['add', 'sub', 'movi', 'movr', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or',
                    'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt']

ls_instructions2 = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or',
                    'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt']
ls_instructions3 = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or',
                    'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',
                    'FLAGS']
ls_registers = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']
ls_registers_2 = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',"FLAGS"]
numarr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphanum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
alphanum.append('_')

variable_store = {}
label_store = {}

#Code before this is written by Sankit

def typeconvertor(a, type, line):
    # Type A ->

    if type == "A":

        if len(line) != 4 or line[1] not in ls_registers or line[2] not in ls_registers or line[3] not in ls_registers:
            if line[1] not in ls_registers or line[2] not in ls_registers or line[3] not in ls_registers:
                if line[1] == "FLAGS" or line[2] == "FLAGS" or line[3] == "FLAGS":
                    a.error = 104
                else:
                    a.error = 101
                return
            else:
                a.error = 110
                return

        elif line[0] == "add":
            return OPcode.OPcode_table["add"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

        elif line[0] == "sub":
            return OPcode.OPcode_table["sub"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

        elif line[0] == "mul":
            return OPcode.OPcode_table["mul"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

        elif line[0] == "xor":
            return OPcode.OPcode_table["xor"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

        elif line[0] == "or":
            return OPcode.OPcode_table["or"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

        elif line[0] == "and":
            return OPcode.OPcode_table["and"][0] + "00" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3) + decToBinary(int(line[3][-1]), 3)

    # Type B

    if type == "B":

        if len(line) != 3 or line[1] not in ls_registers or line[2][0] != "$" or not line[2][1:].isnumeric() or 0>int(line[2][1:]) > 127:
            if line[1] not in ls_registers:
                if line[1] == "FLAGS":
                    a.error = 104
                else:
                    a.error = 101
                return
            
            elif 0>int(line[2][1:]) > 127:
                a.error = 105
                return
            
            else:
                a.error = 110 
                return

        elif line[0] == "movi":
            return OPcode.OPcode_table["movi"][0] + "0" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][1:]), 7)

        elif line[0] == "ls":
            return OPcode.OPcode_table["ls"][0] + "0" + decToBinary(int(line[1][-1]), 3) + decToBinary(int(line[2][1:]),
                                                                                                       7)

        elif line[0] == "rs":
            return OPcode.OPcode_table["rs"][0] + "0" + decToBinary(int(line[1][-1]), 3) + decToBinary(int(line[2][1:]),
                                                                                                       7)

    if type == "C":
        if len(line) != 3 or line[1] not in ls_registers or line[2] not in ls_registers_2:
            if line[1] not in ls_registers or line[2] not in ls_registers_2:
                a.error = 101
                return
            else:
                a.error = 110
                return

        elif line[0] == "movr":
            if line[2] == "FLAGS":
                return OPcode.OPcode_table["movr"][0] + "0" * 5 + decToBinary(int(line[1][-1]), 3) + "111"
            return OPcode.OPcode_table["movr"][0] + "0" * 5 + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3)

        elif line[0] == "div":
            return OPcode.OPcode_table["div"][0] + "0" * 5 + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3)

        elif line[0] == "not":
            return OPcode.OPcode_table["not"][0] + "0" * 5 + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3)

        elif line[0] == "cmp":
            return OPcode.OPcode_table["cmp"][0] + "0" * 5 + decToBinary(int(line[1][-1]), 3) + decToBinary(
                int(line[2][-1]), 3)

    if type == "D":

        if len(line) != 3 or line[1] not in ls_registers or line[-1] not in variable_store:
            if line[1] not in ls_registers:
                if line[1] == "FLAGS":
                    a.error = 104
                else:
                    a.error = 101
            elif line[-1] not in variable_store:
                a.error = 102
                
            else:
                a.error = 110
                
            return

        elif line[0] == "ld":
            return OPcode.OPcode_table["ld"][0] + "0" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                variable_store[line[2]][0], 7)
        elif line[0] == "st":
            return OPcode.OPcode_table["st"][0] + "0" + decToBinary(int(line[1][-1]), 3) + decToBinary(
                variable_store[line[2]][0], 7)

    if type == "E":

        if len(line) != 2 or line[-1] not in label_store:
            if line[-1] not in label_store:
                a.error = 103
            else:
                a.error = 110
            return

        elif line[0] == "jmp":
            return OPcode.OPcode_table["jmp"][0] + "0" * 4 + decToBinary(label_store[line[-1]][0], 7)
        elif line[0] == "jlt":
            return OPcode.OPcode_table["jlt"][0] + "0" * 4 + decToBinary(label_store[line[-1]][0], 7)
        elif line[0] == "jgt":
            return OPcode.OPcode_table["jgt"][0] + "0" * 4 + decToBinary(label_store[line[-1]][0], 7)
        elif line[0] == "je":
            return OPcode.OPcode_table["je"][0] + "0" * 4 + decToBinary(label_store[line[-1]][0], 7)

    if type == "F":
        if len(line) != 1:
            a.error = 110 
            return
        return "11010" + "0" * 11


class Shelf:
    lines = []

    def __init__(self, line):
        try:
            self.type = opcodetype(line[0])
            self.type = opcodetype(line[0])
            self.name = line[0]
            self.opcode = opcodesetter(line[0])
            self.error = 404
            self.bin = typeconvertor(self, opcodetype(line[0]), line)
        except:
            self.error = 101
