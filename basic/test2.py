import binascii


def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def play_yield():
    odd = odd_numbers()
    for i in range(5):
        print(next(odd))

    ll = countdown(5)
    print("cccc: ", next(ll))
    for i in ll:
        print(i)


def play_hexlify():
    hex_str = "48656c6c6f20576f726c64"  # 十六进制字符串
    byte_data = binascii.unhexlify(hex_str)  # 转换为字节数组

    print(byte_data)  # 输出：b'Hello World'
    print(binascii.hexlify(byte_data))


if __name__ == '__main__':
    # play_hexlify()
    play_yield()
