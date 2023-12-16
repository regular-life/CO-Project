from OPcode import *

# Functions

def opcodesetter(name):
    return OPcode_table[name][0]


def opcodetype(name):
    return OPcode_table[name][1]


def decToBinary(n, x):
    binaryNum = [0] * n
    i = 0
    a = ""
    while (n > 0):
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1
    for j in range(i - 1, -1, -1):
        a += str(binaryNum[j])
    while (len(a) < x):
        a = "0" + a
    return a


def bintodec(a):
    c = 0
    for i in range(len(a)):
        if a[i] == "1":
            c = 2 ** i
    return c


def xor(a, b):
    c = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            c = "0" + c
        else:
            c = "1" + c
    return bintodec(c)


def andf(a, b):
    c = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            c = c + "1"
        else:
            c = c + "0"
    return bintodec(c)


def orf(a, b):
    c = ""
    for i in range(len(a)):
        if a[i] == "1" or b[i] == "1":
            c = c + "1"
        else:
            c = c + "0"
    return bintodec(c)


def notf(a):
    c = ""
    for i in a:
        if i == "1":
            c = c + "0"
        else:
            c = c + "1"
    return bintodec(c)



def fractional_to_binary(number, precision):
    integer_part = int(number)
    fractional_part = number - integer_part
    binary_integer = bin(integer_part)[2:]
    binary_fractional = ""
    while (fractional_part > 0 and len(binary_fractional) < precision):
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
    binary_representation = binary_integer + "." + binary_fractional
    return binary_representation

def floatFormatToBinary(a):
    bin_no = fractional_to_binary(a, 8)
    decimal_location = bin_no.find('.')
    integer_part = bin_no[0 : decimal_location]
    fractional_part = bin_no[decimal_location + 1 : len(bin_no)]
    Exponent = decToBinary(2 + len(integer_part))
    Mantissa = integer_part[1:] + fractional_part
    while (len(Exponent) != 3):
        Exponent = "0" + Exponent
    while (len(Mantissa) != 5):
        Mantissa += "0"
    new_representation = Exponent + Mantissa
    return new_representation
   
def BinaryToFloatFormat(a):
    nu = 0
    for i in range(8):
        if (a[i] == "1"):
            nu += 2 ** (2 - i)
    return nu