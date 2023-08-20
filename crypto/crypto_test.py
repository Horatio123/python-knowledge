import binascii
import hashlib
import struct
from functools import reduce

"""
replace bit
"""


def st_lib():
    ll = ['qq', 'ww', 'ee']
    p_k = list(map(lambda k: k + '2', ll))
    print(p_k)

    d = {'a': 'sx', 'bt': 'hz'}
    ks = d.keys()

    r_k = list(map(lambda k: k + d[k], filter(lambda k: k != 'a', ks)))
    print(r_k)


def reduce_fun():
    ll = [1, 20, 3, 4]
    r_sum = reduce(lambda x, y: x + y, ll)
    print(r_sum)
    r_max = reduce(lambda x, y: x if x > y else y, ll)
    print(r_max)


def play_struct():
    with open('xxx.zip', 'rb') as f:
        data = f.read()

    start = 0
    for i in range(3):  # show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start + 16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start + filenamesize]
        start += filenamesize
        extra = data[start:start + extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size, extra)

        start += extra_size + comp_size  # skip to the next header


def caculate_md5sum():
    file_name = "xxx.text"
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print(file_md5)


def play_hexlify():
    # hex_str = "48656c6c6f20576f726c64"  # 十六进制字符串
    hex_str = "cc82de8f04b08635eb75a6bc8a055d49"
    byte_data = binascii.unhexlify(hex_str)  # 转换为字节数组

    print(byte_data)  # 输出：b'Hello World'
    with open(file="secret.in", mode="wb") as f:
        f.write(byte_data)
    print(binascii.hexlify(byte_data))

    with open(file="secret.in", mode="rb") as f:
        text = f.read()
        print(text)
        print(binascii.hexlify(text).decode())


def play_convert_str2hex():
    ss = "hello world"
    bb = binascii.hexlify(ss.encode())
    print(bb)

    hh = hex(int.from_bytes(ss.encode(), 'big'))
    print(hh)


def play_convert_str2bin():
    ss = "hello world"
    bin_str = bin(int.from_bytes(ss.encode(), 'big'))
    print(bin_str)

    s2 = '0b110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
    hex_str = hex(int(s2, 2))
    print(int(s2, 2))
    print(hex_str)

    data = binascii.unhexlify(hex_str[2:])
    print(data)


def play_security_access(challenge_bits):
    seed = 0x9
    seed3 = 0x9
    print(0x99)
    print(hex((seed << 4) + seed3))

    initial_value = 0xC541A9

    # challenge_bits = 0x43BB42AA4164F91A
    # challenge_bits = 0x43BB42AA418A964E

    print(challenge_bits.bit_length())

    for i in range(64):
        print(f'---------this is {i + 1} round-----------')

        initial_value_bin = bin(initial_value)
        print(f'initial_value_bin is {initial_value_bin}')
        challenge_bits_bin = bin(challenge_bits)
        print(f'challenge_bits_bin is {challenge_bits_bin}')

        least_bit_initial_value = initial_value & 0x1
        least_bit_challenge_bits = challenge_bits & 0x1
        print(f'least_bit_initial_value is {least_bit_initial_value}')
        print(f'least_bit_challenge_bits is {least_bit_challenge_bits}')

        new_bit = least_bit_initial_value ^ least_bit_challenge_bits
        print(f'new_bit is {new_bit}')

        initial_value = (new_bit << 23) + (initial_value >> 1)
        challenge_bits = challenge_bits >> 1
        print(f'new initial is {bin(initial_value)}')
        print(f'new challenge_bits is {bin(challenge_bits)}')

        b24 = (initial_value & 0x800000) >> 23
        b21 = (initial_value & 0x100000) >> 20
        b16 = (initial_value & 0x8000) >> 15
        b13 = (initial_value & 0x1000) >> 12
        b6 = (initial_value & 0x20) >> 5
        b4 = (initial_value & 0x8) >> 3

        print(f'b24 is {b24}, b21 is {b21}, b16 is {b16}, b13 is {b13}, b6 is {b6}, b4 is {b4}')

        c21 = b24 ^ b21
        c16 = b24 ^ b16
        c13 = b24 ^ b13
        c6 = b24 ^ b6
        c4 = b24 ^ b4

        print(f'c21 is {c21}, c16 is {c16}, c13 is {c13}, c6 is {c6}, c4 is {c4}')

        initial_value = initial_value & ~(1 << 20) | (c21 << 20)
        initial_value = initial_value & ~(1 << 15) | (c16 << 15)

        initial_value = initial_value & ~(1 << 12) | (c13 << 12)

        initial_value = initial_value & ~(1 << 5) | (c6 << 5)
        initial_value = initial_value & ~(1 << 3) | (c4 << 3)

    print(f'initial_value is {bin(initial_value)}')

    print(f'initial_value is {hex(initial_value)}')

    r1 = (initial_value & 0xFF0) >> 4
    r2 = ((initial_value & 0xF000) >> 8) + ((initial_value & 0xF00000) >> 20)
    r3 = ((initial_value & 0xF) << 4) + ((initial_value & 0xF0000) >> 16)

    return r1, r2, r3


if __name__ == '__main__':
    # play_hexlify()
    # play_convert_str2hex()
    # play_convert_str2bin()

    # res1, res2, res3 = play_security_access(0x43BB42AA4164F91A)  # 0xb6 0xf4 0xcf
    # print(hex(res1), hex(res2), hex(res3))

    # res1, res2, res3 = play_security_access(0x43BB42AA418A964E)  # 0x81 0x4b 0xa6
    # print(hex(res1), hex(res2), hex(res3))

    res1, res2, res3 = play_security_access(0x5e4d3c2b1a64f91a)  # 0xa1 0x1c 0xa8
    print(hex(res1), hex(res2), hex(res3))
