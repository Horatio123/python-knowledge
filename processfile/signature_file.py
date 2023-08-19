"""
r+和w+的区别
python 没有do while语句
index += 1, no index++
在大文件中插入一行
"""
import binascii
import re


def play_get_header():
    with open(file="123456A.txt", mode="r+t") as f:
        content = f.readline()
        num_left_brace = 0
        num_right_brace = 0
        header = ""

        # get rid of lines before {
        while content:
            if content.strip() != '{':
                content = f.readline()
            else:
                break
        # get content between {}
        while content:
            if content.strip() == '{':
                num_left_brace += 1

            if content.strip() == '}':
                num_right_brace += 1

            if num_left_brace == num_right_brace and num_left_brace != 0:
                header += content
                break

            header += content
            content = f.readline()

        print(header)


def get_sign():

    with open(file="123456A.txt", mode="r+t") as f:
        line = f.readline()
        index = 0
        hash_str = ''

        while line:
            if re.match(r"vbt_hash", line.strip()):
                print(line.strip())
                hash_str = line.strip().split("0x")[1].split(";")[0]
                print(hash_str)
                break
            line = f.readline()
            index += 1

    print(index)

    bb = binascii.unhexlify(hash_str)
    sign = f"    vbt_sign = {bb.decode()};\n"
    print(sign)
    return index, sign


def play_insert_sign():
    num, content = get_sign()
    with open(file="123456A.txt", mode="r") as input_file, open(file="out.txt", mode="w") as output_file:
        for line_num, line in enumerate(input_file):
            print(line_num)
            print(line)
            if line_num == num + 1:
                output_file.write(content)

            output_file.write(line)


if __name__ == '__main__':
    # play_get_header()
    # get_sign()
    play_insert_sign()
