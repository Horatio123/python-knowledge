import binascii
import hashlib
import struct
from functools import reduce


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


if __name__ == '__main__':
    play_hexlify()
