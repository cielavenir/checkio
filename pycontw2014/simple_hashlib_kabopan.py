#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#modified by @cielavenir to remove struct; compat with Py3.

#from __future__ import print_function, division
from math import sqrt,sin

if 'maketrans' in str.__dict__:
	xrange=range

#_int.py
class List(list):
    def __lshift__(self, other):
        l = len(self)
        limit = other % l
        return List(self[limit:] + self[:limit])

    def __rshift__(self, other):
        l = len(self)
        limit = (l - other) % l
        return List(self[limit:] + self[:limit])

class Int():
    def __init__(self, number, width):
        self.width = width
        self.modulo = 1 << width
        self.number = int(number) % self.modulo

    def __str__(self):
        return ("%x" % (self.number)).rjust(self.width // 4,"0")

    def __add__(self, other):   return Int((self.number + int(other)) % self.modulo, self.width)
    def __mul__(self, other):   return Int((self.number * int(other)) % self.modulo, self.width)
    def __sub__(self, other):   return Int((self.number - int(other)) % self.modulo, self.width)
    def __div__(self, other):   return Int((self.number / int(other)) % self.modulo, self.width)
    def __xor__(self, other):   return Int((self.number ^ int(other)) % self.modulo, self.width)
    def __or__(self, other):    return Int((self.number | int(other)) % self.modulo, self.width)
    def __and__(self, other):   return Int((self.number & int(other)) % self.modulo, self.width)
    def __mod__(self, other):   return Int((self.number % int(other)) % self.modulo, self.width)
    def __radd__(self, other):  return self.__add__(other)
    def __ror__(self, other):   return self.__or__(other)
    def __rxor__(self, other):   return self.__xor__(other)
    def __rand__(self, other):  return self.__and__(other)
    def __rmod__(self, other):  return self.__mod__(other)
    def __rmul__(self, other):  return self.__mul__(other)

    def __rshift__(self, other):return Int((self.number >> other) % self.modulo, self.width)
    def __lshift__(self, other):return Int((self.number << other) % self.modulo, self.width)

    def __eq__(self, other):    return ((self.number % self.modulo) == other)

    def __invert__(self):      return Int((~self.number) % self.modulo, self.width)
    def __trunc__(self):       return self.number
    def __index__(self):       return self.number
    def rol(self, shift):      return Int(((self.number << shift) | (self.number >> (self.width - shift))) % self.modulo, self.width)
    def ror(self, shift):      return Int(((self.number >> shift) | (self.number << (self.width - shift))) % self.modulo, self.width)

    def endian_swap(self):
        result = 0
        bytewidth = self.width // 8
        for b in range(bytewidth):
            current_byte = (self.number >> ((bytewidth - 1 - b) * 8)) & 0xFF
            result |= current_byte << (b * 8)
        return Int(result, self.width)

    def concat(self, other):
        if not isinstance(other, Int):
            raise TypeError#, "Concatting an Int and an int is not supported yet"
        return Int((self.number << other.width) + other.number, self.width + other.width)

    def __getitem__(self, other):
        """extract bytes"""
        if isinstance(other, slice):
            start = 0 if other.start is None else other.start
            stop = self.width / 8 if self.width / 8 < other.stop else other.stop
            return Int(self.number >> (self.width - stop * 8), (stop - start) * 8)
        elif isinstance(other, int):
            shift = other + 1
            return Int(self.number >> (self.width - shift * 8), 8)
        else:
            raise TypeError

class DQWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 128)

OWORD = DQWORD

class QWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 64)

class DWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 32)

class WORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 16)

class BYTE(Int):
    def __init__(self, number):
        Int.__init__(self, number, 8)

def DWORDS(l):
    return [DWORD(i) for i in l]

def QWORDS(l):
    return [QWORD(i) for i in l]

def BYTES(l):
    return [BYTE(i) for i in l]

#_misc.py
def char_range(start, end):
    return "".join(chr(i) for i in range(ord(start), ord(end) + 1))

