import socket

from time import ctime

HOST = '127.0.0.1'
PORT = 9001
ADDR = (HOST, PORT)
BUFFSIZE = 1024


def tcpClient():
    # 创建客户套接字
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        # 尝试连接服务器
        s.connect(ADDR)
        print('连接服务成功！！')
        # 通信循环
        while True:
            inData = input('pleace input something:')
            # 发送数据到服务器
            # inData = '[{}]:{}'.format(ctime(), inData)

            s.send(inData.encode())
            print('发送成功: ' + str(inData.encode()))

            # 接收返回数据
            outData = s.recv(BUFFSIZE)
            print(f'返回数据信息：{outData.decode()}')

            if inData == 'q':
                break

        # 关闭客户端套接字
        s.close()


def udpClient():
    # 创建客户端套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            # 发送信息到服务器
            data = input('please input message to server or input \'quit\':')
            if data == 'quit':
                break
            data = '[{}]:{}'.format(ctime(), data)

            s.sendto(data.encode('utf-8'), ADDR)

            print('send success')

            # 接收服务端返回信息
            recvData, addrs = s.recvfrom(BUFFSIZE)
            info = recvData.decode()
            print(f'recv message : {info}')

        # 关闭套接字
        s.close()


if __name__ == '__main__':

    while True:
        choice = input('input choice t-tcp or u-udp or q-quit:')
        if choice == 'q':
            break
        if choice != 't' and choice != 'u':
            print('please input t or u,ok?')
            continue

        if choice == 't':
            print('execute tcpsever')
            tcpClient()
        else:
            print('execute udpsever')
            udpClient()