LITTLE, BIG = False, True
DIGITS = char_range("0", "9")
ALPHABET = char_range("A", "Z")
ALPHABET_LOWERCASE = char_range("a", "z")
ASCII = char_range("\x00", "\xff")

def gcd(a,b):
    """returns the greatest common divisor of both parameters"""
    return gcd(b, a % b) if b != 0 else a

def lcm(a,b):
    """returns the least common multiplier of both parameters"""
    return a * b / gcd(a,b)

def getbinlen(value):
    """return the bit length of an integer"""
    result = 0
    if value == 0:
        return 1
    while value != 0:
        value >>= 1
        result += 1
    return result

def getlongestcommon(a, b):
    """returns i, maximum value such that a[:i] == b[:i]"""
    l = min(len(i) for i in  [a, b])
    res = 0
    while res < l and a[res] == b[res]:
        res += 1
    return res


def gethyphenstr(s, limit = 9, sep = " [...] "):
    """turns a long string into a [...]-shortened string"""
    if len(s) > 2*limit + len(sep):
        return s[:limit].rstrip() + sep + s[-limit:].lstrip()
    else:
        return s


def getbinstr(value):
    """return the smallest binary representation of an integer"""
    if value == 0:
        return "0"

    result = ""
    while value != 0:
        if value & 1:
            result = "1" + result
        else:
            result = "0" + result
        value >>= 1
    return result


def getvaluefrombinarystring(string):
    result = 0
    for char in string:
        bit = 1 if char == "1" else 0
        result = (result << 1) + bit
    return result


def countmissing(value, modulo):
    """returns x > 0 so that (value + x) % modulo = 0 (useful to write leading zeroes)"""
    result = value % modulo
    if result == 0:
        result = modulo
    return modulo - result

def prin(*arg):
    pass



def getpadbinstr(value,bits):
    """return a 0-padded binary string."""
    s = getbinstr(value)
    l = len(s)
    mod = countmissing(l,bits)
    return "0" * mod + s


def getunkbinstr(value, currentbit, maxbit):
    """returns a binary string representation of the command/tag

    including unset bits, according to currentbit.
    it displays 'value' as a binary string, padded according to 'maxbit',
    then hides the lowest bits until 'currentbit'"

    """
    s = getpadbinstr(value, maxbit + 1)[:maxbit - currentbit + 1]
    mod = countmissing(len(s), maxbit + 1)
    return s + "x" * mod



def gethexstr(string):
    return " ".join("%02X" % (ord(char)) for char in string)



def int2lebin(value, size):
    """ouputs value in binary, as little-endian"""
    result = ""
    for i in xrange(size):
        result = result + chr((value >> (8 * i)) & 0xFF )
    return result


def int2bebin(value, size):
    """ouputs value in binary, as big-endian"""
    result = ""
    for i in xrange(size):
        result = chr((value >> (8 * i)) & 0xFF ) + result
    return result

def modifystring(s, sub, offset):
    """overwrites 'sub' at 'offset' of 's'"""
    return s[:offset] + sub + s[offset + len(sub):]

def checkfindest(dic, stream, offset, length):
    """checks that findlongeststring result is correct"""
    temp = dic[:]
    for i in xrange(length):
            temp += temp[-offset]
    if temp != dic + stream[:length]:
        #print temp
        #print dic + stream[:length]
        return False
    return True

def insert_string(string, offset, char):
    return string[:offset] + char + string[offset:]



def zip_extend(a,b, null=""):
    """zip 2 sequences after extending the smallest with null elements"""
    if len(a) == len(b):
        return zip(a,b)

    smaller = a if len(a) < len(b) else b
    bigger = a if len(a) > len(b) else b
    max_length = max(len(i) for i in (a,b))
    smaller.extend([null] * (max_length - len(smaller)))
    return zip(bigger, smaller)


def zip_extend_str(a,b, null=""):
    a = list(a)
    b = list(b)
    return zip_extend(a,b,null)

def split_string_blocks(string, block_length):
    return [string[i: i + block_length] for i in range(0, len(string), block_length)]


def rorstr(string, count=1):
    """rotate right"""
    length = len(string)
    count = (length - count) % length

    result = string[count:] + string[:count]
    return result

def setstr(string, index):
    """rotate string until the 'index' char is the first one"""
    rot = string
    for i in xrange(len(string)):
        rot = rorstr(rot)
        if rot[0] == index:
            return rot
    return

test_vector_strings = [
    "",
    "a",
    "abc",
    "message digest",
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    "1234567890" * 8]

MASK = dict([i, (1 << i) - 1] for i in [8, 16, 32, 64])

def rol(number, shift, width=32):
    number &= MASK[width]
    result = ((number << shift) | (number >> (width - shift))) & ((1 << width) - 1)
    result &= MASK[width]
    return result

def rol32(n, s):return rol(n, s, 32)
def rol64(n, s):return rol(n, s, 64)

assert rol(0x12345678, 8, 32) == 0x34567812
assert rol(0x1234567800, 8, 32) == 0x56780034 # entry value is masked first
assert rol(0x12345678, 8, 64) == 0x1234567800


def ror(number, shift, width):
    return rol(number, (width - shift) % width, width)

def ror32(n, s):return ror(n, s, 32)
def ror64(n, s):return ror(n, s, 64)

assert ror(0x12345678, 8, 32) == 0x78123456
assert ror(0x12345678, 8, 64) == 0x7800000000123456

def split_number(number, bits, amount, bigendian=False):
    result = list()
    mask = (1 << bits) - 1
    for i in range(amount):
        value = ( number >> ((amount - 1 - i) * bits)) & mask
        if not bigendian:
            value = byteswap(value, 4)
        result.append(value)
    return result

def merge_number(list, bigendian=False, bits=32):
    result = 0
    for i,l in enumerate(list[::-1]):
        value = l if bigendian else byteswap(l, bits / 8)
        result += (int(value) << (bits * i))
    return result

def byteswap(number, bytesize):
    result = 0
    for b in range(bytesize):
         current_byte = (number >> ((bytesize - 1 - b) * 8)) & 0xFF
         result |= current_byte << (b * 8)
    return result

assert byteswap(0x12345678, 4) == 0x78563412
assert byteswap(0x12345678, 2) == 0x7856    #incorrect use but expected result

def nibbleswap(number, bytesize):
    result = 0
    for b in range(bytesize):
         current_byte = (number >> (b * 8)) & 0xFF
         current_byte =  ((current_byte & 0xF) << 4) | ((current_byte & 0xF0) >> 4)
         result |= current_byte << (b * 8)
    return result

assert nibbleswap(0x1234,2) == 0x2143

def xor(gen, start = 0):
    result = start
    for i in gen:
        result ^= i
    return result

from decimal import Decimal

def nroot(integer, n):
    return Decimal(integer) ** (Decimal(1) / Decimal(n))

def generate_primes(last_prime):
    result = list(range(2,last_prime + 1))
    for i in xrange(2, last_prime):
        for j in result:
            if j != i and j % i == 0:
                result.remove(j)
    return result


def frac(i):
    return i % 1


def hsqrt(i):
    """hex representation of square root of i"""
    return int(2 ** 30 * i ** (1. / 2))


def hcbrt(i):
    """hex representation of cube root of i"""
    return int(2 ** 30 * i ** (1. / 3))

def add(out_, in_, width):
    for i,j in enumerate(out_):
        out_[i] += in_[i]
        out_[i] &= MASK[width]
    return out_ # unneeded if we didn't do a shallow copy of out_

struct_prefixes = {True:">", False:"<"}
struct_sizes = {32:"L", 64:"Q"}

def pack128(number, bigendian=False):
    struct_string = struct_prefixes[bigendian] + struct_sizes[64]
    if bigendian:
        return pack64(number>>64,bigendian)+pack64(number&0xffffffffffffffff,bigendian)
    else:
        return pack64(number&0xffffffffffffffff,bigendian)+pack64(number>>64,bigendian)

def pack64(number, bigendian=False):
    #return struct.pack(struct_prefixes[bigendian] + struct_sizes[64], number)
    if struct_prefixes[bigendian]=='>':
        return ''.join(chr((number>>(64-8*(i+1)))&0xff) for i in range(8))
    else:
        return ''.join(chr((number>>(8*i))&0xff) for i in range(8))

def pack32(number, bigendian=False):
    #return struct.pack(struct_prefixes[bigendian] + struct_sizes[32], number)
    if struct_prefixes[bigendian]=='>':
        return ''.join(chr((number>>(32-8*(i+1)))&0xff) for i in range(4))
    else:
        return ''.join(chr((number>>(8*i))&0xff) for i in range(4))

def pack(number, bigendian, width):
    return {32:pack32, 64:pack64, 128:pack128}[width](number, bigendian)

def pad_0_1_size(message, alignment, sizelength, bigendian, pad_bit_7):        
    pad_char = {True:"\x80", False: "\x01"}[pad_bit_7]
    """ pads 1 bit, then 0 bits until we have enough bits to store the length of the original message"""
    length = len(message)
    bitlength = length * 8
    padding = pad_char    # we have to add 1 bit so let's add 0x80 since we're working on byte-boundary block
    current_length = bitlength + 8  # we just added 8 bits
    needed_bits = (alignment - sizelength - current_length) % alignment   # we want to have a block length that
    padding += "\x00" * (needed_bits // 8)
    padding += pack(bitlength, bigendian, sizelength)
    return padding

def as_words(block, block_size, word_size, bigendian=False):
    count_ = block_size // word_size
    #unpack_string = struct_prefixes[bigendian] + str(count_) + struct_sizes[word_size]
    if struct_prefixes[bigendian]=='>':
        if word_size==32:
            arr=[sum(ord(e[0])<<(32-8*(i+1)) for i,e in enumerate(block[4*i:4*i+4])) for i in range(count_)]
        else:
            arr=[sum(ord(e[0])<<(64-8*(i+1)) for i,e in enumerate(block[8*i:8*i+8])) for i in range(count_)]
    else:
        if self.hv_size==32:
            arr=[sum(ord(e[0])<<(8*i) for i,e in enumerate(block[4*i:4*i+4])) for i in range(count_)]
        else:
            arr=[sum(ord(e[0])<<(8*i) for i,e in enumerate(block[8*i:8*i+8])) for i in range(count_)]
    return [Int(i, word_size) for i in arr]


#list(struct.unpack(">16L", ASCII[:64]))
assert [sum(ord(e[0])<<(32-8*(i+1)) for i,e in enumerate(ASCII[:64][4*i:4*i+4])) for i in range(16)] == as_words(ASCII[:64], 512, 32, True)


def as_bytes_blocks(s, x):
    return (s[i: i + x] for i in xrange(0, len(s), x))

def simplepad(message):
    last_block = len(message) % 4
    pad = "1"
    if last_block  == 3:
        return ["1", "extr"]
    else:
        return ["1" + "_" * (3 - last_block)]
    
    return
    
def slice_and_pad(message, x, pad=simplepad):
    length = len(message)
    # div is the number of complete blocks
    # last_block_length is 0 if all blocksmod is the length of the last block if it's too short
    complete_blocks, last_block_length = divmod(length, x)    
    for block in (message[i: i + x] for i in xrange(0, complete_blocks * x, x)):
        yield block
    padding = pad(message)  #

    if last_block_length > 0:
        last_block = message[-last_block_length:]
        yield last_block + padding[0]
        for block in padding[1:]:
            yield block
    else:
        for block in padding:
            yield block
    return
        
assert list(slice_and_pad("0001" + "0000" + "0", 4))    == ['0001', '0000', '01__']        
assert list(slice_and_pad("0001" + "0000" + "00", 4))   == ['0001', '0000', '001_']        
assert list(slice_and_pad("0001" + "0000" + "000", 4))  == ['0001', '0000', '0001', 'extr']
assert list(slice_and_pad("0001" + "0000" + "0000", 4)) == ['0001', '0000', '0000', '1___']


def hex2bin(s):
    result = str()
    s = s.replace(" ","")
    HEXA = "0123456789ABCDEF"
    for b in as_bytes_blocks(s, 2):
        result += chr( HEXA.index(b[0].upper()) * 16 + HEXA.index(b[1].upper()))
    return result

assert hex2bin("0123456789ABCDEF") == "\x01\x23\x45\x67\x89\xAB\xCD\xEF"

def bin2hex(s):
    result = str()
    HEXA = "0123456789ABCDEF"
    for b in s:
        b = ord(b)
        result += HEXA[b >> 4] + HEXA[b & 0xF]
    return result

assert "0123456789ABCDEF" == bin2hex("\x01\x23\x45\x67\x89\xAB\xCD\xEF")

#Hash.py
class Hash:
    def __init__(self):
        self.IVs = None
        self.block_length = 8
        self.hv_size = 8
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = False

    def process_block(self, block):
        pass

    def finalize(self):
        pass

    def pad(self, message):
        return str()

    def compute(self, message):
        pass

    def digest(self):
        temp = list(self.ihvs)
        if not self.output_big_endianness:
            temp = [i.endian_swap() for i in temp]

        result = temp[0]
        for i in temp[1:]:
            result = result.concat(i)
        return result

    def hexdigest(self):
        return str(self.digest())

class merkledamgaard(Hash):
    def as_words(self, block):
        count_ = self.block_length // self.hv_size
        prefix = ">" if self.block_big_endianness else "<"
        sizes = {32:"L", 64:"Q"}
        #unpack_string = prefix + str(count_) + sizes[self.hv_size]
        #arr=list(struct.unpack(unpack_string, block))
        if prefix=='>':
            if self.hv_size==32:
                arr=[sum(ord(e[0])<<(32-8*(i+1)) for i,e in enumerate(block[4*i:4*i+4])) for i in range(count_)]
            else:
                arr=[sum(ord(e[0])<<(64-8*(i+1)) for i,e in enumerate(block[8*i:8*i+8])) for i in range(count_)]
        else:
            if self.hv_size==32:
                arr=[sum(ord(e[0])<<(8*i) for i,e in enumerate(block[4*i:4*i+4])) for i in range(count_)]
            else:
                arr=[sum(ord(e[0])<<(8*i) for i,e in enumerate(block[8*i:8*i+8])) for i in range(count_)]
        return [Int(i, self.hv_size) for i in arr]

    def compute(self, message):
        self.ihvs = list(self.IVs)
        message += self.pad(message)
        for block in as_bytes_blocks(message, self.block_length // 8):
            self.process_block(block)
        self.finalize()
        return self

#md4.py
class md4(merkledamgaard):
    def __init__(self):
        merkledamgaard.__init__(self)
        self.block_length = 512
        self.padding_size_encoding_length = 64
        self.hv_size = 32
        hex = "0123456789ABCDEF"
        IVhex = hex + hex[::-1]
        self.IVs = [sum(ord(e[0])<<(8*i) for i,e in enumerate(hex2bin(IVhex)[4*i:4*i+4])) for i in range(4)]#DWORDS(struct.unpack("<4L", hex2bin(IVhex)))
        self.pad_bit_7 = True

        self.functions = [self.f, self.g, self.h]

        self.constants = [hsqrt(i) for i in [0, 2, 3]]

        self.shifts = [
            [3, 7, 11, 19],
            [3, 5,  9, 13],
            [3, 9, 11, 15]]


    def f(self, b, c, d):
        return (b & c) | ((~b) & d)

    def g(self, b, c, d):
        return (b & c) | (b & d) | (c & d)

    def h(self, b, c, d):
        return (b ^ c ^ d)

    def r(self, i):
        return [
            i,
            ((i * 4) + (i / 4)) % 16 ,          # 0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15][i] ]


    def pad(self, message):
        return pad_0_1_size(message, self.block_length, self.padding_size_encoding_length, self.padding_big_endianness, self.pad_bit_7)


    def compress(self, block, words):
        return words


    def rounds(self, words):
        bhv = list(self.ihvs) # block hash values
        for round_ in range(3):  # rounds
            F, constant = self.functions[round_], self.constants[round_]    # round-dependant parameters
            for i in range(16): # iterations per round

                #iteration-dependant parameters
                [a, b, c, d] = [((j - i) % 4) for j in range(4)]
                s = self.shifts[round_][i % 4]
                k = self.r(i)[round_]

                bhv[a] = (bhv[a] + F(bhv[b], bhv[c], bhv[d]) + words[k] + constant).rol(s)
        return bhv

    def sum_combine(self, bhvs):
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def combine(self, *args):
        self.sum_combine(*args)

    def process_block(self, block):
        #compression
        words = self.as_words(block)
        words = self.compress(block, words)
        #rounds
        bhvs = self.rounds(words)
        #integration
        self.combine(bhvs)

#md5.py
class md5(md4):
    def __init__(self):
        md4.__init__(self)
        self.functions = [self.f, self.g, self.h, self.i]
    
        self.shifts = [
            [7, 12, 17, 22],
            [5,  9, 14, 20],
            [4, 11, 16, 23],
            [6, 10, 15, 21]]
    
        self.g_coefficients = [[1,0], [5, 1], [3, 5], [7,0]]

    def g(self, b, c, d):
        return (b & d) | (c & (~d))

    def i(self, b, c, d):
        return c ^ (b | (~d))

    def K(self, i):
        return DWORD(abs(sin(i + 1)) * (2**32))

    def rounds(self, words):
        [a,b,c,d] = list(self.ihvs)
        for round_ in range(4): 
            function = self.functions[round_]
            g_multiplier, g_increment = self.g_coefficients[round_]

            for i in range(16):
                shift = self.shifts[round_][i % 4]
                k = self.K(i + round_ * 16)
                g = (g_multiplier * i + g_increment) % 16

                [a,b,c,d] = [
                    d,
                    (a + function(b, c, d) + words[g] + k).rol(shift) + b,
                    b,
                    c]
        return [a, b, c, d]

#sha0.py
class sha0(md4):
    def __init__(self):
        md4.__init__(self)
        self.IVs += [DWORD(0xC0D0E0F0 | 0x03020100)]
        self.constants = [hsqrt(i) for i in [2, 3, 5, 10]]
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True
        # function names are swapped
        self.g, self.h = self.h, self.g
        self.functions = [self.f, self.g, self.h, self.g]


    def compress(self, block, words):
        words.extend(DWORD(0) for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
        return words

    def rounds(self, words):
        [a, b, c, d, e] = list(self.ihvs)
        for round_ in range(4):
            f = self.functions[round_]
            k = self.constants[round_]
            for i in range(20):
                [a, b, c, d, e] = [
                   rol(a,5) + f(b, c, d) + e + k + words[i + 20 * round_],
                    a,
                    rol(b,30),
                    c,
                    d]
        return [a, b, c, d, e]

#sha1.py
class sha1(sha0):

    def compress(self, block, words):
        words.extend(0 for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
            # a rotation was added between sha0 and sha1
            words[i] = words[i].rol(1)
        return words

#_sha2.py
primes = generate_primes(409)

def nroot_primes(start, end, root, precision):
    """returns the 'precision' bits representation of fractional parts of 'root'-root of the prime numbers, from the 'start'th to the 'end'th"""
    return list(Int(frac(nroot(i, root)) * 2 ** precision, precision) for i in primes[start:end])

#sha512.py
class sha512(md4):
    def __init__(self):
        md4.__init__(self)
        self.block_length = 1024
        self.nb_rounds = 80
        self.hv_size = 64
        self.padding_size_encoding_length = 128
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True

        pickled = None#p.get_variables("sha512", ["IVs", "K"])
        if pickled is None:
            # 64bits representation of fractional parts of square root of the 8th first primes
            self.IVs = nroot_primes(0, 8, 2, 64) 
            # 64bits representation of fractional parts of cube root of the 80th first primes
            self.K = nroot_primes(0, 80, 3, 64)
            #p.save_variables("sha512", {"IVs": self.IVs,"K":self.K})
        else:
            self.IVs, self.K = pickled["IVs"], pickled["K"]


    def rxrxr(self, x, i1, i2, i3):
        """rol ^ rol ^ rol """
        return x.ror(i1) ^ x.ror(i2) ^ x.ror(i3)
    def rxrxs(self, x, i1, i2, i3):
        """rol ^ rol ^ shift """
        return x.ror(i1) ^ x.ror(i2) ^ (x >> i3)

    def f1(self, x):
        return self.rxrxr(x, 28, 34, 39)
    def f2(self, x):
        return self.rxrxr(x, 14, 18, 41)

    def f3(self, x):
        return self.rxrxs(x,  1,  8, 7)
    def f4(self, x):
        return self.rxrxs(x, 19, 61, 6)

    def maj(self, x, y, z):
        return ((x & y) ^ (x & z) ^ (y & z))
    def ch(self, x, y, z):
        return (x & y) ^ ((~x) & z)

    def compress(self, block, words):
        words.extend(0 for i in xrange(self.nb_rounds - 16))
        for i in range(16, self.nb_rounds):
            words[i] = words[i-16] + self.f3(words[i-15]) + words[i-7] + self.f4(words[i-2])
        return words
    
    def rounds(self, words):
        a,b,c,d,e,f,g,h = list(self.ihvs)
        for i in range(self.nb_rounds):
            t1 = h + self.f2(e) + self.ch(e, f, g) + self.K[i] + words[i]
            a,b,c,d,e,f,g,h = [
                t1 + self.f1(a) + self.maj(a, b, c),
                a, b, c, 
                d + t1,
                e, f, g
                ]
        return [a, b, c, d, e, f, g, h]

#sha384.py
class sha384(sha512):
    def __init__(self):
        sha512.__init__(self)
        pickled = None#p.get_variables("sha384", ["IVs"])
        if pickled is None:
            self.IVs = nroot_primes(8, 16, 2, 64)
            #p.save_variables("sha384", {"IVs": self.IVs})
        else:
            self.IVs = pickled["IVs"]

    def digest(self):
        return sha512.digest(self)[:48]

#sha256.py
class sha256(sha512):
    def __init__(self):
        sha512.__init__(self)
        self.nb_rounds = 64
        self.block_length = 512
        self.hv_size = 32
        self.padding_size_encoding_length = 64

        self.IVs = DWORDS([i >> 32 for i in  self.IVs])
        self.K = DWORDS([i >> 32 for i in self.K[:64]])

    def f1(self, x):
        return self.rxrxr(x,  2, 13, 22)
    def f2(self, x):
        return self.rxrxr(x,  6, 11, 25)

    def f3(self, x):
        return self.rxrxs(x,  7, 18,  3)
    def f4(self, x):
        return self.rxrxs(x, 17, 19, 10)

#sha224.py
class sha224(sha256):
    def __init__(self):
        sha256.__init__(self)
        pickled = None#p.get_variables("sha224", ["IVs"])
        if pickled is None:
            self.IVs = DWORDS(nroot_primes(8, 16, 2, 64)) #:Lowest 32 bits of sha384 IVs
            #p.save_variables("sha256", {"IVs": self.IVs})
        else:
            self.IVs = pickled["IVs"]

    def digest(self):
        return sha256.digest(self)[:28]

def checkio(str,algo):
    return globals().get(algo)().compute(str).hexdigest()

if __name__ == '__main__':
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
    print('Done')